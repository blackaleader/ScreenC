from io import BytesIO
from PIL import Image

from tkinter import *
import pyautogui

from datetime import datetime

import boto3

access_key = '25df5980-3ba3-4cf8-9f39-1c34fa11d18b'
secret_key = '1d59802c8c9f017e8617e58553fe2fc8b161e340e2b61c03a70ce1ca7fc19e80'





def take_bounded_screenshot(x1, y1, x2, y2):
    image = pyautogui.screenshot(region=(x1, y1, x2, y2))
    file_name = datetime.now().strftime("%f")
    image.save(f"screenc{file_name}.png")


    # output = BytesIO()
    # image.convert('RGB').save(output, 'BMP')
    # data = output.getvalue()[14:]
    # output.close()

    # win32clipboard.OpenClipboard()
    # win32clipboard.EmptyClipboard()
    # win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    # win32clipboard.CloseClipboard()

    b3_session = boto3.Session(aws_access_key_id=access_key,
                           aws_secret_access_key=secret_key,
                           )

    b3_client = b3_session.client('s3', endpoint_url="https://papirous.s3.ir-thr-at1.arvanstorage.ir")  

    bucket = b3_client.upload_file(f'screenc{file_name}.png', "screenC", f'screenc{file_name}.png')

    # b3_client.download_file('screenC', f'screenc{file_name}.png', f'screenc{file_name}.png')






class Application():
    def __init__(self, master):
        self.snip_surface = None
        self.master = master
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None

        root.geometry('400x50+200+200') 
        root.title('ScreenC')

        self.menu_frame = Frame(master)
        self.menu_frame.pack(fill=BOTH, expand=YES, padx=1, pady=1)

        self.buttonBar = Frame(self.menu_frame, bg="")
        self.buttonBar.pack()

        self.snipButton = Button(self.buttonBar, width=5, height=5, command=self.create_screen_canvas, background="green")
        self.snipButton.pack()

        self.master_screen = Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "maroon3")
        self.picture_frame = Frame(self.master_screen, background="maroon3")
        self.picture_frame.pack(fill=BOTH, expand=YES)

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
        self.display_rectangle_position()

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

    def display_rectangle_position(self):
        pass


root = Tk()
app = Application(root)
root.mainloop()