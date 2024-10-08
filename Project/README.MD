# Kays Cafe
### Video Demo: https://youtu.be/q-Z6C0QSytQ
### Description:

Welcome to Kays Cafe!\
This project is a gui application for an online ordering system for Kays Cafe\
It allows you to access the gui interface and navigate through the various menus available to view the selection of products on offer by the cafe. You can then add any of these products to the basket, at which point you can then go to the basket, which you can edit by removing a product if you no longer require it and once satisfied with your selection you can continue through to the checkout window where you will enter your details before confirming your order. Once you have confirmed your order you will be presented with the order confirmation window which will confirm you have placed your order and that a confirmation email along with a receipt will be sent to the email address provided.

I decided to go with a GUI interface for my CS50P final project as I wanted to try applying the skills taught so far on something that has not yet been covered in the course/
Originally I began using Tkinter as the library for the GUI, however not long after starting the project I found this to be quite limiting and having done some research I discovered the Customtkinter library which appeared to offer far more flexibility and options in the design of the GUI along with a more modern design overall and decided to proceed with that instead.

### Files:

#### requirements.txt

This file will allow you to install all of the required libraries for this project with the command pip install -r requirements.txt

#### project.py

This is the main file of the project.

The contents of this file generate, and run the customtkinter gui for Kays Cafe

The file consists of a parent class (App), along with 7 child classes.

The parent App class provides the theme for the rest of the file by linking the json file to the rest of the project, whilst also providing the functionatlity for the generation of and navigation between the various frames in the interface.\

The child classes consist of the following: Title_frame, Menu_navigation_frame, Burger_menu, Not_burger_menu, Desserts_menu, Drinks_menu and Milkshakes_menu

###### Title_frame:

This class generates the first frame of the interface, essentially a welcome page showing a logo, title, message and button to enter further into the interface

##### Menu_navigation_frame:

This class generates the frame/home page which provides access to the remainder of the interface. This frame has buttons for each of the various menus on offer by the cafe (the other child classes referenced below) as well as the basket so that you can view what you currently have in your basket or checkout if ready to do so.

This class has the purpose of providing access to the remainder of the interface via a selection of buttons that take you to each of the other frames, for example there is a selection of buttons for each of the menus on offer by Kays Cafe along with a button that provides access to the basket once you are ready to proceed with your order.

##### Burger_menu, Not_burger_menu, Desserts_menu, Drinks_menu and Milkshakes_menu:

Each of these classes have essentially the same set up/ purpose of generating a menu frame with buttons for each of the products that have been instantiated to the corresponding class from the menu.py file. By clicking on one of these buttons, you are able to call the add_to_basket method from the Food class of the menu.py file which is inherited by each of the corresponding classes in the menu.py file in order to add that product to the basket in the interface.

You can also either navigate back to the Menu_navigation_frame or to the basket using the other buttons available on these menu frames.

##### Functions:

After the classes there are the functions, starting with the main function which simply instantiates and runs the App class when called\
Following on from that are various further functions with a variety of purposes, some create part of the interface, generating customtkinter windows when called and others that simply facilitate some of the functionality within the interface/project such as updating the basket etc

The functions that follow consist of: add_to_basket_window, basket_window, update_basket_total, checkout_window, place_order, clear_basket, confirmation_window, generate_receipt and email_receipt.

##### add_to_basket_window:

This function generates a pop-up window that appears over the current window when you click on one of the products, providing you with the option to select the quantity you require and then add the product to the basket by calling the corresponding add_to_basket method for that instances class in the menu.py file.

##### basket_window:

This function generates a pop-up window that appears over the current window when you click on the basket button from any of the menus or the menu navigation page. This window displays a list of all the items currently in the basket along with the quantities, prices and the total price for the basket. There is also an option to select any of the items currently in the basket within a drop down list, in order to then delete that item from the basket if you have changed your mind about requiring that product. Finally there is a checkout button for when you are ready to proceed with you order which will take you through to the next stage of the ordering process.

##### update_basket_total:

This function simply gets called by various other functions each time the contents of the basket are altered, when that happens this function recalculates the total cost of the basket to ensure the price showing both within the basket but also on each of the menu pages and the navigation page is always up to date

##### checkout_window:

This function when called, closes the basket window and generates another pop-up window for the checkout page. This page provides the user with various fields in which they can enter their details for the purposes of their online order. These details will also be used later on in the project for sending the email receipt to the customer. The user then has the option of clicking the "Place Order" button at the bottom of the page, once they have completed their details and are ready to proceed with the order.

##### place_order:

This function is called when the "Place Order" button is pressed in the checkout_window. The checkout_window function will pass the details taken from the user to the place_order function as parameters at which point the place_order function will then perform some checks on the details provided, such as ensuring that the value provided for house number is a numeric value, or that the post code provided matches the format for a UK postcode. Same for the phone number which must be the correct length for a UK phone number and other fields have checks which will fail if they clearly have invalid values within them. If any of these checks fail then the place_order function will raise a ValueError at which point the user will not be able to proceed past the checkout window until the details are corrected. If they do pass however then the place order function will simply call the following 3 functions: generate_receipt, confirmation_window and clear_basket, passing user details as parameters to the first two. These functions will be explained below.

##### clear_basket:

This function simply resets the basket to an empty dict and then calls the update_basket_total func so that the total basket price also updates back to 0 as now the order has been placed, the user should be able to place another order into a fresh basket if necessary.

##### confirmation_window:

This function will close the checkout window and then generate a new pop-up window over the existing window which will simply display a message with a greeting using the customers name and confirming their order and that they will receive email confirmation and a receipt to the email provided. This is thanks to the parameters passed to this function from the place_order function which originally came from the checkout_window function 

