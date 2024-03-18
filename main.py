from tkinter import Tk, Label, Entry, Button, messagebox
from api import scrape_website
import threading

def submit_credentials():
    username = username_entry.get()
    password = password_entry.get()
    
    threading.Thread(target=perform_scraping, args=(username, password)).start()

def perform_scraping(username, password):
    remaining_swipes = scrape_website(username, password)
    messagebox.showinfo("Remaining Swipes", f"Remaining swipes: {remaining_swipes}")

root = Tk()
root.title("MSU Swipes Checker")

username_label = Label(root, text="Username:")
username_label.grid(row=0, column=0)
username_entry = Entry(root)
username_entry.grid(row=0, column=1)

password_label = Label(root, text="Password:")
password_label.grid(row=1, column=0)
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1)

submit_button = Button(root, text="Submit", command=submit_credentials)
submit_button.grid(row=2, columnspan=2)


if __name__ == "__main__":
    root.mainloop()
