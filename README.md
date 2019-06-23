# Darknet Nodes #

This repository houses documentation and code related to nodes on the Darknet.

## Types of Nodes ##

The type of node indicates the owner of the node and the level of adherence to standard protocol. Further description of capabilities is listed under the node classifications.

* Agent Badge - A special hardware node owned and uniquely identified to Darknet agents & operatives
* Darknet Node - An operative-sanctioned node of any classification
* Daemon Endpoints - Darknet nodes specifically designed for and operated by the Daemon
* Participating Device - Any other node created and owned by agents or other parties

### Node Classifications ###

Nodes can be classified by how they are constucted, configured, and authorized. Some types of nodes, (eg. Agent Badges), only have one classification because they are operative designed hardware and software intended for a single purpose. Other types of nodes, such as Darknet Nodes, may have multiple classifications, (eg. NPCs, Sensors, etc.), as they are a more abstract category of node with many purposes.

**Darknet Nodes**
Operative-sanctioned:
* NPCs
* Sensors
* Communication Nodes

**Participating Devices**
Agent or 3rd Party:
* NPCs
* Sensors
* Communication Nodes
* Shitty Add-Ons
* Non-Darknet Badges

#### More on Classifications ####

**Agent Badges** Agent badges are hardware devices used for challenges/training, communication, and identification. Agent badges can be purchased as a kit from Darknet Industries. Badge versions have varying functionality and interactivity with the Daemon and nodes - please see the associated repository for more details.

Badge Repo (Darknet 8 / DC27): /darknet8-badge/

**NPCs** NPC Endpoints are story, challenge, and lore nodes that have interactive elements provided by a REST API. Agent badges may be designed to interact with NPCs during contests, for specific challenges, or for communication or creative expression by holons or individual agents.

Repo: /nodes/npc/

**Darknet Nodes** Darknet nodes not otherwise classified are nodes created and maintained or otherwise sanctioned by Darknet operatives. Uses will vary, read the instructions.

**Participating Devices** Holons, agents, and other participants may, by adhering to documented protocols, add participating devices to the Darknet. Like Darknet nodes, these devices vary in use and intent, and agents are advised to read instructions and exercise awareness when interacting with a non-sanctioned node.

**Sensors & Services** In some cases, a full node is not required and services from sensor devices or Cloud "gadgets" may be used to provide an explicit function or interaction. These are be designed to adhere to basic Darknet Node Protocols and generally agent badges and the Daemon will only interact with these if operatives have sanctioned or installed them.

Repo: /nodes/sensors/
