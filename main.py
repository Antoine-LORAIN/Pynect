import freenect
import cv2
import sources.frame_convert2 as fc2
import numpy as np
from sources.get_config_params import *

def get_depth():
    return fc2.pretty_depth_cv(freenect.sync_get_depth()[0])

def modifiedColors():
    old_list = get_depth().tolist()
    newList = []
    last_color = [None]
    colours_from_config = get_colors("sources/config.ini")
    for y in range(480):
        newList.append([])
        for x in range(640):

            if last_color[0] == old_list[y][x]:
                newList[y].append(last_color[1])
            else:
                couleur_hors_liste = False
                for loop in colours_from_config:
                    if old_list[y][x] >= int(loop[0][0]) and old_list[y][x] <= int(loop[0][1]):
                        newList[y].append((loop[1]))
                        last_color = [old_list[y][x],loop[1]]
                        couleur_hors_liste = True
                if couleur_hors_liste != True:
                    newList[y].append((255,255,255))
                    last_color = [old_list[y][x],(255,255,255)]


    return np.array(newList,dtype=np.uint8)

while 1:
    cv2.imshow(get_window_title("sources/config.ini"), modifiedColors())
    if cv2.waitKey(10) == 27:
        break
