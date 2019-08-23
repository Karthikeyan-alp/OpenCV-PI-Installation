#TESTING AN PI CAMERA WITH OPENCV

#INSTALLING AN CAMERA WITH PI

#Type "sudo raspi-config" in Terminal

# select Interfacing option and camera press Ok and Restart

#check in the terminal whether camera is working properly by typing

#"raspistill -o test.jpg"

#you can see the photo in home/pi directory

###########################################################################

#Now type the code in the terminal

#$ source ~/.profile
#$ workon cv

#Now you are in cv environment

#.......................................................................#


#Now type this code in python idle

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
 
	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
