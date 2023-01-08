import tkinter

from tkinter import *
import customtkinter
import os
from PIL import Image
import PIL.ImageTk as ptk
import PIL as p

from controllers.creation_controller import Creationcontroller
from views.creation_details import CreationDetails


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("I-Prod")
        self.geometry("700x450")
        self.is_detail = False
        self.detail_is_open = False
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../static/icons")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")),
                                                 size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")),
                                                       size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")),
                                                       size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "ic_home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "ic_home.png")),
                                                 size=(20, 20))
        self.chat_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "ic_creation_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "ic_creation.png")),
            size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "ic_exposition_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "ic_exposition.png")),
            size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  I-Prod",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame,
                                                   corner_radius=0,
                                                   height=40,
                                                   border_spacing=10,
                                                   text="Acceuil",
                                                   fg_color="transparent",
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame,
                                                      corner_radius=0,
                                                      height=40,
                                                      border_spacing=10,
                                                      text="Créations",
                                                      fg_color="transparent",
                                                      text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.chat_image,
                                                      anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame,
                                                      corner_radius=0,
                                                      height=40,
                                                      border_spacing=10,
                                                      text="Expositions",
                                                      fg_color="transparent",
                                                      text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image,
                                                      anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6,
                                       column=0,
                                       padx=20,
                                       pady=20,
                                       sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self,
                                                 corner_radius=0,
                                                 fg_color="transparent"
                                                 )
        self.home_frame.grid_columnconfigure(0, weight=1)

        l1 = customtkinter.CTkLabel(master=self.home_frame,
                                    text="Home Page",
                                    font=('Century Gothic', 60))
        l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # create second frame
        self.controller = Creationcontroller()
        self.creation_list = self.controller.get_all()
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        Grocery_Label = customtkinter.CTkLabel(self.second_frame,
                                               text="Liste des Créations",
                                               fg_color="transparent").grid(row=0,
                                                                            column=0,
                                                                            padx=20)
        myscrollbar = Scrollbar(self.second_frame, orient="vertical")
        myscrollbar.grid(row=0, column=0)
        row = 0
        colum = 0
        for i in range(0, len(self.creation_list)):
            print(i)
            lf_grocery1 = customtkinter.CTkFrame(master=self.second_frame,width=999, height=500 )
            lf_grocery1.grid(row=row,
                             column=colum,
                             padx=(20, 20),
                             pady=(20, 20),
                             ipadx=20,
                             ipady=20,)
            colum += 1
            if colum is 5:
                row += 1
                colum = 0

            grocery1_image = ptk.PhotoImage(p.Image.open("static/Images\{}".format(self.creation_list[i].image)))
            label_grocery_1 = customtkinter.CTkLabel(lf_grocery1,
                                                     image=grocery1_image, anchor='n').grid(row=0, column=0)
            name_grocery1 = customtkinter.CTkLabel(lf_grocery1,
                                                   text=self.creation_list[i].name).grid(row=1, column=0)
            label_qty_grocery1 = customtkinter.CTkLabel(lf_grocery1,
                                                        text="Qty:", anchor='center').grid(row=2, column=0)
            add_grocery1 = customtkinter.CTkButton(lf_grocery1,
                                                   text="Ajouter au panier", anchor='s',
                                                   command=lambda i=i: self.get_current_creation(i)).grid(row=3,
                                                                                                          column=0)
        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def get_current_creation(self, index):

        print(self.creation_list[index].name)
        responce = self.controller.get_by_id(self.creation_list[index].id)
        self.creation = CreationDetails(creation=responce, master=self, app=self)
        self.is_detail = True
        self.select_frame_by_name('creation_details')

    def new_window(self, winclass):
        if self.win2_status == 0:
            try:
                if self.win2.status == 'normal':  # if it's not created yet
                    self.win2.focus_force()
            except:
                self.win2 = Toplevel(self)  # create
                # Win2(self.win2)  # populate
                self.win2_status = 1

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if self.is_detail is True:
            if name == "creation_details":
                self.creation.grid(row=0, column=1, sticky="nsew")
            else:
                self.creation.grid_forget()
            if self.detail_is_open is True:
                if name == "creation_edit":
                    self.creation_edit.grid(row=0, column=1, sticky="nsew")
                else:
                    self.creation_edit.grid_forget()
    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
