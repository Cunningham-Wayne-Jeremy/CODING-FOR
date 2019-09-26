#Max doesnt run his scripts with sudo ask him how? till then we will run the
#Code with sudo name.sh
#you will need a script to install ruby
#test = `ls -a`
#system("ls")
#updates the system and answers yes to any questions


#Well I cannot seem to use a ruby script that will isntall packages so I think
#That configuration will be done by ruby but installation will require a #!/usr/bin/env bash
#script.
apt update -y
#Installs easy-rsa and openvpn. I think for user credentials we still need easy-rsa
#even though you are running the script with sudo you still need to mention sudo
#below when installing packages interesting
sudo apt install openvpn easy-rsa -y
make-cadir ~/openvpn-ca && cd ~/openvpn-ca

ruby configuration.rb
#Maybe when we are done we can have the bash script reference out configuration ruby script.
