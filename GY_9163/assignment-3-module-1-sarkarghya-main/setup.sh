#!/bin/bash
#================================================================================
#title           : nyu-appsec-a3-ubuntu20043lts-setup.sh
#description     : This script will install the software necessary to complete
#		    Assignment 3 as well as clone the assignment files.
#author		: John Ryan Allen (jra457@nyu.edu)
#date            : October 19, 2021
#version         : 0.1
#usage		 : sudo bash nyu-appsec-a3-ubuntu20043lts-setup.sh
#notes           : Run as standard user, ***NOT ROOT***. Provide sudo password
#		    when prompted. Tested on fresh install of Ubuntu 20.04.3 LTS.
#		    Must run this script twice to complete the installation.
#bash_version    : 5.0.17(1)-release (x86_64-pc-linux-gnu)
#================================================================================

if [ "$EUID" -eq 0 ]
  then echo "Please do NOT run as root"
  exit 1
fi

# Install docker if user is not already in docker group
if [[ $(id) != *\(docker\)* ]]; then
	# INSTALL DOCKER
	echo '##################################################'
	echo '[*] Installing Docker...'
	echo '##################################################'
	sleep 3
	sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
	sudo apt-get update
	sudo apt-get install -y docker-ce docker-ce-cli containerd.io

	# CONFIGURE STANDARD USER TO MANAGE DOCKER WITHOUT ROOT
	echo '##################################################'
	echo '[*] Configuring Docker...'
	echo '##################################################'
	sleep 3
	sudo usermod -aG docker $USER

	echo '#####################################################################'
	echo '[*] Almost there! Reboot and run this script one more time to finish.'
	echo '#####################################################################'

else

	# INSTALL KUBERNETES CLI TOOLS
	echo '##################################################'
	echo '[*] Installing kubectl...'
	echo '##################################################'
	sleep 3
	sudo apt-get install -y apt-transport-https ca-certificates curl
	sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
	echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
	sudo apt-get update
	sudo apt-get install -y kubectl

	echo '##################################################'
	echo '[*] Installing minikube...'
	echo '##################################################'
	curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
	sudo install minikube-linux-amd64 /usr/local/bin/minikube
	rm minikube-linux-amd64
fi
