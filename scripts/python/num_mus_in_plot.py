
import sys
import matplotlib

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1.4771212547196624, 1.4913616938342726, 4.750662646134056, 4.879531676370788, 5.186391215695493, 5.22514380468751, 6.601809765634466, 6.601809765634466, 6.6360238661655675, 7.031323778671397, 7.031323778671397, 7.071752435727005, 7.459932607109886, 7.50489975262641, 7.518910467069224, 7.984387740625179, 8.061992598437849, 8.061992598437849, 9.331929865583417, 9.632959861247398, 9.632959861247398, 9.671877927277768, 10.228180428045055, 10.228180428045055, 10.280098227310548, 10.604931137647155, 10.604931137647155, 10.68411238369478, 10.944713722303153, 11.164438778289654, 11.649993200546179, 11.649993200546179, 11.674352546405624, 30.73138849644843, 30.756212080173462, 41.555503363187384, 77.06367888997919, 77.06367888997919, 95.72753862114602, 95.740902582704, 96.03530199946897, 98.32959861247399])
xpoints = np.array([1.4771212547196624, 1.4913616938342726, 4.250980807096349, 4.250980807096349, 4.741490389771279, 4.741490389771279, 4.878877816965764, 5.222073655912279, 5.235285982316584, 6.592789446632547, 6.629001619286992, 6.629001619286992, 7.0241532107915345, 7.0241532107915345, 7.060365383445979, 7.450121943063816, 7.450121943063816, 7.48633411571826, 7.985235144761164, 8.021447317415609, 8.021447317415609])
# solution = {
# "d1": np.array(sorted([121128700285606399731302400, 292470092988416000, 75662, 29572436593165624934400, 105062400, 20098391751093210029490176000, 71403831296000, 54265657727951667079623475200, 430335590400, 4256000, 1762654578278400, 2105784669516595200, 2105784669516595200, 4906833923606740729856000, 29572436593165624934400, 43302518784, 789669251068723200, 17432576000, 1762654578278400, 7219833152628326400, 1197957500880551936000, 292470092988416000, 105062400, 10571904, 30, 11491200, 192790344499200, 4906833923606740729856000, 1197957500880551936000, 18490520411005753227130961920, 17823, 7219833152628326400, 27206641665712374939648, 115473383424, 37146134754252629250932736, 121128700285606399731302400, 3234485252377490227200, 13248451593738199970611200, 13248451593738199970611200, 8625294006339973939200, 1197957500880551936000, 3915520, 55143, 8625294006339973939200, 28191744, 8625294006339973939200, 269072485549342720, 2105784669516595200, 49924405109715533713253597184, 121128700285606399731302400, 789669251068723200, 35329204249968533254963200, 7219833152628326400, 430335590400, 28191744, 587551526092800, 171904, 166753, 3234485252377490227200, 430335590400, 47067955200, 55143, 17432576000, 514107585331200, 96657408, 4906833923606740729856000, 35329204249968533254963200, 18490520411005753227130961920, 31, 17432576000, 125514547200, 3234485252377490227200, 71403831296000, 43302518784, 10571904, 789669251068723200, 514107585331200, 30643200, 13248451593738199970611200, 54265657727951667079623475200, 1762654578278400, 177367116939264, 192790344499200, 17823, 4256000, 71403831296000])),
# "d2": np.array(sorted([75662, 105062400, 430335590400, 4256000, 43302518784, 17432576000, 105062400, 10571904, 30, 11491200, 17823, 115473383424, 3915520, 55143, 28191744, 430335590400, 28191744, 171904, 166753, 430335590400, 47067955200, 55143, 17432576000, 96657408, 31, 17432576000, 125514547200, 43302518784, 10571904, 30643200, 17823, 4256000])),
# "clingo": np.array(sorted([75662, 105062400, 4256000, 105062400, 10571904, 30, 11491200, 17823, 3915520, 55143, 28191744, 28191744, 171904, 166753, 55143, 96657408, 31, 10571904, 30643200, 17823, 4256000]))
# }
# minimal generators
solution = {
    "Clingo": [0.0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.46, 1.46, 1.46, 1.46, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.49, 1.49, 1.49, 1.49, 1.49, 1.49, 1.49, 1.49, 1.49, 1.51, 1.51, 1.51, 1.51, 1.51, 1.51, 1.51, 1.52, 1.52, 1.52, 1.52, 1.52, 1.52, 1.52, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.54, 1.54, 1.54, 1.54, 1.54, 1.54, 1.54, 1.54, 1.54, 1.54, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.61, 1.61, 1.61, 1.61, 1.61, 1.61, 1.61, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.63, 1.63, 1.63, 1.63, 1.63, 1.63, 1.63, 1.63, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.65, 1.65, 1.65, 1.65, 1.65, 1.65, 1.65, 1.66, 1.66, 1.66, 1.66, 1.66, 1.66, 1.66, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.69, 1.69, 1.69, 1.69, 1.69, 1.69, 1.69, 1.7, 1.7, 1.7, 1.7, 1.7, 1.71, 1.71, 1.71, 1.71, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.73, 1.73, 1.73, 1.73, 1.73, 1.73, 1.73, 1.74, 1.74, 1.74, 1.74, 1.74, 1.74, 1.74, 1.74, 1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.77, 1.77, 1.77, 1.77, 1.77, 1.77, 1.77, 1.77, 1.77, 1.77, 1.78, 1.78, 1.78, 1.79, 1.79, 1.79, 1.79, 1.79, 1.8, 1.8, 1.8, 1.8, 1.8, 1.81, 1.81, 1.81, 1.81, 1.81, 1.81, 1.81, 1.81, 1.82, 1.82, 1.82, 1.82, 1.83, 1.83, 1.83, 1.83, 1.83, 1.83, 1.83, 1.83, 1.83, 1.84, 1.85, 1.85, 1.85, 1.85, 1.85, 1.85, 1.85, 1.85, 1.85, 1.85, 1.85, 1.85, 1.86, 1.86, 1.86, 1.86, 1.86, 1.87, 1.88, 1.88, 1.88, 1.88, 1.89, 1.89, 1.89, 1.89, 1.89, 1.89, 1.89, 1.89, 1.89, 1.89, 1.89, 1.9, 1.9, 1.9, 1.9, 1.9, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.93, 1.93, 1.94, 1.94, 1.95, 1.95, 1.95, 1.96, 1.96, 1.96, 1.96, 1.97, 1.97, 1.98, 1.99, 1.99, 1.99, 2.0, 2.0, 2.0, 2.02, 2.03, 2.03, 2.03, 2.03, 2.04, 2.04, 2.04, 2.05, 2.06, 2.06, 2.06, 2.07, 2.07, 2.08, 2.09, 2.09, 2.1, 2.1, 2.1, 2.11, 2.11, 2.11, 2.11, 2.11, 2.11, 2.12, 2.12, 2.12, 2.12, 2.13, 2.13, 2.14, 2.15, 2.15, 2.16, 2.16, 2.17, 2.18, 2.18, 2.18, 2.19, 2.19, 2.2, 2.21, 2.21, 2.21, 2.21, 2.22, 2.22, 2.23, 2.24, 2.24, 2.24, 2.24, 2.24, 2.26, 2.26, 2.26, 2.26, 2.26, 2.26, 2.27, 2.27, 2.27, 2.28, 2.28, 2.29, 2.29, 2.3, 2.3, 2.3, 2.3, 2.3, 2.3, 2.31, 2.31, 2.32, 2.33, 2.35, 2.36, 2.36, 2.37, 2.38, 2.39, 2.4, 2.4, 2.41, 2.41, 2.41, 2.42, 2.42, 2.42, 2.42, 2.43, 2.43, 2.45, 2.45, 2.45, 2.45, 2.46, 2.46, 2.47, 2.47, 2.48, 2.48, 2.49, 2.51, 2.52, 2.56, 2.56, 2.56, 2.56, 2.57, 2.58, 2.59, 2.59, 2.59, 2.6, 2.6, 2.61, 2.63, 2.63, 2.63, 2.64, 2.64, 2.65, 2.65, 2.66, 2.66, 2.66, 2.67, 2.69, 2.7, 2.7, 2.7, 2.71, 2.71, 2.71, 2.71, 2.72, 2.73, 2.73, 2.73, 2.74, 2.75, 2.75, 2.76, 2.76, 2.76, 2.76, 2.77, 2.77, 2.77, 2.78, 2.78, 2.8, 2.8, 2.82, 2.82, 2.83, 2.83, 2.84, 2.84, 2.84, 2.85, 2.85, 2.86, 2.87, 2.87, 2.87, 2.87, 2.87, 2.87, 2.89, 2.9, 2.9, 2.9, 2.9, 2.9, 2.92, 2.92, 2.92, 2.92, 2.92, 2.94, 2.96, 2.99, 3.0, 3.0, 3.0, 3.02, 3.02, 3.02, 3.03, 3.04, 3.05, 3.06, 3.06, 3.07, 3.07, 3.07, 3.07, 3.08, 3.08, 3.09, 3.09, 3.11, 3.11, 3.11, 3.12, 3.13, 3.15, 3.15, 3.15, 3.15, 3.16, 3.17, 3.17, 3.18, 3.19, 3.2, 3.2, 3.21, 3.23, 3.24, 3.25, 3.25, 3.26, 3.26, 3.26, 3.28, 3.28, 3.28, 3.31, 3.31, 3.33, 3.34, 3.35, 3.36, 3.37, 3.37, 3.38, 3.38, 3.39, 3.4, 3.41, 3.41, 3.41, 3.43, 3.43, 3.43, 3.44, 3.45, 3.47, 3.47, 3.47, 3.48, 3.48, 3.49, 3.5, 3.5, 3.5, 3.51, 3.51, 3.51, 3.52, 3.52, 3.53, 3.53, 3.54, 3.54, 3.54, 3.55, 3.56, 3.56, 3.56, 3.57, 3.57, 3.57, 3.58, 3.59, 3.59, 3.59, 3.6, 3.61, 3.61, 3.62, 3.62, 3.63, 3.64, 3.65, 3.66, 3.68, 3.68, 3.7, 3.7, 3.71, 3.71, 3.72, 3.73, 3.74, 3.75, 3.79, 3.8, 3.81, 3.81, 3.82, 3.82, 3.82, 3.83, 3.83, 3.84, 3.84, 3.85, 3.85, 3.86, 3.86, 3.86, 3.87, 3.89, 3.89, 3.91, 3.92, 3.93, 3.93, 3.93, 3.97, 3.97, 3.98, 4.0, 4.02, 4.02, 4.02, 4.04, 4.04, 4.04, 4.06, 4.06, 4.08, 4.08, 4.08, 4.09, 4.1, 4.1, 4.1, 4.12, 4.13, 4.13, 4.14, 4.15, 4.17, 4.17, 4.2, 4.21, 4.21, 4.22, 4.23, 4.25, 4.25, 4.26, 4.27, 4.29, 4.3, 4.3, 4.31, 4.31, 4.33, 4.34, 4.34, 4.36, 4.37, 4.37, 4.4, 4.4, 4.42, 4.42, 4.43, 4.44, 4.47, 4.48, 4.51, 4.51, 4.52, 4.54, 4.57, 4.61, 4.62, 4.69, 4.72, 4.74, 4.77]
    , "marco": [0.0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.34, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.38, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.41, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45, 1.46, 1.46, 1.46, 1.46, 1.46, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.48, 1.49, 1.49, 1.49, 1.49, 1.49, 1.49, 1.49, 1.49, 1.49, 1.49, 1.49, 1.49, 1.51, 1.51, 1.51, 1.51, 1.51, 1.51, 1.51, 1.51, 1.51, 1.51, 1.51, 1.51, 1.52, 1.52, 1.52, 1.52, 1.52, 1.52, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.53, 1.54, 1.54, 1.54, 1.54, 1.54, 1.54, 1.54, 1.54, 1.54, 1.54, 1.54, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.56, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.61, 1.61, 1.61, 1.61, 1.61, 1.61, 1.61, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.63, 1.63, 1.63, 1.63, 1.63, 1.63, 1.63, 1.63, 1.63, 1.63, 1.63, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.64, 1.65, 1.65, 1.65, 1.65, 1.65, 1.65, 1.65, 1.65, 1.65, 1.66, 1.66, 1.66, 1.66, 1.66, 1.66, 1.66, 1.66, 1.66, 1.66, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.67, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.68, 1.69, 1.69, 1.69, 1.69, 1.69, 1.69, 1.7, 1.7, 1.7, 1.7, 1.7, 1.71, 1.71, 1.71, 1.71, 1.71, 1.71, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.72, 1.73, 1.73, 1.73, 1.73, 1.73, 1.73, 1.73, 1.73, 1.73, 1.74, 1.74, 1.74, 1.75, 1.75, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.76, 1.77, 1.77, 1.77, 1.77, 1.77, 1.77, 1.77, 1.77, 1.77, 1.77, 1.78, 1.78, 1.78, 1.78, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.8, 1.8, 1.81, 1.81, 1.81, 1.81, 1.81, 1.81, 1.81, 1.82, 1.82, 1.82, 1.83, 1.83, 1.83, 1.83, 1.83, 1.83, 1.83, 1.83, 1.83, 1.84, 1.85, 1.85, 1.85, 1.85, 1.86, 1.86, 1.86, 1.86, 1.86, 1.86, 1.86, 1.86, 1.86, 1.86, 1.86, 1.86, 1.87, 1.87, 1.87, 1.87, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.88, 1.89, 1.89, 1.89, 1.89, 1.89, 1.89, 1.89, 1.89, 1.9, 1.9, 1.9, 1.9, 1.91, 1.91, 1.91, 1.91, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.93, 1.93, 1.93, 1.93, 1.93, 1.94, 1.94, 1.94, 1.94, 1.95, 1.95, 1.95, 1.95, 1.95, 1.95, 1.96, 1.96, 1.96, 1.96, 1.96, 1.97, 1.97, 1.97, 1.97, 1.98, 1.98, 1.98, 1.98, 1.98, 1.98, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.02, 2.03, 2.03, 2.03, 2.03, 2.03, 2.04, 2.04, 2.04, 2.04, 2.04, 2.04, 2.05, 2.05, 2.05, 2.05, 2.05, 2.05, 2.05, 2.05, 2.05, 2.05, 2.05, 2.05, 2.06, 2.06, 2.06, 2.06, 2.07, 2.07, 2.07, 2.07, 2.08, 2.08, 2.08, 2.09, 2.09, 2.09, 2.1, 2.1, 2.11, 2.11, 2.11, 2.12, 2.12, 2.12, 2.12, 2.12, 2.13, 2.13, 2.13, 2.13, 2.14, 2.14, 2.14, 2.14, 2.15, 2.15, 2.15, 2.15, 2.15, 2.15, 2.16, 2.16, 2.16, 2.16, 2.16, 2.17, 2.17, 2.17, 2.18, 2.18, 2.18, 2.18, 2.18, 2.19, 2.19, 2.19, 2.2, 2.2, 2.2, 2.2, 2.21, 2.21, 2.21, 2.22, 2.23, 2.23, 2.23, 2.24, 2.24, 2.24, 2.24, 2.25, 2.25, 2.25, 2.25, 2.25, 2.25, 2.26, 2.26, 2.26, 2.26, 2.27, 2.28, 2.28, 2.28, 2.28, 2.28, 2.28, 2.29, 2.29, 2.3, 2.3, 2.3, 2.31, 2.32, 2.32, 2.32, 2.33, 2.34, 2.34, 2.34, 2.34, 2.34, 2.34, 2.35, 2.35, 2.35, 2.36, 2.36, 2.36, 2.36, 2.36, 2.36, 2.36, 2.36, 2.36, 2.36, 2.36, 2.36, 2.37, 2.37, 2.37, 2.38, 2.38, 2.38, 2.38, 2.39, 2.39, 2.39, 2.39, 2.39, 2.39, 2.39, 2.4, 2.4, 2.42, 2.43, 2.43, 2.43, 2.44, 2.44, 2.44, 2.45, 2.45, 2.45, 2.45, 2.45, 2.46, 2.46, 2.46, 2.46, 2.47, 2.47, 2.47, 2.48, 2.48, 2.49, 2.5, 2.5, 2.5, 2.51, 2.51, 2.51, 2.51, 2.51, 2.51, 2.51, 2.51, 2.52, 2.53, 2.53, 2.53, 2.53, 2.53, 2.53, 2.53, 2.53, 2.56, 2.57, 2.57, 2.58, 2.58, 2.58, 2.58, 2.6, 2.6, 2.6, 2.6, 2.61, 2.62, 2.62, 2.62, 2.62, 2.63, 2.63, 2.65, 2.66, 2.67, 2.67, 2.67, 2.68, 2.68, 2.68, 2.69, 2.7, 2.71, 2.71, 2.71, 2.72, 2.72, 2.73, 2.74, 2.74, 2.75, 2.75, 2.75, 2.76, 2.76, 2.77, 2.77, 2.77, 2.78, 2.79, 2.8, 2.81, 2.81, 2.81, 2.82, 2.82, 2.82, 2.84, 2.84, 2.84, 2.86, 2.86, 2.86, 2.86, 2.87, 2.87, 2.87, 2.88, 2.9, 2.93, 2.94, 2.95, 2.96, 2.97, 2.99, 3.01, 3.03, 3.04, 3.05, 3.05, 3.11, 3.13, 3.17, 3.17, 3.18, 3.19, 3.22, 3.22, 3.22, 3.25, 3.28, 3.33, 3.45, 3.45, 3.54]
    , "unimus": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.78, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.85, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.26, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.34, 1.34, 1.36, 1.36, 1.36, 1.36, 1.36, 1.36, 1.38, 1.38, 1.38, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.41, 1.43, 1.45, 1.45, 1.45, 1.45, 1.48, 1.48, 1.49, 1.54, 1.54, 1.56, 1.57, 1.58, 1.58, 1.59, 1.64, 1.73, 1.74, 1.77, 1.85, 1.85, 1.88, 1.95, 1.96, 1.99, 2.05, 2.06, 2.23, 2.28, 2.86]
}

# solvers = ["Proj-Enum", "ApproxASP", "clingo", "HashCount", "DefMe"]
solvers = ["Clingo", "marco", "unimus"]
for solver in solvers:
    plt.plot(solution[solver], linestyle = 'solid', label = solver)
    # plt.semilogy()
plt.ylabel("#MUSes", fontsize=14)
plt.xlabel("instances", fontsize=14)
plt.legend(fontsize = 14)
# plt.savefig("solution/{0}.pdf".format("circum"), format = 'pdf')
plt.savefig("solution/{0}.pdf".format("countMUS"), format = 'pdf')
