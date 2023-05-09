import os
import yaml
import imageio
from PIL import Image, ImageDraw, ImageFont

# Load script file for execution
script = yaml.safe_load(open("hello_world.yml").read())

images  = {}
objects = {}

# setup frames
for img in range(script['setup']['length']):
    images[f'f{img}'] = Image.new("RGB", (script["setup"]["width"], script["setup"]["height"]), script["setup"]["background"])
script['setup']['font'] = ImageFont.truetype(script['setup']['font'][0], size=script['setup']['font'][1])

# retrieve objects
try:
    for object in script['objects'].keys():
        objects[object] = script['objects'][object]
except: pass

# Loop through each frame
for frame in images.keys():
    # If frame is listed in timeline of script
    if frame in script['timeline'].keys():
        for task in list(script['timeline'][frame]):
            canvas = ImageDraw.Draw(images[frame]) # create a canvas for drawing
            exec(script['timeline'][frame])
    else:
        # if frame is not listed, copy previous frame
        if int(frame[1:]) > 0:
            images[frame] = images['f'+str(int(frame[1:])-1)]

# use imageio to save mp4 output
imageio.mimsave('./out.mp4', [images[img] for img in images.keys()], fps=script['setup']['fps'])