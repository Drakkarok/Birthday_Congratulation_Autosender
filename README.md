


# Birthday_Congratulation_Autosender

Short description:
Automatically sends emails using Gmail's API to friends and family that happens to have their birthdays on the same day that you run the code!

---

## CONFIGURATION - SMTP Port
Before going through the following steps be sure to have a valid google account!  

1. Make sure you've got the correct smtp address for your email provider and replace it into the line "with smtplib.SMTP("smtp.gmail.com") as connection:"  
Gmail: smtp.gmail.com  
Hotmail: smtp.live.com  
Outlook: outlook.office365.com  
Yahoo: smtp.mail.yahoo.com  
2. Go to [https://myaccount.google.com/](url)  
Select Security on the left and scroll down to How you sign in to Google.  
Enable 2-Step Verification  
3. Click on 2-Step Verification again, and scroll to the bottom.  
There you can add an App password.  
Select Other from the dropdown list and enter an app name, e.g. Python Mail, then click Generate.  
COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.  
4. Replace in main.py "email_dummy" and "password" with your google account address and the newly obtained app password.  
5. Replace the data in birthdays.csv to match your friends/family data.  
6. Run the code!  

---

Build using: 
- smtplib;
- pandas;
- datetime;
- random.

Functions:
- N/A.

Classes:
- N/A.

Methods:
- N/A.
