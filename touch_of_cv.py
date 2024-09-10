
## Library imports
import numpy as np
from PIL import Image
import os
from util.math import conv
from util.image_tools import extract_images

# 0-degree sobel
sobel = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])

edge_img_paths = extract_images()
edge_imgs = []
for path in edge_img_paths:
    img = Image.open(path).convert('L')
    np_img = np.asarray(img)
    edge_img = conv(sobel, np_img)
    edge_img = np.pad(edge_img, (1, 1), 'constant', constant_values=(0,0))
    new_img = Image.fromarray(edge_img)
    edge_imgs.append(new_img)

output_path = "./output"
if not os.isdir(output_path):
    os.mkdir(output_path)
for img, path in zip(edge_imgs, edge_img_paths): 
    img = img.convert("RGB")
    path_to_save = output_path + "/" + os.path.basename(path)
    print(path_to_save)
    img.save(path_to_save)
    
