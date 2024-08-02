import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import os

def draw_x_grid(image):
    width, height = image.size
    center_x, center_y = width // 2, height // 2
    radius = min(center_x, center_y)
    
    draw = ImageDraw.Draw(image)
    
    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), outline="red", width=3)
    

    draw.line((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill="red", width=3)
    draw.line((center_x - radius, center_y + radius, center_x + radius, center_y - radius), fill="red", width=3)
    
    return image

def divide_image_sections(image):
    width, height = image.size
    center_x, center_y = width // 2, height // 2
    radius = min(center_x, center_y)
    
    # Create masks for each section
    mask_top = np.zeros((height, width), dtype=bool)
    mask_right = np.zeros((height, width), dtype=bool)
    mask_bottom = np.zeros((height, width), dtype=bool)
    mask_left = np.zeros((height, width), dtype=bool)
    
    for y in range(height):
        for x in range(width):
            if (x - center_x)**2 + (y - center_y)**2 <= radius**2:
                if y < center_y and x > y - center_x + center_y and x < center_x + center_y - y:
                    mask_top[y, x] = True
                elif x > center_x and y > -x + center_x + center_y and y < x - center_x + center_y:
                    mask_right[y, x] = True
                elif y > center_y and x < y - center_y + center_x and x > center_x + center_y - y:
                    mask_bottom[y, x] = True
                elif x < center_x and y > x - center_x + center_y and y < -x + center_x + center_y:
                    mask_left[y, x] = True

    # Extract each section
    img_array = np.array(image)
    section_top = np.zeros_like(img_array)
    section_right = np.zeros_like(img_array)
    section_bottom = np.zeros_like(img_array)
    section_left = np.zeros_like(img_array)
    
    section_top[mask_top] = img_array[mask_top]
    section_right[mask_right] = img_array[mask_right]
    section_bottom[mask_bottom] = img_array[mask_bottom]
    section_left[mask_left] = img_array[mask_left]

    img_top = Image.fromarray(section_top)
    img_right = Image.fromarray(section_right)
    img_bottom = Image.fromarray(section_bottom)
    img_left = Image.fromarray(section_left)

    
    return [img_top, img_right, img_bottom, img_left]



def show():
    image_path = "Fundus OCT Dataset/fundus/3_OD.jpg"
    image = Image.open(image_path).convert("RGB")
    image = image.resize((256, 256), Image.BOX)

    image_with_grid = draw_x_grid(image.copy())

    re = divide_image_sections(image)
    img_top, img_right, img_bottom, img_left = re[0], re[1], re[2], re[3]

    plt.figure(figsize=(10, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(img_top)
    plt.title('Top Section')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(img_right)
    plt.title('Right Section')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(img_bottom)
    plt.title('Bottom Section')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(img_left)
    plt.title('Left Section')
    plt.axis('off')

    plt.show()

    plt.figure(figsize=(8, 8))
    plt.imshow(image_with_grid)
    plt.title('Fundus Image with X-Shaped Grid')
    plt.axis('off')
    plt.show()

def ss():

    direc = ['Result/GeneratedOCT','Result/SegmentedOCT_iterUnet','Result/SegmentedOCT_saUnet','Fundus OCT Dataset/octa/']
    name = ['Synthetic OCT-A','IterNet','SA-UNet',"OCTA"]

    for i in range(len(direc)):
        images1 = sorted(os.listdir(direc[i]))

        for img_name1 in images1:

            img1 = Image.open(os.path.join(direc[i], img_name1)).convert('L')
            img1 = img1.resize((256, 256), Image.BOX)

            re = divide_image_sections(img1)
            img_top, img_right, img_bottom, img_left = re[0], re[1], re[2], re[3]

            img_top.save(f"Result_divided/{name[i]}/t/{img_name1}")
            img_right.save(f"Result_divided/{name[i]}/r/{img_name1}")
            img_bottom.save(f"Result_divided/{name[i]}/b/{img_name1}")
            img_left.save(f"Result_divided/{name[i]}/l/{img_name1}")


ss()







