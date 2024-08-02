import os
from PIL import Image
import numpy as np
import scipy.stats
from etdrs_grid import * 

name = ['Synthetic OCT-A','IterNet','SA-UNet']

for i in name:
    
    dir1 = "Result_divided/OCTA/" 
    dir2 = "Result_divided/" + i + "/"
    base = "Fundus OCT Dataset/octa/"

    

    grids = ["t","b","r","l"]
    for g in grids:

        images = sorted(os.listdir(base))

        for img_name in images:

            pearson_correlations = []
            spearman_correlations = []
        

            img1 = Image.open(os.path.join(dir1 + g, img_name)).convert('L')
            img2 = Image.open(os.path.join(dir2 + g, img_name)).convert('L')
            
            img1_array = np.array(img1).flatten()
            img2_array = np.array(img2).flatten()

            pearson_corr, _ = scipy.stats.pearsonr(img1_array, img2_array)
            pearson_correlations.append(pearson_corr)
        

            spearman_corr, _ = scipy.stats.spearmanr(img1_array, img2_array)
            spearman_correlations.append(spearman_corr)


        print(f"Average Pearson correlation ({i} , {g}): {np.mean(pearson_correlations)}")
        print(f"Average Spearman correlation ({i} , {g}): {np.mean(spearman_correlations)}")



