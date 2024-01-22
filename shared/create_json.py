import os
import json
import base64
import argparse


# Function to convert an image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_data = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_data


# Function to process a folder of PNG images and generate JSON
def generate_json(path_to_input_folder, output_json_file):
    base64_images = {}

    # Check if the input folder exists
    if not os.path.exists(path_to_input_folder):
        print(f"The folder '{path_to_input_folder}' does not exist.")
        return

    # Iterate through the PNG files in the folder
    for filename in sorted(os.listdir(path_to_input_folder)):
        if filename.lower().endswith('.png'):
            image_path = os.path.join(path_to_input_folder, filename)
            base64_images[filename] = image_to_base64(image_path)

    # Extract the name of the output JSON file (without extension) and use it as the "name" value
    output_file_name = os.path.splitext(os.path.basename(output_json_file))[0]

    # Create the JSON output
    output_data = {
        "name": output_file_name,
        "version": 1,
        "author": "<AUTHOR>",
        "bgColor": 0,
        "delay": 200,
        "setup": [
            {
                "type": "datetime",
                "content": "",
                "font": "",
                "fgColor": 65535,
                "bgColor": 0,
                "x": 0,
                "y": 0
            },
            {
                "type": "datetime",
                "content": "",
                "font": "",
                "fgColor": 65088,
                "bgColor": 0,
                "x": 17,
                "y": 38
            },
            {
                "type": "image",
                "x": 0,
                "y": 0,
                "image": ""
            }
        ],
        "sprites": [
            [{"image": base64_images[filename]} for filename in sorted(base64_images.keys())]
        ],
        "loop": [
            {
                "type": "sprite",
                "x": 0,
                "y": 0,
                "sprite": 0,
                "id": "c5c27h"
            }
        ]
    }

    # Write the JSON to the output file
    with open(output_json_file, "w") as json_file:
        json.dump(output_data, json_file, indent=4)


def main():
    parser = argparse.ArgumentParser(description='Convert PNG images in a folder to base64 and generate a JSON file.')
    parser.add_argument('input_folder', help='Path to the folder containing PNG images')
    args = parser.parse_args()

    input_folder = args.input_folder
    output_json_file = os.path.join(input_folder, os.path.basename(input_folder) + '.json')

    generate_json(input_folder, output_json_file)


if __name__ == "__main__":
    main()
