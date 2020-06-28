#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Mandatory to run on Python 2


from __future__ import print_function
import os, sys, time
import pprint
import subprocess
from multiprocessing import Pool
from multiprocessing import cpu_count


class terminalColors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


if os.getuid() != 0:        # Sudo requirement
    print("[!] Be sure to have root access when running this script")
    exit()


scriptperm = ['bash', '-c', 'cd scripts/ && chmod +x setup && chmod +x ROSinstall && chmod +x OpenCVinstall && chmod +x nvfsresize']
setup = subprocess.Popen(scriptperm, stdin=subprocess.PIPE)
setup.communicate()
print("[!] Script Permissions adjusted in directory '/scripts' ")

print("""\

       ____________
   ___/ ___________\ 
  / ___/            \___
 / /              (____ \ 
| |   NVIDIA JETSON    \ \ 
| |                     ) )
 \ \__ AFTERBURNERS  __/ /           __
  \__ \_____________/ __/        ___/  \ 
     \_______________/       ___/       \_
                \  \     ___/             \ 
                 \  \___/   __/            \ 
                 ___/       \__/\           \ 
             ___/               _\      ___/|
        ____/                  /    ___/ _  ( 
       /       TEGRA            ___/ _   \\ | 
       |\  __               ___/ _   \\  _H_/ 
       | \/  \          ___/ _   \\  _H_/ Y 
       |`|  _/ cu   ___/ _   \\  _H_/ Y   !  
        \|_|\   ___/ _   \\  _H_/ Y   !   ! 
        !  | \_/ _   \\  _H_/ Y   !   ! 
        !  \` |  \\  _H_/ Y   !   ! 
            \`|  _H_/ Y   !   ! 
             \|_/ Y   !   ! 
                  !   ! 
                  ! 
                    """)
time.sleep(2.5)

def sysinfo():
    command = ['bash', '-c', 'source scripts/jetson_variables && env']  # Running jetson_variables.sh
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)

    for line in proc.stdout:
        (key, _, value) = line.partition("=")
        os.environ[key] = value

    proc.communicate()
    print("========================================================================")
    print("                             SYSTEM DETAILS                             ")
    print("========================================================================")
    print(" NVIDIA Board Name: " + os.environ["JETSON_BOARD"].strip())                                                      # Jetson Model
    print(' L4T Version: ' + os.environ['JETSON_L4T'].strip() + ' [ JetPack ' + os.environ['JETSON_JETPACK'].strip() + ' ]')# L4T Version
    print("========================================================================")
    print (" UBUNTU version: ")

    if os.path.exists('/etc/os-release'):                                                                                   # Ubuntu version
        with open('/etc/os-release', 'r') as ubuntuVersionFile:
            ubuntuVersionFileText = ubuntuVersionFile.read()
        for line in ubuntuVersionFileText.splitlines():
            if 'PRETTY_NAME' in line:
                ubuntuRelease = line.split('"')[1]
                print(' ' + ubuntuRelease)
    else:
        print(terminalColors.FAIL + 'Error Enountered while finding Ubuntu Version' + terminalColors.ENDC)
        print('Directory /etc/os-release has not been detected. Try running with SUDO')
    print("========================================================================")

    if os.path.exists('/proc/version'):                                                                                     # Kernel Release
        with open('/proc/version', 'r') as versionFile:
            versionFileText = versionFile.read()
        kernelReleaseArray = versionFileText.split(' ')
        print('System Kernel Version: ' + kernelReleaseArray[2])
    else:
        print(terminalColors.FAIL + 'Error encountered while finding out kernel version' + terminalColors.ENDC)
        print('Directory /proc/version has not been detected. Try running with SUDO')

    print("========================================================================")
    print(' CUDA Version: ' + os.environ['JETSON_CUDA'].strip())
    print("========================================================================")
    print(" ")
    print(" ")
    print("Press Ctrl + C to return to menu")
    while True:
        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            print(" ")
            break

def rosinstall():
    print("[!] Commencing ROS Installation!")
    time.sleep(2.5)
    command = ['bash', '-c', 'cd scripts/ && sudo ./ROSinstall.sh']  # Running ROSinstall
    ros = subprocess.Popen(command, stdin=subprocess.PIPE)
    ros.communicate()


