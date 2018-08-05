import random

class NPC(object):
    def __init__(self, sn, name, health, desc):
        self.sn = sn # int epoch:float Darknet iteration:float version:int id
        self.name = name #str
        self.health = health # dict {hp, hunger, thirst, illcode, mood}
        self.desc = desc #text string with description for "look" action
        self.actions = [] #[{'verb':'look','resp':desc, 'func':None}] # list of dict {verb, description, function to execute before reply
        self.inventory = [] # list of dict {name, desc, qty}

    def rename(self,name):
	self.name = name

    def addAction(self,verb,resp,func):
        self.actions.append({'verb':verb,'resp':resp,'func':func})

    # Darknet 2018 
    #
    # illcode {list of pathogens and injuries}
    #
    def contract(self, pathogen):
        self.health['illcode'].append(pathogen)

    # function to do all math to see if we should pass on the infection
    # loop illcode running rand to see if we should pass it on to whomever is interacting with us
    def infect(self):
        passon = []
        for virus in self.health['illcode']:
            v = random.randint(0, 999)
            #print self.health['illcode']
            #print v
            pct = 0;
            if virus == 0x2: #avian flu
                pct = 90
            if virus == 0x4: #measles
                pct = 300
            if virus == 0x8: #tetanus
                pct = 350
            if virus == 0x10: #polo
                pct = 200
            if virus == 0x20: #plague
                pct = 250
            if virus == 0x40: #toxoplasmosis
                pct = 100
            if virus == 0x80: #chlamydia
                pct = 250
            if virus == 0x100: #herpes
                pct = 350 
            if v < pct:
                passon.append(virus)
        return passon

    def disinfect(self):
        self.health['illcode']=[0x00]

    # Darknet NPC generic gamification actions
    #
    # Boolean: health.hungry, health.thirsty
    # String: health.mood
    # Integer: health.hp (0 == dead)
    # Use NPC addAction and call these to have custom actions change NPC state
    def feed(self, item):
        self.health['hungry']=False
        self.take(item)

    def hydrate(self, item):
        self.health['thirsty']=False
        self.take(item)

    def give(self, item):
        self.inventory.append(item)

    def take(self, item):
        for myitem in self.inventory:
            if item[name] == myitem[name]:
                self.inventory.pop(myitem, None)
