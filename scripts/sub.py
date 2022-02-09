from multiprocessing import shared_memory
from multiprocessing.managers import SharedMemoryManager
import string
from tkinter import N
from cv2 import waitKey
import numpy as np
import rospy
from std_msgs.msg import String,Int16MultiArray
import cv2

def callback(na):
    global N
    N=na.data
    existing_shm = shared_memory.SharedMemory(name=str(N))
    # Note that a.shape is (6,) and a.dtype is np.int64 in this example
    # c = np.ndarray((480,640,3), dtype=np.uint8, buffer=existing_shm.buf)
    # print(c)
    # cv2.imshow('recieved',c)
    # waitKey(1)


    # existing_shm.close()
    # existing_shm.unlink()
    
if __name__ == "__main__":
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("trying",String, callback)
    msg=rospy.wait_for_message("trying",String,timeout=None)
    while(True):
        existing_shm = shared_memory.SharedMemory(name=str(N))
    # Note that a.shape is (6,) and a.dtype is np.int64 in this example
        c = np.ndarray((480,640,3), dtype=np.uint8, buffer=existing_shm.buf)
        print(c)
        cv2.imshow('recieved',c)
        waitKey(1)
rospy.spin()
