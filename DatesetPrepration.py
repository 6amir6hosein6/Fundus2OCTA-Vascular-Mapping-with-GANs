import os


octa_folder = 'Fundus OCT Dataset/octa'
fundus_folder = 'Fundus OCT Dataset/segOCTA'


octa_files = {f for f in os.listdir(octa_folder) if f.endswith('.jpg')}
fundus_files = {f for f in os.listdir(fundus_folder) if f.endswith('.jpg')}

# Find the common files
common_files = octa_files & fundus_files


for file in octa_files - common_files:
    os.remove(os.path.join(octa_folder, file))

for file in fundus_files - common_files:
    os.remove(os.path.join(fundus_folder, file))

print(f'Found {len(common_files)} matching files.')
print(f'Removed {len(octa_files - common_files)} non-matching files from {octa_folder}.')
print(f'Removed {len(fundus_files - common_files)} non-matching files from {fundus_folder}.')
