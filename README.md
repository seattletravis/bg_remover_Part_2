# bg_remover

bg remover is a python program meant to be ran inside of an editor, use any editor that has access to os. First setup a folder where you'll keep you images that need the bg removed, then create an empty folder in another location where the images with transparent backgrounds will get saved.

use the paths to the folders you just made and save them to the variables 'named_directory_in' and 'named_directory_out' in the code. See below.

## [Video Tutorial!](https://youtu.be/5d5JTcTyNkA)

Watch this video to see the code in action, or if you have issues running it, or if you want to learn how it was written. This is a coding tutorial video. [Video Link](https://youtu.be/5d5JTcTyNkA)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install rembg and Pillow.

```bash
pip install rembg
```

```bash
pip install Pillow
```

## Usage - in the code make the following changes

```python
#Replace the string with path of input dir
named_directory_in = r'C:\Your\Directory\With\Images\Here' 
#Replace the string with path to empty dir
named_directory_out = r'C:\Your\EmptyDirectory\Where\Images\WillGo' 

```

## See all the code here
```python
from rembg import remove
from PIL import Image
import os
from datetime import datetime

#Replace the string with path of input dir
named_directory_in = r'C:\Your\Directory\With\Images\Here' 
#Replace the string with path to empty dir
named_directory_out = r'C:\Your\EmptyDirectory\Where\Images\WillGo' 

pic_list = []
pic_list = os.listdir(named_directory_in)
save_number = 0
new_dir_name = datetime.now().strftime('%Y-%m-%d')
path = fr'{named_directory_out}\{new_dir_name}'

#Check for folder, create folder if not there
if not os.path.exists(path):
    os.makedirs(path)

#Loop over all Images
for pic in pic_list:
    save_number += 1
    input_path = fr'{named_directory_in}\{pic}'
    
    # Store path of the output image in the variable output_path
    output_path = fr'{named_directory_out}\{new_dir_name}\no_bg{save_number}.png'

    # Check if image exists if it does, skip it
    if os.path.exists(output_path):
        continue
    
    # Processing the image
    input = Image.open(input_path)

    # Removing the background from the given Image
    output = remove(input)

    #Saving the image in the given path
    output.save(output_path)

```