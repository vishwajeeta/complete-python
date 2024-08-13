import os
from PIL import Image

# Set paths
input_directory = "./convert/"
output_directory = "./converted/"

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all files in the input directory
data = os.listdir(input_directory)

# Process each file in the input directory
for i in data:
    if ".webp" not in i:  # Only process non-webp files
        # Generate the name of the converted file
        a = i[:i.find('.')]
        converted_file_path = os.path.join(output_directory, f"{a}.webp")

        # Check if the converted file already exists
        if not os.path.exists(converted_file_path):
            try:
                # Open the image and convert to RGB
                im = Image.open(os.path.join(input_directory, i)).convert("RGB")
                # Save the converted image to the output directory
                im.save(converted_file_path, "webp")
                print(f"Converted and saved: {a}.webp")
            except PermissionError as e:
                print(f"Permission denied: {e}")
            except Exception as e:
                print(f"Error processing {i}: {e}")
        else:
            print(f"File {a}.webp already exists, skipping conversion.")
