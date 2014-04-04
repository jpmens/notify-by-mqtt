# notify-by-mqtt

a Nagios/Icinga notification module which wraps data into JSON and fires it off to an MQTT broker.

As an example payload:

```json
{
    "_type": "icinga", 
    "date": "2014-04-04", 
    "eventstarttime": "1396621975", 
    "hostdisplayname": "localhost", 
    "hostname": "localhost", 
    "hoststatetype": "HARD", 
    "servicedesc": "JPtest", 
    "servicedisplayname": "JPtest", 
    "serviceoutput": "CRITICAL: file /tmp/f1: ENOENT", 
    "servicestate": "CRITICAL", 
    "servicestateid": "2", 
    "shortdatetime": "2014-04-04 16:38:25", 
    "time": "16:38:25", 
    "timet": "1396622305"
}
```
