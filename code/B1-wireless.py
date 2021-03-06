#!/usr/bin/env python3

from argparse import ArgumentParser

from asynciojobs import Scheduler

from apssh import SshNode, SshJob, Run
from apssh import RunString

##########
gateway_hostname  = 'faraday.inria.fr'
gateway_username  = 'inria_r2lab.tutorial'
verbose_ssh = False
wireless_driver="ath9k"
wireless_interface="atheros"

parser = ArgumentParser()
parser.add_argument("-s", "--slice", default=gateway_username,
                    help="specify an alternate slicename, default={}"
                         .format(gateway_username))
parser.add_argument("-v", "--verbose-ssh", default=False, action='store_true',
                    help="run ssh in verbose mode")
args = parser.parse_args()

gateway_username = args.slice
verbose_ssh = args.verbose_ssh

##########
faraday = SshNode(hostname = gateway_hostname, username = gateway_username,
                  verbose = verbose_ssh)

node1 = SshNode(gateway = faraday, hostname = "fit01", username = "root",
                verbose = verbose_ssh)
node2 = SshNode(gateway = faraday, hostname = "fit02", username = "root",
                verbose = verbose_ssh)

##########
check_lease = SshJob(
    # checking the lease is done on the gateway
    node = faraday,
    # this means that a failure in any of the commands
    # will cause the scheduler to bail out immediately
    critical = True,
    command = Run("rhubarbe leases --check"),
)

####################
# This is our own brewed script for setting up a wifi network
# it run on the remote machine - either sender or receiver
# and is in charge of initializing a small ad-hoc network
#
# Thanks to the RunString class, we can just define this as
# a python string, and pass it arguments from python variables
#

turn_on_wireless_script = """#!/bin/bash

# we expect the following arguments
# * wireless driver name (iwlwifi or ath9k)
# * wireless interface name (intel or atheros)
# * IP-address/mask for that interface
# * the wifi network name to join
# * the wifi frequency to use

driver=$1; shift
ifname=$1; shift
ipaddr_mask=$1; shift
netname=$1; shift
freq=$1;   shift

# load the r2lab utilities - code can be found here:
# https://github.com/parmentelat/r2lab/blob/master/infra/user-env/nodes.sh
source /root/r2lab/infra/user-env/nodes.sh

# make sure to use the latest code on the node
git-pull-r2lab

turn-off-wireless

echo loading module $driver
modprobe $driver

# some time for udev to trigger its rules
sleep 1

echo configuring interface $ifname
# make sure to wipe down everything first so we can run again and again
ip address flush dev $ifname
ip link set $ifname down
# configure wireless
iw dev $ifname set type ibss
ip link set $ifname up
# set to ad-hoc mode
iw dev $ifname ibss join $netname $freq
ip address add $ipaddr_mask dev $ifname
"""

##########
# setting up the wireless interface on both fit01 and fit02
init_node_01 = SshJob(
    node = node1,
    required = check_lease,
    command = RunString(
        turn_on_wireless_script,
        wireless_driver, wireless_interface, "10.0.0.1/24", "foobar", 2412,
#        verbose=True,
    ))
init_node_02 = SshJob(
    node = node2,
    required = check_lease,
    command = RunString(
        turn_on_wireless_script,
        wireless_driver, wireless_interface, "10.0.0.2/24", "foobar", 2412))

# the command we want to run in faraday is as simple as it gets
ping = SshJob(
    node = node1,
    required = (init_node_01, init_node_02),
    command = Run(
        'ping', '-c', '20', '10.0.0.2', '-I', wireless_interface,
#        verbose=True,
    ))

##########
# our orchestration scheduler has 4 jobs to run this time
sched = Scheduler(check_lease, ping, init_node_01, init_node_02)

# run the scheduler
ok = sched.orchestrate()
# give details if it failed
ok or sched.debrief()

success = ok and ping.result() == 0

# return something useful to your OS
exit(0 if success else 1)
