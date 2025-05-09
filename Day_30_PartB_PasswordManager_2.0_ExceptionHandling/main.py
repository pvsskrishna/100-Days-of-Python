# Day_29 Project Enhancement
# GOAL: Is to take the Password Manager to the next level

"""
JSON: JavaScriptObjectNotation
In Python we have an inbuilt json library, and we are going to use the below methods.
json methods to handle data in json file:
    json.dump() --> to Write
    json.load() --> to Read
    json.update() --> to Update"""

from tkinter import *
from tkinter import messagebox
import random
import pyperclip #this package is used to copy and paste the text
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = []
    password_symbols = []
    password_numbers = []

    password_letters += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)#so when we generate password automatically that password will be copied so simply we can past it anywhere

    #print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().lower()
    email_username = emailUsername_entry.get().lower()
    password = password_entry.get()

    new_data = {
        website:{
            "email":email_username,
            "password":password
        }
    }

    #validation
    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json","r") as data_file:
                #Reading old data
                data = json.load(fp=data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving Updated data
                json.dump(new_data, fp=data_file, indent=4)  # Serialize the Python dictionary `new_data` into JSON format and write it to the file object `data_file` with indentation for readability
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving Updated data (both old and new entries)
                json.dump(data, fp=data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().lower()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Data file is empty or corrupted.")

    else:
        if website in data:
            mail = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website.title(),message=f"Mail: {mail}\nPassword: {password}")
        else:
            if len(website) == 0 or website == "":
                messagebox.showinfo(title="Error", message=f"Please enter proper website name")
            else:
                messagebox.showinfo(title=website.title(), message=f"No details for the website {website.upper()} exist.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)  # Adds internal padding around all widgets inside the window; doesn't resize the window itself
window.config(width=700, height=700)  # Sets the fixed size of the main window; controls the overall window dimensions

canvas = Canvas(width=200, height= 200)
lock_image = PhotoImage(file=r"./logo.png")
canvas.create_image(100,100,image = lock_image) #since canvas width and height are 200, if we give create_image x,y as 100,100 so that image will come at center on the canvas
canvas.grid(column=1,row = 0)

#Labels
website_label = Label(text="Website:",font=("Arial",10,"bold"))
website_label.grid(column=0,row=1,sticky="E", pady=5) #adds 5 pixels of horizontal padding on both left and right

emailUsername_label = Label(text="Email/Username:",font=("Arial",10,"bold"))
emailUsername_label.grid(column=0,row=2, sticky="E", pady=5)

password_label = Label(text="Password:",font=("Arial",10,"bold"))
password_label.grid(column=0,row=3, sticky="E", pady=5)

#Entries

website_entry = Entry(width=32)
website_entry.focus() # Keyboard focus is set to website_entry when the app starts i.e cursor will start blinking
website_entry.grid(column = 1,row = 1,sticky="w",padx=(0,5)) # Makes the canvas span across 3 columns to center it above the form

emailUsername_entry = Entry(width=50)
emailUsername_entry.insert(0,"varun@gmail.com") #Here also we can use END instead of 0 index so that it will start inserting from the existing data last index. By default, it will display the string at desired index (here index is 0) when application is launched
emailUsername_entry.grid(column = 1,row = 2,columnspan=2,sticky="w",padx=5)

password_entry = Entry(width=32)
password_entry.grid(column = 1,row = 3,sticky="w",padx=(0,5))

#Buttons

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='W')# Adds 130 pixels of horizontal space to the left, shifting the button to the right within its grid cell. sticky='W', Aligns (sticks) the button to the left (West) side of the grid cell

add_button = Button(text='Add',width=48, command = save_data)
add_button.grid(column=1,row=4,columnspan=2,padx=5,sticky="W")

search_button = Button(text='Search',width=15, command = find_password)
search_button.grid(column = 2,row = 1,sticky="w")
window.mainloop()