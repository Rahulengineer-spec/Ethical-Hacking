from PIL import Image, ImageDraw, ImageFont

# Define image dimensions
width = 400
height = 400

# Create a black background image
image = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(image)

# Generate the binary (0101) pattern in green color
for y in range(height):
    for x in range(width):
        pixel = (x + y) % 2
        color = (0, 255, 0) if pixel == 1 else (0, 0, 0)
        draw.point((x, y), fill=color)

# Add the text "_ardentian" on the body of the hacker
font = ImageFont.truetype("arial.ttf", 30)  # Replace "arial.ttf" with the path to your desired font file
text = "_ardentian"
text_width, text_height = draw.textsize(text, font=font)
text_x = (width - text_width) // 2
text_y = (height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill=(0, 255, 0))

# Save the final image
image.save("hacker_image.png")  # Specify the path and name of the output image file
