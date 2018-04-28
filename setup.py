import boto
from boto.exception import EC2ResponseError
import sys
import time
import argparse
from boto.ec2.regioninfo import RegionInfo
import xml.dom.minidom

# access_key and password. from dashboard>project> access and security>API access >view
EC2_ACCESS_KEY = '163ce2ab5bc04a60ac6ca87a35f05a1e'
EC2_ACCESS_PASSWORD = '807cb765017847a18467589ab2c16107'
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
        try:
            # initialize VM one by one
            for i in range(instance_amount):
                reservation = ec2_conn.run_instances('ami-e2d5e55e',
                                                     key_name='cloud',
                                                     instance_type='m1.medium',
                                                     security_groups=['default'],
                                                     placement='melbourne-qh2')
                instances.append(reservation.instances[0])
                print('instance id:{} is created'.format(reservation.instances[0].id))
        except EC2ResponseError as err:
            print("instance cannot be created:")
            print(err.message)
            ec2_conn.terminate_instances(instance_ids=[lambda x: x.id for instance in instances])
            sys.exit(0)
        else:
            try:
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
                    vol_req = ec2_conn.create_volume(int(250 / instance_amount), 'melbourne-qh2')
                    ec2_conn.attach_volume(vol_req.id, instance.id, '/dev/vdc')
            except EC2ResponseError as err:
                print('volume attached fail, please check your dashboard.')
                print(err.message)
                sys.exit(0)
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
