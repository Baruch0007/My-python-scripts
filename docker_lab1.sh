#!/bin/bash


exit="yes" 
while [ $exit == "yes" ] || [ $exit == "y" ]
do
	echo -e "\nMENUE:\n1. To pull images\n2. Run nginx containers and choose port for each container\n3. Put the internals IP addresses of all containers to log file\n4. Run container of docker ui and check if it works through Wget \n5. We will create html file  at this VM in some directory, then mount directories (between VM and container),\n   make some changes at the content of the html file throuth the VM directory,\n   and afterwards check through Wget if it has changed\n6. To stop/remove all containers\n7. To remove all images\n"
	read num

	if [ $num == 1 ]
	then
		#echo -e "Choose images to install:  nginx / abh1nav/dockerui / jenkins / centos / ubuntu?\n"
		pulled_images=0
		while true
		do
			echo -e "Choose images to install:  nginx / abh1nav/dockerui / jenkins / centos / ubuntu?\n"
			read image 2>/dev/null
			sudo docker pull $image 2>/dev/null
			for i in `sudo docker images | awk '{print $1}'` ; do if [ $i == $image ] ; then  let pulled_images=pulled_images+1 ; else echo "There is no such a image" ; fi ; done 2>/dev/null
			echo -e "\nTo pull another image press n (next), to go back to menue press Enter\n"
			read action
			if [ $action == n ]
			then
				continue
			else
				echo -e "\nNumbers of images were pulled: $pulled_images\n"
				break
			fi
		done
		sleep 2
		echo -e "The updates images table:\n"
		sudo docker images

	elif [ $num == 2 ]
	then
	container_num=1
		echo -e "Enter the number of nginx countainers you want to run\n"
		read total
		while [ $container_num -le $total ]
		do
			echo -e "\nChoose port number for container number: $container_num\n"
			read port
			if [ $port == 80 ]
			then
				echo -e "This port unavailable, Choose another port\n"
				continue
			elif [ $port -gt 1 ] && [ $port -le 65535 ]
			then
				sudo docker run -d -p $port:80 nginx 2>/dev/null
				let container_num=container_num+1
			else
				echo -e "choose port number 1-65535 only\n"
				continue
			fi
		done
		echo -e "\nThe running containers table\n"
		sleep 2
		sudo docker ps


        elif [ $num == 3 ]
        then
		echo -e "" > IPs.log
		for i in `sudo docker ps | awk '{print $1}'` ; do echo `sudo docker inspect $i | grep IPAddress | awk 'NR==2 {print $2}' | cut -d '"' -f2` >> /home/ubuntu/Desktop/docker_lab/IPs.log ; done  2>/dev/null
		ls -l | grep log
		echo -e "\nThe content of the log file `cat IPs.log`"
        elif [ $num == 4 ]
        then
		sudo docker run -d -p 9050:9000 -v /var/run/docker.sock:/docker.sock abh1nav/dockerui:latest -e="/docker.sock" 2>/dev/null
		sudo docker ps
		echo -e "\nDo you want see the inspect of the web page? y/n\n"
		read show_inspect
		if [ $show_inspect == y ]
		then
			wget 34.227.112.19:9050
			cat index.html
			rm index*
			sleep 3
		else
			echo -e "\nOK\n"
			sleep 2
		fi

        elif [ $num == 5 ]
        then
		mkdir /home/ubuntu/Desktop/web 2>/dev/null && cd /home/ubuntu/Desktop/web && touch index.html 2>/dev/null
		echo -e "\nWe are at directory:\n`pwd`\n\nWe created html file:\n`ls -l`\n"
		echo -e "Now we will run nginx container and mount directories"
		sudo docker run -d -p 8001:80 -v /home/ubuntu/Desktop/web/:/usr/share/nginx/html nginx 2>/dev/null
		echo
		sudo docker ps
		sleep 2
		echo -e "\nWget to 34.227.112.19:8001, it will dowload the html file to the script direcory"
		sleep 2
		wget 34.227.112.19:8001
		echo -e "\nThe content of the downloaded html file:\n"
		sleep 2
		
		script_path=`sudo find / -name $0 | sed 's/'$0'//'`
		
		cd  $script_path
		cat index.html
		rm index*
		echo -e "\nDo you want to edit htnk file? y/n?\n"
		read action
		if [ $action ==  'y' ]
		then
			nano /home/ubuntu/Desktop/web/index.html
			echo -e "Wget to 34.227.112.19:8001\n"
			wget 34.227.112.19:8001
			echo -e "\nThe updated  content of the downloaded html file:\n"
			sleep 2
			cat index.html
			rm index*
		else
			echo -e "OK"
		fi

	elif [ $num == 6 ]
	then
		 echo -e "\nType stop / remove\n"
                read action
                if [ $action == remove ]
                then
                        for i in `sudo docker ps | awk '{print $1}'` ; do `sudo docker rm -f $i` ; done 2>/dev/null
                elif [ $action == stop ]
                then
                        for i in `sudo docker ps | awk '{print $1}'` ; do `sudo docker stop $i` ; done  2>/dev/null
                else
                        echo -e "OK, leave them running" 2>/dev/null
                fi
                echo -e "\nThe updated RUNNING containers table:\n"
                sleep 2
                sudo docker ps
	elif [ $num == 7 ]
        then
		for i in `sudo docker images | awk '{print $3}'` ; do `sudo docker rmi -f $i` ; done 2>/dev/null
		echo -e "The updates images table:\n"
		sleep 2
		sudo docker images
	else

		echo -e "\n Choose 1-7 only"
		continue
	fi
	sleep 3
	echo -e "\nDo you want go back to menue? y/n?"
	read exit
done
echo -e "\nThank you, bye bye"

