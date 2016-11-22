title: nepi-ng - the basics
tab: tutorial
float_menu_template: r2lab/float-menu-tutorials.html

<script src="/assets/r2lab/open_tab.js"></script>
<script src="/assets/js/diff.js"></script>
<script src="/assets/r2lab/r2lab-diff.js"></script>
<style>@import url("/assets/r2lab/r2lab-diff.css")</style>

<ul class="nav nav-tabs">
  <li class="active"> <a href="#INTRO">INTRO</a> </li>
  <li> <a href="#A1">A1</a></li>
  <li> <a href="#A2">A2</a></li>
  <li> <a href="#A3">A3</a></li>
  <li> <a href="#A4">A4</a></li>
  <li> <a href="#A5">A5</a></li>
  <li> <a href="#WRAPUP">WRAPUP</a></li>
</ul>


<div id="contents" class="tab-content" markdown="1">

<!------------ INTRO ------------>
<div id="INTRO" class="tab-pane fade in active" markdown="1">
<br>

### Presentation

In this tutorial we will see a few experiments, that run ping
between various locations, and on the networks available to
experimenters in r2lab.

This set of experiments of increasing complexity, that you can see in
the tabs bar above labelled A1 to A*n*, are designed as a series of
small incremental changes, so we can illustrate various concepts one
at a time.

To this end, from one experiment to the other, we highlight the
changes in the source code, in a git-like style: inserted and deleted
lines are shown with a different color, so readers can see what is new
in each tutorial.


### Preparation

Before we can run these experiments however, we need to have

* a valid lease set in the booking system
* the 2 nodes `fit01` and `fit02` up and running

For this first tutorial we will assume that these 2 steps have been
performed manually, and here is how to proceed with that.

### Getting a reservation

Once you are logged in the website, [go to this page](book.md) to get
such a reservation.  In a nutshell, the behaviour in the calendar is
as follows:

* click once in a free slot to create a reservation
* drag a reservation to change it
* double click on a reservation to cancel it
* when you belong in several slices, it can also be useful to drag a slice from the left hand side list right into the calendar. Note that the *current* slice is the one with a back arrow; it is the one that is used when you use single click to create a reservation.

The code in this tutorial assumes you have a slice named `onelab.inria.r2lab.tutorial`, which you will need of course to replace with your actual slice name when trying to run the code yourself.

### Loading images

For loading the images manually on the 2 nodes needed here, please do this (again make sure to use **your slice name** instead of `onelab.inria.r2lab.tutorial`)

```
ssh -i ~/.ssh/onelab.private onelab.inria.r2lab.tutorial@faraday.inria.fr
```

If this results in a `Permission denied` message, it means that you are not properly registered with the testbed. In this case, please make sure that
* you have obtained an account and a project at the Onelab portal
* you have associated the R2lab meta-node named `37-nodes` to your project in the Onelab resources page
* you have downloaded the private key from Onelab, and installed it in `~/.ssh/onelab.private` with proper permissions (typically `chmod 600`)

Feel free to contact us on [the R2lab users mailinglist fit-r2lab-user@inria.fr](mailto:fit-r2lab-user@inria.fr) if none of this is helpful.

***
Once logged in faraday, type the following commands, which were explained [in the previous tutorial](tuto-200-shell-tools.md):

    # it's always a good idea to check you currently own the reservation 
    rleases --check
    # turn off the whole testbed - just in case 
    all-off
    # select nodes 1 and 2
    n 1 2
    # load the default image (on the selected nodes)
    rload
    # wait for ssh to be up (still on the selected nodes)
    rwait

