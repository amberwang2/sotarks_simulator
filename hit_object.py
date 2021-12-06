'''
circle size 128x128
radius 64
'''

class HitObject:
    field = False # is the object on field?
    field_time = 0  # time object has been on field in ms
    opacity = field_time / 400 if field_time <= 400 else 1  # opacity of object
    approach_mult = 2 - field_time / 400  # size of approach circle

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def counter(self):
        self.field_time += 10
