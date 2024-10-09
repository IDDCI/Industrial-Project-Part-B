import rospy
from std_msgs.msg import String

def odom_callback(msg):
	odom_data = eval(msg.data)
	position = odom_data['pose']['pose']['position']
	print("Jetbot Postion (x,y,z,)", position['x'], position['y'], position['z'])

def listener():
	rospy.init_node('odometry_listener', anonymous=True)
	rospy.Subscriber('/odom', String, odom_callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