Running `rload`, which is when the default images are loaded on the 2
nodes, is going to take a couple of minutes. Here's what your output
should look like


    onelab.inria.r2lab.tutorial@faraday:~$ rleases --check
    Checking current reservation for onelab.inria.r2lab.tutorial OK
    
    onelab.inria.r2lab.tutorial@faraday:~$ all-off
    reboot05:already off
    reboot19:already off
    reboot28:already off
    reboot04:already off
    ... <snip>
    reboot12:ok
    reboot02:ok
    reboot20:ok
    reboot13:ok
    Turning WiFi OFF
    Starting: Intent { act=android.intent.action.MAIN cmp=com.android.settings/.wifi.WifiSettings }
    Turning OFF phone : turning on airplane mode
    Broadcasting: Intent { act=android.intent.action.AIRPLANE_MODE (has extras) }
    Broadcast completed: result=0
    
    onelab.inria.r2lab.tutorial@faraday:~$ n 1 2
    export NODES="fit01 fit02"
    export NBNODES=2
    
    onelab.inria.r2lab.tutorial@faraday:~$ rload
    16:12:42 - +000s: Selection: fit01 fit02
    16:12:42 - +000s: Loading image /var/lib/rhubarbe-images/default.ndz
    16:12:42 - +000s: AUTH: checking for a valid lease
    16:12:42 - +000s: AUTH: access granted
    16:12:42 - +000s: fit02 reboot = Sending message 'on' to CMC reboot02
    16:12:42 - +000s: fit01 reboot = Sending message 'on' to CMC reboot01
    16:12:43 - +001s: fit02 reboot = idling for 15s
    16:12:43 - +001s: fit01 reboot = idling for 15s
    16:12:59 - +017s: started <frisbeed@234.5.6.1:10001 on default.ndz at 500 Mibps>
    16:12:59 - +017s: fit01 frisbee_status = trying to telnet..
    16:12:59 - +017s: fit02 frisbee_status = trying to telnet..
    ... <snip>
    |############################################################################################|100% |29.56s|Time: 0:00:29
    16:13:44 - +062s: fit02 Uploading successful
    16:13:44 - +062s: fit02 reboot = Sending message 'reset' to CMC reboot02
    16:13:46 - +064s: stopped <frisbeed@234.5.6.1:10001 on default.ndz at 500 Mibps>
    
    onelab.inria.r2lab.tutorial@faraday:~$ rwait
    <Node fit01>:ssh OK
    <Node fit02>:ssh OK

At this point, both nodes have been loaded with the default image. So
you can log out of `faraday.inria.fr` and go back to your laptop to
run [the tutorial in tab A1](javascript:open_tab('A1')).

</div>


<!------------ A1 ------------>
<div id="A1" class="tab-pane fade" markdown="1">

### Objective

Our first experiment code is designed to run on YOUR computer.
From there we trigger a simple command on the R2lab
gateway, that is to say `faraday.inria.fr`; namely we will simply ping the google server `google.fr` from `faraday`, as depicted below.

<center> <img src="/assets/img/A1.png" alt="a1" height="240px"></center>

### Introduction to `nepi-ng`

This example introduces the following classes:

* `SshNode` is a class that represents an ssh connection; in this
  present case we create one sucj object, with our credentials to
  enter `faraday`;
* `SshJob` is a class that allows to describe what commands we want to
  run in an `SshNode`, here one single command is needed;
* `Scheduler` is the class that runs a collection of `SshJob`s - even
  if in our case we only have one, we will soon see why this is useful
  when several nodes are active at the same time.


### The code

<center>Download the <a href="/code/A1-ping.py" download target="_blank">A1 experiment</a> code</center>

<!-- xxx looks like codediff with a single file is a bit broken,
     I can't see the first charater on each line in my own etup at least
     this only takes out the line numbers that we don't care so much about anyways
     -->
<< codediff a1 A1-ping.py A1-ping.py >>

### Sample output

You should be able to run this script as-is, except for the slice name
that you will need to change manually in the code downloaded from the
link just below the picture above.

    $ ./A1-ping.py
    ---
    for troubleshooting:
    ssh onelab.inria.r2lab.tutorial@faraday.inria.fr ping -c1 google.fr
    ---
    faraday.inria.fr:PING google.fr (216.58.198.3) 56(84) bytes of data.
    faraday.inria.fr:64 bytes from mil04s03-in-f3.1e100.net (216.58.198.3): icmp_seq=1 ttl=55 time=9.76 ms
    faraday.inria.fr:
    faraday.inria.fr:--- google.fr ping statistics ---
    faraday.inria.fr:1 packets transmitted, 1 received, 0% packet loss, time 0ms
    faraday.inria.fr:rtt min/avg/max/mdev = 9.769/9.769/9.769/0.000 ms
    orchestrate - True

### Next

We will now see [in tab A2 how to specify your slice name on the command line](javascript:open_tab('A2')), and other good practices.

</div>

<!------------ A2 ------------>
<div id="A2" class="tab-pane fade" markdown="1">

### Objectives

We now see a slightly different version of the same experiment, but

* using standard python's `argparse` module, we let users specify
  their slice on the command line with `--slice onelab.your.own.slice`
  without having to edit the source.

* we introduce the `Run` class, that is a companion to `SshNode`, and
  that states that `ping` is to be run on the remote side as a
  standard command, supposed to be preinstalled. We will see shortly
  that other types of commands can be used, like providing shell
  scripts, or dealing with files.

* finally, we show a good practice, which is to have your script
  return a meaningful return code to the OS, using `exit()`. A process
  is expected to `exit(0)` when everything is going fine.

### The code

  <center> Download the <a href="/code/A2-ping.py" download target="_blank">A2 experiment</a> code </center>
