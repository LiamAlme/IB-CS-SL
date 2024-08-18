import tkinter as tk

root = tk.Tk()
root.title("Text Input")
root.geometry("500x500")

username_input = tk.StringVar()
password_input = tk.StringVar()

username = username_input.get

user_list = open("user_list.txt", "a")

username_text = tk.Label(root, text = "Username", font = ("calibre", 10, "normal"))
username_text.grid(row=0, column=1)
root.grid_columnconfigure(1, weight=1)

username_box = tk.Entry(root, textvariable = username_input, font = ("calibre", 10, "normal"))
username_box.grid(row=1, column=1)

password_text = tk.Label(root, text = "Password", font = ("calibre", 10, "normal"))
password_text.grid(row=2, column=1)

password_box = tk.Entry(root, textvariable = password_input, font = ("calibre", 10, "normal"), show = "*",)
password_box.grid(row=3, column=1)

linebreak = tk.Label(root, text = "")
linebreak.grid(row=4, column=1)

enter_button = tk.Button(root, text = "Enter", font = ("calibre", 10, "normal"), command= lambda : print(str(username)))
enter_button.grid(row=5, column=1)

root.mainloop()
