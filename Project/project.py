import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from menu import *
import re
from prettytable import PrettyTable
from tabulate import tabulate
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





####################################################### app class ###########################################################
#############################################################################################################################

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__()



###################################################### frame parameters #####################################################

        self.title("Kays Cafe")
        self.eval("tk::PlaceWindow . center")
        ctk.set_default_color_theme(r"Project\theme.json")


        global order_total_var
        order_total_var = tk.StringVar(self, "£0")
        


###################################################### frame controller ##################################################### 
        container = ctk.CTkFrame(self, height=1000, width=1000, fg_color="#161219")
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        


        #empty array for frames
        self.frames = {}

        #iterate through frames
        for F in (Title_frame, Menu_navigation_frame, Burger_menu, Not_burger_menu, Dessert_menu, Drinks_menu, Milkshake_menu):
            frame = F(container, self)

            #inistialize frane of that object
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0, weight=1)

        self.show_frame(Title_frame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


#~~~~~~~~~~~~title frame class~~~~~~~~~~~#

class Title_frame(ctk.CTkFrame):
    def __init__(self, parent, controller):
       super().__init__(parent)

       #--->generate widgets<---#

       #--->title widget
       self.title_page_title = ctk.CTkLabel(self, text="Kays Cafe", font=("Roboto", 70))
       self.title_page_title.pack(pady=(30,30))

       #--->logo widget
       self.title_page_logo = ctk.CTkImage(dark_image=Image.open(r"Project\images\Logo2.png"),size=(350,350))
       self.title_page_logo_widget = ctk.CTkLabel(self,image=self.title_page_logo, fg_color="#161219", text="")
       self.title_page_logo_widget.pack()

       #--->slogan widget
       self.title_page_slogan = ctk.CTkLabel(self, text="The cafe with attitude", font=("Roboto", 30))
       self.title_page_slogan.pack(pady=(80,0))

       #--->order button widget
       self.title_page_button = ctk.CTkButton(self, text="Order online, if you insist...", font=("Roboto", 70), cursor="hand2", border_spacing=20, command=lambda: controller.show_frame(Menu_navigation_frame))
       self.title_page_button.pack(side="bottom", padx=40, pady=40)


#~~~~~~~~~~~~menu navigation class~~~~~~~~~~~#

class Menu_navigation_frame(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

         #--->string variables<---#

        #--->title var
        self.menu_navigation_title_var = tk.StringVar(self, "Kays Cafe")

        #--->basket nav button
        self.menu_navigation_basket_button_var = tk.StringVar(self, "View basket")

        #--->menu buttons
        self.burgers_button_var = tk.StringVar(self, "Burger Menu")
        self.not_burgers_button_var = tk.StringVar(self, "Not Burger Menu")
        self.desserts_button_var = tk.StringVar(self, "Desserts Menu")
        self.drinks_button_var = tk.StringVar(self, "Drinks Menu")
        self.milkshakes_button_var = tk.StringVar(self, "Milkshakes Menu")

        welcome_text = "Welcome to Kays Cafe,\n\n" + "Basically we're sick of all you customers showing up and expecting us to wait on you all night,\n\n" + "So from now on you can order the food and we'll drop it off when its convenient for us"

        self.welcome_var = tk.StringVar(self)
        self.welcome_var.set(welcome_text)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->top frame & widgets<---#

        #--->top row frame
        self.menu_navigation_top_frame = ctk.CTkFrame(self,)
        
        #--->logo
        self.menu_navigation_logo = ctk.CTkImage(dark_image=Image.open(r"Project\images\Logo15.png"),size=(50,50))
        self.menu_navigation_logo_widget = ctk.CTkLabel(self.menu_navigation_top_frame, image=self.menu_navigation_logo, text="")

         #--->title
        self.menu_navigation_title = ctk.CTkLabel(
        self.menu_navigation_top_frame, textvariable=self.menu_navigation_title_var, font=("TkHeadingFont", 30))

        #--->frame for basket button and basket total
        self.menu_navigation_basket_frame = ctk.CTkFrame(self.menu_navigation_top_frame,)

        #--->basket navigation
        self.menu_navigation_basket_button = ctk.CTkButton(
        self.menu_navigation_basket_frame, textvariable=self.menu_navigation_basket_button_var, font=("TkHeadingFont", 10), height=10, width=30, border_width=0)

        #--->basket total
        self.menu_navigation_basket_total = ctk.CTkLabel(
        self.menu_navigation_basket_frame, textvariable=order_total_var, font=("TkHeadingFont", 10))

        #--->menu navigation frame & buttons<---#

        #--->menu navigation buttons frame
        self.menu_navigation_buttons_frame = ctk.CTkFrame(self, border_width=0)

        #--->burger menu widget
        self.burgers_button = ctk.CTkButton(self.menu_navigation_buttons_frame, textvariable=self.burgers_button_var, command=lambda: controller.show_frame(Burger_menu))
         
        #--->not burgers menu widget
        self.not_burgers_button = ctk.CTkButton(self.menu_navigation_buttons_frame, textvariable=self.not_burgers_button_var, command=lambda: controller.show_frame(Not_burger_menu))

        #--->desserts menu widget
        self.desserts_button = ctk.CTkButton(self.menu_navigation_buttons_frame, textvariable=self.desserts_button_var, command=lambda: controller.show_frame(Dessert_menu))

        #--->drinks menu widget
        self.drinks_button = ctk.CTkButton(self.menu_navigation_buttons_frame, textvariable=self.drinks_button_var, command=lambda: controller.show_frame(Drinks_menu))

        #--->milkshakes menu widget
        self.milkshakes_button = ctk.CTkButton(self.menu_navigation_buttons_frame, textvariable=self.milkshakes_button_var, command=lambda: controller.show_frame(Milkshake_menu))

        #---text/photo frame
        self.text_photo_frame = ctk.CTkFrame(self, border_width=0)
        self.welcome_label = ctk.CTkLabel(self.text_photo_frame, textvariable=self.welcome_var)
        
        #--->bottom row frame & widgets<---#

        #--->bottom row frame
        self.menu_navigation_bottom_frame = ctk.CTkFrame(self)

        #--->facebook widget
        facebook_logo = ctk.CTkImage(Image.open(r"Project\images\facebook_logo.gif"),size=(30,30))
        facebook_logo_widget = ctk.CTkButton(self.menu_navigation_bottom_frame, text="",  image=facebook_logo, height=30, width=30)

        #--->instagram widget
        instagram_logo = ctk.CTkImage(Image.open(r"Project\images\instagram_logo.png"),size=(30,30))
        instagram_logo_widget = ctk.CTkButton(self.menu_navigation_bottom_frame, text="",  image=instagram_logo, height=30, width=30)

        #--->twitter/x widget
        x_logo = ctk.CTkImage(Image.open(r"Project\images\x_logo.jpg"),size=(30,30))
        x_logo_widget = ctk.CTkButton(self.menu_navigation_bottom_frame, text="", image=x_logo, height=30, width=30)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->button command configurations<---#

        #--->basket nav button
        self.menu_navigation_basket_button.configure(command=basket_window)

        #--->menu buttons
        self.burgers_button.configure(command=lambda: controller.show_frame(Burger_menu))
        self.not_burgers_button.configure(command=lambda: controller.show_frame(Not_burger_menu))
        self.desserts_button.configure(command=lambda: controller.show_frame(Dessert_menu))
        self.drinks_button.configure(command=lambda: controller.show_frame(Drinks_menu))
        self.milkshakes_button.configure(command=lambda: controller.show_frame(Milkshake_menu))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->place widgets on grid<---#

        #--->top row frame
        self.menu_navigation_top_frame.grid(row=0, column=0, columnspan=7, ipady=20, sticky="nsew")

        #--->logo
        self.menu_navigation_logo_widget.grid(column=0, row=0)

         #--->title
        self.menu_navigation_title.grid(column=1, row=0, columnspan=5)

        #--->frame for basket button and basket total
        self.menu_navigation_basket_frame.grid(row=0, column=6, padx=(0,5), pady=6, sticky="nsew")

        #--->basket navigation
        self.menu_navigation_basket_button.grid(column=0,row=0, sticky="nsew")

        #--->basket total
        self.menu_navigation_basket_total.grid(column=1, row=0, sticky="nsew")

        #--->menu navigation buttons frame
        self.menu_navigation_buttons_frame.grid(row=1, column=0, rowspan=5, columnspan=2, sticky="nsew")

        #--->burger menu widget
        self.burgers_button.grid(column=0, row=0, columnspan=2, ipady=60, padx=20, pady=(20,10), sticky="nsew")
         
        #--->not burgers menu widget
        self.not_burgers_button.grid(column=0, row=1, columnspan=2, ipady=60, padx=20, pady=10, sticky="nsew")

        #--->desserts menu widget
        self.desserts_button.grid(column=0, row=2, columnspan=2, ipady=60, padx=20, pady=10, sticky="nsew")

        #--->drinks menu widget
        self.drinks_button.grid(column=0, row=3, columnspan=2, ipady=60, padx=20, pady=10, sticky="nsew")

        #--->milkshakes menu widget
        self.milkshakes_button.grid(column=0, row=4, columnspan=2, ipady=60, padx=20, pady=(10,20), sticky="nsew")

        #---text/photo frame
        self.text_photo_frame.grid(row=1, column=2, rowspan=5, columnspan=5, sticky="nsew")

        #--->welcome label
        self.welcome_label.grid(column=0, row=0, sticky="nsew")

        #--->bottom row frame
        self.menu_navigation_bottom_frame.grid(row=6, column=0, columnspan=7, ipady=20, sticky="nsew")

        #--->facebook widget
        facebook_logo_widget.grid(column=0, row=0)

        #--->instagram widget
        instagram_logo_widget.grid(column=1, row=0)

        #--->twitter/x widget
        x_logo_widget.grid(column=2, row=0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->configure frames and widgets<---#
        
        #--->configure top row frame
        self.columnconfigure(0, weight=2)
        self.rowconfigure(0, weight=1)
        #--->configure logo
        self.menu_navigation_top_frame.columnconfigure(0, weight=2)
        self.menu_navigation_top_frame.rowconfigure(0, weight=1)
        #--->configure title
        self.menu_navigation_top_frame.columnconfigure(1, weight=2)
        self.menu_navigation_top_frame.rowconfigure(0, weight=1)
        #--->configure basket frame
        self.menu_navigation_top_frame.columnconfigure(6, weight=2)
        self.menu_navigation_top_frame.rowconfigure(0, weight=1)
        #--->configure basket button
        self.menu_navigation_basket_frame.columnconfigure(0, weight=2)
        self.menu_navigation_basket_frame.rowconfigure(0, weight=1)
        #--->configure basket total
        self.menu_navigation_basket_frame.columnconfigure(1, weight=2)
        self.menu_navigation_basket_frame.rowconfigure(0, weight=1)
        
        #--->configure menu nav frame
        self.columnconfigure(0, weight=2)
        self.rowconfigure(1, weight=1)
        #--->configure burger button
        self.menu_navigation_buttons_frame.columnconfigure(0, weight=2)
        self.menu_navigation_buttons_frame.rowconfigure(0, weight=1)
        #--->configure not burger button
        self.menu_navigation_buttons_frame.columnconfigure(0, weight=2)
        self.menu_navigation_buttons_frame.rowconfigure(1, weight=1)
        #--->configure desserts button
        self.menu_navigation_buttons_frame.columnconfigure(0, weight=2)
        self.menu_navigation_buttons_frame.rowconfigure(2, weight=1)
        #--->configure drinks button
        self.menu_navigation_buttons_frame.columnconfigure(0, weight=2)
        self.menu_navigation_buttons_frame.rowconfigure(3, weight=1)
        #--->configure milkshakes button
        self.menu_navigation_buttons_frame.columnconfigure(0, weight=2)
        self.menu_navigation_buttons_frame.rowconfigure(4, weight=1)

        #--->configure text/photo frame
        self.columnconfigure(2, weight=2)
        self.rowconfigure(1, weight=1)
        #--->configure welcome label
        self.text_photo_frame.columnconfigure(0, weight=1)
        self.text_photo_frame.rowconfigure(0, weight=1)

        #--->configure bottom row frame
        self.columnconfigure(0, weight=2)
        self.rowconfigure(6, weight=1)
        #--->configure facebook widget
        self.menu_navigation_bottom_frame.columnconfigure(0,weight=2)
        self.menu_navigation_bottom_frame.rowconfigure(0,weight=1)
        #--->configure instagram widget
        self.menu_navigation_bottom_frame.columnconfigure(1,weight=2)
        self.menu_navigation_bottom_frame.rowconfigure(0,weight=1)
        #--->configure twitter/x widget
        self.menu_navigation_bottom_frame.columnconfigure(2,weight=2)
        self.menu_navigation_bottom_frame.rowconfigure(0,weight=1)
               
#~~~~~~~~~~~~burger menu class~~~~~~~~~~~#

class Burger_menu(ctk.CTkFrame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->string variables<---#

        #--->top frame

        #basket var
        self.burger_basket_var = tk.StringVar(self, f"Placeholder")

        #--->item name & price

        self.burger_var1 = tk.StringVar(self, f"{burger_option_1.product}\n\n £{burger_option_1.price}")
        self.burger_var2 = tk.StringVar(self, f"{burger_option_2.product}\n\n £{burger_option_2.price}")
        self.burger_var3 = tk.StringVar(self, f"{burger_option_3.product}\n\n £{burger_option_3.price}")        
        self.chick_burger_var1 = tk.StringVar(self, f"{chick_burger_option_1.product}\n\n £{chick_burger_option_1.price}")        
        self.chick_burger_var2 = tk.StringVar(self, f"{chick_burger_option_2.product}\n\n £{chick_burger_option_2.price}")
        self.chick_burger_var3 = tk.StringVar(self, f"{chick_burger_option_3.product}\n\n £{chick_burger_option_3.price}")
        self.vegetarian_var = tk.StringVar(self, f"{vegetarian_option_1.product}\n\n £{vegetarian_option_1.price}")        
        self.vegan_var = tk.StringVar(self, f"{vegan_option_1.product}\n\n £{vegan_option_1.price}")

        #--->item description

        self.burger_description1 = tk.StringVar(self, "Placeholder text....")
        self.burger_description2 = tk.StringVar(self, "Placeholder text....")
        self.burger_description3 = tk.StringVar(self, "Placeholder text....")
        self.chick_burger_description1 = tk.StringVar(self, "Placeholder text....")
        self.chick_burger_description2 = tk.StringVar(self, "Placeholder text....")
        self.chick_burger_description3 = tk.StringVar(self, "Placeholder text....")
        self.v_burger_description = tk.StringVar(self, "Placeholder text....")        
        self.ve_burger_description = tk.StringVar(self, "Placeholder text....")

        #--->item basket price

        self.burger_basket1 = tk.StringVar(self, f"£{burger_option_1.price}")
        self.burger_basket2 = tk.StringVar(self, f"£{burger_option_2.price}")
        self.burger_basket3 = tk.StringVar(self, f"£{burger_option_3.price}")
        self.chick_burger_basket1 = tk.StringVar(self, f"£{chick_burger_option_1.price}")
        self.chick_burger_basket2 = tk.StringVar(self, f"£{chick_burger_option_2.price}")
        self.chick_burger_basket3 = tk.StringVar(self, f"£{chick_burger_option_3.price}")
        self.v_burger_basket = tk.StringVar(self, f"£{vegetarian_option_1.price}")
        self.ve_burger_basket = tk.StringVar(self, f"£{vegan_option_1.price}")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->top frame & widgets<---#

        #--->top row frame
        self.burger_menu_top_frame = ctk.CTkFrame(self)
        
        #--->logo
        self.burger_menu_logo = ctk.CTkImage(dark_image=Image.open(r"Project\images\Logo15.png"),size=(50,50))
        self.burger_menu_logo_widget = ctk.CTkLabel(self.burger_menu_top_frame, image=self.burger_menu_logo, text="")

         #--->title
        self.burger_menu_title = ctk.CTkLabel(
        self.burger_menu_top_frame, text="Burger Menu",font=("TkHeadingFont", 30))

        #--->frame for basket button and basket total
        self.burger_menu_basket_frame = ctk.CTkFrame(self.burger_menu_top_frame)

        #--->basket navigation
        self.burger_menu_basket_button = ctk.CTkButton(
        self.burger_menu_basket_frame, text="View basket", font=("TkHeadingFont", 10), height=10, width=30, border_width=0)

        #--->basket total
        self.burger_menu_basket_total = ctk.CTkLabel(
        self.burger_menu_basket_frame, textvariable=order_total_var,font=("TkHeadingFont", 10))

        #--->option buttons<---#
        
        #--->burger buttons
        self.burger_option1 = ctk.CTkButton(self, textvariable=self.burger_var1)
        self.burger_option2 = ctk.CTkButton(self, textvariable=self.burger_var2)
        self.burger_option3 = ctk.CTkButton(self, textvariable=self.burger_var3)

        #--->chicken burger buttons
        self.chick_burger_option1 = ctk.CTkButton(self, textvariable=self.chick_burger_var1)
        self.chick_burger_option2 = ctk.CTkButton(self, textvariable=self.chick_burger_var2)
        self.chick_burger_option3 = ctk.CTkButton(self, textvariable=self.chick_burger_var3)

        #--->vegetarian/vegan buttons
        self.v_burger_option = ctk.CTkButton(self, textvariable=self.vegetarian_var)
        self.ve_burger_option = ctk.CTkButton(self, textvariable=self.vegan_var)

        #--->back button
        self.burger_back = ctk.CTkButton(self, text="Back")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #--->option button command configurations<---#

        #--->basket navigation button
        self.burger_menu_basket_button.configure(command=basket_window)

        #--->option buttons
        self.burger_option1.configure(command=lambda: add_to_basket_window(self, burger_option_1.product, self.burger_description1, self.burger_basket1, burger_option_1, Burger_menu))
        self.burger_option2.configure(command=lambda: add_to_basket_window(self, burger_option_2.product, self.burger_description2, self.burger_basket2, burger_option_2, Burger_menu))
        self.burger_option3.configure(command=lambda: add_to_basket_window(self, burger_option_3.product, self.burger_description3, self.burger_basket3, burger_option_3, Burger_menu))
        self.chick_burger_option1.configure(command=lambda: add_to_basket_window(self, chick_burger_option_1.product, self.chick_burger_description1, self.chick_burger_basket1, chick_burger_option_1, Burger_menu))
        self.chick_burger_option2.configure(command=lambda: add_to_basket_window(self, chick_burger_option_2.product, self.chick_burger_description2, self.chick_burger_basket2, chick_burger_option_2, Burger_menu))
        self.chick_burger_option3.configure(command=lambda: add_to_basket_window(self, chick_burger_option_3.product, self.chick_burger_description3, self.chick_burger_basket3, chick_burger_option_3, Burger_menu))
        self.v_burger_option.configure(command=lambda: add_to_basket_window(self, vegetarian_option_1.product, self.v_burger_description, self.v_burger_basket, vegetarian_option_1, Burger_menu))
        self.ve_burger_option.configure(command=lambda: add_to_basket_window(self, vegan_option_1.product, self.ve_burger_description, self.ve_burger_basket, vegan_option_1, Burger_menu))

        #--->back button
        self.burger_back.configure(command=lambda: controller.show_frame(Menu_navigation_frame))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->place widgets on grid<---#

        #--->top row frame
        self.burger_menu_top_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")

        
        #--->logo
        self.burger_menu_logo_widget.grid(column=0, row=0)

         #--->title
        self.burger_menu_title.grid(column=1, row=0)

        #--->frame for basket button and basket total
        self.burger_menu_basket_frame.grid(row=0, column=2, padx=(0,5), pady=6, sticky="nsew")

        #--->basket navigation
        self.burger_menu_basket_button.grid(column=0,row=0, sticky="nsew")

        #--->basket total
        self.burger_menu_basket_total.grid(column=1, row=0, sticky="nsew")


        #--->burger buttons
        self.burger_option1.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.burger_option2.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)
        self.burger_option3.grid(row=3, column=0, sticky="nsew", padx=20, pady=20)

        #--->chicken burger buttons
        self.chick_burger_option1.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        self.chick_burger_option2.grid(row=2, column=1, sticky="nsew", padx=20, pady=20)
        self.chick_burger_option3.grid(row=3, column=1, sticky="nsew", padx=20, pady=20)

        #--->vegetarian/vegan buttons
        self.v_burger_option.grid(row=1, column=2, sticky="nsew", padx=20, pady=20)
        self.ve_burger_option.grid(row=2, column=2, sticky="nsew", padx=20, pady=20)

        #--->back button
        self.burger_back.grid(row=3, column=2, padx=20, pady=20, sticky="nsew")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->confirguring frames & widgets<---#

        #top row frame already configured in app class#

        #--->logo
        self.burger_menu_top_frame.columnconfigure(0, weight=1)
        self.burger_menu_top_frame.rowconfigure(0, weight=1)
        #--->burger title
        self.burger_menu_top_frame.columnconfigure(1, weight=1)
        self.burger_menu_top_frame.rowconfigure(0, weight=1)
        #burger basket frame
        self.burger_menu_top_frame.columnconfigure(2, weight=1)
        self.burger_menu_top_frame.rowconfigure(0, weight=1)
        #burger basket button
        self.burger_menu_basket_frame.columnconfigure(0, weight=1)
        self.burger_menu_basket_frame.rowconfigure(0, weight=1)
        #burger basket total
        self.burger_menu_basket_frame.columnconfigure(1, weight=1)
        self.burger_menu_basket_frame.rowconfigure(0, weight=1)
        #burger option 1
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        #burger option 2
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        #burger option 3
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        #chick option 1
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        #chick option 2
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        #chick option 3
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)
        #vegetarian option
        self.columnconfigure(2, weight=1)
        self.rowconfigure(1, weight=1)
        #vegan option
        self.columnconfigure(2, weight=1)
        self.rowconfigure(2, weight=1)
        #burger back button
        self.columnconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

#~~~~~~~~~~~~not burger menu class~~~~~~~~~~~#

class Not_burger_menu(ctk.CTkFrame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->string variables<---#
        
        #--->top row frame

        #title var
        self.not_burger_title_var = tk.StringVar(self, "Not Burger Menu")

        #basket button var
        self.not_burger_basket_button_var = tk.StringVar(self, "View Basket")

        #basket total var
        self.not_burger_basket_var = tk.StringVar(self, f"Placeholder")

        #--->item name & price

        self.not_burger_var1 = tk.StringVar(self, f"{not_burger_option_1.product} \n\n £{not_burger_option_1.price}")
        self.not_burger_var2 = tk.StringVar(self, f"{not_burger_option_2.product} \n\n £{not_burger_option_2.price}")
        self.not_burger_var3 = tk.StringVar(self, f"{not_burger_option_3.product} \n\n £{not_burger_option_3.price}")
        self.not_burger_var4 = tk.StringVar(self, f"{not_burger_option_4.product} \n\n £{not_burger_option_4.price}")
        self.not_burger_var5 = tk.StringVar(self, f"{not_burger_option_5.product} \n\n £{not_burger_option_5.price}")
        self.not_burger_var6 = tk.StringVar(self, f"{not_burger_option_6.product} \n\n £{not_burger_option_6.price}")
        self.not_burger_var7 = tk.StringVar(self, f"{not_burger_option_7.product} \n\n £{not_burger_option_7.price}")
        self.not_burger_var8 = tk.StringVar(self, f"{not_burger_option_8.product} \n\n £{not_burger_option_8.price}")
        self.not_burger_var9 = tk.StringVar(self, f"{not_burger_option_9.product} \n\n £{not_burger_option_9.price}")

        #--->item description

        self.not_burger_description1 = tk.StringVar(self, "Placeholder text.....")
        self.not_burger_description2 = tk.StringVar(self, "Placeholder text.....")
        self.not_burger_description3 = tk.StringVar(self, "Placeholder text.....")
        self.not_burger_description4 = tk.StringVar(self, "Placeholder text.....")
        self.not_burger_description5 = tk.StringVar(self, "Placeholder text.....")
        self.not_burger_description6 = tk.StringVar(self, "Placeholder text.....")
        self.not_burger_description7 = tk.StringVar(self, "Placeholder text.....")
        self.not_burger_description8 = tk.StringVar(self, "Placeholder text.....")
        self.not_burger_description9 = tk.StringVar(self, "Placeholder text.....")

        #--->item basket price

        self.not_burger_basket1 = tk.StringVar(self, f"£{not_burger_option_1.price}")
        self.not_burger_basket2 = tk.StringVar(self, f"£{not_burger_option_2.price}")
        self.not_burger_basket3 = tk.StringVar(self, f"£{not_burger_option_3.price}")
        self.not_burger_basket4 = tk.StringVar(self, f"£{not_burger_option_4.price}")
        self.not_burger_basket5 = tk.StringVar(self, f"£{not_burger_option_5.price}")
        self.not_burger_basket6 = tk.StringVar(self, f"£{not_burger_option_6.price}")
        self.not_burger_basket7 = tk.StringVar(self, f"£{not_burger_option_7.price}")
        self.not_burger_basket8 = tk.StringVar(self, f"£{not_burger_option_8.price}")
        self.not_burger_basket9 = tk.StringVar(self, f"£{not_burger_option_9.price}")

        #back button var
        self.not_burger_back_var = tk.StringVar(self, "Back")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->top frame & widgets<---#

        #--->top row frame
        self.not_burger_menu_top_frame = ctk.CTkFrame(self)
        
        #--->logo
        self.not_burger_menu_logo = ctk.CTkImage(dark_image=Image.open(r"Project\images\Logo15.png"),size=(50,50))
        self.not_burger_menu_logo_widget = ctk.CTkLabel(self.not_burger_menu_top_frame, image=self.not_burger_menu_logo, text="")

         #--->title
        self.not_burger_menu_title = ctk.CTkLabel(
        self.not_burger_menu_top_frame, textvariable=self.not_burger_title_var, font=("TkHeadingFont", 30))

        #--->frame for basket button and basket total
        self.not_burger_menu_basket_frame = ctk.CTkFrame(self.not_burger_menu_top_frame)
        self.not_burger_menu_basket_frame.grid(row=0, column=2, padx=(0,5), pady=6, sticky="nsew")

        #--->basket navigation
        self.not_burger_menu_basket_button = ctk.CTkButton(
        self.not_burger_menu_basket_frame, textvariable=self.not_burger_basket_button_var, font=("TkHeadingFont", 10), height=10, width=30, border_width=0)

        #--->basket total
        self.not_burger_menu_basket_total = ctk.CTkLabel(
        self.not_burger_menu_basket_frame, textvariable=order_total_var, font=("TkHeadingFont", 10))
        
        #--->item buttons
        self.not_burger_option1 = ctk.CTkButton(self, textvariable=self.not_burger_var1)
        self.not_burger_option2 = ctk.CTkButton(self, textvariable=self.not_burger_var2)
        self.not_burger_option3 = ctk.CTkButton(self, textvariable=self.not_burger_var3)
        self.not_burger_option4 = ctk.CTkButton(self, textvariable=self.not_burger_var4)
        self.not_burger_option5 = ctk.CTkButton(self, textvariable=self.not_burger_var5)
        self.not_burger_option6 = ctk.CTkButton(self, textvariable=self.not_burger_var6)
        self.not_burger_option7 = ctk.CTkButton(self, textvariable=self.not_burger_var7)
        self.not_burger_option8 = ctk.CTkButton(self, textvariable=self.not_burger_var8)
        self.not_burger_option9 = ctk.CTkButton(self, textvariable=self.not_burger_var9)
       
        #--->back button
        self.not_burger_back = ctk.CTkButton(self, textvariable=self.not_burger_back_var)







#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #--->button command configurations<---#

        #--->basket nav button
        self.not_burger_menu_basket_button.configure(command=basket_window)

        #--->item buttons
        self.not_burger_option1.configure(command=lambda: add_to_basket_window(self, not_burger_option_1.product, self.not_burger_description1, self.not_burger_basket1, not_burger_option_1, Not_burger_menu))
        self.not_burger_option2.configure(command=lambda: add_to_basket_window(self, not_burger_option_2.product, self.not_burger_description2, self.not_burger_basket2, not_burger_option_2, Not_burger_menu))
        self.not_burger_option3.configure(command=lambda: add_to_basket_window(self, not_burger_option_3.product, self.not_burger_description3, self.not_burger_basket3, not_burger_option_3, Not_burger_menu))
        self.not_burger_option4.configure(command=lambda: add_to_basket_window(self, not_burger_option_4.product, self.not_burger_description4, self.not_burger_basket4, not_burger_option_4, Not_burger_menu))
        self.not_burger_option5.configure(command=lambda: add_to_basket_window(self, not_burger_option_5.product, self.not_burger_description5, self.not_burger_basket5, not_burger_option_5, Not_burger_menu))
        self.not_burger_option6.configure(command=lambda: add_to_basket_window(self, not_burger_option_6.product, self.not_burger_description6, self.not_burger_basket6, not_burger_option_6, Not_burger_menu))
        self.not_burger_option7.configure(command=lambda: add_to_basket_window(self, not_burger_option_7.product, self.not_burger_description7, self.not_burger_basket7, not_burger_option_7, Not_burger_menu))
        self.not_burger_option8.configure(command=lambda: add_to_basket_window(self, not_burger_option_8.product, self.not_burger_description8, self.not_burger_basket8, not_burger_option_8, Not_burger_menu))
        self.not_burger_option9.configure(command=lambda: add_to_basket_window(self, not_burger_option_9.product, self.not_burger_description9, self.not_burger_basket9, not_burger_option_9, Not_burger_menu))

        #--->back button
        self.not_burger_back.configure(command=lambda: controller.show_frame(Menu_navigation_frame))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #--->place widgets on grid<---#

        #--->top row frame
        self.not_burger_menu_top_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")

        
        #--->logo
        self.not_burger_menu_logo_widget.grid(column=0, row=0)

         #--->title
        self.not_burger_menu_title.grid(column=1, row=0)

        #--->frame for basket button and basket total
        self.not_burger_menu_basket_frame.grid(row=0, column=2, padx=(0,5), pady=6, sticky="nsew")

        #--->basket navigation
        self.not_burger_menu_basket_button.grid(column=0,row=0, sticky="nsew")

        #--->basket total
        self.not_burger_menu_basket_total.grid(column=1, row=0, sticky="nsew")


        #--->option buttons<---#

        
        #--->not burger buttons
        self.not_burger_option1.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.not_burger_option2.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)
        self.not_burger_option3.grid(row=3, column=0, sticky="nsew", padx=20, pady=20)
        self.not_burger_option4.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        self.not_burger_option5.grid(row=2, column=1, sticky="nsew", padx=20, pady=20)
        self.not_burger_option6.grid(row=3, column=1, sticky="nsew", padx=20, pady=20)
        self.not_burger_option7.grid(row=1, column=2, sticky="nsew", padx=20, pady=20)
        self.not_burger_option8.grid(row=2, column=2, sticky="nsew", padx=20, pady=20)
        self.not_burger_option9.grid(row=3, column=2, sticky="nsew", padx=20, pady=20)
       
        #--->back button
        self.not_burger_back.grid(row=4, column=1, padx=20, pady=20, sticky="nsew")





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #--->confirguring frames & widgets<---#

        #top row frame already configured in app class#

        #--->logo
        self.not_burger_menu_top_frame.columnconfigure(0, weight=1)
        self.not_burger_menu_top_frame.rowconfigure(0, weight=1)
        #--->not_burger title
        self.not_burger_menu_top_frame.columnconfigure(1, weight=1)
        self.not_burger_menu_top_frame.rowconfigure(0, weight=1)
        #not_burger basket frame
        self.not_burger_menu_top_frame.columnconfigure(2, weight=1)
        self.not_burger_menu_top_frame.rowconfigure(0, weight=1)
        #not_burger basket button
        self.not_burger_menu_basket_frame.columnconfigure(0, weight=1)
        self.not_burger_menu_basket_frame.rowconfigure(0, weight=1)
        #not_burger basket total
        self.not_burger_menu_basket_frame.columnconfigure(1, weight=1)
        self.not_burger_menu_basket_frame.rowconfigure(0, weight=1)
        #not_burger option 1
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        #not_burger option 2
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        #not_burger option 3
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        #not_burger option 4
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        #not_burger option 5
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        #not_burger option 6
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)
        #not_burger option 7
        self.columnconfigure(2, weight=1)
        self.rowconfigure(1, weight=1)
        #not_burger option 8
        self.columnconfigure(2, weight=1)
        self.rowconfigure(2, weight=1)
        #not_burger option 9
        self.columnconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        #not_burger back button
        self.columnconfigure(1, weight=1)
        self.rowconfigure(4, weight=1)

#~~~~~~~~~~~~dessert menu class~~~~~~~~~~~

class Dessert_menu(ctk.CTkFrame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->string variables<---#

        #--->title var
        self.dessert_title_var = tk.StringVar(self, "Dessert Menu")

        #--->basket button var
        self.dessert_basket_button_var = tk.StringVar(self, "View Basket")

        #--->basket total var
        self.dessert_basket_var = tk.StringVar(self, f"Placeholder")

        #--->item name & price

        self.dessert_var1 = tk.StringVar(self, f"{dessert_option_1.product} \n\n £{dessert_option_1.price}")
        self.dessert_var2 = tk.StringVar(self, f"{dessert_option_2.product} \n\n £{dessert_option_2.price}")
        self.dessert_var3 = tk.StringVar(self, f"{dessert_option_3.product} \n\n £{dessert_option_3.price}")
        self.dessert_var4 = tk.StringVar(self, f"{dessert_option_4.product} \n\n £{dessert_option_4.price}")
        self.dessert_var5 = tk.StringVar(self, f"{dessert_option_5.product} \n\n £{dessert_option_5.price}")
        self.dessert_var6 = tk.StringVar(self, f"{dessert_option_6.product} \n\n £{dessert_option_6.price}")
        self.dessert_var7 = tk.StringVar(self, f"{dessert_option_7.product} \n\n £{dessert_option_7.price}")
        self.dessert_var8 = tk.StringVar(self, f"{dessert_option_8.product} \n\n £{dessert_option_8.price}")
        self.dessert_var9 = tk.StringVar(self, f"{dessert_option_9.product} \n\n £{dessert_option_9.price}")

        #--->item description

        self.dessert_description1 = tk.StringVar(self, "Placeholder text.....")
        self.dessert_description2 = tk.StringVar(self, "Placeholder text.....")
        self.dessert_description3 = tk.StringVar(self, "Placeholder text.....")
        self.dessert_description4 = tk.StringVar(self, "Placeholder text.....")
        self.dessert_description5 = tk.StringVar(self, "Placeholder text.....")
        self.dessert_description6 = tk.StringVar(self, "Placeholder text.....")
        self.dessert_description7 = tk.StringVar(self, "Placeholder text.....")
        self.dessert_description8 = tk.StringVar(self, "Placeholder text.....")
        self.dessert_description9 = tk.StringVar(self, "Placeholder text.....")


        #--->item basket price

        self.dessert_basket1 = tk.StringVar(self, f"£{dessert_option_1.price}")
        self.dessert_basket2 = tk.StringVar(self, f"£{dessert_option_2.price}")
        self.dessert_basket3 = tk.StringVar(self, f"£{dessert_option_3.price}")
        self.dessert_basket4 = tk.StringVar(self, f"£{dessert_option_4.price}")
        self.dessert_basket5 = tk.StringVar(self, f"£{dessert_option_5.price}")
        self.dessert_basket6 = tk.StringVar(self, f"£{dessert_option_6.price}")
        self.dessert_basket7 = tk.StringVar(self, f"£{dessert_option_7.price}")
        self.dessert_basket8 = tk.StringVar(self, f"£{dessert_option_8.price}")
        self.dessert_basket9 = tk.StringVar(self, f"£{dessert_option_9.price}")

        #--->back button var
        self.dessert_back_var = tk.StringVar(self, "Back")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


        #--->top frame & widgets<---#

        #--->top row frame
        self.dessert_menu_top_frame = ctk.CTkFrame(self)
        
        #--->logo
        self.dessert_menu_logo = ctk.CTkImage(dark_image=Image.open(r"Project\images\Logo15.png"),size=(50,50))
        self.dessert_menu_logo_widget = ctk.CTkLabel(self.dessert_menu_top_frame, image=self.dessert_menu_logo, text="")
        
         #--->title
        self.dessert_menu_title = ctk.CTkLabel(
        self.dessert_menu_top_frame, textvariable=self.dessert_title_var, font=("TkHeadingFont", 30))
        
        #--->frame for basket button and basket total
        self.dessert_menu_basket_frame = ctk.CTkFrame(self.dessert_menu_top_frame)
        
        #--->basket navigation
        self.dessert_menu_basket_button = ctk.CTkButton(
        self.dessert_menu_basket_frame, textvariable=self.dessert_basket_button_var, font=("TkHeadingFont", 10), 
        cursor="hand2", hover_color="#BC006C", height=10, width=30, border_width=0)
        
        #--->basket total
        self.dessert_menu_basket_total = ctk.CTkLabel(
        self.dessert_menu_basket_frame, textvariable=order_total_var, font=("TkHeadingFont", 10))

        #--->dessert buttons
        self.dessert_option1 = ctk.CTkButton(self, textvariable=self.dessert_var1)
        self.dessert_option2 = ctk.CTkButton(self, textvariable=self.dessert_var2)
        self.dessert_option3 = ctk.CTkButton(self, textvariable=self.dessert_var3)
        self.dessert_option4 = ctk.CTkButton(self, textvariable=self.dessert_var4)
        self.dessert_option5 = ctk.CTkButton(self, textvariable=self.dessert_var5)
        self.dessert_option6 = ctk.CTkButton(self, textvariable=self.dessert_var6)
        self.dessert_option7 = ctk.CTkButton(self, textvariable=self.dessert_var7)
        self.dessert_option8 = ctk.CTkButton(self, textvariable=self.dessert_var8)
        self.dessert_option9 = ctk.CTkButton(self, textvariable=self.dessert_var9)
       
        #--->back button
        self.dessert_back = ctk.CTkButton(self, textvariable=self.dessert_back_var)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->button command configurations<---#

        #--->basket nav button
        self.dessert_menu_basket_button.configure(command=basket_window)

        #--->item buttons
        self.dessert_option1.configure(command=lambda: add_to_basket_window(self, dessert_option_1.product, self.dessert_description1, self.dessert_basket1, dessert_option_1, Dessert_menu))
        self.dessert_option2.configure(command=lambda: add_to_basket_window(self, dessert_option_2.product, self.dessert_description2, self.dessert_basket2, dessert_option_2, Dessert_menu))
        self.dessert_option3.configure(command=lambda: add_to_basket_window(self, dessert_option_3.product, self.dessert_description3, self.dessert_basket3, dessert_option_3, Dessert_menu))
        self.dessert_option4.configure(command=lambda: add_to_basket_window(self, dessert_option_4.product, self.dessert_description4, self.dessert_basket4, dessert_option_4, Dessert_menu))
        self.dessert_option5.configure(command=lambda: add_to_basket_window(self, dessert_option_5.product, self.dessert_description5, self.dessert_basket5, dessert_option_5, Dessert_menu))
        self.dessert_option6.configure(command=lambda: add_to_basket_window(self, dessert_option_6.product, self.dessert_description6, self.dessert_basket6, dessert_option_6, Dessert_menu))
        self.dessert_option7.configure(command=lambda: add_to_basket_window(self, dessert_option_7.product, self.dessert_description7, self.dessert_basket7, dessert_option_7, Dessert_menu))
        self.dessert_option8.configure(command=lambda: add_to_basket_window(self, dessert_option_8.product, self.dessert_description8, self.dessert_basket8, dessert_option_8, Dessert_menu))
        self.dessert_option9.configure(command=lambda: add_to_basket_window(self, dessert_option_9.product, self.dessert_description9, self.dessert_basket9, dessert_option_9, Dessert_menu))

        #--->back button
        self.dessert_back.configure(command=lambda: controller.show_frame(Menu_navigation_frame))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->place widgets on grid<---#

        #--->top frame & widgets<---#

        #--->top row frame
        self.dessert_menu_top_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")

        
        #--->logo
        self.dessert_menu_logo_widget.grid(column=0, row=0)

         #--->title
        self.dessert_menu_title.grid(column=1, row=0)

        #--->frame for basket button and basket total
        self.dessert_menu_basket_frame.grid(row=0, column=2, padx=(0,5), pady=6, sticky="nsew")

        #--->basket navigation
        self.dessert_menu_basket_button.grid(column=0,row=0, sticky="nsew")

        #--->basket total
        self.dessert_menu_basket_total.grid(column=1, row=0, sticky="nsew")


        #--->option buttons<---#

        
        #--->dessert buttons
        self.dessert_option1.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.dessert_option2.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)
        self.dessert_option3.grid(row=3, column=0, sticky="nsew", padx=20, pady=20)
        self.dessert_option4.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        self.dessert_option5.grid(row=2, column=1, sticky="nsew", padx=20, pady=20)
        self.dessert_option6.grid(row=3, column=1, sticky="nsew", padx=20, pady=20)
        self.dessert_option7.grid(row=1, column=2, sticky="nsew", padx=20, pady=20)
        self.dessert_option8.grid(row=2, column=2, sticky="nsew", padx=20, pady=20)
        self.dessert_option9.grid(row=3, column=2, sticky="nsew", padx=20, pady=20)
       
        #--->back button
        self.dessert_back.grid(row=4, column=1, padx=20, pady=20, sticky="nsew")





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->confirguring frames & widgets<---#

        #top row frame already configured in app class#

        #--->logo
        self.dessert_menu_top_frame.columnconfigure(0, weight=1)
        self.dessert_menu_top_frame.rowconfigure(0, weight=1)
        #--->dessert title
        self.dessert_menu_top_frame.columnconfigure(1, weight=1)
        self.dessert_menu_top_frame.rowconfigure(0, weight=1)
        #dessert basket frame
        self.dessert_menu_top_frame.columnconfigure(2, weight=1)
        self.dessert_menu_top_frame.rowconfigure(0, weight=1)
        #dessert basket button
        self.dessert_menu_basket_frame.columnconfigure(0, weight=1)
        self.dessert_menu_basket_frame.rowconfigure(0, weight=1)
        #dessert basket total
        self.dessert_menu_basket_frame.columnconfigure(1, weight=1)
        self.dessert_menu_basket_frame.rowconfigure(0, weight=1)
        #dessert option 1
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        #dessert option 2
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        #dessert option 3
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        #dessert option 4
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        #dessert option 5
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        #dessert option 6
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)
        #dessert option 7
        self.columnconfigure(2, weight=1)
        self.rowconfigure(1, weight=1)
        #dessert option 8
        self.columnconfigure(2, weight=1)
        self.rowconfigure(2, weight=1)
        #dessert option 9
        self.columnconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        #dessert back button
        self.columnconfigure(1, weight=1)
        self.rowconfigure(4, weight=1)


