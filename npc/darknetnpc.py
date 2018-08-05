#!/usr/bin/python

import sys
from npc import NPC
from flask import Flask, url_for, jsonify


app = Flask(__name__)
controls = ['reset', 'save']
NPCS = []


def myRatFunc(rat):
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
                'illcode':[0x20], #Plague
                'mood':'bored'
            },
            "This rat looks like a questionable character."
            )
    DarkRat.addAction("lift","Picking up this rat will guarantee the need for bandaids. You leave it alone.",None)
    DarkRat.addAction("diagnose","You daintily poke the rat with a stick, ignoring the chittering complaints.",myRatFunc)
    DarkRat.give({'name':'bauble','desc':'A shiny bauble of unknown origin.','qty':1})
    
    DarkChicken = NPC(
            '1531682536_3.0_1.0-001',
            'DarkChicken',
            {
                'hp':20,
                'hungry':True,
                'thirsty':False,
                'illcode':[0x02, 0x4], #Avian flu and Measles
                'mood':''
            },
            "The chicken has a dark aura of avian malice."
            )
    DarkChicken.addAction("chase","why would you chase a dark chicken?", None);
    DarkChicken.addAction("pluckit","You have to catch it first!", None);
    DarkChicken.addAction("eatit","Do you _really_ want to put that in your mouth?", None);
    
    DarkCat = NPC(
            '1533453702_3.0_1.0-001',
            'DarkCat',
            {
                'hp':40,
                'hungry':False,
                'thirsty':False,
                'illcode':[0x40, 0x20], #Toxoplasmosis and Plague
                'mood':''
            },
            "The cat has a dark aura of avian malice."
            )
    DarkCat.addAction("kickit","You miss and fall on your ass",None);
    DarkCat.addAction("pet","Your hand comes back bloody!", None);
    
    DarkHorse = NPC(
            '1533454339_3.0_1.0-001',
            'DarkHorse',
            {
                'hp':100,
                'hungry':False,
                'thirsty':False,
                'illcode':[0x8, 0x20], #Tetanus & Plague
                'mood':''
            },
            "The horse has a dark aura of avian malice."
            )
    DarkHorse.addAction("kickit","You miss and fall on your ass",None);
    DarkHorse.addAction("pet","Your hand comes back bloody!", None);
    
    DarkFlea = NPC(
            '1533454340_3.0_1.0-001',
            'DarkHorse',
            {
                'hp':100,
                'hungry':False,
                'thirsty':False,
                'illcode':[0x10], #Polio
                'mood':''
            },
            "The Flea  has a dark aura of avian malice."
            )
    DarkFlea.addAction("kickit","You miss and fall on your ass",None);
    DarkFlea.addAction("pet","Your hand comes back bloody!", None);

    return [DarkRat, DarkChicken, DarkCat, DarkHorse, DarkFlea]


@app.route('/')
def api_root():
    return "Darknet NPC Node"


# Get list of NPCs served by this Node by SN & Name, as well as Node controls
@app.route('/helo')
def api_helo():
    allnpcs = []
    for mynpc in NPCS:
        allnpcs.append([mynpc.sn,mynpc.name])
    return jsonify([allnpcs])


# List all NPCs
@app.route('/npc')
def api_npc():
    mynpcs = []
    for mynpc in NPCS:
        mynpcs.append(mynpc.name)
    return jsonify( 
            {
                'npcs':[mynpcs]
            }
    )


# List all NPC verbs and responses 
@app.route('/npc/<npc>')
def api_npc_npc_actions(npc):
    for mynpc in NPCS:
        if mynpc.name == npc:
            myverbs = []
            for action in mynpc.actions:
                myverbs.append(action['verb'])
            infections = mynpc.infect()
            print infections
            return jsonify(
                    {
                        'n':mynpc.name, 
                        'd':mynpc.desc, 
                        'a':[myverbs], 
                        'i':infections
                    }
            )
    return "I don't know that NPC."


# List NPC overall health 
@app.route('/npc/<npc>/health')
def api_npc_health(npc):
    for mynpc in NPCS:
        if mynpc.name == npc:
            return jsonify([mynpc.health])
    return "I don't know that NPC's health."


# List specific NPC healthcode value
@app.route('/npc/<npc>/health/<key>')
def api_npc_health_key(npc,key):
    for mynpc in NPCS:
        if mynpc.name == npc:
            return jsonify([mynpc.health[key]])
    return "I don't know that NPC's health key."


# Do NPC action
@app.route('/npc/<npc>/<action>')
def api_npc_action(npc,action):
    for mynpc in NPCS:
        if mynpc.name == npc:
            for thisaction in mynpc.actions:
                if thisaction['verb'] == action:
                    if thisaction['func']:
                        thisaction['func'](mynpc)
                    return jsonify( {
                        'r':thisaction['resp'],
                        'i':mynpc.infect()
                        }
                    )
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
    for mynpc in NPCS:
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
    app.run(host="0.0.0.0", port=int("8080"), debug=True)
