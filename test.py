import freenect
import cv2
import frame_convert2

def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])

print(len(get_depth()[0].tolist()))
old_list = get_depth().tolist()
newList = []
for y in range(480):
    newList.append([])
    for x in range(640):
        newList[y].append([old_list[y][x], old_list[y][x], old_list[y][x]])

file = open("data.txt", "w")
file.write(str(newList))
file.close()