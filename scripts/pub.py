from logging import shutdown
from multiprocessing import shared_memory
from multiprocessing.managers import SharedMemoryManager
from re import A
import string
import cv2
from cv2 import waitKey
import numpy as np
import rospy
from std_msgs.msg import Int16MultiArray,String
if __name__ == "__main__":
    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher("trying",String, queue_size=10)
    #a = np.array([1, 1, 2, 3, 5, 8])  # Start with an existing NumPy array
    shm = shared_memory.SharedMemory(create=True, size=921600)
   #  ret,frame=cap.read()
   #  cv2.imshow('cam',frame)
   #  shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
    
 # Now create a NumPy array backed by shared memory
   #  b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
   #  b[:] = a[:]  # Copy the original data into shared memory
 
   #  shm.close() 
   #  shm.unlink() 
   #  rospy.spin()
    
    cap=cv2.VideoCapture(0)
    
# while not rospy.is_shutdown():
   # cap=cv2.VideoCapture(0)
while(True):
      ret,frame=cap.read()
      a=frame
      cv2.imshow('cam',frame) 
      b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
      # print(a.shape)
      b[:] = a[:]  # Copy the original data into shared memory
      print(b)
      pub.publish(str(shm.name))
      if cv2.waitKey(1)==ord('q'):
            break
    





