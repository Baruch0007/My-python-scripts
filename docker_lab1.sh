#!/bin/bash
exit="yes" 
while [ $exit == "yes" ] || [ $exit == "y" ]
do
	echo -e "\nMENUE: Choose number 1-6\n1. Installation of 2 images\n2. Run nginx containers ans choose ports for each container\n3. Put the internals IP addresses of all container to log file\n4. Run container of docker ui and check if it works through browser and put his internal IP into log file"
	read num

	if [ $num == "1" ]
	then
		echo -e "Choose 2 images to install:  nginx / abh1nav/dockerui ?\n"
		num_of_images=0
		while [ $num_of_images -lt 2 ]
		do
			read image
			if [ $image == "nginx" ] || [ $image == "abh1nav/dockerui"]
			then
				let num_of_images=num_of_images+1
				sudo docker pull $image
				if [ $num_of_images == 2 ]
				then
					break
				fi
				echo -e "\nChoose the next image"
				sleep 2
			else
				echo -e "There is  no such an image, type again\n"
			fi
		done
		sleep 2
		echo  -e "\nYou installed 2 images successfully\n"

	elif [ $num == "2" ]
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
		echo -e "\nThe table of RUNNING containers only:\n"
		sleep 2
		sudo docker ps
		echo -e "\nDo you want to remove/stop all of these RUNNING containers? if no press enter"
		read action
		if [ $action == "remove" ]
		then
			for i in `sudo docker ps | awk '{print $1}'` ; do `sudo docker rm -f $i` ; done 2>/dev/null
		elif [ $action == "stop" ]
		then
			for i in `sudo docker ps | awk '{print $1}'` ; do `sudo docker stop $i` ; done	2>/dev/null
		else
			echo -e "OK, leave them running" 2>/dev/null
		fi
		echo -e "\nThe updated table of RUNNING containers:\n"
		sleep 2
		sudo docker ps


        elif [ $num == "3" ]
        then
		echo -e "\nNOT DONE YET\n"
        elif [ $num == "4" ]
        then
		echo -e "\nNOT DONE YET\n"
        elif [ $num == "5" ]
        then
		echo -e "\nNOT DONE YET\n"
        elif [ $num == "6" ]
        then
		echo -e "\nNOT DONE YET\n"
	else
		echo -e "\n Enter 1-6 only"
		continue
	fi
	sleep 3
	echo -e "\nDo you want go back to menue? yes/no?"
	read exit
done
echo -e "\nThank you, bye bye"

