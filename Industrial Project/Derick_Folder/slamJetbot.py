import rospy
import subprocess
import os
import time
import keyboard 
# Initialize variables for shutdown of node
slamNode_init = None 

def initNode():
	global slamNode_init

	print ("Initialize Robot Slam Node...")

	# Run ros command to start the Slam Node
	slamNode_init = subprocess.Popen(["roslaunch", "jetbot_pro", "slam.launch"])

	time.sleep(5)

def shutNode():
	# Shutting down nodes after use
	global slamNode_init
	print ("Shutting Down Slam Node")
		
	if slamNode_init is not None: 
		slamNode_init.terminate()
		slamNode_init.wait()
		print("Slam Node Terminated")

def saveMap():

	# Save map into folder creating from LiDAR 
	print ("Saving map... 1")
	subprocess.Popen(["rosrun", "map_server", "map_saver", "-f", "/media/jetbot/jetbot2024/Derick_Folder/Map/mymap"])

if __name__ == '__main__':
	stop = False
	initNode()
	rospy.init_node('map_saver_node', anonymous=True)

	try:
		while not rospy.is_shutdown():
			saveMap()
			time.sleep(5)
	
	except KeyboardInterrupt:
		print("interrupted")
		stop = True
	
	finally:
		shutNode()
