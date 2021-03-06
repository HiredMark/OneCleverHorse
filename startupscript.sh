#!/bin/bash
sudo apt update
sudo apt install build-essential -y 
sudo apt install python3 python3-pip -y
sudo pip3 install pytest 
sudo pip3 install pytest-cov
sudo apt install docker.io -y
sudo apt install -y curl jq
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo su -
su jenkins