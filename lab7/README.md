# Topic: *Database Security*
## Author: *Moglan Mihai*
------
## Main tasks :
__1. Create a MongoDB database which would contain some secured sensitive data (protected via 2-way encryption);__

__2. Create an application which would display the data contained in the database (both common data and the decrypted sensitive data);__

__3. Make sure that the sensitive data can only be accessed via application (i.e. it is secture);__

## Introduction :
All laboratory works are done in Python. The GUI of the application is done using tkinter, but MongoDB manipulation via pymongo and bson for encryption. My working OS is Windows 10.

## A little description and steps to follow:
__1. First of all, install the the current versions of all libraries via the command `pip install -r requirements.txt`;__

__2. Test that you have mongocryptd installed in your path by running `mongocryptd`, ensuring that it prints out some output. You can shut it down again with `Ctrl-C`;__

__3. Create a user on MongoDB cloud, who will have access to the database. Save the username and password of the user, you will need them in order to upload and read data to the database;__

__4. Run the script `create_key.py`. This script generates a secret master key which will be used to protect individual field keys. We will be using a 'local' master key which wull be stored in a local key file. This Python script will generate some random bytes to be used as a secret master key;__

__5. In `read_database.py` and `create_database.py` change all `username` and `passoword` variables with your own information created at point 2. Run the `create_database.py` script to create `people` database on MongoDB cloud with common field `full_name`  and sensitive filed `ssn`, which represents the fictive phone number of the persons;__

__6. In `read_database.py` there are 2 functions `is_correct_log_in` (verifies if username and password for connection to database are correct) and `read_data` (return the all data from the database, in decrypted format) for the application;__

__7. Run `gui.py` to acces the application;__

__8. The GUI very much looks like Notepad GUI's. There is the white field for text and one menus up;__

__9. The menu is 'File Menu' with following commands:;__

  * New (creates a new blank working field);
  * Connect to Database (opens a new window to introduce username and password to connect to database);
  * View data (outputs the data from the database);
  * Log out (logs out from the database);
  * Exit (close the app);

__10. The database can't be accessed if the password and username are wrong;__
  
__11. When persons logs out, all data is deletead automatically from the application;__
