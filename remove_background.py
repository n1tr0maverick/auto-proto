from PIL import Image

def remove_white_background(image_path, output_path):
    """
    Removes the white background from an image and saves it as a PNG with transparency.
    :param image_path: Path to the input image.
    :param output_path: Path to save the output image.
    """
    img = Image.open(image_path)
    img = img.convert("RGBA")

    datas = img.getdata()

    new_data = []
    for item in datas:
        # Change all white (also shades of whites)
        # to transparent
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")

# Example usage:
# remove_white_background("path_to_input_image.jpg", "path_to_output_image.png")