##### generate_receipt:

This function will create 3 lists of item names, quantities and prices as well as a total quantity of items and a total price of items from the values in the basket in the Food class of menu.py. It will then use this data to create a dict named table which will serve as the data for the customer receipt. The function will then call email_receipt and pass as parameters the table dict, a list of headers and the relevant customer details (name & email) that were passed through from the place_order function.

##### email_receipt:

This function will utilize the SMTP library to connect to the gmail.com server and dispatch an email to the email address provided by the customer. Due to the customers name also being passed through from the checkout window, the email will greet them by name, and there are also 2 options for the email, one written in html which is the first option and a second in text. This means if the email fails to send in html then it will retry the text version. The table dict that was passed through for the receipt is reformated using the tabulate library to look like an actual receipt and included in the body of the email.

#### menu.py

The purpose of this file is to keep all of the functionality surrounding creating the actual menu of products, setting the names of the items, setting the prices and storing the classes in which the menu items are instantiated and the basket is managed all in one place.\
This means that any modifications that need to be done to the menu can be done within this file, which will then be realised throughout the remainder of the project without having to navigate through the entirety of the main project file to make individual changes.

The menu.py file consists of a parent class named Food and 5 child classes: Burgers, Not_Burgers, Desserts, Drinks, Milkshakes\
The Food class contains the basket dict which records any items added to the basket which are later accessed by the project.py file, and two instance methods other than the init method which are add_to_basket and delete_from_basket methods. This class provides the functionality for the child classes which all inherit from it and only contian an init method with another super function with init method inside which allow them to pull through the attributes from the parent class.\
At the bottom of the file are each of the class instantiations. Each one is an individual product on the menu and these are seperated into 5 sections based on the menu they are assigned to.\
Any alterations to the menu can be made here, as this is where the name of each product and the prices are passed as parameters when the classes are called

#### table.py

The purpose of this file is purely to be used by the test_project.py file in order to provide a couple of parameters which are passed to the test_email_receipt_sends_mail function.

The code within the table.py file creates a table from the contents of the basket in the menu.py Food class, the purpose of this table would be to be used as a receipt. This has been copied from the project.py file in the generate_receipt function, and has only been extracted to this file for testing purposes.

#### test_project.py

This file consists of 3 test functions whose purpose is to perform unit tests on various functions within the project.py file to ensure it is functioning as intended.

The test functions are as follows:

##### test_generate_receipt_calls_email_receipt:

This function tests the generate receipt funtion from the project.py file by ensuring that it successfully calls the email receipt function from the same file. (However for the purpose of the test I have patched a mock of the email receipt function which I have passed into the unit test in order to check if it attempts to call that)

##### test_email_receipt_sends_mail:

This function tests the email_receipt function from the project.py file by ensuring that the function successfully sends an email. The unit test checks that an empty dict is returned as if the email fails to send then it would return a dict containing the email addresses of the emails that failed to send. In order to facilitate this test I have created a seperate file name table.py with an extract of the code from the email_receipt function that creates the table in order to pass the table and table headers directly from table.py as parameters to this unit test.

##### test_place_order_calls_funcs:

This function tests the place_order function from the project.py file by ensuring that it calls the following 3 functions: confirmation_window, generate_receipt and clear_basket. In order to perform this unit test I have patch the 3 functions that I want to check are called and passed mocks of them in order to see if they are called instead, and have also mocked all of the parameters for the place_order function.


#### theme.json

The purpose of this file is to the keep majority of the design for the project in one location. Fortunately the customtkinter library provides that functionality with the set_default_color_theme method to which you can pass a json file with all of the colours, font, font sizes etc for each type of customtkinter widget contained within. This means that the majority of changes to the design/colours etc of the project can all be done within one place, the theme.json file.

### Reference Material:

Throughout the course I have naturally utulised the internet for research purposes and in some cases adapted snippets of code into my own work, so I just wanted to provide clarification on some of the reference material I have used.

For the actual GUI libraries such as Tkinter and Customtkinter, I had already done a lot of research previously on Tkinter having watched many Youtube tutorials/demonstrations weeks prior to the project which was partially what prompted me to start with that library. Throughout the course of the project I continued to utilise Youtube videos as well as the documentation and particarlarly once I moved over to the Customtkinter library I was able to rely almost solely on the documentation on that as I found it much clearer to follow. The main youtube channels I would say that I utilised for help research with tkinter and customtkinter are Python Simplified and Tkinter.com

I did reach out for some help on Stack Overflow with one question regarding my set up of the classes in the menu.py file https://stackoverflow.com/questions/78818242/how-to-record-attributes-from-each-instance-in-a-class-variable-while-having-th, however although the answers were very helpful and able to answer my question, I realised soon after that I actually was overthinking in the first place and didn't need to do the task I was trying to accomplish when I asked the question, as I only actually needed the parent class to record the attributes to the class variable rather than the child and parent classes doing so.

As for lines of code that I have adapted into my work, please see below list with citations:

- Having done research for a better implementation for swithching frames whithin the GUI over the one I was currently using, I came across the following page https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/, i have adapted this into my project.py file within the App class
- Finally I also adapted some of the code from the following links: https://stackoverflow.com/questions/38275467/send-table-as-an-email-body-not-attachment-in-python, https://stackoverflow.com/questions/47153105/add-borders-of-table-sent-by-email-via-python, for help in correctly constructing and formatting the email receipt in the email_receipt function of the project.py file
- I should add that the above was all done alongside the backdrop of extensive research within the documentation for the relevant libraries.


