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

print(" NVIDIA Jetson " + os.environ["JETSON_BOARD"].strip())  # Jetson Model
print(' L4T ' + os.environ['JETSON_L4T'].strip() + ' [ JetPack ' + os.environ[
    'JETSON_JETPACK'].strip() + ' ]')  # L4T Version

# Ubuntu version
if os.path.exists('/etc/os-release'):
    with open('/etc/os-release', 'r') as ubuntuVersionFile:
        ubuntuVersionFileText = ubuntuVersionFile.read()
    for line in ubuntuVersionFileText.splitlines():
        if 'PRETTY_NAME' in line:
            ubuntuRelease = line.split('"')[1]
            print(' ' + ubuntuRelease)
else:
    print(terminalColors.FAIL + 'Error: Unable to find Ubuntu Version' + terminalColors.ENDC)
    print('Reason: Unable to find file /etc/os-release')

# Kernel Release

if os.path.exists('/proc/version'):
    with open('/proc/version', 'r') as versionFile:
        versionFileText = versionFile.read()
    kernelReleaseArray = versionFileText.split(' ')
    print(' Kernel Version: ' + kernelReleaseArray[2])
else:
    print(terminalColors.FAIL + 'Error: Unable to find Linux kernel version' + terminalColors.ENDC)
    print('Reason: Unable to find file /proc/version')

print(' CUDA ' + os.environ['JETSON_CUDA'].strip())

time.sleep(10)
