from io import BytesIO
import win32clipboard
from tkinter import *
import pyautogui
from datetime import datetime
import boto3

import os

import json


config_file_path = "config.json"
with open(config_file_path, 'r') as config_file:
    config_data = json.load(config_file)

access_key = config_data["access_key"]
secret_key = config_data["secret_key"]
url = config_data["endpoint_url"]




def take_bounded_screenshot(x1, y1, x2, y2):
    image = pyautogui.screenshot(region=(x1, y1, x2, y2))
    file_name = datetime.now().strftime("%f")
    image.save(f"screenc{file_name}.png")



    b3_session = boto3.Session(aws_access_key_id=access_key,
                           aws_secret_access_key=secret_key,
                           )

    b3_client = b3_session.client('s3', endpoint_url=url)  

    bucket = b3_client.upload_file(f'screenc{file_name}.png', "screenC", f'screenc{file_name}.png' , ExtraArgs={'ACL': 'public-read'})


    
    data = f"https://papirous.s3.ir-thr-at1.arvanstorage.ir/screenC/screenc{file_name}.png?versionId="

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT ,data )
    win32clipboard.CloseClipboard()

    if app.no %2 ==0:
        os.remove(f'./screenc{file_name}.png')


class Application():
    

    no_save = '❌'
    yes_save = '✅'

    def __init__(self, master):
        self.no = 1

        global click_btn
        click_btn= PhotoImage(file='plz work.png')
        click_btn = click_btn.subsample(2,2)
        self.snip_surface = None
        self.master = master
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None

        root.geometry('400x50+200+200') 
        root.title('ScreenC')
        root.iconbitmap("./lion.ico")
        root.resizable(False,False)
        self.snipButton1 = Button(root, text=f'Save Images {self.yes_save}', command=self.saveimageicon)
        self.snipButton1.pack(side='right', )

        self.menu_frame = Frame(master)
        self.menu_frame.pack(fill=BOTH, expand=YES, padx=1, pady=1)

        self.buttonBar = Frame(self.menu_frame, bg="")
        self.buttonBar.pack(side='left',)


        self.snipButton = Button(self.buttonBar, command=self.create_screen_canvas,image=click_btn, borderwidth=1)
        self.snipButton.pack()
        

        self.master_screen = Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "maroon3")
        self.picture_frame = Frame(self.master_screen, background="maroon3")
        self.picture_frame.pack(fill=BOTH, expand=YES)
    def saveimageicon(self):

        self.no = self.no + 1
        if self.no % 2 == 0:
            self.snipButton1.config(text=f'Save Images {self.no_save}')


        else :
            self.snipButton1.config(text=f'Save Images {self.yes_save}')


    def create_screen_canvas(self):
        self.master_screen.deiconify()
        root.withdraw()

        self.snip_surface = Canvas(self.picture_frame, cursor="cross", bg="gray11")
        self.snip_surface.pack(fill=BOTH, expand=YES)

        self.snip_surface.bind("<ButtonPress-1>", self.on_button_press)
        self.snip_surface.bind("<B1-Motion>", self.on_snip_drag)
        self.snip_surface.bind("<ButtonRelease-1>", self.on_button_release)

        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .3)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)

    def on_button_release(self, event):


        if self.start_x <= self.current_x and self.start_y <= self.current_y:
            take_bounded_screenshot(self.start_x, self.start_y, self.current_x - self.start_x, self.current_y - self.start_y)

        elif self.start_x >= self.current_x and self.start_y <= self.current_y:
            take_bounded_screenshot(self.current_x, self.start_y, self.start_x - self.current_x, self.current_y - self.start_y)

        elif self.start_x <= self.current_x and self.start_y >= self.current_y:
            take_bounded_screenshot(self.start_x, self.current_y, self.current_x - self.start_x, self.start_y - self.current_y)

        elif self.start_x >= self.current_x and self.start_y >= self.current_y:
            take_bounded_screenshot(self.current_x, self.current_y, self.start_x - self.current_x, self.start_y - self.current_y)

        self.exit_screenshot_mode()
        return event

    def exit_screenshot_mode(self):
        self.snip_surface.destroy()
        self.master_screen.withdraw()
        root.deiconify()

    def on_button_press(self, event):
        self.start_x = self.snip_surface.canvasx(event.x)
        self.start_y = self.snip_surface.canvasy(event.y)
        self.snip_surface.create_rectangle(0, 0, 1, 1, width=3, fill="maroon3")

    def on_snip_drag(self, event):
        self.current_x, self.current_y = (event.x, event.y)
        self.snip_surface.coords(1, self.start_x, self.start_y, self.current_x, self.current_y)


root = Tk()
app = Application(root)
root.mainloop()
