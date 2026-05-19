#!/bin/bash

sudo raspi-config nonint do_camera 0

echo "gpu_mem=256" | sudo tee -a /boot/firmware/config.txt

echo "dtoverlay=vc4-kms-v3d" | sudo tee -a /boot/firmware/config.txt

sudo systemctl disable bluetooth

sudo apt install cpufrequtils -y

echo 'GOVERNOR="performance"' | sudo tee /etc/default/cpufrequtils

sudo reboot