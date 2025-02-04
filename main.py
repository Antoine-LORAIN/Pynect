import freenect
import cv2
import frame_convert2
from src.get_config_params import *

def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])

def modifiedColors():
    old_list = image_data.tolist()
    newList = []
    for y in range(480):
        newList.append([])
        for x in range(640):

            if last_color[0] == old_list[y][x]:
                newList[y].append(last_color[1])
            else:
                jsp = False
                for loop in test1:
                    if old_list[y][x] >= int(loop[0][0]) and old_list[y][x] <= int(loop[0][1]):
                        newList[y].append((loop[1]))
                        last_color = [old_list[y][x],loop[1]]
                        jsp = True
                if jsp != True:
                    newList[y].append((255,0,0))
    return newList

while 1:
    cv2.imshow(get_window_title(), modifiedColors())
    if cv2.waitKey(10) == 27:
        break