#!/bin/bash

# Install packages
echo "*** update & upgrade"
sudo apt-get update
sudo apt-get upgrade -y

# Install python3
echo "*** install python3"
sudo apt install python3-pip

# Install apache2
echo "*** install apache2"
sudo apt-get install apache2 sqlite -y
sudo apt-get install php7.3 php7.3-gd php7.3-sqlite3 php7.3-curl libapache2-mod-php -y
sudo apt-get install php php-gd php-sqlite3 php-curl libapache2-mod-php -y
sudo apt-get install smbclient -y
sudo apt install -y apache2 mariadb-server libapache2-mod-php7.3 php7.3-gd php7.3-json php7.3-mysql php7.3-curl php7.3-intl php7.3-mcrypt php-imagick php7.3-zip php7.3-xml php7.3-mbstring
sudo apt-get install php-mysql php-mbstring php-gettext php-intl php-redis php-imagick php-igbinary php-gmp php-curl php-gd php-zip php-imap php-ldap php-bz2 php-phpseclib php-xml -y
sudo systemctl enable apache2

# Install mariadb
echo "*** install mariadb"
sudo a2enmod rewrite
sudo apt install mariadb-server mariadb-client -y

cd /var/www/html
sudo rm index.html
sudo chown -R www-data:www-data /var/www/
cd /home/pi

#download & unzip owncloud
echo "*** download en install owncloud"
sudo wget https://download.owncloud.org/community/owncloud-complete-20200731.zip
sudo mv owncloud-complete-20200731.zip /var/www/html
cd /var/www/html
sudo unzip -q owncloud-complete-20200731.zip
echo "*** unzip goed"
sudo mkdir owncloud
cd owncloud
sudo mkdir data
sudo chown www-data:www-data /var/www/html/owncloud/data
sudo chmod 750 /var/www/html/owncloud/data
sudo cp -r /home/pi/birdCam/apps-external /var/www/html/owncloud
sudo cp /home/pi/birdCam/owncloud.db /var/www/html/owncloud/data
sudo chmod 777 /var/www/html/owncloud/apps-external

# Install camera
echo "*** install pi cam"
sudo apt install python3-picamera -y

# Install mp4Box
echo "*** install mp4box"
sudo apt install gpac -y

# copy directory
echo "*** make USBdrive"
sudo mkdir /mnt/USBdrive
# install library 
echo "*** install library  for camera_PIR_mp4.py"
sudo apt install python3-gpiozero
sudo apt install python-gpiozero
sudo pip3 install gpiozero
sudo pip install gpiozero
sudo cp /home/pi/birdCam/PythonScript.py /home/pi
cd /home/pi/birdCam
echo "*** copy camera.py complete"

echo "*** autostart Python Script"
sudo cp rc.local /etc/rc.local
echo "*** enable start PythonScript on reboot OK"

# Install hotspot
sudo apt install hostapd -y
sudo apt install dnsmasq -y
sudo DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent

sudo cp -r /home/pi/BirdBox/pi-ap /home/pi
cd /home/pi/pi-ap
sudo chmod 755 install.sh
sudo chmod 755 ap-config.sh
sudo chmod 755 dns.sh
sudo chmod 755 firewall_Default-Policies.sh
sudo chmod 755	firewall_ipv4.sh
sudo chmod 755 firewall_ipv6.sh
sudo chmod 755 functions.sh
sudo chmod 755 hostname.sh
sudo chmod 755 kernel_modifications.sh
sudo chmod 755 login-message.sh
sudo chmod 755 packages.sh
sudo chmod 755 service-pwr-mgmnt-disable.sh
sudo chmod 755 timedate.sh
sudo chmod 755 variables.sh
sudo ./install.sh

