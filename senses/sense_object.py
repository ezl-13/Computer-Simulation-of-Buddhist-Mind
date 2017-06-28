# Sense object, images of rupa objects such as visibleform, sound, etc.

from senses.sense_base import *


class SenseObj(object):
    units_const = 17   # class variables
    unit_time = 1000  # in ms in Python

    def __init__(self, base, obj, dt=0, greatness=0):
        # dt is sampling datetime
        self.base = base  #enum sensory organ as base
        self.obj = obj # obj like visible form etc.
        self.startdt = dt
        self.greatness = greatness

    def unitsleft(self, dt1):
        time_lapse = dt1 - self.startdt
        units = int(time_lapse/self.unit_time)
        return max(0,self.units_const-units)

    def queryObjGreatness(self):
        # 0, 1, 2, 3 for very fine, fine, great, very great objects
        return self.greatness

    def computeObjGreatness(self):
        # 0, 1, 2, 3 for very fine, fine, great, very great objects
        self.greatness = 0


#-------------------------------------
class SenseObjEye(SenseObj):
    # light condition: 0 dark, 1 light dark, 2 light, 3 bright
    def __init__(self, base, visibleform, light):
        super().__init__(base, visibleform)
        self.light = light

    def computeObjGreatness(self):
        # for now let's just return lighting condition
        # 0, 1, 2, 3 for very fine, fine, great, very great objects
        self.greatness = self.light


#-------------------------------------
class SenseObjEar(SenseObj):
    # air or media condition: 0 vaccum, 1 rare/sparse, 2 thin air, 3 dense air
    def __init__(self, base, sounds, air):
        super().__init__(base, sounds)
        self.air = air

    def computeObjGreatness(self):
        # for now let's just return lighting condition
        # 0, 1, 2, 3 for very fine, fine, great, very great objects
        self.greatness = self.air
