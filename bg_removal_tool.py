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

ttk.Label(root, text="Uncha - Batch Background Removal Tool", padding=(30, 30)).pack()

choose_path_in_button = ttk.Button(root, text="Choose Input Path", command=get_path_in).pack()

ttk.Label(root, textvariable=named_directory_in).pack(pady=6)

choose_path_out_button = ttk.Button(root, text="Choose Output Path", command=get_path_out).pack()

ttk.Label(root, textvariable=named_directory_out).pack(pady=6)

run_batch_removal_tool_button = ttk.Button(
    root,
    text="Start background Removal Tool",
    command=threading.Thread(target=run_batch_removal_tool).start
).pack(pady=20)


quit_button = ttk.Button(root, text="Quit", command=root.destroy).pack()

root.mainloop()





