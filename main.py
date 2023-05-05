from PIL import Image, ImageDraw, ImageFont

# Define the dictionary
text = {
    "x": 10, 
    "y": 10, 
    "width": 100, 
    "height":100, 
    "string": "Hello, World", 
    "background": "#202020", 
    "foreground": "#FFFFFF", 
    "font": "Consolas 12"
}

# Create a new image with the specified dimensions and background color
image = Image.new("RGB", (text["width"], text["height"]), text["background"])

# Create a new drawing object
draw = ImageDraw.Draw(image)

# Set the font for the text
#font = ImageFont.truetype(text["font"], size=12)

# Draw the text on the image with the specified color and font
draw.text((text["x"], text["y"]), text["string"], fill=text["foreground"])#, font=font)

# Save the image to a file in png format
image.save("text_image.png", format="png")
