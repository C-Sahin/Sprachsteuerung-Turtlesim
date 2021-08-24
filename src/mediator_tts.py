#!/usr/bin/env python3.9

import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient

#rospy.init_node('say', anonymous=True)
soundhandle = SoundClient()
rospy.sleep(1)
voice = 'voice_kal_diphone'
volume = 2.0


def callback(data):
    rospy.loginfo('echo: %s', data.data)
    #rospy.loginfo('Saying: %s' % data.data)
    #rospy.loginfo('Voice: %s' % voice)
    #rospy.loginfo('Volume: %s' % volume)
    soundhandle.say(data.data, voice, volume)
    rospy.sleep(1)


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('Mediator_TTS', anonymous=True)

    rospy.Subscriber('result', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
