'''
circle size 128x128
radius 64
'''

class HitObject:
    field = False
    field_time = 0 # time object has been on field in ms
    opacity = 0 # opacity of object

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def counter(self):
        self.field_time += 10
