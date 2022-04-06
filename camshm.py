
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
class comu(Node):
  def __init__(self):
      super().__init__('camera')
      self.camPub= self.create_publisher(String,'shmN', 10)
      self.shm = shared_memory.SharedMemory(create=True, size=921600)
      self.publisher()

  def publisher(self):
      cap=cv2.VideoCapture(0)
      while(True):
        ret,frame=cap.read()
        a=frame
        cv2.imshow('cam',frame) 
        b = np.ndarray((480, 640, 3), 'uint8', buffer=self.shm.buf)
        b[:] = a[:]  
        print(str(self.shm.name))
        k=String()
        k.data=self.shm.name
        self.camPub.publish(k)
        if cv2.waitKey(1)==ord('q'):
              break
def main(args=None):
    rclpy.init(args=args)
    camera_publisher= comu()
    rclpy.spin(camera_publisher)
if __name__ == '__main__':
    main()
