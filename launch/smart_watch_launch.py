from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='smart_watch',
            executable='sensor_node',
            name='sensor_node'
        ),
        Node(
            package='smart_watch',
            executable='monitor_node',
            name='monitor_node'
        )
    ])
