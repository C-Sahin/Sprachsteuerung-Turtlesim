#!/usr/bin/env python3.9

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3



rospy.sleep(1)



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
        else:
            cmd_on = False
        
        if cmd_on:
            
            command = Twist(Vector3(flag_acceleration,0,0),Vector3(0,0,flag_turn_direction)) #finalize command from flags
            pub.publish(command)
            
            rospy.sleep(1)


    
    
def listener():

    rospy.init_node('Speech_Recognition_Listener_Turtle_Sim_Mediator', anonymous=True)
    rospy.Subscriber('result', String, callback)
    
    global pub 
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    

if __name__ == '__main__':
    listener()
        