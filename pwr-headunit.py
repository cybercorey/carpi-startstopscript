#!/usr/bin/env python

import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# GPIO25 (pin 22) set up as input. It is pulled up to stop false signals
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("WAIT")

# wait for the pin to be sorted with GND and, if so, halt the system
GPIO.wait_for_edge(17, GPIO.RISING)
subprocess.call(['shutdown -h -P now "System halted by GPIO action"'], shell=True)

print("HALT")

# clean up GPIO on normal exit
GPIO.cleanup()