#!/bin/bash

#who is the user behind sudo (add to docker group)?
suser=$(sudo sh -c 'echo $SUDO_USER')
dep() { echo "--[DEP] $*" >&2; }
#install git, curl and certificate-keyring
dep "Installing the Basics.."
sudo apt-get -qq update
sudo apt-get -qq install curl git ca-certificates pipx -y
sudo install -m 0755 -d /etc/apt/keyrings

#install JDK21
dep "Installing OpenJDK21"
sudo apt-get -qq install openjdk-21-jre openjdk-21-jdk openjdk-21-demo openjdk-21-doc openjdk-21-jre-headless openjdk-21-source -y

#check for uv and if not install via pipx
dep "Checking for uv.."
if ! command -v uv >/dev/null 2>&1; then
	dep "Installing uv.."
	pipx install uv
else
	dep " Found a uv installation"
fi

#check for docker and if not found install repo and docker
dep "Checking for docker.."
if ! command -v docker >/dev/null 2>&1; then
	dep "Installing docker.."
	bash ./install_dockerrepo.sh

	sudo apt-get -qq update
	#Installing Docker
	sudo apt-get -qq install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

	sudo usermod -aG docker "$suser"
else
	dep "Found a docker installation"
fi

dep "All Dependencies installed"
