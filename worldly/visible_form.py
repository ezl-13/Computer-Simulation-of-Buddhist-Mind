# Object, such as visibleform, sound, smell, taste, and touch
# different fom SenseObject which are sesory organ's image of these rupa objects


import datetime
from worldly.rupa_object import RupaObj
from process.basics import *

class VisibleForm(RupaObj):
    sense_type = SenseType.eye

    def __init__(self,  size, shape, color):
        RupaObj.__init__(self, datetime.datetime.now())
        self.size = size
        self.shape = shape
        self.color = color
        super().addFeature('size', size)
        super().addFeature('shape', shape)
        super().addFeature('color', color)