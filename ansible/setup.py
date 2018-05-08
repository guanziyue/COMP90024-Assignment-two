import boto
import json
from boto.exception import EC2ResponseError
import sys
import time
import argparse
from boto.ec2.regioninfo import RegionInfo
import re


# access_key and password. from dashboard>project> access and security>API access >view
EC2_ACCESS_KEY = '89ec4102a2394e1c83461dbea2a02fcf'
EC2_ACCESS_PASSWORD = 'a25b61b08d3a4bd6bca1eb1d55927d6d'
# establish connection
# modify code from lecture5
ec2_conn = boto.connect_ec2(aws_access_key_id=EC2_ACCESS_KEY,
                            aws_secret_access_key=EC2_ACCESS_PASSWORD,
                            is_secure=True,
                            region=RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au'),
                            port=8773,
                            path='/services/Cloud',
                            validate_certs=False)


# end of modified code

# def get_host_group(ip_address):
#     if len(ip_address) == 0:
#         print('no ip given, return back')
#         return None
#     else:
#         new_group = Group(name='new_group')
#         for ip in ip_address:
#             host = Host(name=ip, port=22)
#             new_group.add_host(host)
#     return new_group


if __name__ == '__main__':
    # parse arguments
    arguments_parser = argparse.ArgumentParser()
    arguments_parser.add_argument('-c', type=str, help='setup or delete')
    arguments_parser.add_argument('-n', type=int, default=4, help='amount of instances')
    arguments_parser.add_argument('-v', type=int, default=250, help='indicate volume size')

    args = arguments_parser.parse_args()
    # if argument out of range
    if not args.c:
        arguments_parser.print_help()
        sys.exit(0)
    # setup VMs
    elif args.c.lower() == 'setup':
        instance_amount = args.n
        volume_size = args.v
        instances = []
        ip_address = []
        try:
            # initialize VM one by
            original=[]
            f=open('/etc/ansible/hosts','r')
            for line in f.readlines():
                if re.findall(r'\[new\]',line):
                    original.append(line)
                    f.close()
                    break
                else:
                    original.append(line)
            for i in range(instance_amount):
                reservation = ec2_conn.run_instances('ami-e2d5e55e',
                                                     key_name='cloud',
                                                     instance_type='m1.medium',
                                                     security_groups=['default'],
                                                     placement='melbourne-qh2')
                instances.append(reservation.instances[0])
                print('instance id:{} is created'.format(reservation.instances[0].id))
                while reservation.instances[0].state != "running":
                    print('instance being launched,Please wait.')
                    time.sleep(5)
                    reservation.instances[0].update()
                print('instance status'.format(reservation.instances[0].state))
                original.append('{} ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa'.format(reservation.instances[0].private_ip_address))
                print('instance ip address is {}'.format(reservation.instances[0].private_ip_address))
            with open('/etc/ansible/hosts','w+') as output:
                for line in original:
                    output.write(line)
            time.sleep(60)
        except EC2ResponseError as err:
            print("instance cannot be created:")
            print(err.message)
            ec2_conn.terminate_instances(instance_ids=[lambda x: x.id for instance in instances])
            sys.exit(0)
        else:
            try:
                if volume_size != 0:
                    # attach volumes to each VM
                    for instance in instances:
                        timeout_count = 0
                        while instance.state != "running":
                            if timeout_count > 12:
                                print('instance: {} is still {}. Volume attachment time out. Please check.'.format(
                                    instance.id,
                                    instance.state))
                                sys.exit(0)
                            time.sleep(5)
                            timeout_count += 1
                            instance.update()
                            print('instance: {}, is {}'.format(instance.id, instance.state))
                        vol_req = ec2_conn.create_volume(int(volume_size / instance_amount), 'melbourne-qh2')
                        ec2_conn.attach_volume(vol_req.id, instance.id, '/dev/vdc')
            except EC2ResponseError as err:
                print('volume attached fail, please check your dashboard.')
                print(err.message)
                sys.exit(0)
        # # setup ansible
        # print ('setup ansible')
        # loader = DataLoader()
        # this_inventory = InventoryManager(loader)
        # this_inventory.add_group(get_host_group(ip_address))
        # this_inventory.subset('new_group')
        # this_inventory.refresh_inventory()
        # Options = namedtuple('Options',
        #                      ['listtags', 'listtasks', 'listhosts','syntax','connection', 'module_path', 'forks', 'remote_user', 'private_key_file',
        #                       'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args',
        #                       'become', 'become_method', 'become_user', 'verbosity', 'check'])
        # options = Options( listtags=False, listtasks=False, listhosts=False,syntax=False,connection='ssh', module_path=None, forks=100, remote_user='ubuntu',
        #                   private_key_file='id_rsa',
        #                   ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None,
        #                   become=True,
        #                   become_method=None, become_user='root', verbosity=None, check=False)
        # resultcallback = ResultCallback()
        # passwords = {}
        # varsmanager = VariableManager(loader=loader,inventory=this_inventory)
        # print('playbook start')
        # path='install.yml'
        # play_a_book = ansible.playbook.PlayBook(playbook=[path],
        #                                inventory=this_inventory,
        #                                options=options,
        #                                loader=loader,
        #                                passwords=passwords,
        #                                variable_manager=varsmanager,
        #                                )
        # status=play_a_book.run()
        # print(json.dumps(status, sort_keys=True, indent=4, separators=(',', ': ')))
    # terminate all VMs
    elif args.c.lower() == 'delete':
        try:
            id_list = []
            for instance in ec2_conn.get_only_instances():
                id_list.append(instance.id)
            ec2_conn.terminate_instances(instance_ids=id_list)
            print('all instance terminated.')
        except EC2ResponseError as err:
            print('cannot terminate instances')
            print(err.message)
            sys.exit(0)
    else:
        arguments_parser.print_help()
        sys.exit(0)
