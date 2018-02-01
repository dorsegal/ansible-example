Get your environment ready
---
You'll need a linux machine with the ability to run vms.

1. Make sure you have python 2.7 installed. (Ubuntu 14.04 is highly recommended).
1. Install Ansible (version 2.1).
1. Install Vagrant.
1. Install VirtualBox.
1. Run `vagrant up base` and make sure you can ssh into the machine using `vagrant ssh base`.

Developing
---

Copy `example` role and rename `example` to your service name.
Add files under `files/your_service`
make sure main `.py` file is in the same name of you service.
ex. if you service called `panda` then python script should be `panda.py`

next add your service to ansible script by adding this line in `base.yml`
`- { role: your_service, tags: your_service }`

Deployment
---

To deploy services simply run this command to deploy all services: <br/>
`ansible-playbook base.yml -i dev/hosts`

if you want specific service just add `-t your_service`: <br/>
`ansible-playbook base.yml -i dev/hosts -t your_service`


Usage
---

###img-panda 
Open your browser, go to <http://localhost:8080> and you will get random pandas on your screen.

###smart-panda
Open your browser, go to <http://localhost:8090> and you will the number of time you did POST to <http://localhost:8090> <br/>
To test it run `curl -X POST localhost:8090` 