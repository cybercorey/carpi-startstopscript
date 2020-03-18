    1  ifconfig
    2  sudo apt install python3-gpiozero
    3  sudo mkdir -p /usr/local/bin
    4  sudo apt install git
    5  git clone https://github.com/scruss/shutdown_button.git
    6  ll
    7  ls -la
    8  cd shutdown_button/
    9  chmod +x shutdown_button.py
   10  sudo cp shutdown_button.py /usr/local/bin
   11  sudo cp shutdown_button.service /etc/systemd/system
   12  sudo systemctl enable shutdown_button.service
   13  sudo systemctl start shutdown_button.service
   14  systemctl status shutdown_button.service
   15  ./shutdown_button.py 
   16  /sbin/poweroff
   17  sudo /sbin/poweroff
   18  ifconfig
   19  wget https://files.mausberrycircuits.com/carsetup.sh
   20  wget http://files.mausberrycircuits.com/carsetup.sh
   21  chmod +x carsetup.sh 
   22  sudo ./carsetup.sh 
   23  reboot
   24  sudo nano /boot/config.txt 
   25  sudo apt updaye
   26  cd
   27  wget https://www.bluewavestudio.io/cc849a0885f774fc8/94c820c762a/openauto_3_3_1_update.tar.gz
   28  tar -xzf openauto_3_3_1_update.tar.gz
   29  cd openauto_3_3_1_update
   30  ll
   31  ls -la
   32  cat update.sh 
   33  sudo ./update.sh 
   34  ifconfig
   35  passwd
   36  cat /boot/config.txt 
   37  sudo nano /boot/config.txt 
   38  sudo reboot
   39  ifconfig
   40  htop
   41  cd /usr/local/bin/
   42  ls -la
   43  cat shutdown_button.py 
   44  sudo nano shutdown_button.py 
   45  reboot
   46  sudo reboot
   47  nano pwr-headunit.py 
   48  ls -la
   49  nano check_gpio.py 
   50  nano pwr-headunit.py 
   51  ./pwr-headunit.py 
   52  nano pwr-headunit.py 
   53  ./pwr-headunit.py 
   54  nano pwr-headunit.py 
   55  sudo nano nano /etc/systemd/system/pwr-dashcam.service
   56  sudo nano /etc/systemd/system/pwr-dashcam.service
   57  sudo mkdir /root/scripts
   58  sudo mv pwr-headunit.py /root/scripts
   59  sudo -s
   60  ifconfig
   61  ls -la
   62  wget https://bluewavestudio.io/bb99577ad49/ff949aad9483/openauto_update_package.zip
   63  unzip openauto_update_package.zip
   64  history


       1  echo 30 > /sys/class/backlight/rpi_backlight/brightness
    2  exit
    3  cd /root/scripts/
    4  nano pwr-headunit.py 
    5  systemctl daemon-reload
    6  systemctl start pwr-dashcam.service
    7  systemctl enavble pwr-dashcam.service
    8  systemctl enable pwr-dashcam.service
    9  systemctl status pwr-dashcam.service
   10  /root/scripts/pwr-dashcam.py
   11  cd /root/
   12  ls -la
   13  cd scripts/
   14  /root/scripts/pwr-dashcam.py
   15  ll
   16  ls -la /root/scripts/pwr-headunit.py 
   17  chown -x /root/scripts/pwr-headunit.py 
   18  chmod -x /root/scripts/pwr-headunit.py 
   19  /root/scripts/pwr-dashcam.py
   20  cat 
   21  cat /root/scripts/pwr-dashcam.py
   22  ls -la
   23  chown root:root ./pwr-headunit.py 
   24  cat /root/scripts/pwr-dashcam.py
   25  ls -la /root/scripts/pwr-dashcam.py
   26  ls -la /root/scripts/
   27  sudo nano /etc/systemd/system/pwr-dashcam.service 
   28  systemctl start pwr-dashcam.service
   29  systemctl daemon-reload
   30  systemctl start pwr-dashcam.service
   31  systemctl status pwr-dashcam.service
   32  /root/scripts/pwr-headunit.py
   33  chmod +x /root/scripts/pwr-headunit.py
   34  /root/scripts/pwr-headunit.py
   35  history


systemctl daemon-reload
systemctl enable pwr-dashcam.service

/etc/systemd/system/pwr-dashcam.service 
[Unit]
Description=Service to start the power detection for Dashcam
After=syslog.target network.target
[Service]
ExecStart=/root/scripts/pwr-headunit.py
Restart=on-abort
[Install]
WantedBy=multi-user.target

/root/scripts/pwr-headunit.py
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