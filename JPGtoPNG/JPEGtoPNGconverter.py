import sys
import os
from PIL import Image

# Specify a folder as first parameter
# Enter name of new folder as second parameter
# Grab first and second argument using Sys
# Check if second param folder exists, if it doesnt, create the folder
# Loop through first parameter folder and convert images to png
# Save images to the new folder


path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}/{filename}')
    # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
    img.save(f'{directory}/{clean_name}.tiff', 'tiff')
    print('all done!')
