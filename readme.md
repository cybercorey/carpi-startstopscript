/etc/systemd/system/pwr-dashcam.service 
/root/scripts/pwr-headunit.py

sudo chmod +x /root/scripts/pwr-headunit.py
sudo systemctl daemon-reload
sudo systemctl enable pwr-dashcam.service