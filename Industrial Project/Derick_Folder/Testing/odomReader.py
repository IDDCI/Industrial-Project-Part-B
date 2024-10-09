import rospy
from nav_msgs.msg import Odometry

def odomPos(msg):
	coordinate = msg.pose.pose.position
	print("Recieved odometry data")
	print("Jetbot Coordinates (x, y, z):", coordinate.x, coordinate.y, coordinate.z)

def listener():
	print("Initializing node...")
	rospy.init_node('odometry_listener', anonymous=True)
	rospy.Subscriber('/odom', Odometry, odomPos)
	print("Subscribed to /odom topic")
	rospy.spin()

if __name__ == '__main__':
	listener()
