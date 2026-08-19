#!/bin/bash

install_dep() {
#who is the user behind sudo (add to docker group)?
suser=$(sudo sh -c 'echo $SUDO_USER')

dep() { echo "--[DEP] $*" >&2; }
# Install git, curl and certificate-keyring and pipx
dep "Installing the Basics.."
sudo apt-get -qq update
sudo apt-get -qq install curl git ca-certificates pipx -y

# Create keyrings directory
dep "Installing certificate-keyring..."
sudo install -m 0755 -d /etc/apt/keyrings

# Install JDK21
dep "Installing OpenJDK21..."
sudo apt-get -qq install openjdk-21-jre openjdk-21-jdk -y

# Install xdg-terminal-exec (optional)
if check_response "Do you want to install xdg-terminal-exec? [y/N] " "N"; then
	dep "Install xdg-terminal-exec"
	sudo apt-get -qq install xdg-terminal-exec -y
fi

# Check for uv
dep "Checking for uv..."
if ! command -v uv >/dev/null 2>&1; then
    dep "Installing uv via pipx..."
    pipx install uv
else
    dep "Found a uv installation"
fi

# Check for docker
dep "Checking for docker.."
if ! command -v docker >/dev/null 2>&1; then
	dep "Installing docker.."
	bash ./install_dockerrepo.sh
	sudo apt-get -qq update
	sudo apt-get -qq install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
	sudo usermod -aG docker "$suser"
else
	dep "Found a docker installation"
fi

dep "All Dependencies installed"
}

advise() {
	cat >&2 <<USAGE
	This script will install necessary dependencies which are listed in the README.
	However, it is recommended to do this manually.
USAGE
}