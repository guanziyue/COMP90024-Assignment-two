import boto
import sys
import time
from boto.ec2.regioninfo import RegionInfo

# copy code from lecture
region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
# access_key and password. from dashboard>project> access and security>API access >view
ec2_conn = boto.connect_ec2(aws_access_key_id='163ce2ab5bc04a60ac6ca87a35f05a1e',
                            aws_secret_access_key='807cb765017847a18467589ab2c16107',
                            is_secure=True,
                            region=region,
                            port=8773,
                            path='/services/Cloud',
                            validate_certs=False)
# end of copy code
# get all instances
reservations = ec2_conn.get_all_reservations()
# if there is no instance, set up
if not reservations:
    # get how many instance should we create
    instance_amount = sys.argv[1]
    for i in range(int(instance_amount)):
        # creat instance ami-190a1773 is 16.04 Ubuntu official image. key name is security key pair name.
        reservation = ec2_conn.run_instances('ami-190a1773',
                                             key_name='cloud',
                                             instance_type='m1.medium',
                                             security_groups=['default'])
    # get reservation
    reservations = ec2_conn.get_all_reservations()
    # traversal all instance, attach volume for them
    for instance in reservations[0].instances:
        # first check status of instance
        while instance.state != "running":
            time.sleep(5)
            instance.update()
            print(instance.state)
        vol_req = ec2_conn.create_volume(250 / instance_amount, 'melbourne-qh2')
        ec2_conn.attach_volume(vol_req.id, instance.id, '/dev/vdc')
