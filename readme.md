```shell
cp ./pwr-headunit.py /root/scripts/pwr-headunit.py
cp ./pwr-dashcam.service /etc/systemd/system/pwr-dashcam.service 
sudo chmod +x /root/scripts/pwr-headunit.py
sudo systemctl daemon-reload
sudo systemctl enable pwr-dashcam.service
```
