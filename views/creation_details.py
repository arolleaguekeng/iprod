import tkinter

from tkinter import *
import customtkinter
import os
from PIL import Image
import PIL.ImageTk as ptk
import PIL as p

from controllers.creation_controller import Creationcontroller
from models.creations import Creation


class CreationDetails(customtkinter.CTkFrame):
    def __init__(self,creation: Creation,master):
        super().__init__(master=master)
        l1 = customtkinter.CTkLabel(master=self, text=creation.name, font=('Century Gothic', 60))
        l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


if __name__ == "__main__":
    app = CreationDetails()
    app.mainloop()
