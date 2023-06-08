from tkinter import Button, Entry
from canvas import root, frame
from helpers import clean_screen
from json import loads, dump
# loads takes a string and converts it to an object
# dump takes a dictionary and converts it to a string


def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=register,    # It should be a reference to the function, not the result of the function
    )

    login_button = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
    )
    frame.create_window(350, 250, window=register_button)
    frame.create_window(350, 320, window=login_button)


def get_users_data():
    info_data = []

    with open("users_information.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def register():
    clean_screen()

    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=registration
    )

    frame.create_window(210, 265, window=register_button)


def registration():
    info_dict = {
        "First name": first_name_box.get(),
        "Last name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get(),
    }

    if check_registration(info_dict):
        with open("users_information.txt", "a") as users_file:
            dump(info_dict, users_file)    # Instead of .write
            users_file.write("\n")
            # TODO: Display products


def check_registration(info):
    frame.delete("error")    # This deletes tags which are equal to "error"
    for key, value in info.items():
        if not value.strip():    # Remove the spaces
            frame.create_text(
                392,
                265,
                text=f"{key} cannot be empty!",
                fill="red",
                font=("Helvetica", "11", "bold"),
                tags="error",    # We set the tags to "error" so that the frame.delete can delete the error
            )

            return False

    info_data = get_users_data()

    for record in info_data:
        if record["Username"] == info["Username"]:
            frame.create_text(
                392,
                265,
                text="Username is already taken!",
                fill="red",
                font=("Helvetica", "11", "bold"),
                tags="error",  # We set the tags to "error" so that the frame.delete can delete the error
            )

            return False

    return True


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")
