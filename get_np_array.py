from PIL import Image
import numpy as np
imageRGB = Image.open("img.png") # ou jpg
imageGrey = imageRGB.convert("L")
image_data = np.asarray( imageGrey )
old_list = image_data.tolist()
newList = []
for y in range(480):
    newList.append([])
    for x in range(640):
        newList[y].append((old_list[y][x], old_list[y][x], old_list[y][x]))
print(newList)