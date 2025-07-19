#!/bin/bash
#
#####################################################
#
#  Projekt: BSI-625
#  Matching Agent installation
#  file: install-MatchingAgent.bash
#
#####################################################


echo "Installation MatchingAgent starting..."

apt install -y postgresql
systemctl start postgresql
systemctl enable postgresql

sudo -i -u postgres psql -f /home/Matching-Agent/initdb.sql

curl -LsSf https://astral.sh/uv/install.sh | sh

cd /home

echo "Installation MatchingAgent finished!"
echo "rebooting now"
reboot

