Documentation covering the Darknet node architecture, usage, and repository.

## Terminology ##

Quick reference in [terms.txt](https://github.com/thedarknet/nodes/blob/master/docs/terms.txt)

## Operating Examples ##

Nodes and affiliated Darknet devices will participate in several key scenarios:
* **Daemon (actual)** - badges, nodes, and participating devices communicate to the Daemon in the standard fashion
* **Daemon (instance)** - a cloud hosted instance of the Daemon is providing Daemon functionality in lieu of communication with (actual)
* **Offline** - a Daemon instance is run to provide Daemon functionality in lieu of communication with (actual) 
Instances of the Daemon (actual) are run by operatives authorized to do so for Darknet Industries. 


*Notation: first letter indicates source, second destination. Ex. s2n indicates a sensor initiating communication with a node.*
* a - agent (action by agent via badge)
* b - badge (automatic action via badge)
* d - daemon
* n - node
* s - sensor

#### Daemon (actual) ####
*To be uploaded*

#### Daemon (instance) ####
*To be uploaded*

#### Offline ####

![alt text][offline-scenarios]

## Node Protocol Stack ##

Node communication is currently in development. The protocol stack is based on existing wired or 802.11 IP standards, or using custom RF protocols based on the vendor of a given technology used in a node, sensor, etc. Documentation for each protocol and usage examples will be added as they are developed.

![alt text][pstack1]

### Hardware Communications ###
For hardware developers and designers wishing to integrate with Darknet badges or nodes, the following standards will be implemented as available and indicated in the associated repository documentation.

**Shitty Add-On & I2C**
*To be updated*






[pstack1]: https://github.com/thedarknet/nodes/blob/master/docs/images/dstack.jpg "Darknet Node Stack"
[offline-scenarios]: https://github.com/thedarknet/nodes/blob/master/docs/images/offline-scenarios.JPG "Offline Daemon Scenarios"
