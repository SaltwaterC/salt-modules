# -*- coding: utf-8 -*-
"""
Get the EC2 metadata by wrapping the ec2metadata script from AWS

Author: Ștefan Rusu <saltwaterc@gmail.com>

TODO: make it independent on ec2metatada which is Python anyway. This was the five minute solution for the issue.

"""

import inspect

_ec2meta_wrap = lambda: __salt__['cmd.run']('ec2metadata ' + '--' + inspect.stack()[1][3].replace('_', '-'))

"""
Generated with a little bit of shell magic:

ec2metadata --help 2>&1 | grep "display the" | cut -d "-" -f 3-4 | cut -d " " -f 1 | sed 's/-/_/g' | sed 's/^/def /' | sed 's/$/():\n\treturn _ec2meta_wrap()\n/'
"""

def kernel_id():
	return _ec2meta_wrap()

def ramdisk_id():
	return _ec2meta_wrap()

def reservation_id():
	return _ec2meta_wrap()

def ami_id():
	return _ec2meta_wrap()

def ami_launch():
	return _ec2meta_wrap()

def ami_manifest():
	return _ec2meta_wrap()

def ancestor_ami():
	return _ec2meta_wrap()

def product_codes():
	return _ec2meta_wrap()

def availability_zone():
	return _ec2meta_wrap()

def instance_id():
	return _ec2meta_wrap()

def instance_type():
	return _ec2meta_wrap()

def local_hostname():
	return _ec2meta_wrap()

def public_hostname():
	return _ec2meta_wrap()

def local_ipv4():
	return _ec2meta_wrap()

def public_ipv4():
	return _ec2meta_wrap()

def block_device():
	return _ec2meta_wrap()

def security_groups():
	return _ec2meta_wrap()

def mac():
	return _ec2meta_wrap()

def profile():
	return _ec2meta_wrap()

def instance_action():
	return _ec2meta_wrap()

def public_keys():
	return _ec2meta_wrap()

def user_data():
	return _ec2meta_wrap()
