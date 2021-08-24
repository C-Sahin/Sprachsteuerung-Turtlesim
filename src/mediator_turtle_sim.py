#!/usr/bin/env python3.9

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

rospy.sleep(1)
def zahluebersetzer(wort):
    if(wort == "NULL"):
        zahl = 0
    elif(wort == "EINS"):
        zahl = 1
    elif(wort == "ZWEI"):
        zahl = 2
    elif(wort == "DREI"):
        zahl = 3
    elif(wort == "VIER"):
        zahl = 4
    elif(wort == "FÜNF"):
        zahl = 5
    elif(wort == "SECHS"):
        zahl = 6
    elif(wort == "SIEBEN"):
        zahl = 7
    elif(wort == "ACHT"):
        zahl = 8
    elif(wort == "NEUN"):
        zahl = 9
    elif(wort == "ZEHN"):
        zahl = 10
    elif(wort == "ELF"):
        zahl = 11
    else:
        zahl = -1
    return zahl

def callback(data): 
    data.data = data.data.upper()
    str_arr = data.data.split(" ")
    rospy.loginfo('echo: %s', data.data)
    

    
    for word in str_arr:
        #flags for state machine
        flag_turn_direction = 0
        flag_acceleration = 0
        cmd_on = False

        if("RECHTS" in word):
            cmd_on = True
            flag_turn_direction =  -1.57079632679 #-pi/2
            
        elif("LINKS" in word):
            cmd_on = True
            flag_turn_direction = 1.57079632679 #pi/2
            
        elif("VORWÄRTS" in word):
            cmd_on = True
            flag_acceleration = 1
            
        elif("RÜCKWÄRTS" in word):
            cmd_on = True
            flag_acceleration = -1
        elif("ZU" in word): #Gehe zu X Y
            try:
                str_index = str_arr.index(word)
                if("GEHE" in (str_arr[str_index-1])):
                    str_arr[str_index]="" #delete old condition for repeated action
                    str_arr[str_index-1]=""
                    x = None
                    y = None
                    for word in str_arr[str_index:]:
                        zahl = zahluebersetzer(word)
                        #word = ""
                        if(zahl == -1):
                            pass
                        else:
                            if(x == None):
                                x = zahl
                            elif(y == None):
                                y = zahl
                                #break

                        
                    MoveToGoalController.move2goal(x,y)
                



            except:
                pass
                #str_arr[str_arr.index(word)-1] = -1
        else:
            cmd_on = False
        



        if cmd_on:
            
            command = Twist(Vector3(flag_acceleration,0,0),Vector3(0,0,flag_turn_direction)) #finalize command from flags
            pub.publish(command)
            
            rospy.sleep(1)

"""
clebercoutof 
turtlesim_cleaner 
https://github.com/clebercoutof/turtlesim_cleaner/blob/master/src/gotogoal.py
"""
class TurtleBot:

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('Mediator_Turtlesim', anonymous=True)
        rospy.Subscriber('result', String, callback)
        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant = 3):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant = 12):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self,x,y):
        """Moves the turtle to the goal."""
        goal_pose = Pose()

        # Get the input from the user.
        goal_pose.x = float(x)#float(input("Set your x goal: "))
        goal_pose.y = float(y)#float(input("Set your y goal: "))

        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        distance_tolerance = 0.2#input("Set your tolerance: ")

        vel_msg = Twist()

        while self.euclidean_distance(goal_pose) >= distance_tolerance:

            # Porportional controller.
            # https://en.wikipedia.org/wiki/Proportional_control

            # Linear velocity in the x-axis.
            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal_pose)

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
MoveToGoalController = TurtleBot()

def listener():
    global pub 
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    
if __name__ == '__main__':
    listener()
        