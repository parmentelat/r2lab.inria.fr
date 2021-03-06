title: R2lab Status
tab: status
skip_header: yes

This page gives you live details on the individual nodes in the R2lab testbed.

---
## Overall status (livemap)

<a name="livemap"></a>
For accurate dimensions of the room, please see the [static blueprint
at the bottom of this page](#accurate-layout)

For more details about each node, please click in the node number or badge.

<div class="row" id="all">
  <div class="col-lg-2"></div>
  <div class="col-lg-10">
    <div id="livemap_container"></div>
    <script type="text/javascript" src="/assets/r2lab/livemap.js"></script>
    <style type="text/css"> @import url("/assets/r2lab/livemap.css"); </style>
    <script>
    // override livemap default settings 
    Object.assign(livemap_options, {
        usrp_width : 15,
    	usrp_height : 26,
//    debug : true,
   });
    </script>
  </div>
</div>

<a name="livemap:legend"></a>

#### Legend

##### Nodes
* A round shape with a O.S. icon (fedora or ubuntu) informs that the node is turned on, running the
  referenced O.S. and reachable through ssh.
* If only a number appears, this node is turned off.
* Smaller bullets indicate intermediate / temporary status
  * a small gray bullet means the node is turned ON but does not answer to ping
  (usually this means the node is being turned on or off)
  * a slightly larger and green-ish bullet means the node answers to ping but cannot be
  reached through ssh yet (usually this means an image is being
  loaded).
* Finally, if a node is hidden behind a large red circle, it means it
  is out of order, and altogether unavailable.

In addition, you will find the following symbols close to some nodes

* <img src="/assets/img/gnuradio-logo-icon-red.svg" height=20px> when the node has a USRP device, that is turned OFF
* <img src="/assets/img/gnuradio-logo-icon-green.svg" height=20px> when the node has a USRP device, that is turned ON

##### Phone
* Phones in the testbed appear as either
  * <span class='fa fa-plane'></span> (meaning the phone is in airplane mode) 
  * <span class='fa fa-phone'></span> (meaning it's not in airplane mode) 
* At this time we have a single Nexus 5 phone deployed in the testbed

***

## Detailed status (livetable)

<a name="livetable"></a>

<br />

<div class="row" id="all">
  <div class="col-lg-12">
    <table class="table table-condensed" id='livetable_container'> </table>
    <script type="text/javascript" src="/assets/r2lab/livecolumns.js"></script>
    <script type="text/javascript" src="/assets/r2lab/livetable.js"></script>
    <script>
    // override livetable default settings 
    Object.assign(livetable_options, {
//    debug : true,
   });
    </script>
    <style type="text/css"> @import url("/assets/r2lab/livecolumns.css"); </style>
    <style type="text/css"> @import url("/assets/r2lab/livetable.css"); </style>
  </div>
</div>

<a name="livetable:legend"></a>

#### Legend

* The ***availability*** column
  tells you whether the node is usable or not. If not, this means you should not try to use that node for your experiment, as it may be physically powered off, or otherwise behave erratically.
* The ***on/off*** column
  reports if the node is currently turned on or off.
* The ***usrp*** column shows both
  * the type of the USRP companion (or `none`),
  * and the status of the corresponding software switch.
* The ***ping*** column
  says whether the node currently answers a single ping at the wired network interface or not.
* The ***ssh*** column says whether the node can currently be reached through ssh on its wired interface.
* The ***last O.S***, ***last uname*** and ***last image*** columns shows information about the node ***the last time it was reachable***, i.e. even if the node is currently off.

Also please note that

 * Clicking anywhere in the header will focus on the nodes that are currently up; a second click returns to full mode.
 * Clicking a node badge will take it off the list

***

### Accurate layout

Below is the ground plan layout of the anechoic room which provides thirty-seven wireless nodes distributed in a **≈ 90m<sup>2</sup>** room.

The nodes are arranged in a grid with ≈1.0m (vertical) and ≈1.15m (horizontal) of distance between them, except for nodes 12, 16, 17, 20 and 23, 24, 27 which are the ones surrounding close to the two columns in the room.

<a name="accurate-layout">
<center>
	<img src="/assets/img/status-chamber.png" style="width:950px; height:592px;"/><br>
	<!-- <center> Fig. 1 - Resources status</center> -->
</center>
</a>

<br />

<script type="text/javascript" src="/assets/r2lab/xhttp-django.js"></script>
<!-- defines node_details_modal -->
<< include r2lab/nodes-details-modal.html >>
