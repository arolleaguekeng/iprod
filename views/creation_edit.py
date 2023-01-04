import tkinter

from tkinter import *
import customtkinter
import os
from PIL import Image
import PIL.ImageTk as ptk
import PIL as p

from controllers.creation_controller import Creationcontroller
from models.creations import Creation


class CreationEdit(customtkinter.CTkFrame):
    def __init__(self, creation: Creation, master):
        super().__init__(master=master)
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../static/images")
        self.creation_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path,
                                                                                         creation.image)),
                                                     size=(400, 400))
        self.lb_creation_image = customtkinter.CTkLabel(self, text=creation.name+'\n'+'sdfsdfsdfsdfsdfsdfsdfs',
                                                        image=self.creation_image,
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=20,
                                                                                   weight="bold",
                                                                                   family='Century Gothic'))
        self.lb_creation_image.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


if __name__ == "__main__":
    app = CreationEdit()
    app.mainloop()
