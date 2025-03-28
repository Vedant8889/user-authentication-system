from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import json

USER_DATA_FILE = "users.json"

def load_users():
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

d = load_users()

def create_otp():
    return ''.join(str(random.randint(0, 9)) for _ in range(4))

def send_otp():
    otp = create_otp()
    messagebox.showinfo('OTP', f'Your OTP is: {otp}')

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email in d and d[email]["password"] == password:
        messagebox.showinfo('Message', 'Login successful')
    else:
        messagebox.showerror('Error', 'Invalid Email or Password')

def handle_signup():
    email = signup_email_input.get()
    password = signup_password_input.get()

    if email in d:
        messagebox.showinfo('Message', 'Email already exists! Logging in...')
        email_input.delete(0, END)
        password_input.delete(0, END)
        email_input.insert(0, email)
        password_input.insert(0, d[email]["password"])
    else:
        send_otp()
        d[email] = {"password": password, "security_answers": [], "details": []}
        save_users(d)
        messagebox.showinfo('Signup', 'Signup successful! You can now log in.')

def open_signup_window():
    global signup_email_input, signup_password_input
    signup_window = Toplevel(root)
    signup_window.title('Signup Form')
    signup_window.geometry('350x400')
    signup_window.config(background='black')

    Label(signup_window, text='Signup', fg='red', bg='black', font=('verdana', 20)).pack(pady=(10, 10))

    Label(signup_window, text='Enter Email', fg='white', bg='black', font=('verdana', 14)).pack(pady=(5, 5))
    signup_email_input = Entry(signup_window, width=30)
    signup_email_input.pack(ipady=5, pady=(1, 10))

    Label(signup_window, text='Enter Password', fg='white', bg='black', font=('verdana', 14)).pack(pady=(5, 5))
    signup_password_input = Entry(signup_window, width=30, show='*')
    signup_password_input.pack(ipady=5, pady=(1, 10))

    Button(signup_window, text='Signup', bg='white', fg='black', width=10, command=handle_signup).pack(pady=10)

root = Tk()
root.title('Login Form')
root.geometry('350x500')
root.config(background='black')

img = Image.open('netflix.jpg')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(20, 20))

text_label = Label(root, text='Netflix', fg='red', bg='black', font=('verdana', 20))
text_label.pack()

email_label = Label(root, text='Enter Email', fg='white', bg='black', font=('verdana', 14))
email_label.pack(pady=(10, 10))
email_input = Entry(root, width=30)
email_input.pack(ipady=5, pady=(1, 15))

password_label = Label(root, text='Enter Password', fg='white', bg='black', font=('verdana', 14))
password_label.pack(pady=(10, 10))
password_input = Entry(root, width=30, show='*')
password_input.pack(ipady=5, pady=(1, 15))

login_btn = Button(root, text='Login', bg='white', fg='black', width=10, command=handle_login)
login_btn.pack(padx=10, pady=10)

signup_btn = Button(root, text='Signup', bg='white', fg='black', width=10, command=open_signup_window)
signup_btn.pack(padx=10, pady=10)

root.mainloop()
