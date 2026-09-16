#!/bin/bash

install_dep() {
#who is the user behind sudo (add to docker group)?
suser=$(sudo sh -c 'echo $SUDO_USER')

dep() { echo "--[DEP] $*" >&2; }

if command -v apt-get >/dev/null 2>&1; then
	package_manager=apt
	basic_packages=(curl git ca-certificates pipx)
	jdk_packages=(openjdk-21-jre openjdk-21-jdk)
	docker_packages=(docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin)
elif command -v pacman >/dev/null 2>&1; then
	package_manager=pacman
	basic_packages=(curl git ca-certificates python-pipx)
	jdk_packages=(jdk21-openjdk)
	docker_packages=(docker docker-buildx docker-compose)
else
	dep "Unsupported package manager (supported: apt, pacman)"
	return 1
fi

pkg_update() {
	case "$package_manager" in
		apt)
			sudo apt-get -qq update
			;;
		pacman)
			# Do not refresh package databases here.
			# Refreshing with -Sy without a full upgrade can create
			# an unsupported partial-upgrade state on Arch.
			;;
	esac
}

pkg_install() {
	case "$package_manager" in
		apt)
			sudo apt-get -qq install -y "$@"
			;;
		pacman)
			sudo pacman -S --needed --noconfirm "$@"
			;;
	esac
}

aur_install() {
	local package="$1"
	local helper

	for helper in paru yay aura pikaur trizen; do
		if ! command -v "$helper" >/dev/null 2>&1; then
			continue
		fi

		dep "Trying to install $package using $helper..."

		case "$helper" in
			paru|yay|pikaur|trizen)
				if sudo -u "$suser" "$helper" -S --needed --noconfirm "$package"; then
					return 0
				fi
				;;
			aura)
				if sudo -u "$suser" aura -A --noconfirm "$package"; then
					return 0
				fi
				;;
		esac

		dep "$helper failed to install $package"
	done

	return 1
}

# Install git, curl, certificate-keyring and pipx
dep "Installing the Basics.."
pkg_update
pkg_install "${basic_packages[@]}"

# Create keyrings directory (apt only)
if [[ "$package_manager" == "apt" ]]; then
	dep "Installing certificate-keyring..."
	sudo install -m 0755 -d /etc/apt/keyrings
fi

# Install JDK21
dep "Installing OpenJDK21..."
pkg_install "${jdk_packages[@]}"

# Install xdg-terminal-exec (optional)
if check_response "Do you want to install xdg-terminal-exec? [y/N] " "N"; then
	dep "Install xdg-terminal-exec"

	if [[ "$package_manager" == "pacman" ]]; then
		# Try the official repositories first. If unavailable there,
		# fall back to an already-installed AUR helper.
		if ! pkg_install xdg-terminal-exec; then
			dep "xdg-terminal-exec not available through pacman, trying AUR helpers..."

			if ! aur_install xdg-terminal-exec; then
				dep "Could not install xdg-terminal-exec."
				dep "Install it manually or install a supported AUR helper."
			fi
		fi
	else
		pkg_install xdg-terminal-exec
	fi
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

	if [[ "$package_manager" == "apt" ]]; then
		bash ./install_dockerrepo.sh
		pkg_update
	fi

	pkg_install "${docker_packages[@]}"
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
