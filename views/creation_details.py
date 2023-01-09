import tkinter

from tkinter import *
from tkinter import messagebox

import customtkinter
import os
from PIL import Image
import PIL.ImageTk as ptk
import PIL as p

from controllers.creation_controller import Creationcontroller
from models.creations import Creation
from views.creation_edit import CreationEdit


class CreationDetails(customtkinter.CTkFrame):
    def __init__(self, creation: Creation, master, app):
        super().__init__(master=master)
        self.app = app
        self.creation = creation
        self.configure(fg_color="transparent")
        self.f_container = customtkinter.CTkFrame(self)
        self.f_container.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../static/images")
        self.creation_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path,
                                                                                         creation.image)),
                                                     size=(400, 400))
        self.lb_creation_image = customtkinter.CTkLabel(self.f_container, text=creation.name,
                                                        image=self.creation_image,
                                                        compound="top",
                                                        font=customtkinter.CTkFont(size=30,
                                                                                   family='Century Gothic'))
        self.lb_creation_image.grid(row=0, column=0)

        # Create custom button
        self.btn_edit = customtkinter.CTkButton(master=self.f_container, width=220, text="Modifier",
                                               corner_radius=6, command=self.open_edit_page)
        self.btn_edit.grid(row=4, column=0)

        self.btn_delete = customtkinter.CTkButton(master=self.f_container,
                                                  width=220, text="Supprimer",
                                               corner_radius=6,
                                                  fg_color='red',
                                                command=self.delete_creation)
        self.btn_delete.grid(row=4, column=1)

        self.lb_description = customtkinter.CTkLabel(self.f_container,
                                                     text=creation.description,
                                                     font=customtkinter.CTkFont(size=15,
                                                                                family='Century Gothic'))

        self.lb_description.grid(row=1, column=0)

        self.lb_description = customtkinter.CTkLabel(self.f_container, text=str(creation.amound)+' XAF',
                                                     font=customtkinter.CTkFont(size=15,
                                                                                family='Century Gothic'))

        self.lb_description.grid(row=2, column=0)

        self.lb_created_at = customtkinter.CTkLabel(self.f_container, text=creation.created_at,
                                                     font=customtkinter.CTkFont(size=15,
                                                                                family='Century Gothic'))

        self.lb_created_at.grid(row=3, column=0)

    def open_edit_page(self):
        self.app.creation_edit = CreationEdit(creation=self.creation, master=self.app)
        self.app.detail_is_open = True
        self.app.select_frame_by_name("creation_edit")

    def delete_creation(self):
        mb = messagebox.askyesno("Suppression de la creation",
                                 "Voulez vous vraiment supprimer {} ?".format(self.creation.name))
        if mb is True:
            controller = Creationcontroller()
            status = controller.delete_creation(self.creation.id)
            if status is 204:
                messagebox.showinfo("Message", "Suppréssion éffectuée avec succès")



if __name__ == "__main__":
    app = CreationDetails()
    app.mainloop()
