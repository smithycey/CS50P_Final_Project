# Kays Cafe
### Video Demo:
### Description:

Welcome to Kays Cafe!\
This project is a gui application for an online ordering system for Kays Cafe\
It allows you to access the gui interface and navigate through the various menus available to view the selection of products on offer by the cafe. You can then add any of these products to the basket, at which point you can then go to the basket, which you can edit by removing a product if you no longer require it and once satisfied with your selection you can continue through to the checkout window where you will enter your details before confirming your order. Once you have confirmed your order you will be presented with the order confirmation window which will confirm you have placed your order and that a confirmation email along with a receipt will be sent to the email address provided.

### Files:

#### requirements.txt

This file will allow you to install all of the required libraries for this project with the command pip install -r requirements.txt

#### project.py

This is the main file of the project.

The contents of this file generate, and run the customtkinter gui for Kays Cafe\

The file consists of a parent class (App), along with 7 child classes.\

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

