# Steps for deploying private docker image in ICTA SL UDI POC Infrastructure setup (Sandbox Env.)

This guide include steps that can be performed to build and deploy Pre-Registration UI module from private docker registry E.g Docker Hub


#### Instructions :

1. Make a directory and switch to it before  building angular based Pre-Registration UI module

	cd /home/icta-mosip/


	Know your environment and make sure following prerequisite are already there. if not set up accordingly

		- git, node/npm, Angular CLI and docker



  	For (Red Hat 4.8.5-44) Environment


		cat /proc/version curl -sL https://rpm.nodesource.com/setup_12.x | sudo -E bash - sudo yum install nodejs

		node --version 
		npm --version

		npm install -g @angular/cli 			# get Angular latest or a specifi ng version

		docker -version



2. Clone MOSIP’s mosip-ref implmentation repository (https://github.com/ICTASL/mosip-ref-impl.git) into the directory created as above


	git clone https://github.com/ICTASL/mosip-ref-impl.git

	note : currently above one is forked from mosip/mosip-ref-impl repository



3. Update Docker file in order to run as a nginx instance with angular app

	
	FROM nginx
	COPY default.conf /etc/nginx/conf.d/
	COPY dist/pre-registration-ui /usr/share/nginx/html


#### Note : Update .dockerignore and Dockerfile accordingly


### Below steps have to performed upon proper updation of Step 3.


4. Build the Angular app from pre-registration-ui directory

	ng build --prod --base-href .

	Login into related Docker Hub

	docker login --username=udipoc --password=<password>



5.  login to docker registry and list existing images/container list in the loval environment

	docker images

	docker ps -a 			#list currently running images in env

        docker container list
	
	

5.1   Build the docker image


        docker build -t <docker-username/image-name-with-version> .

	E.g.  docker build -t udipoc/pre-registration-ui:1.1.3 .


5.2   Tag Docker image

	E.g.  docker tag d2aef248131c udipoc/pre-registration-ui:1.1.3



5.3   Run Docker image in local env with given port bindings after checking currentlu used port mapping

	E.g.  docker run -d -p 8080:80 --rm --name nginx udipoc/pre-registration-ui:1.1.3



5.4 Checking whether above created image runanble as proof of validation

	  docker ps -a 							#list currently running images in env

	E.g.  curl http://localhost:8080/pre-registration-ui/#/eng		# check whether is running




5.5   Pushing Docker image to repository you wanted

	E.g.  docker push udipoc/pre-registration-ui:1.1.3




5.6   Deleting unused images after checking

	 E.g.  sudo docker stop  cf5e2a857f08
	
	 E.g.  sudo docker rm cf5e2a857f08

	 E.g.  docker image rm --force 0beae72f7d73



5.7. Pulling images to required envirnment

	E.g. docker pull udipoc/pre-registration-ui:1.1.3



#### Initial docker configuration

#### Below step has already been done in current sandbox environment one time and not needed re-running for each & every docker image


1. If you want to create the docker secrets after the cluster is created please run the below command from sandboxv2 directory in Console:

	for mz:

	an playbooks/docker-secrets.yml --extra-vars "kube_config={{clusters.mz.kube_config}}"

	for dmz:

	an playbooks/docker-secrets.yml --extra-vars "kube_config={{clusters.dmz.kube_config}}"       



2. Pull the images from Docker Hub after login successfully

	E.g. docker pull udipoc/pre-registration-ui:1.1.3



3. Open tmux terminal session and execute prereg module related Ansible script to load modules

	tmux
	an playbooks/prereg.yml


4. Check images

	kc1 get pods | grep prereg




#### Configuration steps for pulling private docker image and deploying it in a MOSIP Sandbox environment

1. Switch to mosip user in sandbox deployed server

	 sudo su - mosipuser


2. Change to /home/mosipuser/mosip-infra/deployment/sandbox-v2

	 cd /home/mosipuser/mosip-infra/deployment/sandbox-v2


3. List the pre reg UI related modules running and stop them

	kc1 get pods | grep prereg


4. Stop/remove existing pre-registration ui modules

	helm1 delete prereg


5. Set a secret in secrets.yml if not set up

	av edit secrets.yml

	docker: server: '' # Default is docker hub 
	username: 'udipoc' 
	password: '<password>'


6. Check whether the created has been loaded by the system
      kc1 get secret 			# to check Whether above defined secret has taken by the system



7. Make changes to all.yml to load images from private repository ( set private and assign a password)

	nano group_vars/all.yml
   
	hub: private: true                     # For private repo on Docker Hub, set this to true, and set credentials in secrets.yml
	keyname: <plaintext secret>            # Name of kubernetes secret


8 . Edit versions.yml to reflect docker image changes required

	ui: 'prereg-ui': 'udipoc/pre-registration-ui:1.1.3'



Note : This guide subject to revision based on perirodic updates from the MOSIP Team

