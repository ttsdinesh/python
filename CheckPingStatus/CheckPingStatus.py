# /usr/lib/python2.7
# Ping a host/IP at a particular interval and log packet loss in %

import commands
import time
import datetime

_target_host = "172.30.0.10"
_ping_timeout = str(5)  # In seconds
_sleep = 3 # In seconds
_output_file = "/tmp/check_ping_status"


def main():

    while True:
        filewriter = open(_output_file, "a+")
        ping_op = commands.getoutput("ping -w" + _ping_timeout + " -c1 " + _target_host + " | grep -oP '\d+(?=% packet loss)'")

        filewriter.write( str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " -> " + ping_op + "% packet loss \n" );
        time.sleep(_sleep);
        filewriter.close();

main()
