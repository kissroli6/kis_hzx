# Smart Watch Simulation

Ez a package egy okosóra szimulációját valósítja meg, amely két szenzort tartalmaz: egy pulzusmérőt és egy vér-oxigénszint mérőt. A szenzorok adatait két külön topicban hirdeti, és egy monitor node figyeli ezeket az adatokat, és riasztást küld, ha bármelyik érték túl magas vagy túl alacsony.

## Mappastruktúra

```
smart_watch/
├── CMakeLists.txt
├── package.xml
├── README.md
├── launch/
│   └── smart_watch_launch.py
└── src/
    └── smart_watch/
        ├── sensor_node.py
        ├── monitor_node.py
        └── __init__.py
```

## Build és Futás

```bash
cd ~/ros2_ws
colcon build
. install/setup.bash
ros2 launch smart_watch smart_watch_launch.py
```
