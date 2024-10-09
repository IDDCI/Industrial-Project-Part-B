import rospy
import subprocess
import time
from nav_msgs.msg import Odometry

class RobotPos:
	# Start Robot Master Node & Robot Chassis Node
	def __init__():
		print ("Initialize Robot Master Node...")
		
		# Run ros command 
		subprocess.Popen(["roscore"])

		# Delay for initialization
		time.sleep(5)

		print("Initializing Robot Chassis Node...")
		
		# Run ros command
		subprocess.Popen(["roslaunch", "jetbot_pro", "jetbot.launch"])

		# Delay for initialization
		time.sleep(10)

	# Get Odometry data
	def odomData(msg):

		# Get data on robot's postion from /odom
		data = msg.pose.pose.position

		# Display Coordinates
		print("Jetbot Coordinates (x,y,z,):", data.x, data.y, data.z)

	# Get current position of robot
	def getCords():

		# Initialize ROS node
		rospy.init_node('odometry_listener', anonymous = True)

		# Subscribe to /odom to get data from it
		rospy.Subscriber('/odom', Odometry, odomData)

		rospy.spin()

