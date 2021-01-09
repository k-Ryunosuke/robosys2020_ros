#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def ROC():
    rospy.init_node('rock_scissors_paper')
    pub = rospy.Publisher('result', String, queue_size=10)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        print("---------------------------------------------")
        print("Tom : Rock, Paper, Scissors, One Two Three!")
        print("*Please input r:Rock or p:Paper or s:Scissors.")

        key = input()
        if key == 'r':
            kekka = 'Scissors'
        elif key == 's':
            kekka = 'Paper'
        elif key == 'p':
            kekka = 'Rock'
        else:
            print("Please input r, s, p")
            kekka = 'x'
        pub.publish(kekka)
        rate.sleep()

if __name__ == '__main__':
    try:
        ROC()
    except rospy.ROSInterruptException: pass


