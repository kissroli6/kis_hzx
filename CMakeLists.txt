cmake_minimum_required(VERSION 3.5)
project(smart_watch)

# ...existing code...

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

# ...existing code...

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

install(
  PROGRAMS
    src/sensor_node.py
    src/monitor_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