def stressT(mode):
    if mode == 'A': # CPU Stress test
        set_time = input("[!] Enter a CPU stress timeout in minutes >> ")
        while True:
            if set_time > 0:
                break
            print("[!] Invalid timeout. Enter an integer greater than 0.")

        def f(x):
            timeout = time.time() + 60 * float(set_time)  # X minutes from now
            while True:
                if time.time() > timeout or KeyboardInterrupt:
                    break
                x*x

        if __name__ == '__main__':
            processes = cpu_count()
            print ('[!] utilizing %d cores\n' % processes)
            pool = Pool(processes)
            pool.map(f, range(processes))
  # elif mode == 'B':

def sysint(parram):
    if parram == 'A': # Main Sys int
        print("[!] Commencing System Initialization!")
        time.sleep(2.5)
        command = ['bash', '-c', 'cd scripts/ && sudo ./setup sysinit']  # Running sys_int

    elif parram == 'B': # Open CV install
        print("[!] Commencing Installation of OpenCV")
        time.sleep(2.5)
        command = ['bash', '-c', 'cd scripts/ && sudo ./setup opencv']

    elif parram =='C': # VSCode install
        print("[!] Commencing Installation of Visual Studio Code IDE")
        time.sleep(2.5)
        command = ['bash', '-c', 'cd scripts/ && sudo ./setup vscode']

    elif parram == 'D': # Arduino
        print("[!] Commencing Installation of Arduino IDE and Libraries")
        time.sleep(2.5)
        command = ['bash', '-c', 'cd scripts/ && sudo ./setup arduino']

    elif parram == 'E': # GPU STAT
        command = ['bash', '-c', 'cd scripts/ && sudo python3 tegra_gpu_stat.py']

    elif parram == 'F': # Virt envs
        command = ['bash', '-c', 'cd scripts/ && sudo ./setup virtenvs']

    setup = subprocess.Popen(command, stdin=subprocess.PIPE)
    setup.communicate()


def partition():
    print("[!] Commencing System Initialization!")
    time.sleep(2.5)
    command = ['bash', '-c', 'cd scripts/&& sudo nvfsresize.sh']  # Running another script from Python
    part = subprocess.Popen(command, stdin=subprocess.PIPE)
    part.communicate()

os.system('clear')

print(""" \
######################################################################################
          ______ _______ ______ _____  ____  _    _ _____  _   _ ______ _____   _____ 
    /\   |  ____|__   __|  ____|  __ \|  _ \| |  | |  __ \| \ | |  ____|  __ \ / ____|
   /  \  | |__     | |  | |__  | |__) | |_) | |  | | |__) |  \| | |__  | |__) | (___  
  / /\ \ |  __|    | |  |  __| |  _  /|  _ <| |  | |  _  /| . ` |  __| |  _  / \___ \ 
 / ____ \| |       | |  | |____| | \ \| |_) | |__| | | \ \| |\  | |____| | \ \ ____) |
/_/    \_\_|       |_|  |______|_|  \_\____/ \____/|_|  \_\_| \_|______|_|  \_\_____/   

                                        nano
######################################################################################
1) System Information                      |     (8) Install VSCode
2) System Initialization                   |     (9) Install Arduino IDE
3) Partition Resize unallocated SD space   |    (10) System Stress Test (CPU)
4) Install ROS                             |    (11) System Stress Test (GPU)
5) Install OpenCV                          |
6) Display GPU Activity                    |
7) Setup Virtual environments              |   (100) Exit
=====================================================================================
Always Press Ctrl + C if things go wrong!
=====================================================================================
""")
while True:
    try:
        fcmp = input("you@Afterburners:~  ")

        if fcmp == 100:
            break
        elif fcmp == 1:
            sysinfo()
        elif fcmp == 2:
            sysint('A')
        elif fcmp == 3:
            partition()
        elif fcmp == 4:
            rosinstall()
        elif fcmp == 10:
            stressT('A')
        elif fcmp == 11:
            print("Still in Development...")
        elif fcmp == 5:
            sysint('B')
        elif fcmp == 6:
            sysint('E')
        elif fcmp == 8:
            sysint('C')
        elif fcmp == 9:
            sysint('D')
        elif fcmp == 7:
            sysint('F')
        else:
            print(">> [!] Invalid entry. Please re-check you choice.")
    except KeyboardInterrupt:
        print(" ")
        break

print("[!] Exit Interrupt detected, Exiting...")
time.sleep(0.8)
exit()
