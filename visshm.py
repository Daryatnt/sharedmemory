
from logging import shutdown
from multiprocessing import shared_memory
from multiprocessing.managers import SharedMemoryManager
from pickletools import uint8
from re import A
from tkinter import Frame
import cv2
from cv2 import waitKey
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16MultiArray,String
class cmu(Node):
        def __init__(self):
            super().__init__('vision')
            self.visionSub = self.create_subscription(
                String,
                'shmN',
                self.visSub_callback,
                10)
            self.visionPub= self.create_publisher(Int16MultiArray, 'visiondata', 10)
            global data

        def visSub_callback(self, shmName):
            self.N=shmName.data
            self.existing_shm = shared_memory.SharedMemory(name=str(self.N))
            self.publisher()
        def publisher(self):
           self.c = np.ndarray((480,640,3), dtype=np.uint8, buffer=self.existing_shm.buf)
           cv2.imshow('recieved',self.c)
        #    data=Int16MultiArray()
           
        #    data.data=[1,2,3,4]
           self.visionPub.publish(data) 


           cv2.waitKey(1)
def main(args=None):
    rclpy.init(args=args)
    vision_node= cmu()
    rclpy.spin(vision_node)
if __name__ == '__main__':
    main()

            



    