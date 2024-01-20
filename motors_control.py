# Управление

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import rospy, sys
import moveit_commander
from control_msgs.msg import GripperCommand
 
class MoveItFkDemo:
    def __init__(self):
        # Инициализировать API move_group
        moveit_commander.roscpp_initialize(sys.argv)
 
                 # Инициализировать узел ROS
        rospy.init_node('moveit_fk_demo', anonymous=True)
 
                 # Инициализировать группу рук в руке робота, которой должна управлять группа движений
        arm = moveit_commander.MoveGroupCommander('arm')
        
                 # Инициализировать группу захвата в руке робота, управляемую группой перемещения
        gripper = moveit_commander.MoveGroupCommander('gripper')
        
                 # Установите допустимое значение ошибки манипулятора и захвата робота
        arm.set_goal_joint_tolerance(0.001)
        gripper.set_goal_joint_tolerance(0.001)
        
                 # Управляйте манипулятором робота, чтобы сначала вернуться в исходное положение
        arm.set_named_target('arm_init_pose')
        arm.go()
        rospy.sleep(2)
         
                 # Установите целевое положение захвата и контролируйте движение захвата
        '''
        gripper.set_joint_value_target([0.01])
        gripper.go()
        rospy.sleep(1)
        '''
                 # Установите целевое положение руки робота и используйте шестиосевые данные о положении для описания (единица измерения: радианы)
        joint_positions = [1.5708,1.5708,1.5708,1.5708,1.5708,1.5708,1.5708]
        result=arm.set_joint_value_target(joint_positions)
        rospy.loginfo(str(result))
                 
                 # Управление рукой робота, чтобы завершить движение
        arm.go()
        joint=arm.get_current_joint_values()
        print("final joint=",joint)
        pose=arm.get_current_pose('link7')
        print('pose=',pose)
        rospy.sleep(1)
        
                 # Закрыть и выйти из moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)
 
if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
