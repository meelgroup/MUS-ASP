#!/bin/bash

filespos="rules/"

ulimit -t unlimited
shopt -s nullglob
rm -f todo
touch todo
solver="sharpSAT"

opts_arr=("2" "3" "4")

output="initial"
tlimit="5000"
#4GB mem limit
memlimit="16000000"
numthreads=$((OMPI_COMM_WORLD_SIZE))

################
# testing
################
#opts_arr=( " -t 60 -cs 3500 ")
#output="out-test"
#tlimit="60"
#filespos="test_wcnf"
################


SERVER=$PBS_O_HOST
WORKDIR="scratch/${PBS_JOBID}_${OMPI_COMM_WORLD_RANK}"
output="${output}-${PBS_JOBID}"
resultDir="output"

# echo ------------------------------------------------------
# echo "Job is running on node ${PBS_NODEFILE}"
# echo ------------------------------------------------------
# echo "PBS: qsub is running on $PBS_O_HOST"
# echo "PBS: originating queue is $PBS_O_QUEUE"
# echo "PBS: executing queue is $PBS_QUEUE"
# echo "PBS: working directory is $PBS_O_WORKDIR"
# echo "PBS: execution mode is $PBS_ENVIRONMENT"
# echo "PBS: job identifier is ${PBS_JOBID}"
# echo "PBS: job name is $PBS_JOBNAME"
# echo "PBS: node file is $PBS_NODEFILE"
# echo "PBS: current home directory is $PBS_O_HOME"
# echo "PBS: PATH = $PBS_O_PATH"
# echo "server      is ${SERVER}"
# echo "workdir     is ${WORKDIR}"
# echo "servpermdir is ${SERVPERMDIR}"
# echo "Output dir  is ${output}"

mkdir -p "${WORKDIR}"
cd "${WORKDIR}" || exit

#files=$(ls ${PBS_O_WORKDIR}//${filespos}/credit_*.wcnf ${PBS_O_WORKDIR}//${filespos}/adult_*.wcnf ${PBS_O_WORKDIR}//${filespos}/connect_*.wcnf ${PBS_O_WORKDIR}//${filespos}/bank_*.wcnf | shuf --random-source=${PBS_O_WORKDIR}//myrnd)
files=$(ls ${PBS_O_WORKDIR}//${filespos}/*.csv | shuf --random-source=${PBS_O_WORKDIR}//myrnd)
#files=$(ls  ${PBS_O_WORKDIR}//${filespos}/*.wcnf | shuf --random-source=${PBS_O_WORKDIR}//myrnd)
cp ${PBS_O_WORKDIR}//clingo .
cp ${PBS_O_WORKDIR}//gringo .
cp -r ${PBS_O_WORKDIR}//minds/* .

# an example run
# todo="/usr/bin/time ./stream-maxsat_static -epsilon=0.25 -percentile=0.6 -Rvalue=5 -Fvalue=5 -timeout=5000 -small-timeout=100 ${filename} >> result-${filename}.out 2>&1"
# echo "$todo" >> todo

#create todo
rm -f todo
at_opt=0
numlines=0
for opts in "${opts_arr[@]}"
do
    mkdir -p "${output}" || exit
    mkdir -p "${resultDir}" || exit
    for file in $files
    do
        filename=$(basename "$file")
        aspfile=${filename%.xz}
        # filename=$(basename "$file")
        # does the file run earlier
        if [[ ! -f "${PBS_O_WORKDIR}/$resultDir/result-${filename}.out" ]]
        then

            #copy and unzip
            todo="cp ${PBS_O_WORKDIR}//${filespos}/${filename} ."
            echo "$todo" >> todo

            # todo="unxz ${filename}"
            # echo "$todo" >> todo

            todo="/usr/bin/time --verbose -o dlp_${filename}-${opts}.timeout ~/anaconda3/envs/potassco/bin/python tool/mds.py -a 2stage -C mxsat -v -r ${opts} -p dlp ${filename} >> result-${filename}-${opts}.out 2>&1"
            echo "$todo" >> todo

            todo="/usr/bin/time --verbose -o mxsat_${filename}-${opts}.timeout ~/anaconda3/envs/potassco/bin/python tool/mds.py -a 2stage -C mxsat -v -r ${opts} -p mxsat ${filename} >> result-${filename}-${opts}.out 2>&1"
            echo "$todo" >> todo

            todo="mkdir -p ${PBS_O_WORKDIR}//${output}"
            echo "$todo" >> todo

            todo="mv dlp_${filename}-${opts}.timeout mxsat_${filename}-${opts}.timeout result-${filename}-${opts}.out ${PBS_O_WORKDIR}//${output}"
            echo "$todo" >> todo

            numlines=$((numlines+1))
        fi
    done
    let at_opt=at_opt+1
done
todoper=5

# create per-core todos
echo "The total number of benchmarks: $numlines"
numper=$((numlines/numthreads))
remain=$((numlines-numper*numthreads))
if [[ $remain -ge 1 ]]; then
    numper=$((numper+1))
fi
remain=$((numlines-numper*(numthreads-1)))
mystart=0
memlimit="16000000"
for ((myi=0; myi < numthreads ; myi++))
do
    rm -f todo_$myi.sh
    touch todo_$myi.sh
    echo "#!/bin/bash" > todo_$myi.sh
    echo "ulimit -t $tlimit" >> todo_$myi.sh
    echo "ulimit -v $memlimit" >> todo_$myi.sh
    echo "ulimit -c 0" >> todo_$myi.sh
    echo "set -x" >> todo_$myi.sh
    typeset -i myi
    typeset -i numper
    typeset -i mystart
    mystart=$((mystart + numper))
    if [[ $myi -lt $((numthreads-1)) ]]; then
        if [[ $mystart -gt $((numlines+numper)) ]]; then
            echo "No need, over the limit by more than numper"
        else
            if [[ $mystart -lt $numlines ]]; then
                myp=$((numper*todoper))
                mys=$((mystart*todoper))
                head -n $mys todo | tail -n $myp >> todo_$myi.sh
                mysmyp=$((mys - myp))
                echo "$myi th thread => $mysmyp, $mys"
            else
                #we are at boundary, e.g. numlines is 100, numper is 3, mystart is 102
                #we must only print the last numper-(mystart-numlines) = 3-2 = 1
                mys=$((mystart*todoper))
                p=$(( numper-mystart+numlines ))
                if [[ $p -gt 0 ]]; then
                    myp=$((p*todoper))
                    head -n $mys todo | tail -n $myp >> todo_$myi.sh
                    mysmyp=$((mys - myp))
                    echo "$myi th thread => $mysmyp, $mys"
                fi
            fi
        fi
    else
        if [[ $remain -gt 0 ]]; then
            mys=$((mystart*todoper))
            mr=$((remain*todoper))
            head -n $mys todo | tail -n $mr >> todo_$myi.sh
            mysmyp=$((mys - mr))
            echo "$myi th thread => $mysmyp, $mys"
        fi
    fi
    chmod +x todo_$myi.sh
done

# Execute todos
echo "This is MPI exec number $OMPI_COMM_WORLD_RANK"
rm -f ${output}/out_${OMPI_COMM_WORLD_RANK}
./todo_${OMPI_COMM_WORLD_RANK}.sh > ${output}/out_${OMPI_COMM_WORLD_RANK}
echo "Finished waiting ${OMPI_COMM_WORLD_RANK}"