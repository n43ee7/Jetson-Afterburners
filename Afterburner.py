#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function
import os, sys, time
import pprint
import subprocess


class terminalColors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


command = ['bash', '-c', 'source scripts/jetson_variables && env']  # Running another script from Python
proc = subprocess.Popen(command, stdout=subprocess.PIPE)

for line in proc.stdout:
    (key, _, value) = line.partition("=")
    os.environ[key] = value

proc.communicate()


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


def sysinfo():
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
    input(""" \
    Press ENTER key to continue system Initialization...
          """)


def rosinstall():
    command = ['bash', '-c', 'source scripts/ROSinstall && env']  # Running another script from Python
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)


