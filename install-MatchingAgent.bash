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

git config user.email "root@assetmanager.bsi.corp"

apt install -y postgresql
systemctl start postgresql
systemctl enable postgresql

sudo -i -u postgres psql -f /home/Matching-Agent/initdb.sql

# apt-get -y install postgresql postgresql-contrib
# cp /home/Matching-Agent/pg_hba.conf /etc/postgresql/16/main/
# service postgresql start
# sudo -i -u postgres createuser -d -e -s -P analyst
# sudo -i -u postgres createdb -e cachedb

curl -LsSf https://astral.sh/uv/install.sh | sh

cd /home

echo "Installation MatchingAgent finished!"
echo "rebooting now"
reboot

