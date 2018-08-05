#!/usr/bin/python

import sys
from npc import NPC
from flask import Flask, url_for, jsonify


app = Flask(__name__)
controls = ['reset', 'save']
NPCS = []

def myRatFunc(rat):
    rat.infect(0x03)
    rat.health['mood'] = "annoyed"

def startNode():
    # Add NPCs - serialnum, name, healthcode dict, moodcode dict
    DarkRat = NPC(
            '1531682535_3.0_1.0-001',
            'DarkRat',
            {
                'hp':100,
                'hungry':False,
                'thirsty':False, 
                'illcode':[0x01],
                'mood':'bored'
            },
            "This rat looks like a questionable character."
            )
    DarkChicken = NPC(
            '1531682536_3.0_1.0-001',
            'DarkChicken',
            {
                'hp':20,
                'hungry':True,
                'thirsty':False,
                'illcode':[0x00],
                'mood':''
            },
            "The chicken has a dark aura of avian malice."
            )


    DarkRat.addAction("lift","Picking up this rat will guarantee the need for bandaids. You leave it alone.",None)
    DarkRat.addAction("diagnose","You daintily poke the rat with a stick, ignoring the chittering complaints.",myRatFunc)
    DarkRat.infect(0x0A)
    DarkRat.give({'name':'bauble','desc':'A shiny bauble of unknown origin.','qty':1})
    return [DarkRat, DarkChicken]

    
@app.route('/')
def api_root():
    return "Darknet NPC Node"


# Get list of NPCs served by this Node by SN & Name, as well as Node controls
@app.route('/helo')
def api_helo():
    allnpcs = []
    for mynpc in NPC._NPCs:
        allnpcs.append([mynpc.sn,mynpc.name])
    return jsonify([allnpcs, controls])


# List all NPCs
@app.route('/npc')
def api_npc():
    mynpcs = []
    for mynpc in NPC:
        mynpcs.append(mynpc.name)
    return jsonify([mynpcs])


# List all NPC verbs and responses 
@app.route('/npc/<npc>/actions')
def api_npc_npc_actions(npc):
    for mynpc in NPC:
        if mynpc.name == npc:
            myverbs = []
            for action in mynpc.actions:
                myverbs.append(action['verb'])
            return jsonify([myverbs])
    return "I don't know that NPC."


# List NPC overall health 
@app.route('/npc/<npc>/health')
def api_npc_health(npc):
    for mynpc in NPC:
        if mynpc.name == npc:
            return jsonify([mynpc.health])
    return "I don't know that NPC's health."


# List specific NPC healthcode value
@app.route('/npc/<npc>/health/<key>')
def api_npc_health_key(npc,key):
    for mynpc in NPC:
        if mynpc.name == npc:
            return jsonify([mynpc.health[key]])
    return "I don't know that NPC's health key."


# Do NPC action
@app.route('/npc/<npc>/<action>')
def api_npc_action(npc,action):
    for mynpc in NPC:
        if mynpc.name == npc:
            for thisaction in mynpc.actions:
                if thisaction['verb'] == action:
                    if thisaction['func']:
                        thisaction['func'](mynpc)
                    return jsonify([thisaction['resp']])
    return "I don't know that NPC."


# Node controls - these should not be part of gamification
# Reset *all* Node NPCs to original state
@app.route('/ctrl/reset')
def api_ctrl_reset():
    global NPCS
    NPCS = []
    npcs = startNode()
    for npc in npcs:
        NPCS.append(npc)
    return "Node reinitialized."


@app.route('/ctrl/save')
def api_ctrl_save():
    allills = "0"
    allactions = ""
    allitems = ""
    allnpcs = ""
    for mynpc in NPC:
        #CLEAN THIS UP
        for thisaction in mynpc.actions:
            if str(thisaction['func']) != "None":
                thisfunc = str(thisaction['func'].__name__)
            else:
                thisfunc = str(thisaction['func'])
            allactions = allactions + "~A:" + thisaction['verb'] + "^" + thisaction['resp'] + "^" + thisfunc 
        for item in mynpc.inventory:
            if 'name' in item:
                allitems = allitems + "~I:"+ item['name'] + "^" + item['desc'] + "^" + str(item['qty'])
        for ill in mynpc.health['illcode']:
            allills = allills + "^" + str(ill)
        allnpcs = allnpcs + mynpc.sn + "~" + mynpc.name + "~" + str(mynpc.health['hp'])+":"+ str(mynpc.health['hungry']) + ":" + str(mynpc.health['thirsty']) + ":" + allills + ":" + mynpc.health['mood'] + allactions + allitems + "\n"
        allills = "0"
        allactions = ""
        allitems = ""
    cfgfile = open("npc.cfg", 'w')
    cfgfile.write(allnpcs)
    cfgfile.close()
    return allnpcs


if __name__ == '__main__':
    npcs = startNode()
    for npc in npcs:
        NPCS.append(npc)
    app.run()
