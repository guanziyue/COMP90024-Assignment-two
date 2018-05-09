#!/bin/sh
python3 setup.py -c $1 -n $2 -v $3
ansible-playbook install.yml