#~~~~~~~~~~~~drinks menu class~~~~~~~~~~~#

class Drinks_menu(ctk.CTkFrame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->string variables<---#

        #--->title var
        self.drinks_title_var = tk.StringVar(self, "Drinks Menu")

        #--->basket button var
        self.drinks_basket_button_var = tk.StringVar(self, "View Basket")

        #--->basket total var
        self.drinks_basket_var = tk.StringVar(self, f"Placeholder")

        #--->item name & price

        self.drinks_var1 = tk.StringVar(self, f"{drinks_option_1.product} \n\n £{drinks_option_1.price}")
        self.drinks_var2 = tk.StringVar(self, f"{drinks_option_2.product} \n\n £{drinks_option_2.price}")
        self.drinks_var3 = tk.StringVar(self, f"{drinks_option_3.product} \n\n £{drinks_option_3.price}")
        self.drinks_var4 = tk.StringVar(self, f"{drinks_option_4.product} \n\n £{drinks_option_4.price}")
        self.drinks_var5 = tk.StringVar(self, f"{drinks_option_5.product} \n\n £{drinks_option_5.price}")
        self.drinks_var6 = tk.StringVar(self, f"{drinks_option_6.product} \n\n £{drinks_option_6.price}")
        self.drinks_var7 = tk.StringVar(self, f"{drinks_option_7.product} \n\n £{drinks_option_7.price}")
        self.drinks_var8 = tk.StringVar(self, f"{drinks_option_8.product} \n\n £{drinks_option_8.price}")
        self.drinks_var9 = tk.StringVar(self, f"{drinks_option_9.product} \n\n £{drinks_option_9.price}")

        #--->item description

        self.drinks_description1 = tk.StringVar(self, "Placeholder text....")
        self.drinks_description2 = tk.StringVar(self, "Placeholder text....")
        self.drinks_description3 = tk.StringVar(self, "Placeholder text....")
        self.drinks_description4 = tk.StringVar(self, "Placeholder text....")
        self.drinks_description5 = tk.StringVar(self, "Placeholder text....")
        self.drinks_description6 = tk.StringVar(self, "Placeholder text....")
        self.drinks_description7 = tk.StringVar(self, "Placeholder text....")
        self.drinks_description8 = tk.StringVar(self, "Placeholder text....")
        self.drinks_description9 = tk.StringVar(self, "Placeholder text....")


        #--->item basket price

        self.drinks_basket1 = tk.StringVar(self, f"£{drinks_option_1.price}")
        self.drinks_basket2 = tk.StringVar(self, f"£{drinks_option_2.price}")
        self.drinks_basket3 = tk.StringVar(self, f"£{drinks_option_3.price}")
        self.drinks_basket4 = tk.StringVar(self, f"£{drinks_option_4.price}")
        self.drinks_basket5 = tk.StringVar(self, f"£{drinks_option_5.price}")
        self.drinks_basket6 = tk.StringVar(self, f"£{drinks_option_6.price}")
        self.drinks_basket7 = tk.StringVar(self, f"£{drinks_option_7.price}")
        self.drinks_basket8 = tk.StringVar(self, f"£{drinks_option_8.price}")
        self.drinks_basket9 = tk.StringVar(self, f"£{drinks_option_9.price}")

        #--->back button var
        self.drinks_back_var = tk.StringVar(self, "Back")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->top frame & widgets<---#

        #--->top row frame
        self.drinks_menu_top_frame = ctk.CTkFrame(self)
        
        #--->logo
        self.drinks_menu_logo = ctk.CTkImage(dark_image=Image.open(r"Project\images\Logo15.png"),size=(50,50))
        self.drinks_menu_logo_widget = ctk.CTkLabel(self.drinks_menu_top_frame, image=self.drinks_menu_logo, text="")

         #--->title
        self.drinks_menu_title = ctk.CTkLabel(
        self.drinks_menu_top_frame, textvariable=self.drinks_title_var, font=("TkHeadingFont", 30))

        #--->frame for basket button and basket total
        self.drinks_menu_basket_frame = ctk.CTkFrame(self.drinks_menu_top_frame)

        #--->basket navigation
        self.drinks_menu_basket_button = ctk.CTkButton(
        self.drinks_menu_basket_frame, textvariable=self.drinks_basket_button_var, font=("TkHeadingFont", 10), 
        cursor="hand2", hover_color="#BC006C", height=10, width=30, border_width=0)

        #--->basket total
        self.drinks_menu_basket_total = ctk.CTkLabel(
        self.drinks_menu_basket_frame, textvariable=order_total_var, font=("TkHeadingFont", 10))

        #--->option buttons<---#
        
        #--->drinks buttons
        self.drinks_option1 = ctk.CTkButton(self, textvariable=self.drinks_var1)
        self.drinks_option2 = ctk.CTkButton(self, textvariable=self.drinks_var2)
        self.drinks_option3 = ctk.CTkButton(self, textvariable=self.drinks_var3)
        self.drinks_option4 = ctk.CTkButton(self, textvariable=self.drinks_var4)
        self.drinks_option5 = ctk.CTkButton(self, textvariable=self.drinks_var5)
        self.drinks_option6 = ctk.CTkButton(self, textvariable=self.drinks_var6)
        self.drinks_option7 = ctk.CTkButton(self, textvariable=self.drinks_var7)
        self.drinks_option8 = ctk.CTkButton(self, textvariable=self.drinks_var8)
        self.drinks_option9 = ctk.CTkButton(self, textvariable=self.drinks_var9)
       
        #--->back button
        self.drinks_back = ctk.CTkButton(self, textvariable=self.drinks_back_var)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->button command configurations<---#

        #--->basket nav button
        self.drinks_menu_basket_button.configure(command=basket_window)

        #--->item buttons
        self.drinks_option1.configure(command=lambda: add_to_basket_window(self, drinks_option_1.product, self.drinks_description1, self.drinks_basket1, drinks_option_1, Drinks_menu))
        self.drinks_option2.configure(command=lambda: add_to_basket_window(self, drinks_option_2.product, self.drinks_description2, self.drinks_basket2, drinks_option_2, Drinks_menu))
        self.drinks_option3.configure(command=lambda: add_to_basket_window(self, drinks_option_3.product, self.drinks_description3, self.drinks_basket3, drinks_option_3, Drinks_menu))
        self.drinks_option4.configure(command=lambda: add_to_basket_window(self, drinks_option_4.product, self.drinks_description4, self.drinks_basket4, drinks_option_4, Drinks_menu))
        self.drinks_option5.configure(command=lambda: add_to_basket_window(self, drinks_option_5.product, self.drinks_description5, self.drinks_basket5, drinks_option_5, Drinks_menu))
        self.drinks_option6.configure(command=lambda: add_to_basket_window(self, drinks_option_6.product, self.drinks_description6, self.drinks_basket6, drinks_option_6, Drinks_menu))
        self.drinks_option7.configure(command=lambda: add_to_basket_window(self, drinks_option_7.product, self.drinks_description7, self.drinks_basket7, drinks_option_7, Drinks_menu))
        self.drinks_option8.configure(command=lambda: add_to_basket_window(self, drinks_option_8.product, self.drinks_description8, self.drinks_basket8, drinks_option_8, Drinks_menu))
        self.drinks_option9.configure(command=lambda: add_to_basket_window(self, drinks_option_9.product, self.drinks_description9, self.drinks_basket9, drinks_option_9, Drinks_menu))


        #--->back button
        self.drinks_back.configure(command=lambda: controller.show_frame(Menu_navigation_frame))




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #--->place widgets on grid<---#

        #--->top row frame
        self.drinks_menu_top_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")

        
        #--->logo
        self.drinks_menu_logo_widget.grid(column=0, row=0)

         #--->title
        self.drinks_menu_title.grid(column=1, row=0)

        #--->frame for basket button and basket total
        self.drinks_menu_basket_frame.grid(row=0, column=2, padx=(0,5), pady=6, sticky="nsew")

        #--->basket navigation
        self.drinks_menu_basket_button.grid(column=0,row=0, sticky="nsew")

        #--->basket total
        self.drinks_menu_basket_total.grid(column=1, row=0, sticky="nsew")


        #--->option buttons<---#

        
        #--->drinks buttons
        self.drinks_option1.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.drinks_option2.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)
        self.drinks_option3.grid(row=3, column=0, sticky="nsew", padx=20, pady=20)
        self.drinks_option4.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        self.drinks_option5.grid(row=2, column=1, sticky="nsew", padx=20, pady=20)
        self.drinks_option6.grid(row=3, column=1, sticky="nsew", padx=20, pady=20)
        self.drinks_option7.grid(row=1, column=2, sticky="nsew", padx=20, pady=20)
        self.drinks_option8.grid(row=2, column=2, sticky="nsew", padx=20, pady=20)
        self.drinks_option9.grid(row=3, column=2, sticky="nsew", padx=20, pady=20)
       
        #--->back button
        self.drinks_back.grid(row=4, column=1, padx=20, pady=20, sticky="nsew")





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #--->confirguring frames & widgets<---#

        #top row frame already configured in app class#

        #--->logo
        self.drinks_menu_top_frame.columnconfigure(0, weight=1)
        self.drinks_menu_top_frame.rowconfigure(0, weight=1)
        #--->drinks title
        self.drinks_menu_top_frame.columnconfigure(1, weight=1)
        self.drinks_menu_top_frame.rowconfigure(0, weight=1)
        #drinks basket frame
        self.drinks_menu_top_frame.columnconfigure(2, weight=1)
        self.drinks_menu_top_frame.rowconfigure(0, weight=1)
        #drinks basket button
        self.drinks_menu_basket_frame.columnconfigure(0, weight=1)
        self.drinks_menu_basket_frame.rowconfigure(0, weight=1)
        #drinks basket total
        self.drinks_menu_basket_frame.columnconfigure(1, weight=1)
        self.drinks_menu_basket_frame.rowconfigure(0, weight=1)
        #drinks option 1
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        #drinks option 2
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        #drinks option 3
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        #drinks option 4
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        #drinks option 5
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        #drinks option 6
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)
        #drinks option 7
        self.columnconfigure(2, weight=1)
        self.rowconfigure(1, weight=1)
        #drinks option 8
        self.columnconfigure(2, weight=1)
        self.rowconfigure(2, weight=1)
        #drinks option 9
        self.columnconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        #drinks back button
        self.columnconfigure(1, weight=1)
        self.rowconfigure(4, weight=1)


