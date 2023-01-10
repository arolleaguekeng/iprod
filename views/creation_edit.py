import base64
import os
import tkinter

from tkinter import *
from tkinter import messagebox, filedialog

import customtkinter
from PIL import ImageTk

from controllers.creation_controller import Creationcontroller
from models.creations import Creation


class CreationEdit(customtkinter.CTkFrame):
    def __init__(self, creation: Creation, master):
        super().__init__(master=master)

        self.creation = creation
        self.master = master
        self.configure(fg_color='transparent')
        self.tv_creation_name = tkinter.StringVar(self, value=creation.name)
        self.tv_creation_description = tkinter.StringVar(self, value=creation.description)
        self.tv_creation_amound = tkinter.StringVar(self, value=creation.amound)
        self.controller = Creationcontroller()
        input_width = 400
        input_height = 50
        input_padding_y = 10
        input_padding_x = 10
        self.f_container = customtkinter.CTkFrame(self)
        self.f_container.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        lb_title = customtkinter.CTkLabel(master=self.f_container,
                                          text= "Modification d'une Création" if self.creation.id is 0 else "Ajout d'une création",
                                          font=('Century Gothic', 30))
        lb_title.grid(row=0, column=0, padx=input_padding_x, pady=input_padding_y)

        lb_name = customtkinter.CTkLabel(self.f_container, text='Nom',
                                         font=customtkinter.CTkFont(size=20,
                                                                    family='Century Gothic'))
        lb_name.grid(row=1, column=0)

        lb_name = customtkinter.CTkLabel(self.f_container, text='Description ',
                                         font=customtkinter.CTkFont(size=20,
                                                                    family='Century Gothic'))
        lb_name.grid(row=1, column=1)

        et_creation_name = customtkinter.CTkEntry(master=self.f_container,
                                                  width=input_width,
                                                  height=input_height,
                                                  placeholder_text='Creation name',
                                                  textvariable=self.tv_creation_name)
        et_creation_name.grid(row=2, column=0, padx=input_padding_x, pady=input_padding_y)

        et_creation_description = customtkinter.CTkEntry(master=self.f_container, width=input_width,
                                                         height=input_height,
                                                         placeholder_text='Creation description',
                                                         textvariable=self.tv_creation_description)
        et_creation_description.grid(row=2, column=1)

        lb_amound = customtkinter.CTkLabel(self.f_container, text='Prix',
                                           font=customtkinter.CTkFont(size=20,
                                                                      family='Century Gothic'))
        lb_amound.grid(row=3, column=0)

        et_creation_amound = customtkinter.CTkEntry(master=self.f_container, width=input_width,
                                                    height=input_height,
                                                    placeholder_text='Creation amound',
                                                    textvariable=self.tv_creation_amound)
        et_creation_amound.grid(row=4, column=0)

        lb_creation_created_at = customtkinter.CTkLabel(master=self.f_container, text=creation.created_at)
        lb_creation_created_at.grid(row=4, column=1)

        btn_edit = customtkinter.CTkButton(master=self.f_container,
                                           width=input_width,
                                           height=input_height,
                                           text="Modifier",
                                           command=self.edit_creation,
                                           corner_radius=6)
        btn_edit.grid(row=5, column=1)

        my_font1 = ('times', 18, 'bold')
        b1 = tkinter.Button(self.f_container, text='Upload File',
                            width=20, command=lambda: self.upload_file())
        b1.grid(row=3, column=1)

    def edit_creation(self):
        self.creation.name = self.tv_creation_name.get()
        self.creation.description = self.tv_creation_description.get()
        self.creation.amound = float(self.tv_creation_amound.get())
        self.creation.image = self.filename

        statut_code = self.controller.edit_creation(creation=self.creation)
        if statut_code is 200:
            messagebox.showinfo("showinfo", "Modification éffectuée avec succès")
            self.grid_forget()

    def upload_file(self):
        global img
        f_types = [('Jpg Files', '*.jpg')]
        self.filename = filedialog.askopenfilename(filetypes=f_types)
        print(self.filename)
        img = ImageTk.PhotoImage(file=self.filename)
        b2 = tkinter.Button(self.f_container, image=img)  # using Button
        b2.grid(row=3, column=1)
        print(os.popen(r'copy "{0}"  "{1}" '.format(self.filename, '../static/images')))



if __name__ == "__main__":
    app = CreationEdit()
    app.mainloop()
