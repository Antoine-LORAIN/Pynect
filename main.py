import freenect
import cv2
import frame_convert2

def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])

while 1:
    cv2.imshow('Depth', get_depth())
    if cv2.waitKey(10) == 27:
        break