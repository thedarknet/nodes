# Darknet Nodes

Nodes are any device that communicates with a Darknet asset, agent, or the Daemon. There are several types of nodes:

* Agent Badge
* NPC Endpoint
* Participating Device

An Agent Badge is an official Darknet Node and electronic PCB "badge" generally sold at conference and tied to an Agent by the Daemon with a unique ID. Badges have special capabilities and associated quests. Badges are designed by the Darknet badge team and are located in a seperate repository. Badge design usually changes annually.

NPC Endpoints are Nodes that communicate with a basic interface to other Darknet Badges and Participating Devices. An NPC Endpoint style Node is equipped with an API for communication and interactions. NPCs all have a name, characteristics, inventory, allowed actions, and responses. 

“Participating Devices” are other electronic devices that participate with the Darknet and/or interact with the Daemon via Darknet protocols and APIs. 

virtualenv ~/nodes-venv

source ~/nodes-venv/bin/activate

cd npc
pip install -r requirements.txt
python darknetnpc.py

