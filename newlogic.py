import os
import yaml
import imageio
from PIL import Image, ImageDraw, ImageFont

script = yaml.safe_load(open("hello_world.yml").read())

images  = {}
objects = {}

for img in range(script['setup']['length']):
    images[f'f{img}'] = Image.new("RGB", (script["setup"]["width"], script["setup"]["height"]), script["setup"]["background"])
script['setup']['font'] = ImageFont.truetype(script['setup']['font'][0], size=script['setup']['font'][1])

for object in script['objects'].keys():
    objects[object] = script['objects'][object]

for frame in images.keys():
    if frame in script['timeline'].keys():
        for task in list(script['timeline'][frame]):
            canvas = ImageDraw.Draw(images[frame])
            obj = task.split(".")[0]
            fnc = task.split(".")[1]
            if (fnc == "text"):
                canvas.text((objects[obj]["x"], objects[obj]["y"]), objects[obj][fnc]["string"], fill=script['setup']["foreground"], font=script['setup']['font'])
    else:
        if int(frame[1:]) > 0:
            images[frame] = images['f'+str(int(frame[1:])-1)]
    images[frame].save(f'{frame}.png', format="png")