<< codediff a2 A1-ping.py A2-ping.py >>

### Sample output

So with all this in place you can now run the downloaded script for example like this, 

    $ ./A2-ping.py --slice onelab.your.slice.name
    ---
    for troubleshooting:
    ssh onelab.your.slice.name@faraday.inria.fr ping -c1 google.fr
    ---
    faraday.inria.fr:PING google.fr (216.58.198.35) 56(84) bytes of data.
    faraday.inria.fr:64 bytes from mil04s04-in-f35.1e100.net (216.58.198.35): icmp_seq=1 ttl=55 time=9.79 ms
    faraday.inria.fr:
    faraday.inria.fr:--- google.fr ping statistics ---
    faraday.inria.fr:1 packets transmitted, 1 received, 0% packet loss, time 0ms
    faraday.inria.fr:rtt min/avg/max/mdev = 9.794/9.794/9.794/0.000 ms

### Next
In [the next tutorial in tab A3](javascript:open_tab('A3')) we will see how to run commands in a node rather than on the gateway.

</div>

<!------------ A3 ------------>
<div id="A3" class="tab-pane fade" markdown="1">

### Objective : controlling a node beyond the gateway

This time, we want to run the same `ping` command, but from a node,
and not from the gateway.

To this end, we only need to build a second instance of an `SshNode`,
that leverages on the one we had created to join the gateway.  This is
achieved by creating an `SshNode` object with the `gateway = `
argument.

This materializes the fact that we reach node `fit01` through the
gateway. It also ensures that only one ssh connection gets established
to the gateway, regardless of the number of nodes actually controlled.

  <center>
    Note - this picture is out of date<br/>
    <img src="/assets/img/A3.png" alt="a3" height="240px"><br/>
  </center>

### The code

<center>Download the <a href="/code/A3-ping.py" download target="_blank">A3 experiment</a> code</center>

<< codediff a3 A2-ping.py A3-ping.py >>

### Sample output

    $ ./A3-ping.py --slice onelab.your.slice.name
    ---
    for troubleshooting:
    ssh onelab.your.slice.name@faraday.inria.fr ssh root@fit01 ping -c1 google.fr
    ---
    fit01:PING google.fr (216.58.198.35) 56(84) bytes of data.
    fit01:64 bytes from mil04s04-in-f35.1e100.net (216.58.198.35): icmp_seq=1 ttl=54 time=9.98 ms
    fit01:
    fit01:--- google.fr ping statistics ---
    fit01:1 packets transmitted, 1 received, 0% packet loss, time 0ms
    fit01:rtt min/avg/max/mdev = 9.987/9.987/9.987/0.000 ms


### Next

In the next improvement, we see [in tab A4 how to check for leases before](javascript:open_tab('A4')) running our experiment.

</div>

<!------------ A4 ------------>
<div id="A4" class="tab-pane fade" markdown="1">

### Objectives

Our experiment now performs the exact same thing, but before it does
anything, it will check that we do have a valid reservation.

This will allow us to

* first, implement a good practice, because at this point your ssh
  access to the gateway is essentially opened once and for good; so it
  is a good idea to check for this early on, so you do not get error
  messages later on, at a point where the actual cause might be harder
  to figure;

* second, it will us a chance to this time run one command on the
  gateway and one command on the node, and so to get a first glimpse
  at how to deal with that.

### `asynciojobs` basics

The important things to note here are that

* a `Scheduler` object is filled with any number of jobs; the
  order in which jobs are defined and added to the scheduler has no
  meaning whatsoever.

* the only thing that truly matters is the set of `requires`
relationships between the jobs in the scheduler.  So in our example,
we just run 2 jobs in sequence, so the second one is defined with
`requires = check_lease`.

* a `Scheduler` does not propagate result values from one job to its
successors.  The only logic that a `Scheduler` knows about is that if
one of its jobs raises an exception, and when that job is `critical`,
the scheduler then bails out immediately.

* In our case, `rhubarbe leases --check` returns 0 when you currently
  own the reservation, and 1 otherwise, so by defining `check_lease`
  as `critical` we ensure that the overall scenario will fail
  immediately if we do not own the reservation at that time.

### The code

<center>Download the <a href="/code/A4-ping.py" download target="_blank">A4 experiment</a> code</center>

<< codediff a4 A3-ping.py A4-ping.py >>

