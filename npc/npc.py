class NPC(object):

    def __init__(self, sn, name, health, desc):
        self._NPCs.append(self)
        self.sn = sn # int epoch:float Darknet iteration:float version:int id
	self.name = name #str
	self.health = health # dict {hp, hunger, thirst, illcode, mood}
	self.desc = desc #text string with description for "look" action
        self.actions = [{'verb':'look','resp':desc, 'func':None}] # list of dict {verb, description, function to execute before reply
        self.inventory = [] # list of dict {name, desc, qty}

    def rename(self,name):
	self.name = name

    def addAction(self,verb,resp,func):
        self.actions.append({'verb':verb,'resp':resp,'func':func})

    # Darknet 2018 infection interactions
    #
    # illcode {list of pathogens and injuries}
    #
    def infect(self, pathogen):
        self.health['illcode'].append(pathogen)

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
