import tkinter

from tkinter import *
from tkinter import messagebox

import customtkinter
import os
from PIL import Image
import PIL.ImageTk as ptk
import PIL as p

from controllers.creation_controller import Creationcontroller
from controllers.mtn_api import PaiementMoMo
from models.creations import Creation
from views.creation_add import CreationAdd
from views.creation_details import CreationDetails
from views.creation_edit import CreationEdit


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.creation_edit = None
        self.title("I-Prod")
        self.geometry("700x450")
        self.is_detail = False
        self.detail_is_open = False
        self.add_is_open = False
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

        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        h = Scrollbar(self.second_frame, orient='horizontal')

        Grocery_Label = customtkinter.CTkLabel(self.second_frame,
                                               text="Liste des Créations",
                                               fg_color="transparent").grid(row=0,
                                                                            column=0,
                                                                            padx=20)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

        btn_add_creation = customtkinter.CTkButton(self,
                                                   command=lambda i=2: self.open_add_page(Creation()),
                                                   text="Ajouter")
        btn_add_creation.grid(column=2, row=0, sticky=SW, pady=20)



    def get_all_creations(self):
        self.creation_list = []
        self.creation_list.clear()
        self.creation_list = self.controller.get_all()
        row = 1
        colum = 0
        for i in range(0, len(self.creation_list)):
            print(i)
            lf_grocery1 = customtkinter.CTkFrame(master=self.second_frame, width=999, height=500)

            lf_grocery1.grid(row=row,
                             column=colum,
                             padx=(20, 20),
                             pady=(20, 20),
                             ipady=20, )
            colum += 1
            if colum is 5:
                row += 1
                colum = 0

            current_creation = self.creation_list[i]
            print(current_creation)
            # self.image_path = ptk.PhotoImage(p.Image.open("static/Images\{}".format(self.creation_list[i].image)))
            self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../static/images")
            self.creation_image = customtkinter.CTkImage(light_image=Image.open(current_creation.image),
                                                         size=(260, 300))
            self.lb_creation_image = customtkinter.CTkLabel(lf_grocery1, text=current_creation.name,
                                                            image=self.creation_image,
                                                            compound="top",
                                                            font=customtkinter.CTkFont(size=20,
                                                                                       family='Century Gothic'))
            self.lb_creation_image.grid(row=0, column=0)
            name_grocery1 = customtkinter.CTkLabel(lf_grocery1,
                                                   text=current_creation.description).grid(row=1, column=0)
            label_qty_grocery1 = customtkinter.CTkLabel(lf_grocery1,
                                                        text=str(current_creation.amound) + 'XAF',
                                                        anchor='center').grid(row=2, column=0)
            btn_details = customtkinter.CTkButton(lf_grocery1,
                                                  text="Détails", anchor='s',
                                                  command=lambda i=i: self.get_current_creation(i)).grid(row=3,
                                                                                                         column=0)
            btn_buy = customtkinter.CTkButton(lf_grocery1,
                                              text="Acheter", anchor='s',
                                              command=lambda i=i: self.popupwin(current_creation)).grid(row=4,
                                                                                                        column=0,
                                                                                                        pady=10)
    def open_add_page(self, creation: Creation):
        self.add_is_open = True
        self.creation_add = CreationAdd(master=self)
        self.select_frame_by_name("creation_add")
        
    def get_current_creation(self, index):

        print(self.creation_list[index].name)
        responce = self.controller.get_by_id(self.creation_list[index].id)
        self.creation = CreationDetails(creation=responce, master=self, app=self)
        self.is_detail = True
        self.select_frame_by_name('creation_details')

    def paiement_momo(self, creation):
        paiement = PaiementMoMo(phone_number="44444444", amound=creation.amound)
        statut = paiement.requesttopay()
        print(statut)
        if statut is not 201:
            messagebox.showinfo("Info Paiement", "Paiement éffectué avec succès")
            self.top.destroy()
        else:
            messagebox.showerror("Echec", "Une erreur c'est produite lors du paiement")
            self.top.destroy()

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
        if self.add_is_open is True:
            if name == "creation_add":
                self.creation_add.grid(row=0, column=1, sticky="nsew")
            else:
                self.creation_add.grid_forget()
    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.get_all_creations()
        self.select_frame_by_name("frame_2")


    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def popupwin(self, creation):
        # Create a Toplevel window
        self.top = Toplevel(self.master)
        self.top.geometry("300x100")
        self.top.title = "Payement par MoMo"

        # Create an Entry Widget in the Toplevel window
        entry = customtkinter.CTkEntry(self.top, width=270, placeholder_text="Entrer Votre numéro de téléphone")
        entry.pack()

        # Create a Button Widget in the Toplevel Window
        btn_buy = customtkinter.CTkButton(self.top,
                                          text="Payer",
                                          command=lambda creation=creation:
                                          self.paiement_momo(creation=creation))
        btn_buy.pack(pady=5, side=TOP)

    def close_win(self):
        self.top.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