### Sample output

    $ ./A4-ping.py -s onelab.your.slice.name
    ---
    for troubleshooting:
    ssh onelab.your.slice.name@faraday.inria.fr ssh root@fit01 ping -c1 google.fr
    ---
    faraday.inria.fr:Checking current reservation for onelab.inria.r2lab.tutorial OK
    fit01:PING google.fr (216.58.198.3) 56(84) bytes of data.
    fit01:64 bytes from mil04s03-in-f3.1e100.net (216.58.198.3): icmp_seq=1 ttl=54 time=10.0 ms
    fit01:
    fit01:--- google.fr ping statistics ---
    fit01:1 packets transmitted, 1 received, 0% packet loss, time 0ms
    fit01:rtt min/avg/max/mdev = 10.049/10.049/10.049/0.000 ms


Or

    $ ./A4-ping.py -s onelab.inria.oai.oai_build
    ---
    for troubleshooting:
    ssh onelab.inria.r2lab.tutorial@faraday.inria.fr ssh root@fit01 ping -c1 google.fr
    ---
    faraday.inria.fr:Checking current reservation for onelab.inria.oai.oai_build WARNING: Access currently denied

  <center>
  <!-- no pic needed here
    <img src="/assets/img/A4.png" alt="a4" height="240px"><br/> -->
  </center>

### Next

Let us now see [how to use other network interfaces](javascript:open_tab('A5')).
</div>


<!------------ A5 ------------>
<div id="A5" class="tab-pane fade" markdown="1">

### Objectives

This time, we are going to run the same experiment, but using the `data` network.

Each R2lab node has 4 network interfaces (not counting the special `reboot` interface, that can reset and reboot the node, but that is not visible from a linux kernel).
With the images that we offer, here is how these 4 four interfaces are managed:

* `control` is
  * a wired interface, it is the one that you actually use when you ssh into the node for the first time;
  * it is automatically turned on when you boot,
  * it is known as e.g. `fit01`, and sits on the `192.168.3.0/24` subnet;

* `data` is
  * another wired interface,
  * that is **NOT** turned on automatically at boot time,
  * since it is dedicated for your usage, so you can turn it on or off as you please
  * even using DHCP if it is convenient for you; in this case its IP address will be on `192.168.2.x/24` and known to DNS as e.g. `data01`

* `atheros`, and `intel`
  * both are the 2 WiFi interfaces,
  * that are also **NOT** turned on automatically at boot-time
  * so it is your entire responsability to set them up.

We will see how to manage the wireless interfaces [in the next
tutorial](tuto-500-wireless.md).

But for now we will run the same ping as before, from `fit01` to
`google.fr`, but using the `data` interface, so we can see how to turn
these on and off.

Here is what deserves to be outlined in the code below

* on all nodes you will find a command named `data-up`; this of course
  is not a standard command, it is preinstalled on the nodes for your
  convenience. It's job is to turn on the data interface using DHCP.

* you will find this command documented if you type `help` when logged
  on any node.

* take a look [at the source code for similar utilities
  here](https://github.com/parmentelat/r2lab/blob/master/infra/user-env/nodes.sh)

* also notice how we can very easily make sure to run our ping once
  **BOTH** nodes have configured their data interface, by just using 2
  jobs in the `requires` attribute of the ping job.

### The code

<center>Download the <a href="/code/A5-ping.py" download target="_blank">A5 experiment</a> code</center>

<< codediff a5 A4-ping.py A5-ping.py >>

### Sample output

    $ A5-ping.py onelab.your.slice.name
    faraday.inria.fr:Checking current reservation for onelab.your.slice.name OK
    fit02:Turning on data network on interface data
    fit01:Turning on data network on interface data
    fit01:data
    fit02:data
    fit01:PING data02 (192.168.2.2) from 192.168.2.1 data: 56(84) bytes of data.
    fit01:64 bytes from data02 (192.168.2.2): icmp_seq=1 ttl=64 time=0.244 ms
    fit01:
    fit01:--- data02 ping statistics ---
    fit01:1 packets transmitted, 1 received, 0% packet loss, time 0ms
    fit01:rtt min/avg/max/mdev = 0.244/0.244/0.244/0.000 ms

</div>

<!------------ WRAPUP ------------>
<div id="WRAPUP" class="tab-pane fade" markdown="1">

### Summary
At this point, you should have a rather good understanding of the following fundamentals of R2lab:

##### Interfaces

Each node has 4 network interfaces, `control` being considered
reserved for testbed administration, the other ones being reserved for
the experimenter who is in charge of setting them up.

##### `nepi-ng`

By leveraging the standard `asyncio` library, and by combining the
`asynciojobs` and `apssh` libraries on top of that, it is possible to
write scripts that are

* reasonably simple and short
* able to run as many jobs as needed simultaneously and in a single thread
* able to deal with simple time constraints.

### Next

In [the next tutoorial](tuto-500-wireless.md), we will see how to deal
with the more complex task of setting up a wireless network.

</div>

</div> <!-- end div contents -->
