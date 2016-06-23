# /usr/lib/python2.7

# This scripts scans for the external HDD and when added, copies the movies from
# local drive to the external HDD

# Call this script from cron. Below is the cron for everyminute
# * * * * * <script_file> >> <log_file>

# TODO - make the script to run only once after the HDD is connected.

from subprocess import Popen, PIPE
import shutil as copyUtil

local_drive = "/home/dinesh/Downloads/*"
external_HDD_ID = "NA7NT4KK"
external_HDD_Locations = "/run/media/dinesh/DINESH_HDD/videos/movie"
op_command = "cp -r -n " + local_drive + " " + external_HDD_Locations
grep_command = "dmesg | tail -20 | grep 'NA7NT4KK'"


def main():
    p = Popen(grep_command, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()

    if p.returncode is 0:
        print "Found the HDD attached. Copying from " + local_drive + " to " + external_HDD_Locations
        p = Popen(op_command, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        if p.returncode is 0:
            print "Copied the files..."
        else:
            print "Error copying the files..."
    else:
        print "External HDD not attached. Exiting...."

main()
