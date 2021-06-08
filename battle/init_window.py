from tkinter import *
from tkinter import messagebox
import json

def popup():
    response = messagebox.showinfo("Input Error", "Use only int numbers and fill all fields")

def run_default():
    app.destroy()

def callback():
    try:
        data = {
            "yellow_base_units": int(yellow_base_units.get()),
            "yellow_special_units": int(yellow_special_units.get()),
            "red_base_units": int(red_base_units.get()),
            "red_special_units": int(red_special_units.get()),
            "blue_base_units": int(blue_base_units.get()),
            "blue_special_units": int(blue_special_units.get()),
            "green_base_units": int(green_base_units.get()),
            "green_special_units": int(green_special_units.get()),
            "board_x": int(board_width.get()),
            "board_y": int(board_height.get()),
            "delay": int(frames_delay.get())
        }
        with open("init_data.json", "w") as outfile: 
            json.dump(data, outfile)
        app.destroy()
    except:
        popup()

app = Tk()

yellow_base_units = StringVar()
yellow_special_units = StringVar()
red_base_units = StringVar()
red_special_units = StringVar()
blue_base_units = StringVar()
blue_special_units = StringVar()
green_base_units = StringVar()
green_special_units = StringVar()
board_width = StringVar()
board_height = StringVar()
frames_delay = StringVar()

#Board size X
part_label = Label(app, text='Board Size X:', font = ('bold', 12), pady=20, padx = 20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=board_width)
part_entry.grid(row=0, column=1)
#Board size Y
part_label = Label(app, text='Board Size Y:', font = ('bold', 12), pady=20, padx = 20)
part_label.grid(row=0, column=2, sticky=W)
part_entry = Entry(app, textvariable=board_height)
part_entry.grid(row=0, column=3)

#Army Yellow base units
part_label = Label(app, text='Yellow army base units: ', font = ('bold', 12), pady=20, padx = 20)
part_label.grid(row=2, column=0, sticky=W)
part_entry = Entry(app, textvariable=yellow_base_units)
part_entry.grid(row=2, column=1)
#Army Yellow special units
part_label = Label(app, text='Yellow army special units: ', font = ('bold', 12), pady=20, padx = 20)
part_label.grid(row=2, column=2, sticky=W)
part_entry = Entry(app, textvariable=yellow_special_units)
part_entry.grid(row=2, column=3)

#Army Red base units
part_label = Label(app, text='Red army base units: ', font = ('bold', 12), pady=20, padx = 20)
part_label.grid(row=3, column=0, sticky=W)
part_entry = Entry(app, textvariable=red_base_units)
part_entry.grid(row=3, column=1)
#Army Red special units
part_label = Label(app, text='Red army special units: ', font = ('bold', 12), pady=20, padx = 20)
part_label.grid(row=3, column=2, sticky=W)
part_entry = Entry(app, textvariable=red_special_units)
part_entry.grid(row=3, column=3)

#Army Blue base units
part_label = Label(app, text='Blue army base units: ', font = ('bold', 12), pady=20, padx = 20)
part_label.grid(row=4, column=0, sticky=W)
part_entry = Entry(app, textvariable=blue_base_units)
part_entry.grid(row=4, column=1)
#Army Blue special units
part_label = Label(app, text='Blue army special units: ', font = ('bold', 12), pady=20, padx = 20)
part_label.grid(row=4, column=2, sticky=W)
part_entry = Entry(app, textvariable=blue_special_units)
part_entry.grid(row=4, column=3)

#Army Green base units
part_label = Label(app, text='Green army base units: ', font = ('bold', 12), pady=20, padx = 20)
part_label.grid(row=5, column=0, sticky=W)
part_entry = Entry(app, textvariable=green_base_units)
part_entry.grid(row=5, column=1)
#Army Green special units
part_label = Label(app, text='Green army special units: ', font = ('bold', 12), pady=20, padx = 20)
part_label.grid(row=5, column=2, sticky=W)
part_entry = Entry(app, textvariable=green_special_units)
part_entry.grid(row=5, column=3)

#Framerate
part_label = Label(app, text='Delay between frames (ms): ', font = ('bold', 12), pady=20, padx = 20)
part_label.grid(row=6, column=0, sticky=W)
part_entry = Entry(app, textvariable=frames_delay)
part_entry.grid(row=6, column=1)

MyButton1 = Button(app, text="Submit and run", width=15, command=callback)
MyButton1.grid(row=6, column=2)

MyButton2 = Button(app, text="Run default", width=15, command=run_default)
MyButton2.grid(row=6, column=3)

app.title('Initialization')
app.geometry('750x400')

app.mainloop()