#~~~~~~~~~~~~milkshake menu class~~~~~~~~~~~#

class Milkshake_menu(ctk.CTkFrame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        #--->string variables<---#

        #--->title var
        self.milkshake_title_var = tk.StringVar(self, "Milkshake Menu")

        #--->basket button var
        self.milkshake_basket_button_var = tk.StringVar(self, "View Basket")

        #--->basket total var
        self.milkshake_basket_var = tk.StringVar(self, f"Placeholder")

        #--->item name & price

        self.milkshake_var1 = tk.StringVar(self, f"{milkshake_option_1.product} \n\n £{milkshake_option_1.price}")
        self.milkshake_var2 = tk.StringVar(self, f"{milkshake_option_2.product} \n\n £{milkshake_option_2.price}")
        self.milkshake_var3 = tk.StringVar(self, f"{milkshake_option_3.product} \n\n £{milkshake_option_3.price}")
        self.milkshake_var4 = tk.StringVar(self, f"{milkshake_option_4.product} \n\n £{milkshake_option_4.price}")
        self.milkshake_var5 = tk.StringVar(self, f"{milkshake_option_5.product} \n\n £{milkshake_option_5.price}")
        self.milkshake_var6 = tk.StringVar(self, f"{milkshake_option_6.product} \n\n £{milkshake_option_6.price}")
        self.milkshake_var7 = tk.StringVar(self, f"{milkshake_option_7.product} \n\n £{milkshake_option_7.price}")
        self.milkshake_var8 = tk.StringVar(self, f"{milkshake_option_8.product} \n\n £{milkshake_option_8.price}")
        self.milkshake_var9 = tk.StringVar(self, f"{milkshake_option_9.product} \n\n £{milkshake_option_9.price}")

        #--->item description
        
        self.milkshake_description1 = tk.StringVar(self, "Placeholder text......")
        self.milkshake_description2 = tk.StringVar(self, "Placeholder text......")
        self.milkshake_description3 = tk.StringVar(self, "Placeholder text......")
        self.milkshake_description4 = tk.StringVar(self, "Placeholder text......")
        self.milkshake_description5 = tk.StringVar(self, "Placeholder text......")
        self.milkshake_description6 = tk.StringVar(self, "Placeholder text......")
        self.milkshake_description7 = tk.StringVar(self, "Placeholder text......")
        self.milkshake_description8 = tk.StringVar(self, "Placeholder text......")
        self.milkshake_description9 = tk.StringVar(self, "Placeholder text......")

        #--->item basket price

        self.milkshake_basket1 = tk.StringVar(self, f"£{milkshake_option_1.price}")
        self.milkshake_basket2 = tk.StringVar(self, f"£{milkshake_option_2.price}")
        self.milkshake_basket3 = tk.StringVar(self, f"£{milkshake_option_3.price}")
        self.milkshake_basket4 = tk.StringVar(self, f"£{milkshake_option_4.price}")
        self.milkshake_basket5 = tk.StringVar(self, f"£{milkshake_option_5.price}")
        self.milkshake_basket6 = tk.StringVar(self, f"£{milkshake_option_6.price}")
        self.milkshake_basket7 = tk.StringVar(self, f"£{milkshake_option_7.price}")
        self.milkshake_basket8 = tk.StringVar(self, f"£{milkshake_option_8.price}")
        self.milkshake_basket9 = tk.StringVar(self, f"£{milkshake_option_9.price}")

        #--->back button var
        self.milkshake_back_var = tk.StringVar(self, "Back")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->top frame & widgets<---#

        #--->top row frame
        self.milkshake_menu_top_frame = ctk.CTkFrame(self)
        
        #--->logo
        self.milkshake_menu_logo = ctk.CTkImage(dark_image=Image.open(r"Project\images\Logo15.png"),size=(50,50))
        self.milkshake_menu_logo_widget = ctk.CTkLabel(self.milkshake_menu_top_frame, image=self.milkshake_menu_logo, text="")

         #--->title
        self.milkshake_menu_title = ctk.CTkLabel(
        self.milkshake_menu_top_frame, textvariable=self.milkshake_title_var, font=("TkHeadingFont", 30))

        #--->frame for basket button and basket total
        self.milkshake_menu_basket_frame = ctk.CTkFrame(self.milkshake_menu_top_frame)

        #--->basket navigation
        self.milkshake_menu_basket_button = ctk.CTkButton(
        self.milkshake_menu_basket_frame, textvariable=self.milkshake_basket_button_var, font=("TkHeadingFont", 10), 
        cursor="hand2", hover_color="#BC006C", height=10, width=30, border_width=0)

        #--->basket total
        self.milkshake_menu_basket_total = ctk.CTkLabel(
        self.milkshake_menu_basket_frame, textvariable=order_total_var, font=("TkHeadingFont", 10))
        
        #--->option buttons<---#

        #--->milkshake buttons
        self.milkshake_option1 = ctk.CTkButton(self, textvariable=self.milkshake_var1)
        self.milkshake_option2 = ctk.CTkButton(self, textvariable=self.milkshake_var2)
        self.milkshake_option3 = ctk.CTkButton(self, textvariable=self.milkshake_var3)
        self.milkshake_option4 = ctk.CTkButton(self, textvariable=self.milkshake_var4)
        self.milkshake_option5 = ctk.CTkButton(self, textvariable=self.milkshake_var5)
        self.milkshake_option6 = ctk.CTkButton(self, textvariable=self.milkshake_var6)
        self.milkshake_option7 = ctk.CTkButton(self, textvariable=self.milkshake_var7)
        self.milkshake_option8 = ctk.CTkButton(self, textvariable=self.milkshake_var8)
        self.milkshake_option9 = ctk.CTkButton(self, textvariable=self.milkshake_var9)
       
        #--->back button
        self.milkshake_back = ctk.CTkButton(self, textvariable=self.milkshake_back_var)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->button command configurations<---#
        
        #--->basket nav button
        self.milkshake_menu_basket_button.configure(command=basket_window)

        #--->option buttons
        self.milkshake_option1.configure(command=lambda: add_to_basket_window(self, milkshake_option_1.product, self.milkshake_description1, self.milkshake_basket1, milkshake_option_1, Milkshake_menu))
        self.milkshake_option2.configure(command=lambda: add_to_basket_window(self, milkshake_option_2.product, self.milkshake_description2, self.milkshake_basket2, milkshake_option_2, Milkshake_menu))
        self.milkshake_option3.configure(command=lambda: add_to_basket_window(self, milkshake_option_3.product, self.milkshake_description3, self.milkshake_basket3, milkshake_option_3, Milkshake_menu))
        self.milkshake_option4.configure(command=lambda: add_to_basket_window(self, milkshake_option_4.product, self.milkshake_description4, self.milkshake_basket4, milkshake_option_4, Milkshake_menu))
        self.milkshake_option5.configure(command=lambda: add_to_basket_window(self, milkshake_option_5.product, self.milkshake_description5, self.milkshake_basket5, milkshake_option_5, Milkshake_menu))
        self.milkshake_option6.configure(command=lambda: add_to_basket_window(self, milkshake_option_6.product, self.milkshake_description6, self.milkshake_basket6, milkshake_option_6, Milkshake_menu))
        self.milkshake_option7.configure(command=lambda: add_to_basket_window(self, milkshake_option_7.product, self.milkshake_description7, self.milkshake_basket7, milkshake_option_7, Milkshake_menu))
        self.milkshake_option8.configure(command=lambda: add_to_basket_window(self, milkshake_option_8.product, self.milkshake_description8, self.milkshake_basket8, milkshake_option_8, Milkshake_menu))
        self.milkshake_option9.configure(command=lambda: add_to_basket_window(self, milkshake_option_9.product, self.milkshake_description9, self.milkshake_basket9, milkshake_option_9, Milkshake_menu))

        #--->back button
        self.milkshake_back.configure(command=lambda: controller.show_frame(Menu_navigation_frame))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        #--->place widgets on grid<---#

        #--->top row frame
        self.milkshake_menu_top_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")

        
        #--->logo
        self.milkshake_menu_logo_widget.grid(column=0, row=0)

         #--->title
        self.milkshake_menu_title.grid(column=1, row=0)

        #--->frame for basket button and basket total
        self.milkshake_menu_basket_frame.grid(row=0, column=2, padx=(0,5), pady=6, sticky="nsew")

        #--->basket navigation
        self.milkshake_menu_basket_button.grid(column=0,row=0, sticky="nsew")

        #--->basket total
        self.milkshake_menu_basket_total.grid(column=1, row=0, sticky="nsew")


        #--->option buttons<---#

        
        #--->milkshake buttons
        self.milkshake_option1.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.milkshake_option2.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)
        self.milkshake_option3.grid(row=3, column=0, sticky="nsew", padx=20, pady=20)
        self.milkshake_option4.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        self.milkshake_option5.grid(row=2, column=1, sticky="nsew", padx=20, pady=20)
        self.milkshake_option6.grid(row=3, column=1, sticky="nsew", padx=20, pady=20)
        self.milkshake_option7.grid(row=1, column=2, sticky="nsew", padx=20, pady=20)
        self.milkshake_option8.grid(row=2, column=2, sticky="nsew", padx=20, pady=20)
        self.milkshake_option9.grid(row=3, column=2, sticky="nsew", padx=20, pady=20)
       
        #--->back button
        self.milkshake_back.grid(row=4, column=1, padx=20, pady=20, sticky="nsew")






