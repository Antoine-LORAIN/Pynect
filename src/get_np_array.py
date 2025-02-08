from PIL import Image
import numpy as np
import cv2
from get_config_params import * 

test1 = get_colors()
last_color = [None]

imageRGB = Image.open("src/other.png") # ou jpg
imageGrey = imageRGB.convert("L")
image_data = np.asarray( imageGrey )
old_list = image_data.tolist()
newList = []

for y in range(480):                # si deux ligne identique on peut peut etre opti 
    newList.append([])              #creation direct d'une liste de 480 []
    for x in range(640):            #traitement de plusieur pixel a la fois ?

        if last_color[0] == old_list[y][x]:
            newList[y].append(last_color[1])
        else:                 
            jsp = False
            for loop in test1: 
                if old_list[y][x] >= int(loop[0][0]) and old_list[y][x] <= int(loop[0][1]):   # trop de test peut etre ?
                    newList[y].append((loop[1]))
                    last_color = [old_list[y][x],loop[1]]
                    jsp = True
                    break
            if jsp != True:                     #possibiltée de simplification 
                newList[y].append((255,0,0))    #
   

            




test = np.array(newList,dtype=np.uint8)
cv2.imshow("test",test)


while 1:
    if cv2.waitKey(10) == 27:
        break