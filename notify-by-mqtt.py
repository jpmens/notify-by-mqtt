#!/usr/bin/env python

__author__    = 'Jan-Piet Mens <jpmens()gmail.com>'
__copyright__ = 'Copyright 2014 Jan-Piet Mens'
__license__   = """Eclipse Public License - v 1.0 (http://www.eclipse.org/legal/epl-v10.html)"""

import paho.mqtt.publish as mqtt  # pip install --upgrade paho-mqtt
try:
    import json
except ImportError:
    import simplejson as json
import os

hostname = '127.0.0.1'
port = 1883
qos=0
retain=False
auth=None
prefix = 'ICINGA_'

data = {
    "_type" : "icinga"
    }

env_keys = [
    'DATE',                 # 2014-04-04
    'EVENTSTARTTIME',       # 1396620153
    'SHORTDATETIME',        # 2014-04-04 16:02:53
    'TIME',                 # 16:02:53
    'TIMET',                # 1396620173
    ]

for key in env_keys:
    val = os.getenv(prefix + key, None)
    if val is not None:
        data[key.lower()] = val


state = os.getenv(prefix + 'SERVICESTATE', '').lower()
if state is None or state == '':
	state = os.getenv(prefix + 'HOSTSTATE', '').lower()
	if state is None or state == '':
		state = 'unknown'
	else:
		env_keys = [
		    'HOSTDISPLAYNAME',      # localhost
		    'HOSTNAME',             # localhost
		    'HOSTSTATE',            # UP
		    'HOSTSTATETYPE',        # HARD
		    'HOSTSTATEID',          # 2
		    'HOSTOUTPUT',           # Ping OK
		    ]

		for key in env_keys:
		    val = os.getenv(prefix + key, None)
		    if val is not None:
		        data[key.lower()] = val

else:
	env_keys = [
	    'HOSTDISPLAYNAME',      # localhost
	    'HOSTNAME',             # localhost
	    'HOSTSTATE',            # UP
	    'HOSTSTATETYPE',        # HARD
	    'SERVICEDESC',          # JPtest
	    'SERVICEDISPLAYNAME',   # JPtest
	    'SERVICEOUTPUT',        # File /tmp/f1 is missing
	    'SERVICESTATE',         # CRITICAL
	    'SERVICESTATEID',       # 2
	    ]

	for key in env_keys:
	    val = os.getenv(prefix + key, None)
	    if val is not None:
	        data[key.lower()] = val


topic = 'monitoring/' + state

payload = None
try:
    payload = json.dumps(data)
except:
    pass

rc = mqtt.single(topic, payload,
            qos=qos, retain=retain,
        hostname=hostname, port=port,
        auth=auth)
