import boto
import sys
from boto.ec2.regioninfo import RegionInfo
# copy code from lecture
region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
# access_key and password. from dashboard>project> access and security>API access >view
ec2_conn = boto.connect_ec2(aws_access_key_id='89ec4102a2394e1c83461dbea2a02fcf',
                            aws_secret_access_key='a25b61b08d3a4bd6bca1eb1d55927d6d',
                            is_secure=True,
                            region=region,
                            port=8773,
                            path='/services/Cloud',
                            validate_certs=False)
reservations = ec2_conn.get_all_reservations()
print('\nID: {}\tIP: {}\tPlacement: {}'.format(reservations[0].id,
 reservations[0].instances[0].private_ip_address,
 reservations[0].instances[0].image_id,
 reservations[0].instances[0].placement))