#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #--->confirguring frames & widgets<---#

        #top row frame already configured in app class#

        #--->logo
        self.milkshake_menu_top_frame.columnconfigure(0, weight=1)
        self.milkshake_menu_top_frame.rowconfigure(0, weight=1)
        #--->milkshake title
        self.milkshake_menu_top_frame.columnconfigure(1, weight=1)
        self.milkshake_menu_top_frame.rowconfigure(0, weight=1)
        #milkshake basket frame
        self.milkshake_menu_top_frame.columnconfigure(2, weight=1)
        self.milkshake_menu_top_frame.rowconfigure(0, weight=1)
        #milkshake basket button
        self.milkshake_menu_basket_frame.columnconfigure(0, weight=1)
        self.milkshake_menu_basket_frame.rowconfigure(0, weight=1)
        #milkshake basket total
        self.milkshake_menu_basket_frame.columnconfigure(1, weight=1)
        self.milkshake_menu_basket_frame.rowconfigure(0, weight=1)
        #milkshake option 1
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        #milkshake option 2
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        #milkshake option 3
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        #milkshake option 4
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        #milkshake option 5
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        #milkshake option 6
        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)
        #milkshake option 7
        self.columnconfigure(2, weight=1)
        self.rowconfigure(1, weight=1)
        #milkshake option 8
        self.columnconfigure(2, weight=1)
        self.rowconfigure(2, weight=1)
        #milkshake option 9
        self.columnconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        #milkshake back button
        self.columnconfigure(1, weight=1)
        self.rowconfigure(4, weight=1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~main function~~~~~~~~~~~#   
def main():
    global app
    app = App()
    app.mainloop()


def add_to_basket_window(master, product, description, price, instance, menu):

    #--->create window
   
    add_to_basket_window = ctk.CTkToplevel(master)
    add_to_basket_window.attributes("-topmost", True)
    
    

    add_to_basket_window.title("Add To Basket")
    add_to_basket_window.geometry("800x400")

    add_to_basket_frame = ctk.CTkFrame(add_to_basket_window)
    add_to_basket_frame.grid(column=0, row=0, sticky="nsew")

    quantity_var = tk.StringVar(add_to_basket_frame, 1)
    up_arrow = ctk.CTkImage(Image.open(r"Project\images\up_arrow.png"),size=(20,20))
    down_arrow = ctk.CTkImage(Image.open(r"Project\images\down_arrow.png"),size=(20,20))

    
    product_title = ctk.CTkLabel(add_to_basket_frame, text=product, font=("TkHeadingFont", 30))
    product_description = ctk.CTkLabel(add_to_basket_frame, textvariable=description)
    quantity_label = ctk.CTkLabel(add_to_basket_frame, text="Quantity:")
    quantity_increase_button = ctk.CTkButton(add_to_basket_frame, image=up_arrow, text="", width=20, height=20)
    quantity_count = ctk.CTkLabel(add_to_basket_frame, textvariable=quantity_var)
    quantity_decrease_button = ctk.CTkButton(add_to_basket_frame, image=down_arrow, text="", width=20, height=20)
    product_price = ctk.CTkLabel(add_to_basket_frame, textvariable=price)
    add_to_basket_button = ctk.CTkButton(add_to_basket_frame, text="Add to basket")

    #--->widget configurations<---#


    #--->quantity buttons
    quantity_increase_button.configure(command=lambda: change_quantity("plus"))
    quantity_decrease_button.configure(command=lambda: change_quantity("minus"))


    #--->basket button
    add_to_basket_button.configure(command=lambda: add_to_basket_func(instance))

   
   
    def change_quantity(operator):
        if int(quantity_var.get()) == 0 and operator == "minus":
            pass
        else:
            if operator == "plus":
                current = quantity_var.get()
                new = int(current) + 1
                quantity_var.set(new)
            elif operator == "minus":
                current = quantity_var.get()
                new = int(current) - 1
                quantity_var.set(new)
            new_price = int(quantity_var.get()) * instance.price
            price.set(f"£{new_price}")
        

    
    def add_to_basket_func(instance):
        qty = int(quantity_var.get())
        instance.add_to_basket(qty)
        quantity_var.set(1)
        price.set(f"£{instance.price}")
        update_basket_total()

    #--->place widgets on grid<---#
    product_title.grid(column=0, row=0, columnspan=5, padx=10, pady=(20,10), sticky="nsew")
    product_description.grid(column=0, row=1, columnspan=5, rowspan=3, padx=20, pady=10, sticky="nsew")
    quantity_label.grid(column=2, row=6, padx=10, pady=10, sticky="nsew")
    quantity_increase_button.grid(column=1, row=7, padx=10, pady=10, sticky="nsew")
    quantity_count.grid(column=2, row=7, padx=10, pady=10, sticky="nsew")
    quantity_decrease_button.grid(column=3, row=7, padx=10, pady=10, sticky="nsew")
    product_price.grid(column=2, row=8, padx=10, pady=10, sticky="nsew")
    add_to_basket_button.grid(column=2, row=9, padx=10, pady=(10,20), sticky="nsew")


    #title
    add_to_basket_window.columnconfigure(0, weight=1)
    add_to_basket_window.rowconfigure(0, weight=1)
    #description
    add_to_basket_frame.columnconfigure(0, weight=3)
    add_to_basket_frame.rowconfigure(1, weight=3)
    #spare row?
    add_to_basket_frame.columnconfigure(0, weight=1)
    add_to_basket_frame.columnconfigure(1, weight=1)
    add_to_basket_frame.columnconfigure(2, weight=1)
    add_to_basket_frame.columnconfigure(3, weight=1)
    add_to_basket_frame.columnconfigure(4, weight=1)
    add_to_basket_frame.rowconfigure(5, weight=1)
    #qty label
    add_to_basket_frame.columnconfigure(2, weight=1)
    add_to_basket_frame.rowconfigure(6, weight=1)
    #qty count & buttons
    add_to_basket_frame.columnconfigure(1, weight=1)
    add_to_basket_frame.columnconfigure(2, weight=1)
    add_to_basket_frame.columnconfigure(3, weight=1)
    add_to_basket_frame.rowconfigure(7, weight=1)
    #price
    add_to_basket_frame.columnconfigure(2, weight=1)
    add_to_basket_frame.rowconfigure(8, weight=1)
    #add button
    add_to_basket_frame.columnconfigure(2, weight=1)
    add_to_basket_frame.rowconfigure(9, weight=1)
    
########################################################################################################################################

def basket_window():

    basket_window = ctk.CTkToplevel(app)
    basket_window.attributes("-topmost", True)

    basket_window.geometry("800x400")
    basket_window.title("Your Basket")

    def load_window():    

        current_total = 0
        for key, value in Food.basket.items():
            for i, value in enumerate(Food.basket[key]):
                if i == 1:
                    current_total += value

        basket_window_frame = ctk.CTkFrame(basket_window, fg_color="#161219", border_color="#BC006C", border_width=5)
        basket_window_frame.grid(column=0, row=0, sticky="nsew")

        basket_window_title = ctk.CTkLabel(basket_window_frame, text="Your Basket", font=("TkHeadingFont", 30))
        basket_window_title.grid(row=0, column=0, columnspan=5, padx=5, pady=(10,0), sticky="nsew")

        order_summary_frame = ctk.CTkScrollableFrame(
            basket_window_frame,
            corner_radius=0,
            scrollbar_fg_color="gray85",
            scrollbar_button_color="gray52",
            scrollbar_button_hover_color="blue",
            label_fg_color="#BC006C",
            label_text_color="black",
            label_text="Order Summary",
            label_font=ctk.CTkFont(family="TkHeadingFont", size=20),
            label_anchor="n",
            orientation="vertical",
            fg_color="#161219", 
            border_color="#BC006C", 
            border_width=5
            )
        order_summary_frame.grid(row=1, column=0, columnspan=5, rowspan=5, padx=15, pady=10, sticky="nsew")
        
        total_var = tk.StringVar(basket_window_frame)
        total_var.set(f"£{current_total}")

        def generate_order_list():

            items_list = [key for key in Food.basket.keys()]
            qty_list = [value for key, value in Food.basket.items() for i, value in enumerate(Food.basket[key]) if i == 0]
            prices_list = [value for key, value in Food.basket.items() for i, value in enumerate(Food.basket[key]) if i == 1]

            item_list_str = ""
            qty_list_str = ""
            prices_list_str = ""

            for key in items_list:
                item_list_str += key + "\n"

            for qty in qty_list:
                qty_list_str += str(qty) + "\n"
            
            for price in prices_list:
                prices_list_str += "£" + str(price) + "\n"

            items_list_var = tk.StringVar(basket_window_frame, item_list_str)

            qty_list_var = tk.StringVar(basket_window_frame, qty_list_str)

            prices_list_var = tk.StringVar(basket_window_frame, prices_list_str)

            
            return items_list, qty_list, prices_list, item_list_str, qty_list_str, prices_list_str, items_list_var, qty_list_var, prices_list_var
        
        items_list, qty_list, prices_list, item_list_str, qty_list_str, prices_list_str, items_list_var, qty_list_var, prices_list_var = generate_order_list()

        

        items_list_label = ctk.CTkLabel(order_summary_frame)
        items_list_label.configure(textvariable=items_list_var)
        

        qty_list_label = ctk.CTkLabel(order_summary_frame)
        qty_list_label.configure(textvariable=qty_list_var)
        
        
        prices_list_label = ctk.CTkLabel(order_summary_frame)
        prices_list_label.configure(textvariable=prices_list_var)
    
        
        item_to_delete = tk.StringVar(basket_window_frame)
        item_to_delete.set("Select item to delete")

        def delete_item_option_callback(choice):
            item_to_delete.set(choice)

        delete_item_option = ctk.CTkOptionMenu(
            basket_window_frame, 
            values=items_list,
            command=delete_item_option_callback,
            variable=item_to_delete,
            width=80,
            height=20,
            corner_radius=6,
            fg_color="gray28",
            button_color="gray85",
            button_hover_color="blue",
            dropdown_fg_color="gray52",
            dropdown_hover_color="blue",
            dropdown_text_color="white",
            text_color="white",
            text_color_disabled="black",
            font=ctk.CTkFont(family="Roboto", size=13),
            dropdown_font=ctk.CTkFont(family="Roboto", size=13),
            state="normal",
            dynamic_resizing=True,
            anchor="w")
        
        
        ###################################################################### 
        def delete_item():
            Food.delete_from_basket(item_to_delete.get())
            update_basket_total()
            load_window()
        ######################################################################      




        delete_button = ctk.CTkButton(basket_window_frame, text="Delete Item", command=delete_item)
        delete_button.grid(column=1, row=7, padx=30, pady=5, sticky="nsew")

        basket_total_label = ctk.CTkLabel(basket_window_frame, text="Order Total:")
        basket_total_label.grid(column=1, row=8, padx=30, pady=5, sticky="nsew")

        basket_total_amount = ctk.CTkLabel(basket_window_frame)
        basket_total_amount.configure(textvariable=total_var)
        basket_total_amount.grid(column=3, row=8, padx=30, pady=5, sticky="nsew")


        checkout_button = ctk.CTkButton(basket_window_frame, text="Proceed to checkout", command=lambda: checkout_window(basket_window))
        checkout_button.grid(column=1, row=9, padx=30, pady=(5,20), sticky="nsew")

        back_button = ctk.CTkButton(basket_window_frame, text="Back", command=lambda: [app.show_frame(Menu_navigation_frame), basket_window.destroy()])
        back_button.grid(row=9, column=3, padx=30, pady=(5,20), sticky="nsew")


        items_list_label.grid(column=0, row=0, rowspan=5, sticky="nsew")
        qty_list_label.grid(column=1, row=0, rowspan=5, sticky="nsew")
        prices_list_label.grid(column=2, row=0, rowspan=5, sticky="nsew")
        delete_item_option.grid(column=3, row=7, padx=30, pady=5, sticky="nsew")

        #window frame
        basket_window.columnconfigure(0, weight=1)
        basket_window.rowconfigure(0, weight=1)
        #title
        basket_window_frame.columnconfigure(0, weight=1)
        basket_window_frame.rowconfigure(0, weight=1)
        #summary frame
        basket_window_frame.columnconfigure(0, weight=3)
        basket_window_frame.rowconfigure(1, weight=3)
        #item list label
        order_summary_frame.columnconfigure(0, weight=1)
        order_summary_frame.rowconfigure(0, weight=1)
        #qty list label
        order_summary_frame.columnconfigure(1, weight=1)
        order_summary_frame.rowconfigure(0, weight=1)
        #prices list label
        order_summary_frame.columnconfigure(2, weight=1)
        order_summary_frame.rowconfigure(0, weight=1)
        #basket total
        basket_window_frame.columnconfigure(0, weight=1)
        basket_window_frame.columnconfigure(1, weight=1)
        basket_window_frame.columnconfigure(2, weight=1)
        basket_window_frame.columnconfigure(3, weight=1)
        basket_window_frame.columnconfigure(4, weight=1)
        basket_window_frame.rowconfigure(2, weight=1)
        basket_window_frame.rowconfigure(3, weight=1)
        basket_window_frame.rowconfigure(4, weight=1)
        basket_window_frame.rowconfigure(5, weight=1)
        basket_window_frame.rowconfigure(6, weight=1)
        #checkout button
        basket_window_frame.columnconfigure(2, weight=1)
        basket_window_frame.rowconfigure(7, weight=1)
        #back button
        basket_window_frame.columnconfigure(2, weight=1)
        basket_window_frame.rowconfigure(8, weight=1)
        basket_window_frame.rowconfigure(9, weight=1)

    load_window()

def update_basket_total():

    prices_list = [value for key, value in Food.basket.items() for i, value in enumerate(Food.basket[key]) if i == 1]

    total_price = 0
    
    for price in prices_list:
        total_price += price

    order_total_var.set(f"£{total_price}")

    return order_total_var.get()
    
#######################################################################################################################################    

def checkout_window(basket_window):

    basket_window.destroy()

    checkout_window = ctk.CTkToplevel(app)
    checkout_window.attributes("-topmost", True)

    checkout_window.geometry("1000x600")
    checkout_window.title("Checkout")

    checkout_window_frame = ctk.CTkFrame(checkout_window, fg_color="#161219", border_color="#BC006C", border_width=5)
    

    prices_list = [value for key, value in Food.basket.items() for i, value in enumerate(Food.basket[key]) if i == 1]

    total_price = 0
    
    for price in prices_list:
        total_price += price

    #order total
    checkout_order_total_var = tk.StringVar(checkout_window_frame)
    checkout_order_total_var.set(f"£{total_price}")

    #--->top frame & top row widgets<---#

    #--->top row frame
    checkout_menu_top_frame = ctk.CTkFrame(checkout_window_frame,  fg_color="#161219", border_color="#BC006C", border_width=5)
    

    
    #--->logo
    checkout_menu_logo = ctk.CTkImage(dark_image=Image.open(r"Project\images\Logo15.png"),size=(50,50))
    checkout_menu_logo_widget = ctk.CTkLabel(checkout_menu_top_frame, image=checkout_menu_logo, fg_color="#161219", text="")
    

    #--->title
    checkout_menu_title = ctk.CTkLabel(
    checkout_menu_top_frame, text="Checkout", text_color="white", fg_color="#161219", font=("TkHeadingFont", 30))
    

    #--->frame for basket button and basket total
    checkout_menu_basket_frame = ctk.CTkFrame(checkout_menu_top_frame, fg_color="#161219")
    

    #--->basket navigation
    checkout_menu_basket_button = ctk.CTkButton(
    checkout_menu_basket_frame, text="Basket", text_color="white", fg_color="#161219", font=("TkHeadingFont", 10), 
    cursor="hand2", command=lambda: basket_window, hover_color="#BC006C", height=10, width=30, border_width=0)
    

    #--->basket total
    checkout_menu_basket_total = ctk.CTkLabel(
    checkout_menu_basket_frame, text_color="white", fg_color="#161219", font=("TkHeadingFont", 10))
    checkout_menu_basket_total.configure(textvariable=checkout_order_total_var)


    #--->widgets<---#

    first_name_label = ctk.CTkLabel(checkout_window_frame, text="First Name:")
    first_name_entry = ctk.CTkEntry(checkout_window_frame)
    first_name_var = tk.StringVar(checkout_window_frame)
    

    surname_label = ctk.CTkLabel(checkout_window_frame, text="Surname:")
    surname_entry = ctk.CTkEntry(checkout_window_frame)
    surname_var = tk.StringVar(checkout_window_frame)
    

    house_num_label = ctk.CTkLabel(checkout_window_frame, text="House Number:")
    house_num_entry = ctk.CTkEntry(checkout_window_frame)
    house_num_var = tk.StringVar(checkout_window_frame)
    
    street_name_label = ctk.CTkLabel(checkout_window_frame, text="Street Name:")
    street_name_entry = ctk.CTkEntry(checkout_window_frame)
    street_name_var = tk.StringVar(checkout_window_frame)
    

    town_city_label = ctk.CTkLabel(checkout_window_frame, text="Town/City:")
    town_city_entry = ctk.CTkEntry(checkout_window_frame)
    town_city_var = tk.StringVar(checkout_window_frame)
    

    county_label = ctk.CTkLabel(checkout_window_frame, text="County:")
    county_entry = ctk.CTkEntry(checkout_window_frame)
    county_var = tk.StringVar(checkout_window_frame)
    

    post_code_label = ctk.CTkLabel(checkout_window_frame, text="Post Code:")
    post_code_entry = ctk.CTkEntry(checkout_window_frame)
    post_code_var = tk.StringVar(checkout_window_frame)
    

    phone_number_label = ctk.CTkLabel(checkout_window_frame, text="Phone Number:")
    phone_number_entry = ctk.CTkEntry(checkout_window_frame)
    phone_number_var = tk.StringVar(checkout_window_frame)

    email_address_label = ctk.CTkLabel(checkout_window_frame, text="Email Address:")
    email_address_entry = ctk.CTkEntry(checkout_window_frame)
    email_address_var = tk.StringVar(checkout_window_frame)

    order_total_text_label = ctk.CTkLabel(checkout_window_frame, text="Order Total:") 
    order_total_label = ctk.CTkLabel(checkout_window_frame)
    order_total_label.configure(textvariable=checkout_order_total_var)

    ##############################Validate entry fields#######################################

    
    place_order_button = ctk.CTkButton(checkout_window_frame, text="Place Order", height=30, font=("TkHeadingFont", 20), 
                                       command=lambda: place_order(first_name_var, first_name_entry, 
                                                                   surname_var, surname_entry, 
                                                                   house_num_var, house_num_entry, 
                                                                   street_name_var, street_name_entry, 
                                                                   town_city_var, town_city_entry, 
                                                                   county_var, county_entry, 
                                                                   post_code_var, post_code_entry, 
                                                                   phone_number_var, phone_number_entry, 
                                                                   email_address_var, email_address_entry, checkout_window))
    

    #--->place frames & widgets on grid<---#

    #--->window frame
    checkout_window_frame.grid(column=0, row=0, sticky="nsew")
    
    #--->top row frame & widgets
    checkout_menu_top_frame.grid(row=0, column=0, pady=(0, 7.5), columnspan=3, sticky="nsew")
    checkout_menu_logo_widget.grid(column=0, pady=10, row=0)
    checkout_menu_title.grid(column=1, pady=10, row=0)
    checkout_menu_basket_frame.grid(row=0, column=2, padx=(0,5), pady=6, sticky="nsew")
    checkout_menu_basket_button.grid(column=0,row=0, sticky="nsew")
    checkout_menu_basket_total.grid(column=1, row=0, sticky="nsew")

    #--->widgets
    first_name_label.grid(column=0, row=1, padx=(5,0), pady=7.5, sticky="nsew")
    first_name_entry.grid(column=1, row=1, columnspan=2, padx=(0,15), pady=7.5, sticky="nsew")

    surname_label.grid(column=0, row=2, padx=(5,0), pady=7.5, sticky="nsew")
    surname_entry.grid(column=1, row=2, columnspan=2, padx=(0,15), pady=7.5, sticky="nsew")

    house_num_label.grid(column=0, row=3, padx=(5,0), pady=7.5, sticky="nsew")
    house_num_entry.grid(column=1, row=3, columnspan=2, padx=(0,15), pady=7.5, sticky="nsew")

    street_name_label.grid(column=0, row=4, padx=(5,0), pady=7.5, sticky="nsew")
    street_name_entry.grid(column=1, row=4, columnspan=2, padx=(0,15), pady=7.5, sticky="nsew")

    town_city_label.grid(column=0, row=5, padx=(5,0), pady=7.5, sticky="nsew")
    town_city_entry.grid(column=1, row=5, columnspan=2, padx=(0,15), pady=7.5, sticky="nsew")

    county_label.grid(column=0, row=6, padx=(5,0), pady=7.5, sticky="nsew")
    county_entry.grid(column=1, row=6, columnspan=2, padx=(0,15), pady=7.5, sticky="nsew")

    post_code_label.grid(column=0, row=7, padx=(5,0), pady=7.5, sticky="nsew")
    post_code_entry.grid(column=1, row=7, columnspan=2, padx=(0,15), pady=7.5, sticky="nsew")

    phone_number_label.grid(column=0, row=8, padx=(5,0), pady=7.5, sticky="nsew")
    phone_number_entry.grid(column=1, row=8, columnspan=2, padx=(0,15), pady=7.5, sticky="nsew")

    email_address_label.grid(column=0, row=9, padx=(5,0), pady=7.5, sticky="nsew")
    email_address_entry.grid(column=1, row=9, columnspan=2, padx=(0,15), pady=7.5, sticky="nsew")

    order_total_text_label.grid(column=1, row=10, pady=15, sticky="nsew") 
    order_total_label.grid(column=1, row=11, pady=7.5, sticky="nsew")

    place_order_button.grid(column=1, row=12, pady=(7.5,20), sticky="nsew")

   
   


    #--->configure grid<---#

    #--->window frame
    checkout_window.columnconfigure(0, weight=1)
    checkout_window.rowconfigure(0, weight=1)
    #--->top row frame
    checkout_window_frame.columnconfigure(0, weight=1)
    checkout_window_frame.rowconfigure(0, weight=1)
    #--->top row widgets
    checkout_menu_top_frame.columnconfigure(0, weight=1)
    checkout_menu_top_frame.columnconfigure(1, weight=1)
    checkout_menu_top_frame.columnconfigure(2, weight=1)
    checkout_menu_top_frame.rowconfigure(0, weight=1)
    checkout_menu_basket_frame.columnconfigure(0, weight=1)
    checkout_menu_basket_frame.columnconfigure(1, weight=1)
    checkout_menu_basket_frame.rowconfigure(0, weight=1)
    #--->widgets
    checkout_window_frame.columnconfigure(0, weight=1)
    checkout_window_frame.columnconfigure(1, weight=1)
    checkout_window_frame.columnconfigure(2, weight=1)
    checkout_window_frame.rowconfigure(2, weight=1)
    checkout_window_frame.rowconfigure(3, weight=1)
    checkout_window_frame.rowconfigure(4, weight=1)
    checkout_window_frame.rowconfigure(5, weight=1)
    checkout_window_frame.rowconfigure(6, weight=1)
    checkout_window_frame.rowconfigure(7, weight=1)
    checkout_window_frame.rowconfigure(8, weight=1)
    checkout_window_frame.rowconfigure(9, weight=1)
    checkout_window_frame.rowconfigure(10, weight=1)
    checkout_window_frame.rowconfigure(11, weight=1)
    checkout_window_frame.rowconfigure(12, weight=1)
    


def place_order(first_name_var, first_name_entry, 
                    surname_var, surname_entry, 
                    house_num_var, house_num_entry, 
                    street_name_var, street_name_entry, 
                    town_city_var, town_city_entry, 
                    county_var, county_entry,
                    post_code_var, post_code_entry,
                    phone_number_var, phone_number_entry,
                    email_address_var, email_address_entry, checkout_window):        
        first_name_var.set(first_name_entry.get())
        surname_var.set(surname_entry.get())
        house_num_var.set(house_num_entry.get())
        street_name_var.set(street_name_entry.get())
        town_city_var.set(town_city_entry.get())
        county_var.set(county_entry.get())
        post_code_var.set(post_code_entry.get())
        phone_number_var.set(phone_number_entry.get())
        email_address_var.set(email_address_entry.get())
        vars = [first_name_var, surname_var]
        vars2 = [street_name_var, town_city_var, county_var]
        for var in vars:
            if var.get().isalpha() == False:
                raise ValueError
        for var in vars2:
            if re.search(r"^[a-z -.,]+$", var.get(), re.IGNORECASE) == False:
                raise ValueError
        if house_num_var.get().isnumeric() == False:
            raise ValueError
        elif re.search(r"^[a-z]{1,2}[a-z0-9]{1,2}\s[0-9]{1}[a-z]{2}$", post_code_var.get(), re.IGNORECASE) == False:
            raise ValueError
        elif re.search(r"^[+0]{1}[74]{1}[0-9]{9,14}$", phone_number_var.get()) == False:
            raise ValueError
        else:
            generate_receipt(email_address_var.get(), first_name_var.get())
            confirmation_window(first_name_var.get(), email_address_var.get(), checkout_window)
            clear_basket()


def clear_basket():
    Food.basket = {}
    update_basket_total()




def confirmation_window(customer_name, customer_email, checkout_window):
    
    checkout_window.destroy()

    confirmation_window = ctk.CTkToplevel(app)
    confirmation_window.attributes("-topmost", True)

    confirmation_window.geometry("600x200")
    confirmation_window.title("Order Confirmation")

    confirmation_window_frame = ctk.CTkFrame(confirmation_window, fg_color="#161219", border_color="#BC006C", border_width=5)

    confirmation_title_label = ctk.CTkLabel(confirmation_window_frame, text="Order Confirmed")

    confirmation_label = ctk.CTkLabel(confirmation_window_frame, text=f"Hi {customer_name}, \n\nYour order has been received,\n\nEmail confirmation along with a receipt will be sent to {customer_email}")
    
    confirmation_window_frame.grid(column=0, row=0, sticky="nsew")
    confirmation_title_label.grid(column=0, row=0, sticky="nsew")
    confirmation_label.grid(column=0, row=1, sticky="nsew")

    confirmation_window.columnconfigure(0, weight=1)
    confirmation_window.rowconfigure(0, weight=1)
    confirmation_window_frame.columnconfigure(0, weight=1)
    confirmation_window_frame.rowconfigure(0, weight=1)
    confirmation_window_frame.rowconfigure(1, weight=6)


def generate_receipt(customer_email, customer_name):
        
    items_list = [key for key in Food.basket.keys()]

    item_list_str = ""

    for key in items_list:
        item_list_str += key + "\n"

    qty_list = [value for key, value in Food.basket.items() for i, value in enumerate(Food.basket[key]) if i == 0]

    qty_total = 0

    for qty in qty_list:
        qty_total += qty

    prices_list = [value for key, value in Food.basket.items() for i, value in enumerate(Food.basket[key]) if i == 1]


    order_amount = 0

    for price in prices_list:
        order_amount += price


    order_list_headers = ["Product", "Qty", "Price" ]

    table = []

    for item, qty, price in zip(items_list, qty_list, prices_list):
        table.append([item, qty, f"£{price}"])
    table.append(["Total", qty_total, f"£{order_amount}"])

    email_receipt(customer_email, customer_name, table, order_list_headers)
        

def email_receipt(recipient_email, recipient_name, table, order_list_headers):
    
    from_email = "Kayscafe86@gmail.com"
    password = "zyzm nrdy dall hyaw"
    server = "smtp.gmail.com:587"
    to_email = recipient_email


    text = """
    Hi """ +recipient_name+""",
    
    Thanks for your order,
    
    Please find your receipt below,
    
    {receipt}
    
    Regards
    
    Kay
    """

    html = """
    <html>
    <head>
    <meta charset="UTF-8">
    <style>receipt, th, td {{ border: 1px solid white; border-collapse: collapse; }} th, td {{ padding: 5px; }}</style>
    </head>
    <body>
    <p>Hi """+recipient_name+""",</p>
    <p>Thanks for your order,</p>
    <p>Please find your receipt below,</p>
    {receipt}
    <p>Regards</p>
    <p>Kay</p>
    </body>
    </html>
    """
    with SMTP(server) as smtp:
        text = text.format(receipt = tabulate(table, headers=order_list_headers, tablefmt="outline", colalign=("left", "center", "center")))
        html = html.format(receipt = tabulate(table, headers=order_list_headers, tablefmt="html", colalign=("left", "center", "center")))
        message = MIMEMultipart("alternative", None, [MIMEText(text), MIMEText(html, "html")])
        message["Subject"] = "Order Confirmation"
        message["From"] = from_email
        message["To"] = to_email
        smtp.starttls()
        smtp.login(from_email, password, initial_response_ok=True)
        #smtp.sendmail(from_email, to_email, message.as_string())
        return smtp.sendmail(from_email, to_email, message.as_string())

    
if __name__ == "__main__":
    main()
    
    







   





    
    





