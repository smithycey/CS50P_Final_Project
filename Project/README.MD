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

#### menu.py
The purpose of this file is to keep all of the functionality surrounding creating the actual menu of products, setting the names of the items, setting the prices and storing the classes in which the menu items are instantiated and the basket is managed all in one place.\
This means that any modifications that need to be done to the menu can be done within this file, which will then be realised throughout the remainder of the project without having to navigate through the entirety of the main project file to make individual changes.

The menu.py file consists of a parent class (Food) and 5 child classes.

###### Food class:
The Food class is the parent class which both manages, records and updates the basket whilst also providing the functionality for all of the child classes.

The Food class begins with an empty dictionary named basket. This is where any items that are added to the basket will be stored in order for the project file to access later.

Next is the init method which takes in the self, product and price variables as arguments and uses them to assign the product and price instance variables. It also assigns the self.total instance variable to the same value as self.price.

Following the init method is the add_to_basket instance method which as the name suggests is used to add products to the basket dictionary referenced above. This method takes in the self and qty arguments.\
This method updates the self.total using the self.price * qty, it checks that qty is not less than 1 and then checks if the product is already in the basket\
If the product is in the basket already, then the method will update the basket adding the total price and quantity onto that product in the basket.\
If however the item is not already in the basket then the method will simply add the product, quantity and total price to the basket.

Finally in the Food class is the class method delete_from_basket which takes two arguments cls and key. This method has only one line of code which simply takes whichever key is passed to it and deletes that from the basket dict.

##### Child Classes (Burgers, Not_Burgers, Desserts, Drinks, Milkshakes):

The five child classes are all identical, they have the Food class as the parent, and then simply one just a init method which takes in self, product and price. This does the same with these arguments as the Food class. Also within this method is another init method which is used with the super function to initialize the attributes of the parent class, in this case product and price.

##### Class Instantiation

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