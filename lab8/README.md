# Topic: *Email Confirmation*
## Author: *Moglan Mihai*
------
## Main tasks :
__1. Create an application that could register a new user;__

__2. Perform email confirmation (via a one time password / code or via a link);__

__3. Output on the screen whether a user confirmed their email or did not confirm it yet;__

## Introduction :
All laboratory works are done in Python. The GUI of the application is done using tkinter, there was created a new gmail account which is used like a host for sending emails for authentification. My working OS is Windows 10.

## A little description and steps to follow:
__1. First of all, install the the current versions of all libraries via the command `pip install -r requirements.txt`;__

__2. Run `gui.py` to acces the application;__

__3. The GUI very much looks like Notepad GUI's. There is the white field for text and one menus up;__

__4. The menu is 'File Menu' with following commands:;__

  * New (creates a new blank working field);
  * Confirm email (opens a new window to introduce new email to register it in the application);
  * Check email status (checks the status of email: it is confirmed, pending or not confirmed);
  * Exit (close the app);

__5. After you submit the email, you will receive a confirmation code made of a 4-digit number. You should introduce this number in the new pop-up from the application;__
  
__6. If you close the pop-ups you can open them at the same stage where you stopped;__
