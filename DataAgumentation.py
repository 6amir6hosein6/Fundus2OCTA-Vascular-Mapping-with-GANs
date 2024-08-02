import os
import cv2

def resize_images(input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)

#      
            scale_percent = 60 # percent of original size
            width = int(img.shape[1] / 7.579375)
            height = int(img.shape[0] / 7.579375)
            dim = (width, height)
  
            # resize image
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(output_folder + "/" + filename[:-4] + ".jpg", resized)



def rotate_images(input_folder, output_folder, clockwise=True):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)

            crotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

            output_filename = os.path.join(output_folder, f"r_{filename}")
            cv2.imwrite(output_filename, rotated_img)
            output_filename = os.path.join(output_folder, f"cr_{filename}")
            cv2.imwrite(output_filename, crotated_img)

            ccrotated_img = cv2.rotate(crotated_img, cv2.ROTATE_90_CLOCKWISE)
            output_filename = os.path.join(output_folder, f"ccr_{filename}")
            cv2.imwrite(output_filename, crotated_img)
            cv2.imwrite(output_folder + "/" + filename[:-4] + ".jpg", img)


if __name__ == "__main__":
    input_folder = "Fundus OCT Dataset/segOCTA" 
    output_folder = "Fundus OCT Dataset/rsegOCTA"
    rotate_images(input_folder, output_folder)
    print("Images rotated and saved successfully!")
