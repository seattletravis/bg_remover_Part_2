# bg_remover_with_GUI

bg remover is a python program meant to be ran inside of an editor, use any editor that has access to os. (Or run from terminal/CMD) First setup a folder where you'll keep you images that need the bg removed, then create an empty folder in another location where the images with transparent backgrounds will get saved.

Run bg_remover_with_GUI, then select both folders using the GUI navigation.

## [Video Tutorial!](https://youtu.be/MIAukamudl4)

Watch this video to see the code in action, or if you have issues running it, or if you want to learn how it was written. This is a coding tutorial video. [Video Link](https://youtu.be/MIAukamudl4)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install rembg, Pillow, and Tkinter.

```bash
pip install rembg
```

```bash
pip install Pillow
```

```bash
pip install tk
```


## See all the code here
```python
from rembg import remove
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import threading 


def get_path_in():
    named_directory_in.set(filedialog.askdirectory())

def get_path_out():
    named_directory_out.set(filedialog.askdirectory())

def run_batch_removal_tool():
    pic_list = os.listdir(named_directory_in.get())
    save_number = 0
    input_path = fr'{named_directory_out}'

    #Loop over all Images
    for pic in pic_list:
        save_number += 1
        input_path = fr'{named_directory_in.get()}\{pic}'
        
        # Store path of the output image in the variable output_path
        output_path = fr'{named_directory_out.get()}\no_bg{save_number}.png'

        # Check if image exists
        if os.path.exists(output_path):
            continue
        
        # Processing the image
        input = Image.open(input_path)

        # Removing the background from the given Image
        output = remove(input)

        #Saving the image in the given path
        output.save(output_path)

root = tk.Tk()

named_directory_in = tk.StringVar(root, "None Selected")
named_directory_out = tk.StringVar(root, "None Selected")
root.geometry("640x400")
#GUI Title
ttk.Label(root, text="Uncha - Batch Background Removal Tool", padding=(30, 30)).pack()

#File In Button and Info Lable
choose_path_in_button = ttk.Button(root, text="Choose Input Path", command=get_path_in).pack()
ttk.Label(root, textvariable=named_directory_in).pack(pady=6)

#File Out Button and Infor Lable
choose_path_out_button = ttk.Button(root, text="Choose Output Path", command=get_path_out).pack()
ttk.Label(root, textvariable=named_directory_out).pack(pady=6)

#Run Tool Button
run_batch_removal_tool_button = ttk.Button(
    root,
    text="Start background Removal Tool",
    command=threading.Thread(target=run_batch_removal_tool).start
).pack(pady=20)

#Quit GUI and process Button
quit_button = ttk.Button(root, text="Quit", command=root.destroy).pack()

root.mainloop()

```