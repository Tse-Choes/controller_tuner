from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import OpaqueFunction
from launch import LaunchContext

def generate_launch_description():
    button_ui = Node(
            package='pid_tune',
            executable='pid_tune_drone_button_ui.py',
            name='drone_pid_tuner'
        )
    

    return LaunchDescription([
        button_ui
    ])
