cmake_minimum_required(VERSION 3.5)
project(smart_watch)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

install(
  FILES
    launch/smart_watch_launch.py
  DESTINATION share/${PROJECT_NAME}/launch
)

install(
  PROGRAMS
    src/smart_watch/sensor_node.py
    src/smart_watch/monitor_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
