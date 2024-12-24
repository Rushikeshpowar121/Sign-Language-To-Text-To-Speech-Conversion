<<<<<<< HEAD
from customtkinter import *

# Gloval Initialization
d = {"English":"en", "Hindi":"hi", "Marathi":"mr", "French":"fr", "German":"es", "Spanish":"sp", "Korian":"ko", "Arebic":"ar"}

class App(CTk):
    def __init__(self):
        # Call the constructor of the parent class (CTk) using super()
        super().__init__()
        self.root = CTk()
        self.root.title("Sign Language To Text Conversion")
        self.root.geometry("1920x1080")
        self.root.config(bg="red")


        # self.frame1 = CTkFrame(self,width=450,height=400,corner_radius=20)
        # self.frame1.pack(padx=20,pady=20)
        # self.frame1.place(x=150,y=100)

        # self.frame2 = CTkFrame(self,width=450,height=400,corner_radius=20)
        # self.frame2.pack(padx=20,pady=20)
        # self.frame2.place(x=800,y=100)

        # self.combo_box = CTkComboBox(self)
        # self.combo_box.pack(padx=20, pady=20)
        # self.combo_box.configure(values=d.keys())
        # # Connecting it to a callback function to print the selected option on click event
        # self.combo_box.configure(command=self.combobox_callback)
        # self.combo_box.place(x=1300,y=600)
        self.l1 = CTkLabel(master=self.root,text="Rushikesh")
        self.l1.place(x=20,y=50)

    # def combobox_callback(self,choice):
    #     print("combobox dropdown clicked:", d.get(choice))


app = App()
app.geometry("800x800")
# app.attributes("-fullscreen", True)
=======
from customtkinter import *

# Gloval Initialization
d = {"English":"en", "Hindi":"hi", "Marathi":"mr", "French":"fr", "German":"es", "Spanish":"sp", "Korian":"ko", "Arebic":"ar"}

class App(CTk):
    def __init__(self):
        # Call the constructor of the parent class (CTk) using super()
        super().__init__()
        self.root = CTk()
        self.root.title("Sign Language To Text Conversion")
        self.root.geometry("1920x1080")
        self.root.config(bg="red")


        # self.frame1 = CTkFrame(self,width=450,height=400,corner_radius=20)
        # self.frame1.pack(padx=20,pady=20)
        # self.frame1.place(x=150,y=100)

        # self.frame2 = CTkFrame(self,width=450,height=400,corner_radius=20)
        # self.frame2.pack(padx=20,pady=20)
        # self.frame2.place(x=800,y=100)

        # self.combo_box = CTkComboBox(self)
        # self.combo_box.pack(padx=20, pady=20)
        # self.combo_box.configure(values=d.keys())
        # # Connecting it to a callback function to print the selected option on click event
        # self.combo_box.configure(command=self.combobox_callback)
        # self.combo_box.place(x=1300,y=600)
        self.l1 = CTkLabel(master=self.root,text="Rushikesh")
        self.l1.place(x=20,y=50)

    # def combobox_callback(self,choice):
    #     print("combobox dropdown clicked:", d.get(choice))


app = App()
app.geometry("800x800")
# app.attributes("-fullscreen", True)
>>>>>>> f6ad058038ff994e68179139f8be41e5415178a5
app.mainloop()