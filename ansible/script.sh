#!/bin/sh
python3 setup.py -c setup -n 1 -v 0
ansible-playbook install.yml