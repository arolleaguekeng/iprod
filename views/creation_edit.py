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
        self.creation = creation
        self.configure(fg_color='transparent')
        self.tv_creation_name = tkinter.StringVar(self, value=creation.name)
        self.tv_creation_description = tkinter.StringVar(self, value=creation.description)
        self.tv_creation_amound = tkinter.StringVar(self, value=creation.amound)
        self.controller = Creationcontroller()
        input_width = 400
        input_height = 50
        input_padding_y = 10
        input_padding_x = 10
        lb_title = customtkinter.CTkLabel(master=self,
                                          text="Modification d'une Création",
                                          font=('Century Gothic', 30))
        lb_title.grid(row=0, column=0, padx=input_padding_x, pady=input_padding_y)

        self.f_container = customtkinter.CTkFrame(self)
        self.f_container.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        et_creation_name = customtkinter.CTkEntry(master=self.f_container,
                                                  width=input_width,
                                                  height=input_height,
                                                  placeholder_text='Creation name',
                                                  textvariable=self.tv_creation_name)
        et_creation_name.grid(row=0, column=0, padx=input_padding_x, pady=input_padding_y)

        et_creation_description = customtkinter.CTkEntry(master=self.f_container, width=input_width,
                                                         height=input_height,
                                                         placeholder_text='Creation description',
                                                         textvariable=self.tv_creation_description)
        et_creation_description.grid(row=0, column=1)

        et_creation_amound = customtkinter.CTkEntry(master=self.f_container, width=input_width,
                                                    height=input_height,
                                                    placeholder_text='Creation amound',
                                                    textvariable=self.tv_creation_amound)
        et_creation_amound.grid(row=1, column=0)

        lb_creation_created_at = customtkinter.CTkLabel(master=self.f_container, text=creation.created_at)
        lb_creation_created_at.grid(row=1, column=1)

        btn_edit = customtkinter.CTkButton(master=self.f_container,
                                           width=input_width,
                                           height=input_height,
                                           text="Modifier",
                                           command=self.edit_creation,
                                           corner_radius=6)
        btn_edit.grid(row=2, column=1)

    def edit_creation(self):
        self.creation.name = self.tv_creation_name.get()
        self.creation.description = self.tv_creation_description.get()
        self.creation.amound = float(self.tv_creation_amound.get())
        self.controller.edit_creation(creation=self.creation)


if __name__ == "__main__":
    app = CreationEdit()
    app.mainloop()
