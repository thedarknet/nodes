Documentation covering the Darknet node architecture, usage, and repository.

Terminology
------

Quick reference in [terms.txt](https://github.com/thedarknet/nodes/blob/master/docs/terms.txt)

Operating Examples
------

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
![alt text][online-scenarios]

#### Daemon (instance) ####
*To be uploaded*

#### Offline ####

![alt text][offline-scenarios]

Node Protocol Stack
------

Node communication is currently in development. The protocol stack is based on existing wired or 802.11 IP standards, or using custom RF protocols based on the vendor of a given technology used in a node, sensor, etc. Documentation for each protocol and usage examples will be added as they are developed.

![alt text][pstack1]

### Hardware Communications ###
For hardware developers and designers wishing to integrate with Darknet badges or nodes, the following standards will be implemented as available and indicated in the associated repository documentation.

**Shitty Add-On & I2C**
*To be updated*

Node Classification
------

Warning: Not all nodes are designed and maintained by Darknet operatives. Nodes are devices "in the wild" and should be used with the understanding that malicious devices may mimic valid and non-malicious Darknet devices.

**Agent Badges**
*Agent badges are hardware devices used for challenges/training, communication, and identification. Agent badges can be purchased as a kit from Darknet Industries. Badge versions have varying functionality and interactivity with the Daemon and nodes - please see the associated repository for more details.*

**NPC Endpoints** 
*NPC Endpoints are story, challenge, and lore nodes that have interactive elements provided by a REST API. Agent badges may be designed to interact with NPCs during contests, for specific challenges, or for communication or creative expression by holons or individual agents.*

Repo: [/nodes/npc/](https://github.com/thedarknet/nodes/tree/master/npc)

**Darknet Nodes**
*Darknet nodes not otherwise classified are nodes created and maintained or otherwise sanctioned by Darknet operatives. Uses will vary, read the instructions.*

**Participating Devices**
*Holons, agents, and other participants may, by adhering to documented protocols, add participating devices to the Darknet. Like Darknet nodes, these devices vary in use and intent, and agents are advised to read instructions and exercise awareness when interacting with a non-sanctioned node.*

**Sensors & Services**
*In some cases, a full node is not required and services from sensor devices or Cloud "gadgets" may be used to provide an explicit function or interaction. These are be designed to adhere to basic Darknet Node Protocols and generally agent badges and the Daemon will only interact with these if operatives have sanctioned or installed them.*






[pstack1]: https://github.com/thedarknet/nodes/blob/master/docs/images/dstack.jpg "Darknet Node Stack"
[offline-scenarios]: https://github.com/thedarknet/nodes/blob/master/docs/images/offline-scenarios.JPG "Offline Daemon Scenarios"
[online-scenarios]: https://github.com/thedarknet/nodes/blob/master/docs/images/online-scenarios.JPG "Online Daemon Scenarios"
