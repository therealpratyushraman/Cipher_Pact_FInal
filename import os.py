import tkinter as tk
from tkinter import messagebox
from functools import partial

def login(username, password, app, login_window):
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        app.deiconify()  # Show the main application window
        login_window.destroy()  # Close the login window
        import main
        main.app.mainloop()
        
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def validate_login(entry_username, entry_password, app, login_window):
    username = entry_username.get()
    password = entry_password.get()
    login(username, password, app, login_window)

def show_login_window():
    login_window = tk.Toplevel()
    login_window.title("Login")
    login_window.geometry("300x200")

    tk.Label(login_window, text="Username:").pack()
    entry_username = tk.Entry(login_window)
    entry_username.pack()

    tk.Label(login_window, text="Password:").pack()
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack()

    validate_login_partial = partial(validate_login, entry_username, entry_password, app, login_window)
    tk.Button(login_window, text="Login", command=validate_login_partial, width=15, height=2).pack(pady=10)

    login_window.mainloop()

def quit_application():
    app.destroy()

def show_help_desk():
    help_desk_window = tk.Toplevel()
    help_desk_window.title("Help Desk")
    help_desk_window.geometry("300x200")

    phone_number = "1234567899"
    email = "compress@gmail.com"

    tk.Button(help_desk_window, text="Phone Number: " + phone_number, width=25, height=2).pack(pady=5)
    tk.Button(help_desk_window, text="Email: " + email, width=25, height=2).pack(pady=5)

    back_to_main = partial(back_to_main_window, help_desk_window)
    tk.Button(help_desk_window, text="Back", command=back_to_main, width=15, height=2).pack(pady=10)

def back_to_main_window(help_desk_window):
    help_desk_window.destroy()

def help_desk():
    show_help_desk()

app = tk.Tk()
app.title("File Processing Application")
app.geometry("1200x700")
app.configure(bg="midnight blue")

login_button = tk.Button(app, text="Login", command=show_login_window, width=15, height=2)
login_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

quit_button = tk.Button(app, text="Quit", command=quit_application, width=15, height=2)
quit_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

help_button = tk.Button(app, text="Help Desk", command=help_desk, width=15, height=2)
help_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

app.mainloop()
