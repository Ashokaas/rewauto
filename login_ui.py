import tkinter as tk
from os.path import expanduser

from screeninfo import get_monitors



def login_ui():
    global output
    output = None

    home_folder = expanduser("~").replace("\\", "/")

    open(home_folder + "/rewauto_data.txt", "a+").close()
    save = open(home_folder + "/rewauto_data.txt", "r")
    data = save.readlines()
    data += ["" for _ in range(2 - len(data))]

    def done(*args):
        savew = open(home_folder + "/rewauto_data.txt", "w")
        data[0] = remember_values[0].get() * email_input.get()
        data[1] = remember_values[1].get() * pass_input.get()
        data.insert(1, "\n")

        savew.writelines(data)
        global output
        output = (email_input.get(), pass_input.get())
        if True:
            print(output[0], *["●" for _ in output[1]])
        else:
            print(output)
            
        root.destroy()
        return

    root = tk.Tk()
    
    largeur = 500
    hauteur = 350
    root.geometry(f"{largeur}x{hauteur}+{str(get_monitors()[0].width/2-largeur/2)[0:-2]}+{str(get_monitors()[0].height/2-(hauteur-50))[0:-2]}")
    root.title("Login")

    tk.Label(root, text="Rewauto",
             font=('bold', 20), wraplength=450).pack()
    tk.Label(root, text="Please enter the Email and Password of your Microsoft Rewards account",
             font=('bold', 10), wraplength=450).pack()

    login_frame = tk.Frame(root)
    login_frame.pack(pady=20)

    tk.Label(login_frame, text="Email:").grid(column=0, row=0)
    email_input = tk.Entry(login_frame, width=30)
    email_input.grid(column=1, row=0)
    
    global pass_input, is_hidden
    is_hidden = True
    
    tk.Label(login_frame, text="Password:").grid(column=0, row=1, pady=(10, 0))
    pass_input = tk.Entry(login_frame, show="●", width=30)
    pass_input.grid(column=1, row=1, pady=(10, 0))
    
    def show_password():
        global is_hidden
        if is_hidden == True:
            pass_input.configure(show="")
            is_hidden = False
        elif is_hidden == False:
            pass_input.configure(show="●")
            is_hidden = True
        
    tk.Button(login_frame, text="👁️", command=show_password).grid(column=2, row=1)

    remember_frame = tk.Frame(root)
    remember_frame.pack()

    remember_values = [tk.IntVar(), tk.IntVar()]
    remember_email = tk.Checkbutton(remember_frame, text="Remember Email", variable=remember_values[0])
    remember_email.pack(side="top", anchor="w")
    remember_pass = tk.Checkbutton(remember_frame, text="Remember Password", variable=remember_values[1])
    remember_pass.pack(side="top", anchor="w")

    email_input.insert(0, data[0].replace("\n", ""))
    pass_input.insert(0, data[1].replace("\n", ""))
    if data[0] != "":
        remember_email.select()
    if data[1] != "":
        remember_pass.select()
    save.close()

    tk.Button(root, text="Done", command=done).pack(pady=20)
    root.bind('<Return>', done)

    root.mainloop()
    return output

if __name__ == "__main__":
    login_ui()
