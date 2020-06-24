# Jetson Afterburners
___________________________________________________________________________________________
Automatically configure your __NVIDIA Jetson NANO__ with all your Machine Learning libraries and vital packages, Python Virtual Enviorments, system necessities and other system modifications like resizing unallocated SD partitions. 

_Basically a handy toolkit for devs that don't wanna spend an entire day fidling around the sys and concentrate on what really matters_
_____________________________________________________________________________________________
## Prerequisites
JetPack version <= [JetPack 4.2.2](https://developer.nvidia.com/embedded/jetpack)   
Python 3  ''' apt-get install python3```
_____________________________________________________________________________________________
## Installation
Clone the repository
``` git clone https://github.com/n43ee7/Jetson-Afterburners.git ```

Run the script for the first boot
``` python3 Afterburner.py ```

Use the interactive menu to navigate throught what you need to initialize.

_______________________________________________________________________________________________
Note: 
This script is solely designed on and for __NVIDIA Jetson Nano Developer kit__. A lower probability of functionality is possible on Jetson Boards such as the AGX Xavier, TX2, Xavier NX and other market ready Nvidia Jetson boards. 

_Please review each induvidual script in this repository before executing them if you are on any other kernel or a new board._

Credits to __Jetsonhacks.com__ for some of the configuration scripts.
