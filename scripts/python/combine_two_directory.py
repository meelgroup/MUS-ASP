import os

# Set your directories here
dir1 = 'initial-9097461.pbs101'
dir2 = 'initial-9195896.pbs101'
output_dir = 'combined'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Get filenames in both directories
files_dir1 = set(os.listdir(dir1))
files_dir2 = set(os.listdir(dir2))

# Find common filenames
common_files = files_dir1 & files_dir2

for filename in common_files:
    path1 = os.path.join(dir1, filename)
    path2 = os.path.join(dir2, filename)
    output_path = os.path.join(output_dir, filename)

    try:
        with open(path1, 'r', encoding='utf-8') as f1, \
             open(path2, 'r', encoding='utf-8') as f2, \
             open(output_path, 'w', encoding='utf-8') as out:
            
            out.write(f1.read())
            out.write('\n')  # Optional separator
            out.write(f2.read())
            
        print(f"Merged: {filename}")
    except Exception as e:
        print(f"Failed to merge {filename}: {e}")

print(f"✅ Done. Merged {len(common_files)} files to '{output_dir}'.")
