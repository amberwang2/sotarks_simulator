import random

def update_objects(objects, time):
    for i in objects:
        if i.timing_point - 600 == time:
            i.field = True
        if i.timing_point + 120 == time:
            i.field = False
            i.hit_window = False
        if i.field:
            if i.timing_point - 120 == time:
                i.hit_window = True
            i.updater()

def new_map(n):
    points = [(random.randint(150, 1130), random.randint(150, 570))]

    for i in range(n - 1):
        temp = True
        while temp:
            point = (random.randint(150, 1130), random.randint(150, 570))
            dist = ((point[0] - points[-1][0])**2 + (point[1] - points[-1][1])**2)**0.5
            if dist > 400 and dist < 600:
                points.append(point)
                temp = False

    return [HitObject(points[i][0], points[i][1], i*720 + 3000) for i in range(len(points))]

class HitObject: # circle size 128x128
    field = False # is the object on field?
    hit_window = False # is the hit window for the object active?
    field_time = 0  # time object has been on field in ms
    hit = False
    score = 0

    def __init__(self, x, y, timing_point):
        self.x = x
        self.y = y
        self.timing_point = timing_point

    def updater(self):
        self.approach_mult = round(134 * (3 - self.field_time / 200)) if self.field_time <= 400 else 1
        self.opacity = self.field_time / 400 if self.field_time <= 400 else 1
        self.field_time += 10
