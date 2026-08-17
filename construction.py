from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox


# =================================================
# First  Page
# =================================================

def first_page():
    root = Tk()

    root.geometry("1500x1000")
    root.title("Dwivedi Construction")
    icon=PhotoImage(file="image16.png")
    root.iconphoto(True,icon)
    
    img=PhotoImage(file="image16.png")
    Label(root,image=img).place(x=200,y=10,width=50)
    
    image = Image.open("image14.jpg")
    image = image.resize((1500, 800))

    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.image = photo
    label.pack(fill="both", expand=True)


# =========================================
 # SMALL COMPANY LOGO
 # =========================================

    img = PhotoImage(file="image16.png")

    small_logo = img.subsample(8, 8)

    logo_label = Label(root, image=small_logo, bg="white")
    logo_label.image = small_logo

    logo_label.place(x=600, y=30)

    # =========================================
    open_button = Button( root, text="OPEN", font=("Arial", 20, "bold"), bg="orange", fg="white",  padx=20, pady=10,  command=lambda: main_page(root) )

    open_button.place(x=650, y=550)

    # =========================================
    # CLOSE BUTTON
    # =========================================

    close_button = Button( root, text="CLOSE",font=("Arial", 15, "bold"),bg="red", fg="white", padx=28,pady=10,command=root.destroy)

    close_button.place(x=650, y=650)
    
    root.mainloop()





# ==========================================
# IMAGE LOADER
# ==========================================

def load_image(path, size):

    img = Image.open(path)

    img = img.resize(size)

    return ImageTk.PhotoImage(img)


# ==========================================
# BACK FUNCTION
# ==========================================

def go_back(current, previous):

    current.destroy()

    previous.deiconify()


# ========================================================================================================
# APARTMENT WINDOWS
# ========================================================================================================

def apartment5(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="purple")

    win.title("Apartment 5")

    img = load_image("image21.png", (400, 250))

    lbl = Label(win, image=img, bg="purple")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue",fg="white",command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button(win,text="CLOSE",font=("Arial", 15, "bold"),bg="red",fg="white",command=win.destroy ).pack(side=RIGHT, padx=40, pady=30)


def apartment4(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="pink")

    win.title("Apartment 4")

    img = load_image("image20.png", (400, 250))

    lbl = Label(win, image=img, bg="pink")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda: apartment5(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)


def apartment3(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightblue")

    win.title("Apartment 3")

    img = load_image("image19.png", (400, 250))

    lbl = Label(win, image=img, bg="lightblue")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white", command=lambda: apartment4(win) ).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white",  command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)


def apartment2(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightgreen")

    win.title("Apartment 2")

    img = load_image("image18.png", (400, 250))

    lbl = Label(win, image=img, bg="lightgreen")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button( win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda: apartment3(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)


def apartment1(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightyellow")

    win.title("Apartment 1")

    img = load_image("image17.png", (400, 250))

    lbl = Label(win, image=img, bg="lightyellow")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda: apartment2(win)).pack(side=RIGHT, padx=40, pady=30)

    Button(win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)




#===================================================================================================================
                                                  #Smaple Designs\n of Row_Houses#
#===================================================================================================================


def Row_Houses5(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="purple")

    win.title("Row_Houses 5")

    img = load_image("image26.png", (650, 350))

    lbl = Label(win, image=img, bg="purple")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue",fg="white",command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button(win,text="CLOSE",font=("Arial", 15, "bold"),bg="red",fg="white",command=win.destroy ).pack(side=RIGHT, padx=40, pady=30)

   

def Row_Houses4(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="pink")

    win.title("Row_Houses 4")

    img = load_image("image25.png", (650, 350))

    lbl = Label(win, image=img, bg="pink")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda: Row_Houses5(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def Row_Houses3(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightblue")

    win.title("Row_Houses 3")

    img = load_image("image22.png", (650, 350))

    lbl = Label(win, image=img, bg="lightblue")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white", command=lambda: Row_Houses4(win) ).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white",  command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def Row_Houses2(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightgreen")

    win.title("Row_Houses 2")

    img = load_image("image24.png", (650, 350))

    lbl = Label(win, image=img, bg="lightgreen")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button( win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda: Row_Houses3(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def Row_Houses1(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightyellow")

    win.title("Row_Houses 1")

    img = load_image("image23.png", (650, 350))

    lbl = Label(win, image=img, bg="lightyellow")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda: Row_Houses2(win)).pack(side=RIGHT, padx=40, pady=30)
   
    Button(win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)
    
    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)
#====================================================================================================================================
                                                                                    #Smaple Designs\n of Villa#
#====================================================================================================================================


def  Villa5(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="purple")

    win.title(" Villa 5")

    img = load_image("image31.png", (650, 350))

    lbl = Label(win, image=img, bg="purple")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue",fg="white",command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button(win,text="CLOSE",font=("Arial", 15, "bold"),bg="red",fg="white",command=win.destroy ).pack(side=RIGHT, padx=40, pady=30)

   

def  Villa4(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="pink")

    win.title(" Villa 4")

    img = load_image("image30.png", (650, 350))

    lbl = Label(win, image=img, bg="pink")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda:  Villa5(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def  Villa3(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightblue")

    win.title(" Villa 3")

    img = load_image("image29.png", (650, 350))

    lbl = Label(win, image=img, bg="lightblue")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white", command=lambda:  Villa4(win) ).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white",  command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def  Villa2(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightgreen")

    win.title(" Villa 2")

    img = load_image("image28.png", (650, 350))

    lbl = Label(win, image=img, bg="lightgreen")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button( win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda:  Villa3(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def  Villa1(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightyellow")

    win.title(" Villa 1")

    img = load_image("image27.png", (650, 350))
    
 
    lbl = Label(win, image=img, bg="lightyellow")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda: Villa2(win)).pack(side=RIGHT, padx=40, pady=30)
   
    Button(win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)
    
    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

#===================================================================================================================================
                                                                                    #Hotal#
#===================================================================================================================================


def  Hotal5(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="purple")

    win.title(" Hotal 5")

    img = load_image("image36.png", (650, 350))

    lbl = Label(win, image=img, bg="purple")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue",fg="white",command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button(win,text="CLOSE",font=("Arial", 15, "bold"),bg="red",fg="white",command=win.destroy ).pack(side=RIGHT, padx=40, pady=30)

   

def  Hotal4(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="pink")

    win.title(" Hotal 4")

    img = load_image("image35.png", (650, 350))

    lbl = Label(win, image=img, bg="pink")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda:  Hotal5(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def  Hotal3(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightblue")

    win.title(" Hotal 3")

    img = load_image("image34.png", (650, 350))

    lbl = Label(win, image=img, bg="lightblue")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white", command=lambda:  Hotal4(win) ).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white",  command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def  Hotal2(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightgreen")

    win.title(" Hotal 2")

    img = load_image("image33.png", (650, 350))

    lbl = Label(win, image=img, bg="lightgreen")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button( win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda:  Hotal3(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def  Hotal1(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightyellow")

    win.title(" Hotal 1")

    img = load_image("image32.png", (650, 350))
    
 
    lbl = Label(win, image=img, bg="lightyellow")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda: Hotal2(win)).pack(side=RIGHT, padx=40, pady=30)
   
    Button(win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)
    
    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

#========================================================================================================================================
                                                                                        #Modern Homes#
#========================================================================================================================================


def   Homes5(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="purple")

    win.title("  Homes 5")

    img = load_image("image41.png", (650, 350))

    lbl = Label(win, image=img, bg="purple")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue",fg="white",command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button(win,text="CLOSE",font=("Arial", 15, "bold"),bg="red",fg="white",command=win.destroy ).pack(side=RIGHT, padx=40, pady=30)

   

def   Homes4(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="pink")

    win.title("  Homes 4")

    img = load_image("image40.png", (650, 350))

    lbl = Label(win, image=img, bg="pink")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda:   Homes5(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def   Homes3(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightblue")

    win.title("  Homes 3")

    img = load_image("image39.png", (650, 350))

    lbl = Label(win, image=img, bg="lightblue")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white", command=lambda:   Homes4(win) ).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white",  command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def   Homes2(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightgreen")

    win.title("  Homes 2")

    img = load_image("image38.png", (650, 350))

    lbl = Label(win, image=img, bg="lightgreen")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button( win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda:   Homes3(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def   Homes1(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightyellow")

    win.title("  Homes 1")

    img = load_image("image37.png", (650, 350))
    
 
    lbl = Label(win, image=img, bg="lightyellow")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda:  Homes2(win)).pack(side=RIGHT, padx=40, pady=30)
   
    Button(win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)
    
    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)


#===================================================================================================================================
                                                                                    #Office#
#===================================================================================================================================


def   Office5(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="purple")

    win.title("  Office 5")

    img = load_image("image46.png", (650, 350))

    lbl = Label(win, image=img, bg="purple")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue",fg="white",command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button(win,text="CLOSE",font=("Arial", 15, "bold"),bg="red",fg="white",command=win.destroy ).pack(side=RIGHT, padx=40, pady=30)

   

def   Office4(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="pink")

    win.title("  Office 4")

    img = load_image("image45.png", (650, 350))

    lbl = Label(win, image=img, bg="pink")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button( win, text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda:   Office5(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def  Office3(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightblue")

    win.title("  Office 3")

    img = load_image("image44.png", (650, 350))

    lbl = Label(win, image=img, bg="lightblue")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white", command=lambda:   Office4(win) ).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white",  command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def   Office2(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightgreen")

    win.title("  Office 2")

    img = load_image("image43.png", (650, 350))

    lbl = Label(win, image=img, bg="lightgreen")

    lbl.image = img

    lbl.pack(pady=20)

    

    Button( win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda:  Office3(win)).pack(side=RIGHT, padx=40, pady=30)

    Button( win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)

    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)

def   Office1(prev):

    prev.withdraw()

    win = Toplevel()

    win.geometry("700x500")

    win.configure(bg="lightyellow")

    win.title("  Office 1")

    img = load_image("image42.png", (650, 350))
    
 
    lbl = Label(win, image=img, bg="lightyellow")

    lbl.image = img

    lbl.pack(pady=20)

    
    Button(win,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",command=lambda:  Office2(win)).pack(side=RIGHT, padx=40, pady=30)
   
    Button(win, text="BACK", font=("Arial", 15, "bold"), bg="blue", fg="white", command=lambda: go_back(win, prev)).pack(side=LEFT, padx=40, pady=30)
    
    Button( win, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", command= win.destroy ).pack(side=LEFT, padx=150, pady=30)



# ================= DASHBOARD FUNCTION =================
def open_design(prev, title, image_path, next_func=None):

    prev.withdraw()

    win = Toplevel()

    win.geometry("800x600")

    win.title(title)

    win.configure(bg="white")

    # ================= IMAGE =================
    try:
        img = load_image(image_path, (650, 350))

        lbl = Label(win, image=img, bg="white")

        lbl.image = img

        lbl.pack(pady=30)

    except:
        Label( win, text="Image Not Found",fg="red",bg="white", font=("Arial", 20, "bold")).pack(pady=50)

    # ================= BUTTON FRAME =================
    btn_frame = Frame(win, bg="white")

    btn_frame.pack(pady=20)

    # NEXT BUTTON
    if next_func:Button(btn_frame,text="NEXT",font=("Arial", 15, "bold"),bg="orange",fg="white",padx=20,pady=10,command=lambda: next_func(win) ).pack(side=LEFT, padx=20)

    # BACK BUTTON
    Button( btn_frame,text="BACK",font=("Arial", 15, "bold"),bg="blue",fg="white",padx=20,pady=10,command=lambda: go_back(win, prev)).pack(side=LEFT, padx=20)

    # CLOSE BUTTON
    Button(btn_frame, text="CLOSE", font=("Arial", 15, "bold"), bg="red", fg="white", padx=20, pady=10, command=win.destroy).pack(side=LEFT, padx=20)


# ================================
# APARTMENTS
# ================================
def apartment5(prev):
    open_design(prev, "Apartment 5", "image21.png")


def apartment4(prev):
    open_design(prev, "Apartment 4", "image20.png", apartment5)


def apartment3(prev):
    open_design(prev, "Apartment 3", "image19.png", apartment4)


def apartment2(prev):
    open_design(prev, "Apartment 2", "image18.png", apartment3)


def apartment1(prev):
    open_design(prev, "Apartment 1", "image17.png", apartment2)


# ================================
# ROW HOUSES
# ================================
def row5(prev):
    open_design(prev, "Row House 5", "image26.png")


def row4(prev):
    open_design(prev, "Row House 4", "image25.png", row5)


def row3(prev):
    open_design(prev, "Row House 3", "image24.png", row4)


def row2(prev):
    open_design(prev, "Row House 2", "image23.png", row3)


def row1(prev):
    open_design(prev, "Row House 1", "image22.png", row2)


# ================================
# VILLAS
# ================================
def villa5(prev):
    open_design(prev, "Villa 5", "image31.png")


def villa4(prev):
    open_design(prev, "Villa 4", "image30.png", villa5)


def villa3(prev):
    open_design(prev, "Villa 3", "image29.png", villa4)


def villa2(prev):
    open_design(prev, "Villa 2", "image28.png", villa3)


def villa1(prev):
    open_design(prev, "Villa 1", "image27.png", villa2)


# ================================
# DASHBOARD
# ================================
def dashboard():

    dash = Toplevel()

    dash.geometry("1200x700")

    dash.title("Modern Dashboard")

    dash.config(bg="#f0f0f0")

    # ================= HEADER =================
    header = Frame(dash, bg="#1e3d59", height=70)

    header.pack(fill=X)

    Label(header,text="House Design Dashboard",bg="#1e3d59",fg="white",font=("Arial", 24, "bold")).pack(pady=15)

    # ================= SIDEBAR =================
    sidebar = Frame(dash, bg="#16324f", width=220)

    sidebar.pack(side=LEFT, fill=Y)

    Label(sidebar,text="MENU",bg="#16324f",fg="white",font=("Arial", 18, "bold") ).pack(pady=20)

    # ================= MAIN AREA =================
    main = Frame(dash, bg="white")

    main.pack(side=LEFT, fill=BOTH, expand=True)

    Label(main,text="Welcome to Dashboard",bg="white",fg="#1e3d59",font=("Arial", 24, "bold")).pack(pady=20)

    # ================= IMAGE =================
    try:
        img = Image.open("image40.png")

        img = img.resize((500, 300))

        photo = ImageTk.PhotoImage(img)

        lbl = Label(main, image=photo, bg="white")

        lbl.image = photo

        lbl.pack(pady=30)

    except:
        Label(main, text="Image Not Found", fg="red", bg="white", font=("Arial", 18)).pack()

    # ================= BUTTONS =================
    Button(sidebar,text="Apartments",width=18,height=2,bg="orange",fg="white",command=lambda: apartment1(dash)).pack(pady=10)

    Button(sidebar,text="Row Houses",width=18,height=2,bg="orange",fg="white", command=lambda: row1(dash)).pack(pady=10)

    Button(sidebar, text="Villas", width=18, height=2, bg="orange", fg="white", command=lambda: villa1(dash)).pack(pady=10)

    Button( sidebar, text="Close", width=18, height=2, bg="red", fg="white", command=dash.destroy).pack(pady=30)

    # ================= FOOTER =================
    footer = Frame(dash, bg="#1e3d59", height=40)

    footer.pack(fill=X, side=BOTTOM)

    Label(footer,text="Dwivedi Construction © 2026",bg="#1e3d59",fg="white").pack(pady=10)




# ================================
# MODERN OVERVIEW WINDOW
# ================================
def overview_window():

    overview = Toplevel()

    overview.geometry("1500x850")

    overview.title("Modern Overview Window")

    overview.configure(bg="#e6f2ff")

    # ================= HEADER =================
    header = Frame(overview,bg="#1e3d59",height=90)

    header.pack(fill=X)

    title = Label(  header,  text="DWIVEDI CONSTRUCTION",  font=("Arial Black", 28, "bold"),  bg="#1e3d59",  fg="white")

    title.pack(pady=20)

    # ================= SUB TITLE =================
    Label(overview,text="Modern Designs | Luxury Villas | Smart Apartments",font=("Arial", 18, "bold"),bg="#e6f2ff",fg="#16324f").pack(pady=20)

    # ================= MAIN FRAME =================
    main_frame = Frame(overview,bg="#e6f2ff" )

    main_frame.pack(pady=20)

    # =====================================================
    # APARTMENT CARD
    # =====================================================
    apartment_frame = Frame(main_frame,bg="white",bd=3,relief=RIDGE)

    apartment_frame.grid(row=0, column=0, padx=25)

    try:

        apartment_img = Image.open("image17.png")

        apartment_img = apartment_img.resize((320, 220))

        apartment_photo = ImageTk.PhotoImage(apartment_img)

        apartment_label = Label(apartment_frame,image=apartment_photo,bg="white" )

        apartment_label.image = apartment_photo

        apartment_label.pack(pady=10)

    except:

        Label(apartment_frame,text="Apartment Image Not Found",bg="white",fg="red",font=("Arial", 15, "bold") ).pack(pady=40)

    Label(apartment_frame,text="Luxury Apartments",font=("Arial", 18, "bold"),bg="white",fg="#1e3d59" ).pack(pady=10)

    Button(apartment_frame,text="OPEN",font=("Arial", 14, "bold"),bg="orange",fg="white",padx=20,pady=8,command=lambda: apartment1(overview)).pack(pady=15)

    # =====================================================
    # ROW HOUSE CARD
    # =====================================================
    row_frame = Frame(main_frame,bg="white",bd=3,relief=RIDGE )

    row_frame.grid(row=0, column=1, padx=25)

    try:

        row_img = Image.open("image23.png")

        row_img = row_img.resize((320, 220))

        row_photo = ImageTk.PhotoImage(row_img)

        row_label = Label(row_frame,image=row_photo,bg="white")

        row_label.image = row_photo

        row_label.pack(pady=10)

    except:

        Label(row_frame,text="Row House Image Not Found",bg="white",fg="red",font=("Arial", 15, "bold")).pack(pady=40)

    Label( row_frame, text="Modern Row Houses", font=("Arial", 18, "bold"), bg="white", fg="#1e3d59").pack(pady=10)

    Button( row_frame,text="OPEN",font=("Arial", 14, "bold"),bg="orange",fg="white",padx=20, pady=8, command=lambda: Row_Houses1(overview)).pack(pady=15)

    # =====================================================
    # VILLA CARD
    # =====================================================
    villa_frame = Frame(main_frame, bg="white", bd=3, relief=RIDGE )

    villa_frame.grid(row=0, column=2, padx=25)

    try:

        villa_img = Image.open("image27.png")

        villa_img = villa_img.resize((320, 220))

        villa_photo = ImageTk.PhotoImage(villa_img)

        villa_label = Label(villa_frame,image=villa_photo,bg="white" )

        villa_label.image = villa_photo

        villa_label.pack(pady=10)

    except:

        Label( villa_frame, text="Villa Image Not Found", bg="white", fg="red", font=("Arial", 15, "bold")).pack(pady=40)

    Label( villa_frame, text="Luxury Villas", font=("Arial", 18, "bold"), bg="white", fg="#1e3d59").pack(pady=10)

    Button(villa_frame,text="OPEN",font=("Arial", 14, "bold"),bg="orange",fg="white",padx=20,pady=8,command=lambda: Villa1(overview)).pack(pady=15)

    # ================= DESCRIPTION =================
    Label(overview,text="We create premium apartments, villas, row houses and modern commercial buildings.",font=("Arial", 17), bg="#e6f2ff", fg="#16324f").pack(pady=30)

    # ================= BOTTOM BUTTONS =================
    button_frame = Frame(overview, bg="#e6f2ff")

    button_frame.pack(pady=20)

    Button(button_frame,text="HOME",font=("Arial", 15, "bold"),bg="#1e3d59",fg="white",padx=25,pady=10).pack(side=LEFT, padx=20)

    Button(button_frame,text="CONTACT",font=("Arial", 15, "bold"),bg="green",fg="white",padx=25,pady=10).pack(side=LEFT, padx=20)

    Button(button_frame,text="CLOSE",font=("Arial", 15, "bold"),bg="red",fg="white",padx=25,pady=10,command=overview.destroy).pack(side=LEFT, padx=20)

# ================================
# latest_updates_window
# ================================
def latest_updates_window():

    win = Toplevel()
    win.title("Latest Construction Dashboard")
    win.geometry("1550x850")
    win.config(bg="#eef2f7")


    # ================= HEADER =================
    header = Frame(win, bg="white", height=70)
    header.pack(fill=X)

    Label(header,text="LATEST CONSTRUCTION UPDATES",bg="white",fg="#111827",font=("Segoe UI", 18, "bold")).place(x=260, y=18)

    Label(header,text="Real-time Monitoring Dashboard",bg="white",fg="gray",font=("Segoe UI", 9) ).place(x=265, y=45)


    
    Button(header,text="✖ Close",bg="#ef4444",fg="white",font=("Segoe UI", 10, "bold"),bd=0,padx=12,pady=5,cursor="hand2", command=win.destroy).place(x=1400, y=20)


    # ================= SIDEBAR =================
    sidebar = Frame(win, bg="#0f172a", width=240)
    sidebar.pack(side=LEFT, fill=Y)

    Label(sidebar,text="CONSTRUCTO",bg="#0f172a",fg="white",font=("Segoe UI", 16, "bold") ).pack(pady=25)

    menu = ["Dashboard", "Projects", "Workers", "Materials",
            "Expenses", "Reports", "Settings"]

    for item in menu:Button( sidebar, text=item, bg="#1f2937", fg="white", font=("Segoe UI", 10), bd=0, width=20, pady=6, activebackground="#2563eb").pack(pady=4)


    # ================= MAIN =================
    main = Frame(win, bg="#eef2f7")
    main.pack(fill=BOTH, expand=True)


    # ================= CARDS =================
    c1 = Frame(main, bg="white")
    c1.place(x=100, y=20, width=320, height=190)

    Label(c1, text="Project Status", bg="white", fg="#2563eb",font=("Segoe UI", 12, "bold")).pack(pady=8)

    ttk.Progressbar(c1, length=240, value=78).pack(pady=8)

    Label(c1, text="78% Completed", bg="white", fg="green", font=("Segoe UI", 9, "bold")).pack()


    c2 = Frame(main, bg="white")
    c2.place(x=450, y=20, width=320, height=190)

    Label(c2, text="Weather",bg="white", fg="#2563eb",font=("Segoe UI", 12, "bold")).pack(pady=8)

    Label(c2, text="☀ 31°C Sunny",bg="white", font=("Segoe UI", 10)).pack()


    c3 = Frame(main, bg="white")
    c3.place(x=840, y=20, width=320, height=190)

    Label(c3, text="Budget", bg="white", fg="#2563eb", font=("Segoe UI", 12, "bold")).pack(pady=8)

    Label(c3, text="₹50,00,000 Total",
          bg="white", font=("Segoe UI", 9)).pack()

    Label(c3, text="₹32,00,000 Used",
          bg="white", font=("Segoe UI", 9)).pack()

    Label(c3, text="₹18,00,000 Left",
          bg="white", fg="green",
          font=("Segoe UI", 9, "bold")).pack()


    # ================= NOTIFICATIONS =================
    notif = Frame(main, bg="white")
    notif.place(x=100, y=240, width=500, height=420)

    Label(notif, text="Notifications",
          bg="white", fg="#2563eb",
          font=("Segoe UI", 14, "bold")).pack(pady=10)

    for n in ["Site inspection tomorrow",
              "Cement stock updated",
              "New worker joined",
              "Payment received"]:
        Label(notif, text="• " + n,
              bg="white", font=("Segoe UI", 9),
              anchor="w").pack(fill=X, padx=15, pady=3)


    # ================= MATERIAL TABLE =================
    mat = Frame(main, bg="white")
    mat.place(x=680, y=240, width=600, height=420)

    Label(mat, text="Materials",
          bg="white", fg="#2563eb",
          font=("Segoe UI", 14, "bold")).pack(pady=10)

    tree = ttk.Treeview(mat, columns=("A", "B", "C"), show="headings", height=12)
    tree.heading("A", text="Item")
    tree.heading("B", text="Price")
    tree.heading("C", text="Status")

    tree.pack(pady=10)

    for i in [("Cement", "₹380", "OK"),
              ("Steel", "₹68", "Stable"),
              ("Bricks", "₹9", "Low")]:
        tree.insert("", END, values=i)


#=====================================================
# recent_projects_window
#====================================================

def recent_projects_window():
    win = Toplevel()
    win.title("Construction Dashboard - Recent Projects")
    win.geometry("1000x650")
    win.config(bg="#f4f6f8")

    # ================= HEADER =================
    header = Frame(win, bg="#1f3b4d", height=70)
    header.pack(fill=X)

    Label(header, text="RECENT PROJECTS",
          font=("Arial", 20, "bold"),
          bg="#1f3b4d", fg="white").pack(pady=18)

    # ================= SUMMARY CARDS =================
    summary_frame = Frame(win, bg="#f4f6f8")
    summary_frame.pack(fill=X, pady=10)

    def card(parent, text, color):
        f = Frame(parent, bg=color, width=200, height=80)
        f.pack(side=LEFT, padx=15, pady=5)
        f.pack_propagate(False)

        Label(f, text=text, bg=color, fg="white",
              font=("Arial", 12, "bold")).pack(expand=True)

    card(summary_frame, "Total Projects\n25", "#2d89ef")
    card(summary_frame, "Ongoing\n8", "#f39c12")
    card(summary_frame, "Completed\n15", "#27ae60")
    card(summary_frame, "Delayed\n2", "#e74c3c")

    # ================= SCROLL AREA =================
    container = Frame(win)
    container.pack(fill=BOTH, expand=True)

    canvas = Canvas(container, bg="#f4f6f8")
    scrollbar = Scrollbar(container, orient=VERTICAL, command=canvas.yview)
    scroll_frame = Frame(canvas, bg="#f4f6f8")

    scroll_frame.bind( "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    img = Image.open("image32.png")
    img = img.resize((380, 300))
    img_tk = ImageTk.PhotoImage(img)

    win.img_tk = img_tk
    img_label = Label(scroll_frame, image=img_tk, bg="white")
    img_label.pack(side=RIGHT,padx=80,pady=20)
     
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=X)

    # ================= PROJECT DETAILS WINDOW =================
    def open_details(name, location, status, budget, contractor, start, end, description):

        detail = Toplevel(win)
        detail.title("Project Details")
        detail.geometry("600x450")
        detail.config(bg="white")

        Label(detail, text="PROJECT DETAILS",
              font=("Arial", 18, "bold"),
              bg="white", fg="#1f3b4d").pack(pady=10)

        def add(text):
            Label(detail, text=text,
                  font=("Arial", 11),
                  bg="white", anchor="w", justify="left").pack(fill=X, padx=20, pady=2)

        add(f"Project Name: {name}")
        add(f"Location: {location}")
        add(f"Status: {status}")
        add(f"Budget: {budget}")
        add(f"Contractor: {contractor}")
        add(f"Start Date: {start}")
        add(f"End Date: {end}")

        Label(detail, text="Description:",
              font=("Arial", 12, "bold"),
              bg="white").pack(anchor="w", padx=20, pady=5)

        Label(detail, text=description,
              wraplength=250,
              justify="left",
              bg="white").pack(anchor="w", padx=20)

        Button(detail, text="Close",
               bg="#2c3e50", fg="white",
               command=detail.destroy).pack(pady=15)

    # ================= PROJECT CARD =================
    def project_card(parent, name, location, status, budget, contractor, start, end, desc):
        colors = {"Completed": "#27ae60","Ongoing": "#f39c12", "Delayed": "#e74c3c" }

        frame = Frame(parent, bg="white", bd=1, relief=SOLID)
        frame.pack(fill=X, padx=20, pady=10)

        Label(frame, text=name, font=("Arial", 14, "bold"),bg="white").pack(anchor="w", padx=10, pady=2)

        Label(frame, text=f"Location: {location}", bg="white").pack(anchor="w", padx=10)
        Label(frame, text=f"Budget: {budget}", bg="white").pack(anchor="w", padx=10)

        Label(frame, text=f"Status: {status}",fg=colors.get(status, "black"),bg="white",font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=2)

        Button(frame, text="View Details",bg="#3498db", fg="white",  cursor="hand2",
               command=lambda: open_details(name, location, status, budget,contractor, start, end, desc)).pack(anchor="e", padx=10, pady=5)

    # ================= SAMPLE DATA =================
    project_card(scroll_frame,
        "Skyline Residency Tower",
        "Pune",
        "Ongoing",
        "₹50 Cr",
        "ABC Constructions",
        "01-Jan-2025",
        "30-Dec-2026",
        "A modern high-rise residential project with luxury apartments, parking facility, and rooftop garden." )

    project_card( scroll_frame,
        "Green Valley Villas",
        "Mumbai",
        "Completed",
        "₹80 Cr",
        "XYZ Builders",
        "10-Mar-2023",
        "15-Apr-2025",
        "Luxury villa project with eco-friendly architecture and private gardens.")

    project_card( scroll_frame,
        "Metro City Mall",
        "Delhi",
        "Delayed",
        "₹120 Cr",
        "Urban Infra Ltd",
        "05-Jun-2024",
        "Expected 2026",
        "Large commercial mall project with multiplex, food court, and shopping complex.")

    # ================= CLOSE =================
    Button(win, text="Close Window",bg="#2c3e50", fg="white",font=("Arial", 12, "bold"),command=win.destroy).pack(pady=10)
    win.mainloop()

#===========================================================================================
#site_progress_window
#==========================================================================================

def site_progress_window():

    win = Toplevel()
    win.title("Site Progress Dashboard")
    win.geometry("1100x700")
    win.config(bg="#f4f6f8")

    # ================= MAIN FRAME =================
    main = Frame(win,)
    main.pack(fill=BOTH, expand=True)

    # ================= LEFT PANEL =================
    left = Frame(main, bg="red")
    left.place(x=5,y=10,width=750,height=700)

    # ================= RIGHT PANEL (IMAGE) =================
    right = Frame(main, bg="pink", width=300)
    right.place(x=760,y=10,width=350,height=700)

    # ================= HEADER =================
    Label(left, text="SITE PROGRESS DASHBOARD",font=("Arial", 20, "bold"),bg="#f4f6f8", fg="#1f3b4d").pack(pady=10)

    Label(left, text="Project: Skyline Residency Tower | Location: Pune",font=("Arial", 12), bg="#f4f6f8").pack()

    # ================= PROGRESS BAR =================
    progress_label = Label(left, text="Overall Progress: 65%", font=("Arial", 12, "bold"), bg="#f4f6f8", fg="#27ae60")
    progress_label.pack(pady=10)

    progress = ttk.Progressbar(left, length=600, mode='determinate')
    progress.pack()
    progress['value'] = 65

    # ================= PHASE BREAKDOWN =================
    phase_frame = Frame(left, bg="white")
    phase_frame.pack(pady=20, fill=X, padx=20)

    Label(phase_frame, text="PHASE COMPLETION",font=("Arial", 14, "bold"),bg="white").pack(pady=5)

    phases = {
        "Foundation": 100,
        "Structure": 80,
        "Masonry": 60,
        "Electrical": 40,
        "Plumbing": 50,
        "Finishing": 20
    }

    for k, v in phases.items():
        row = Frame(phase_frame, bg="white")
        row.pack(fill=X, padx=10, pady=3)

        Label(row, text=k, width=15, anchor="w", bg="white").pack(side=LEFT)

        bar = ttk.Progressbar(row, length=300, mode='determinate')
        bar.pack(side=LEFT, padx=10)
        bar['value'] = v

        Label(row, text=f"{v}%", bg="white").pack(side=LEFT)

    # ================= SITE INFO =================
    info = Frame(left, bg="#f4f6f8")
    info.pack(pady=15)

    Label(info, text="Workers: 120 | Engineers: 8 | Contractor: ABC Constructions",font=("Arial", 11), bg="#f4f6f8").pack()

    Label(info, text="Start Date: 01-Jan-2025 | Expected End: 30-Dec-2026",font=("Arial", 11), bg="#f4f6f8").pack()

    # ================= ALERT BOX =================
    alert = Frame(left, bg="#fff3cd", bd=2, relief=SOLID)
    alert.pack(fill=X, padx=20, pady=10)

    Label(alert, text="⚠ ALERTS",font=("Arial", 12, "bold"),bg="#fff3cd").pack(anchor="w", padx=10)

    Label(alert, text="• Minor delay in plumbing work\n• Weather disruption reported",bg="#fff3cd", justify="left").pack(anchor="w", padx=10)

    # ================= ACTION BUTTONS =================
    btn_frame = Frame(left, bg="#f4f6f8")
    btn_frame.pack(pady=10)

    Button(btn_frame, text="Update Progress",bg="#3498db", fg="white", width=18).pack(side=LEFT, padx=10)

    Button(btn_frame, text="Upload Report",bg="#27ae60", fg="white", width=18).pack(side=LEFT, padx=10)

    Button(btn_frame, text="Close",bg="#2c3e50", fg="white", width=18,command=win.destroy).pack(side=LEFT, padx=10)

    # ================= IMAGE PANEL =================
    try:
        img = Image.open("image40.png")
        img = img.resize((320, 250))
        img_tk = ImageTk.PhotoImage(img)

        win.img_tk = img_tk  
        Label(right, image=img_tk, bg="white").pack(pady=10)

    except:
        Label(right, text="No Image Found",bg="white", fg="red").pack(pady=20)

    Label(right, text="Site Progress View",bg="white", font=("Arial", 12, "bold")).pack()

#====================================================================================================
#testimonials_window
#====================================================================================================
def testimonials_window():

    win = Toplevel()
    win.title("Testimonials")
    win.geometry("800x500")   
    win.config(bg="#2c3e50")  
    testimonials = [
        ("Rahul Mehta",
         "Amazing construction quality and timely delivery.",
         "Client - Pune"),

        ("Anita Sharma",
         "Excellent project management and smooth execution.",
         "Client - Mumbai"),

        ("John Fernandes",
         "Highly satisfied with the villa construction.",
         "Client - Goa")
    ]

    index = [0]

    # ================= CARD =================
    card = Frame(win, bg="#75163F", bd=2, relief=SOLID)
    card.pack(pady=60, padx=40, fill=BOTH, expand=True)

    name_label = Label(card, font=("Arial", 16, "bold"), bg="#75163F",fg="white")
    name_label.pack(pady=10)

    text_label = Label(card, font=("Arial", 12),
                       bg="#75163F", wraplength=600, justify="center")
    text_label.pack(pady=20)

    role_label = Label(card, font=("Arial", 10, "italic"),
                       bg="#75163F", fg="gray")
    role_label.pack()

    def show(i):
        name, text, role = testimonials[i]
        name_label.config(text=name)
        text_label.config(text=f"“{text}”")
        role_label.config(text=role)

    show(0)

    # ================= BUTTONS =================
    btn_frame = Frame(win, bg="#2c3e50")
    btn_frame.pack(pady=10)

    def next_test():
        index[0] = (index[0] + 1) % len(testimonials)
        show(index[0])

    def prev_test():
        index[0] = (index[0] - 1) % len(testimonials)
        show(index[0])

    Button(btn_frame, text="⬅ Previous",
           bg="#3498db", fg="white",
           width=12, command=prev_test).pack(side=LEFT, padx=10)

    Button(btn_frame, text="Next ➡",
           bg="#27ae60", fg="white",
           width=12, command=next_test).pack(side=LEFT, padx=10)

    Button(btn_frame, text="Close",
           bg="#e74c3c", fg="white",
           width=12, command=win.destroy).pack(side=LEFT, padx=10)


# =====================================================
# QUALITY ASSURANCE WINDOW (MODERN STYLE)
# =====================================================
def quality_assurance_window():

    win = Toplevel()
    win.title("Quality Assurance")
    win.geometry("900x600")
    win.config(bg="#1e272e")   # 🌑 dark professional background

    # ================= HEADER =================
    header = Frame(win, bg="#0f172a", height=60)
    header.pack(fill=X)

    Label(header, text="QUALITY ASSURANCE DASHBOARD",
          font=("Arial", 18, "bold"),
          bg="#0f172a", fg="white").pack(pady=15)

    # ================= MAIN AREA =================
    main = Frame(win, bg="#1e272e")
    main.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # ================= LEFT PANEL =================
    left = Frame(main, bg="#1e272e")
    left.pack(side=LEFT, fill=BOTH, expand=True)

    # ================= RIGHT PANEL =================
    right = Frame(main, bg="#0f172a", width=300)
    right.pack(side=RIGHT, fill=Y)

    # ================= QA ITEMS =================
    Label(left, text="INSPECTION CHECKLIST",
          font=("Arial", 14, "bold"),
          bg="#1e272e", fg="white").pack(anchor="w")

    qa_items = [
        ("Foundation Strength", "PASS"),
        ("Concrete Quality", "PASS"),
        ("Steel Reinforcement", "FAIL"),
        ("Waterproofing", "PASS"),
        ("Electrical Safety", "PASS"),
        ("Plumbing Check", "FAIL"),
    ]

    def color(status):
        return "#2ecc71" if status == "PASS" else "#e74c3c"

    for item, status in qa_items:

        card = Frame(left, bg="#2c3e50", pady=8)
        card.pack(fill=X, pady=5)

        Label(card, text=item,
              font=("Arial", 12),
              bg="#2c3e50", fg="white").pack(side=LEFT, padx=10)

        Label(card, text=status,
              font=("Arial", 12, "bold"),
              bg="#2c3e50",
              fg=color(status)).pack(side=RIGHT, padx=10)

    # ================= SUMMARY PANEL =================
    Label(right, text="QA SUMMARY",
          font=("Arial", 14, "bold"),
          bg="#0f172a", fg="white").pack(pady=10)

    total = len(qa_items)
    passed = len([i for i in qa_items if i[1] == "PASS"])
    failed = total - passed

    def box(text, value, bg):
        f = Frame(right, bg=bg, width=200, height=80)
        f.pack(pady=10, padx=10, fill=X)
        f.pack_propagate(False)

        Label(f, text=text,
              bg=bg, fg="white",
              font=("Arial", 11, "bold")).pack()

        Label(f, text=value,
              bg=bg, fg="white",
              font=("Arial", 14, "bold")).pack()

    box("TOTAL CHECKS", total, "#2980b9")
    box("PASSED", passed, "#27ae60")
    box("FAILED", failed, "#e74c3c")

    # ================= BUTTONS =================
    Button(right, text="Run Full Inspection",
           bg="#f39c12", fg="white",
           font=("Arial", 10, "bold"),
           command=lambda: print("Running QA...")).pack(pady=20, fill=X, padx=10)

    Button(right, text="Close",
           bg="#c0392b", fg="white",
           command=win.destroy).pack(fill=X, padx=10)

# =====================================================
# COMPANY PROFILE WINDOW
# =====================================================
def company_profile_window():

    win = Toplevel()
    win.title("Company Profile")
    win.geometry("1000x650")
    win.config(bg="#f4f6f8")

    # ================= HEADER =================
    header = Frame(win, bg="#1f3b4d", height=70)
    header.pack(fill=X)

    Label(header, text="COMPANY PROFILE",
          font=("Arial", 20, "bold"),
          fg="white", bg="#1f3b4d").pack(pady=15)

    # ================= MAIN FRAME =================
    main = Frame(win, bg="#f4f6f8")
    main.pack(fill=BOTH, expand=True)

    # ================= LEFT SECTION =================
    left = Frame(main, bg="#f4f6f8")
    left.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)

    # ================= RIGHT SECTION =================
    right = Frame(main, bg="white", width=300)
    right.pack(side=RIGHT, fill=Y)

    # ================= COMPANY INFO =================
    Label(left, text="ABOUT COMPANY",
          font=("Arial", 14, "bold"),
          bg="#f4f6f8").pack(anchor="w")

    about_text = """
ABC Constructions is a leading construction company specializing in residential,
commercial, and infrastructure development projects.

We deliver high-quality, sustainable, and innovative construction solutions
with a strong focus on safety, design, and customer satisfaction.
"""

    Label(left, text=about_text,
          font=("Arial", 11),
          bg="#f4f6f8",
          justify="left",
          wraplength=600).pack(anchor="w", pady=10)

    # ================= STATS CARDS =================
    stats_frame = Frame(left, bg="#f4f6f8")
    stats_frame.pack(pady=20)

    def card(text, value, color):
        f = Frame(stats_frame, bg=color, width=150, height=80)
        f.pack(side=LEFT, padx=10)
        f.pack_propagate(False)

        Label(f, text=text,
              bg=color, fg="white",
              font=("Arial", 10, "bold")).pack(pady=5)

        Label(f, text=value,
              bg=color, fg="white",
              font=("Arial", 14, "bold")).pack()

    card("Projects", "120+", "#3498db")
    card("Clients", "85+", "#27ae60")
    card("Years", "15+", "#f39c12")
    card("Awards", "10+", "#e74c3c")

    # ================= RIGHT PROFILE PANEL =================
    Label(right, text="COMPANY DETAILS",
          font=("Arial", 14, "bold"),
          bg="white").pack(pady=10)

    details = [
        "CEO: Mr. Rajesh Sharma",
        "Head Office: Pune, India",
        "Founded: 2009",
        "Employees: 500+",
        "ISO Certified: Yes"
    ]

    for d in details:
        Label(right, text="• " + d,
              font=("Arial", 11),
              bg="white",
              anchor="w").pack(fill=X, padx=10, pady=5)

    # ================= BUTTONS =================
    Button(right, text="Edit Profile",bg="#2980b9", fg="white", font=("Arial", 10, "bold")).pack(pady=20, fill=X, padx=10)

    Button(right, text="Close", bg="#c0392b", fg="white", command=win.destroy).pack(fill=X, padx=10)



#==========================================================================================================================
                                                                                 # our_mission_window#
#==========================================================================================================================

def our_mission_window():

    win = Toplevel()
    win.title("Our Mission")
    win.geometry("950x620")
    win.configure(bg="#f3f0ff")   
    # ================= HEADER =================
    header = Frame(win, bg="#4b2e83", height=80)
    header.pack(fill=X)

    title = Label(header,text="OUR MISSION",font=("Georgia", 28, "bold"),bg="#4b2e83",fg="white" )
    title.pack(pady=18)

    # ================= MAIN FRAME =================
    main_frame = Frame(win, bg="#f3f0ff")
    main_frame.pack(fill=BOTH, expand=True, padx=25, pady=20)

    # ================= LEFT SECTION =================
    left_frame = Frame(main_frame,bg="#ffffff",bd=0,relief=RIDGE)
    left_frame.place(x=10, y=10, width=430, height=470)

    Label(left_frame,text="🏗 Our Vision",font=("Helvetica", 20, "bold"),bg="#ffffff",fg="#4b2e83").pack(anchor="w", padx=20, pady=18)

    vision_text = """
We aim to build modern, durable,
and sustainable infrastructure that
improves people's lives and supports
future generations.

Our mission is to deliver projects
with innovation, quality materials,
advanced technology, and complete
customer satisfaction.
"""

    Label(left_frame,text=vision_text, font=("Arial", 13), bg="#ffffff", fg="#333333", justify=LEFT, wraplength=370).pack(anchor="w", padx=20)

    # ================= RIGHT SECTION =================
    right_frame = Frame(main_frame,bg="#fff5e6",bd=0)
    right_frame.place(x=470, y=10, width=430, height=470)

    Label( right_frame,text="🎯 Our Goals",font=("Helvetica", 20, "bold"),bg="#fff5e6",fg="#d35400").pack(anchor="w", padx=20, pady=18)

    goals = [
        "✔ Deliver high-quality construction projects",
        "✔ Maintain safety standards at every site",
        "✔ Complete projects on time and within budget",
        "✔ Use eco-friendly and sustainable methods",
        "✔ Build long-term client relationships",
        "✔ Focus on innovation and modern designs"]

    for goal in goals:
        
        Label(right_frame,text=goal,font=("Arial", 12),bg="#fff5e6",fg="#444444",anchor="w",justify=LEFT).pack(anchor="w", padx=25, pady=10)

    # ================= FOOTER =================
    footer = Frame(win, bg="#4b2e83", height=60)
    footer.pack(side=BOTTOM, fill=X)

    Label(footer,text="Building Dreams • Creating Landmarks • Delivering Excellence",font=("Arial", 12, "italic"), bg="#4b2e83", fg="white").pack(side=LEFT, padx=20, pady=18)

    # ================= CLOSE BUTTON =================
    close_btn = Button( footer,  text="Close",  font=("Arial", 11, "bold"),  bg="#ff4d4d",  fg="white",
    activebackground="#cc0000",  activeforeground="white",  padx=18, pady=5,relief=FLAT,cursor="hand2",command=win.destroy)
    close_btn.pack(side=RIGHT, padx=20)


#====================================================================================================================
#OUR VISION
#====================================================================================================================

def  OUR_VISION_window():

    win = Toplevel()
    win.title("Our Mission")
    win.geometry("950x620")
    win.configure(bg="#edf6f9")

    # ================= HEADER =================
    header = Frame(win, bg="#003049", height=80)
    header.pack(fill=X)

    Label(header,text="OUR MISSION",font=("Georgia", 28, "bold"),bg="#003049",fg="white").pack(pady=18)

    # ================= MAIN FRAME =================
    main_frame = Frame(win, bg="#edf6f9")
    main_frame.pack(fill=BOTH, expand=True, padx=25, pady=20)

    # =====================================================
    #                 OUR VISION SECTION
    # =====================================================

    left_frame = Frame(main_frame,bg="#5f0f40",)
    left_frame.place(x=10, y=10, width=430, height=470)

    # ===== TOP DESIGN =====
    top_design = Frame( left_frame, bg="#ffbe0b",height=12)
    top_design.pack(fill=X)

    # ===== TITLE =====
    Label( left_frame,text="✦ OUR VISION ✦",font=("Lucida Calligraphy", 22, "bold"),bg="#5f0f40",fg="#ffbe0b" ).pack(pady=25)

    # ===== SUBTITLE =====
    Label(left_frame,text="Creating Future with Innovation",font=("Comic Sans MS", 13, "italic"),bg="#5f0f40",fg="#ffffff").pack()

    # ===== DECORATION LINE =====
    Frame(left_frame,bg="#ffbe0b",height=3,width=260).pack(pady=15)

    # ===== TEXT =====
    vision_text = """
        Our vision is to redefine construction
        through creativity, smart engineering,
        and sustainable development.

        We strive to build iconic structures
        that combine modern architecture,
          advanced technology, and long-lasting quality.
       Our goal is to inspire trust, deliver
       excellence, and shape a better future
       for communities worldwide.
"""

    Label( left_frame,text=vision_text,font=("Trebuchet MS", 11),  bg="#5f0f40",fg="#f8f9fa",justify=CENTER,wraplength=340,padx=20,pady=8).pack(anchor="w")

    # ===== BOTTOM BOX =====
    bottom_box = Frame(left_frame,bg="#3a0a2a",height=70)
    bottom_box.pack(side=BOTTOM, fill=X)

    Label( bottom_box, text="🏗 Engineering Excellence & Modern Design", font=("Verdana", 11, "bold"), bg="#3a0a2a", fg="#ffbe0b").pack(pady=22)

    # =====================================================
    #                 OUR GOALS SECTION
    # =====================================================

    right_frame = Frame(main_frame,bg="#ffffff" )
    right_frame.place(x=470, y=10, width=430, height=470)

    Label(right_frame,text="🎯 Our Goals",font=("Helvetica", 20, "bold"),bg="#ffffff",fg="#d62828").pack(anchor="w", padx=20, pady=18)

    goals = [
        "✔ Deliver world-class infrastructure",
        "✔ Ensure maximum safety at worksites",
        "✔ Complete projects within deadlines",
        "✔ Use sustainable construction methods",
        "✔ Focus on customer satisfaction",
        "✔ Bring innovation into every design"
    ]

    for goal in goals:
        Label(right_frame,text=goal,font=("Arial", 12),bg="#ffffff",fg="#444444",anchor="w",justify=LEFT).pack(anchor="w", padx=25, pady=10)

    # ================= FOOTER =================
    footer = Frame(win, bg="#003049", height=60)
    footer.pack(side=BOTTOM, fill=X)

    Label(footer,text="Building Dreams • Creating Excellence • Inspiring Future",font=("Arial", 12, "italic"),bg="#003049",fg="white").pack(side=LEFT, padx=20, pady=18)

    # ================= CLOSE BUTTON =================
    Button(footer,text="Close",font=("Arial", 11, "bold"),bg="#ef233c",fg="white",activebackground="#d90429",
    activeforeground="white",padx=18,pady=5,relief=FLAT,cursor="hand2",command=win.destroy ).pack(side=RIGHT, padx=20)



#===============================================================================================================
#our_team_window
#===============================================================================================================

def our_team_window():

    win = Toplevel()
    win.title("Our Team")
    win.geometry("1000x650")
    win.configure(bg="#edf2f4")

    # ================= HEADER =================
    header = Frame(win, bg="#14213d", height=80)
    header.pack(fill=X)

    Label(header,text="OUR TEAM",font=("Georgia", 30, "bold"),bg="#14213d",fg="white").pack(pady=18)

    # ================= MAIN FRAME =================
    main_frame = Frame(win, bg="#edf2f4")
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # ===================================================
    #                 TEAM MEMBER 1
    # ===================================================

    card1 = Frame(main_frame,bg="#ffffff",bd=0,relief=RIDGE)
    card1.place(x=20, y=20, width=280, height=420)

    Label(card1,text="👷",font=("Arial", 55),bg="#ffffff").pack(pady=10)

    Label(card1,text="Rahul Sharma",font=("Helvetica", 18, "bold"),bg="#ffffff",fg="#14213d").pack()

    Label(card1,text="Chief Architect",font=("Arial", 12, "italic"),bg="#ffffff",fg="#f77f00").pack(pady=5)

    about1 = """
Expert in modern architectural
designs and smart infrastructure
planning with 10+ years experience.
"""

    Label(card1,text=about1,font=("Calibri", 11),bg="#ffffff",fg="#444444",justify=CENTER,wraplength=220).pack(pady=15)

    Button(card1,text="View Profile",font=("Arial", 11, "bold"),bg="#14213d",fg="white",relief=FLAT,padx=12,pady=5,cursor="hand2" ).pack(pady=10)

    # ===================================================
    #                 TEAM MEMBER 2
    # ===================================================

    card2 = Frame( main_frame, bg="#fff1e6", bd=0)
    card2.place(x=360, y=20, width=280, height=420)

    Label(card2,text="👷‍♂️",font=("Arial", 55),bg="#fff1e6").pack(pady=10)

    Label(card2,text="Prachi Dwivedi",font=("Helvetica", 18, "bold"),bg="#fff1e6",fg="#9d0208").pack()

    Label(card2,text="Project Manager",font=("Arial", 12, "italic"),bg="#fff1e6",fg="#e85d04").pack(pady=5)

    about2 = """
Handles large-scale construction
projects with excellent management
and leadership skills.
"""

    Label(card2,text=about2,font=("Calibri", 11),bg="#fff1e6",fg="#444444",justify=CENTER,wraplength=220).pack(pady=15)

    Button( card2, text="View Profile", font=("Arial", 11, "bold"), bg="#9d0208", fg="white", relief=FLAT, padx=12, pady=5,cursor="hand2" ).pack(pady=10)

    # ===================================================
    #                 TEAM MEMBER 3
    # ===================================================

    card3 = Frame( main_frame, bg="#e0fbfc", bd=0)
    card3.place(x=700, y=20, width=280, height=420)

    Label(card3,text="👨‍💼",font=("Arial", 55),bg="#e0fbfc" ).pack(pady=10)

    Label(card3,text="Durga Kapoor",font=("Helvetica", 18, "bold"),bg="#e0fbfc",fg="#003049").pack()

    Label( card3, text="Site Engineer", font=("Arial", 12, "italic"), bg="#e0fbfc", fg="#0077b6").pack(pady=5)

    about3 = """
Responsible for site supervision,
quality assurance, and construction
safety operations.
"""

    Label( card3, text=about3, font=("Calibri", 11), bg="#e0fbfc", fg="#444444", justify=CENTER, wraplength=220 ).pack(pady=15)

    Button(card3,text="View Profile",font=("Arial", 11, "bold"),bg="#003049",fg="white",relief=FLAT,padx=12,pady=5,cursor="hand2").pack(pady=10)

    # ================= FOOTER =================

    footer = Frame(win, bg="#14213d", height=60)
    footer.pack(side=BOTTOM, fill=X)

    Label(footer,text="Professional Team • Smart Planning • Quality Construction",font=("Arial", 12, "italic"),bg="#14213d",fg="white").pack(side=LEFT, padx=20, pady=18)

    Button( footer, text="Close", font=("Arial", 11, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=18, pady=5, cursor="hand2",
    command=win.destroy ).pack(side=RIGHT, padx=20)



#================================================================================================================================
#why_choose_us
#================================================================================================================================

def why_choose_us_window():

    win = Toplevel()
    win.title("Why Choose Us")
    win.geometry("1000x650")
    win.configure(bg="#f4f7fb")

    # ================= HEADER =================
    header = Frame(win, bg="#0b2545", height=70)
    header.pack(fill=X)

    Label(header, text="WHY CHOOSE US", font=("Georgia", 24, "bold"), bg="#0b2545", fg="white").pack(pady=15)

    # ================= MAIN FRAME =================
    main_frame = Frame(win, bg="#f4f7fb")
    main_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

    # ======================================================
    #                  BOX 1
    # ======================================================

    box1 = Frame(main_frame, bg="#ffffff")
    box1.place(x=10, y=10, width=300, height=210)

    Label(box1, text="🏗", font=("Arial", 35),bg="#ffffff").pack(pady=5)

    Label( box1,text="Modern Designs",font=("Helvetica", 15, "bold"),bg="#ffffff",fg="#0b2545" ).pack()

    Label( box1,text="Creative and modern\narchitectural solutions\nwith smart planning.",font=("Calibri", 10),bg="#ffffff",fg="#444444",justify=CENTER).pack(pady=5)

    # ======================================================
    #                  BOX 2
    # ======================================================

    box2 = Frame(main_frame, bg="#e3f2fd")
    box2.place(x=340, y=10, width=300, height=210)

    Label(box2, text="⏳", font=("Arial", 35),bg="#e3f2fd").pack(pady=5)

    Label(box2,text="On-Time Delivery",font=("Helvetica", 15, "bold"),bg="#e3f2fd",fg="#1565c0").pack()

    Label(box2,text="Projects completed\nwithin deadlines while\nmaintaining quality.",font=("Calibri", 10),bg="#e3f2fd",fg="#333333",justify=CENTER).pack(pady=5)

    # ======================================================
    #                  BOX 3
    # ======================================================

    box3 = Frame(main_frame, bg="#fff3e0")
    box3.place(x=670, y=10, width=300, height=210)

    Label(box3, text="🛡", font=("Arial", 35),bg="#fff3e0").pack(pady=5)

    Label(box3,text="Quality Assurance",font=("Helvetica", 15, "bold"),bg="#fff3e0",fg="#ef6c00").pack()

    Label(box3,text="Premium materials and\nadvanced technology for\nsafe construction.",font=("Calibri", 10),bg="#fff3e0",fg="#444444",justify=CENTER).pack(pady=5)

    # ======================================================
    #                  BOX 4
    # ======================================================

    box4 = Frame(main_frame, bg="#e8f5e9")
    box4.place(x=10, y=250, width=300, height=210)

    Label(box4, text="👨‍💼", font=("Arial", 35),bg="#e8f5e9").pack(pady=5)

    Label( box4,text="Expert Team",font=("Helvetica", 15, "bold"),bg="#e8f5e9",fg="#2e7d32").pack()

    Label(box4,text="Experienced engineers\nand designers ensure\nexcellent execution.",font=("Calibri", 10),bg="#e8f5e9",fg="#444444",justify=CENTER).pack(pady=5)

    # ======================================================
    #                  BOX 5
    # ======================================================

    box5 = Frame(main_frame, bg="#f3e5f5")
    box5.place(x=340, y=250, width=300, height=210)

    Label(box5, text="💡", font=("Arial", 35),
          bg="#f3e5f5").pack(pady=5)

    Label(box5,text="Innovative Ideas",font=("Helvetica", 15, "bold"),bg="#f3e5f5",fg="#6a1b9a" ).pack()

    Label(box5,text="Smart technology and\ninnovative solutions for\nmodern infrastructure.",font=("Calibri", 10),bg="#f3e5f5",fg="#444444",justify=CENTER).pack(pady=5)

    # ======================================================
    #                  BOX 6
    # ======================================================

    box6 = Frame(main_frame, bg="#ffebee")
    box6.place(x=670, y=250, width=300, height=210)

    Label(box6, text="🤝", font=("Arial", 35),bg="#ffebee").pack(pady=5)

    Label(  box6,  text="Client Satisfaction",  font=("Helvetica", 15, "bold"),  bg="#ffebee",  fg="#c62828" ).pack()

    Label( box6, text="Trusted and transparent\nservices focused on\ncustomer satisfaction.", font=("Calibri", 10), bg="#ffebee", fg="#444444", justify=CENTER ).pack(pady=5)

    # ================= FOOTER =================

    footer = Frame(win, bg="#0b2545", height=55)
    footer.pack(side=BOTTOM, fill=X)

    Label( footer, text="Innovation • Quality • Trust • Excellence", font=("Arial", 11, "italic"), bg="#0b2545", fg="white").pack(side=LEFT, padx=20, pady=15)

    Button( footer, text="Close", font=("Arial", 10, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=15, pady=4, cursor="hand2", command=win.destroy ).pack(side=RIGHT, padx=20)


#=================================================================================================================================
#residential_construction
#==================================================================================================================================

def residential_construction_window():

    win = Toplevel()
    win.title("Residential Construction")
    win.geometry("1000x680")
    win.configure(bg="#f5f7fa")

    # ================= HEADER =================
    header = Frame(win, bg="#1b4332", height=80)
    header.pack(fill=X)

    Label(header, text="RESIDENTIAL CONSTRUCTION", font=("Georgia", 26, "bold"), bg="#1b4332", fg="white").pack(pady=18)

    # ================= MAIN FRAME =================
    main_frame = Frame(win, bg="#f5f7fa")
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # ======================================================
    #                 LEFT SECTION
    # ======================================================

    left_frame = Frame(main_frame, bg="#ffffff")
    left_frame.place(x=10, y=10, width=460, height=500)

    Label( left_frame, text="🏠 Modern Home Construction", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#1b4332").pack(pady=20)

    home_text = """
We specialize in designing and building
modern residential homes with high-quality
materials and smart infrastructure planning.

Our residential construction services include:

• Luxury Villas
• Duplex Houses
• Apartments & Flats
• Row Houses
• Smart Home Designs
• Interior & Exterior Planning

We ensure safety, durability, comfort,
and elegant architectural designs for
every residential project.
"""

    Label(left_frame,text=home_text,font=("Calibri", 12),bg="#ffffff",fg="#444444",justify=LEFT,wraplength=400).pack(padx=25, pady=10)

    # ======================================================
    #                 RIGHT SECTION
    # ======================================================

    right_frame = Frame(main_frame, bg="#d8f3dc")
    right_frame.place(x=500, y=10, width=460, height=500)

    Label( right_frame, text="✨ Key Features", font=("Helvetica", 20, "bold"), bg="#d8f3dc", fg="#2d6a4f").pack(pady=20)

    features = [
        "✔ Modern & Elegant House Designs",
        "✔ Earthquake Resistant Structures",
        "✔ Premium Quality Materials",
        "✔ Smart Space Utilization",
        "✔ Eco-Friendly Construction Methods",
        "✔ Affordable & Customizable Plans",
        "✔ Experienced Architects & Engineers",
        "✔ Timely Project Completion",
        "✔ Interior & Exterior Decoration",
        "✔ 24×7 Project Support & Guidance"
    ]

    for item in features:
        Label(right_frame,text=item,font=("Arial", 11),bg="#d8f3dc",fg="#1b4332",anchor="w" ).pack(anchor="w", padx=30, pady=7)

    # ======================================================
    #                 PROJECT DETAILS BUTTON
    # ======================================================

    def project_details():

        details = Toplevel()
        details.title("Residential Project Details")
        details.geometry("520x650")
        details.configure(bg="#ffffff")

        top = Frame(details, bg="#1b4332", height=70)
        top.pack(fill=X)

        Label(top, text="Residential Project Details", font=("Georgia", 22, "bold"), bg="#1b4332", fg="white").pack(pady=15)

        detail_text = """
🏡 Services Included

• Complete House Construction
• Architectural Planning & Design
• Interior Designing Solutions
• Modular Kitchen Setup
• Electrical & Plumbing Work
• Landscape & Garden Design

📌 Why Our Residential Projects?

• Strong and durable structures
• Modern and luxurious designs
• Affordable project packages
• Highly experienced construction team
• Use of advanced construction technology

📞 Contact Support

Phone : +91 98765 43210
Email : support@construction.com
        """

        Label( details, text=detail_text, font=("Calibri", 12), bg="#ffffff", fg="#333333", justify=LEFT, wraplength=450).pack(padx=25, pady=25)

        Button(details,text="Close",font=("Arial", 11, "bold"),bg="#e63946",fg="white",relief=FLAT,padx=18,pady=5,cursor="hand2",command=details.destroy).pack(pady=10)

    Button(win, text="View Project Details", font=("Arial", 12, "bold"), bg="#2d6a4f", fg="white", relief=FLAT, padx=20, pady=8, cursor="hand2",
    command=project_details ).place(x=390, y=575)

    # ================= FOOTER =================

    footer = Frame(win, bg="#1b4332", height=55)
    footer.pack(side=BOTTOM, fill=X)

    Label( footer, text="Modern Homes • Smart Living • Trusted Construction", font=("Arial", 11, "italic"),bg="#1b4332",fg="white" ).pack(side=LEFT, padx=20, pady=15)

    Button(footer, text="Close", font=("Arial", 10, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=15, pady=4, cursor="hand2",
    command=win.destroy ).pack(side=RIGHT, padx=20)



#=======================================================================================================================
# commercial_construction
#========================================================================================================================

def commercial_construction_window():

    win = Toplevel()
    win.title("Commercial Construction")
    win.geometry("1100x650")
    win.config(bg="#edf2f4")

    # ================= HEADER =================
    header = Frame(win, bg="#1f3b4d", height=70)
    header.pack(fill=X)

    Label(header,text="COMMERCIAL CONSTRUCTION PROJECTS",font=("Arial", 20, "bold"),bg="#1f3b4d",fg="white").pack(pady=18)

    # ================= MAIN FRAME =================
    main = Frame(win, bg="#edf2f4")
    main.pack(fill=BOTH, expand=True)

    # ================= LEFT SIDE =================
    left = Frame(main, bg="#edf2f4")
    left.pack(side=LEFT, fill=BOTH, expand=True)

    canvas = Canvas(left, bg="#edf2f4")
    scrollbar = Scrollbar(left, orient=VERTICAL, command=canvas.yview)

    scroll_frame = Frame(canvas, bg="#edf2f4")

    scroll_frame.bind( "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    
    img_refs = []

    # ================= DETAILS WINDOW =================
    def open_details(title, location, floors, budget, status, features):

        detail = Toplevel(win)
        detail.title("Commercial Project Details")
        detail.geometry("600x450")
        detail.config(bg="white")

        Label(detail,text="PROJECT DETAILS",font=("Arial", 18, "bold"),bg="white",fg="#1f3b4d").pack(pady=15)

        details = [
            f"Project Name : {title}",
            f"Location : {location}",
            f"Floors : {floors}",
            f"Budget : {budget}",
            f"Status : {status}",
        ]

        for d in details:
            Label(detail,text=d,bg="white",font=("Arial", 11),anchor="w").pack(fill=X, padx=20, pady=3)

        Label(detail, text="\nBuilding Features", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", padx=20)

        Label(detail,   text=features,   wraplength=540,   justify=LEFT,   bg="white",   font=("Arial", 10)).pack(anchor="w", padx=20)

        Button(detail,  text="Close",  bg="#2c3e50",  fg="white",  font=("Arial", 10, "bold"),  command=detail.destroy).pack(pady=15)

    # ================= PROJECT CARD =================
    def project_card(parent, title, location, floors,budget, status, features, image_path):

        frame = Frame(parent, bg="white", bd=1, relief=SOLID)
        frame.pack(fill=X, padx=20, pady=10)

        # LEFT INFO
        info = Frame(frame, bg="white")
        info.pack(side=LEFT, fill=BOTH, expand=True)

        Label(info,text=title,  font=("Arial", 15, "bold"),  bg="white").pack(anchor="w", padx=10, pady=3)

        Label(info, text=f"Location : {location}", bg="white").pack(anchor="w", padx=10)

        Label(info, text=f"Floors : {floors}", bg="white").pack(anchor="w", padx=10)

        Label(info, text=f"Budget : {budget}", bg="white").pack(anchor="w", padx=10)

        Label(info,  text=f"Status : {status}",  fg="#27ae60",  bg="white",  font=("Arial", 10, "bold")).pack(anchor="w", padx=10)

        Button(info,text="View Details",  bg="#3498db",  fg="white",  font=("Arial", 10, "bold"),
        command=lambda: open_details(  title, location, floors, budget, status, features )).pack(anchor="w", padx=10, pady=8)

        # RIGHT IMAGE
        try:
            img = Image.open(image_path)
            img = img.resize((220, 140))

            photo = ImageTk.PhotoImage(img)
            img_refs.append(photo)

            Label(frame, image=photo, bg="white").pack(side=RIGHT, padx=10, pady=10)

        except:
            Label(frame,  text="No Image",  bg="white").pack(side=RIGHT, padx=30)

    # ================= PROJECTS =================
    project_card( scroll_frame,
        "Skyline Corporate Tower",
        "Mumbai",
        "25 Floors",
        "₹250 Cr",
        "Completed",
        "Modern office tower with smart parking, conference halls, food court, and glass elevation.",
        "image30.png"
    )

    project_card(scroll_frame,
        "Metro Business Park",
        "Pune",
        "18 Floors",
        "₹180 Cr",
        "Ongoing",
        "Commercial IT park with eco-friendly design and advanced security systems.",
        "image57.png"
    )

    project_card(scroll_frame,
        "Royal Grand Hotel",
        "Delhi",
        "12 Floors",
        "₹300 Cr",
        "Completed",
        "Luxury hotel project including banquet halls, rooftop restaurant, and swimming pool.",
        "image36.png"
    )

    # ================= RIGHT PANEL =================
    right = Frame(main, bg="white", width=300)
    right.pack(side=RIGHT, fill=Y)

    Label(right,text="COMMERCIAL INSIGHTS", font=("Arial", 16, "bold"), bg="white", fg="#1f3b4d").pack(pady=15)

    def info_box(title, value, color):

        f = Frame(right, bg=color, height=70)
        f.pack(fill=X, padx=15, pady=8)

        Label(f, text=title, bg=color, fg="white", font=("Arial", 10, "bold")).pack(pady=5)

        Label(f, text=value, bg=color, fg="white", font=("Arial", 12, "bold")).pack()

    info_box("Total Projects", "32", "#3498db")
    info_box("Completed", "20", "#27ae60")
    info_box("Ongoing", "10", "#f39c12")
    info_box("Upcoming", "2", "#9b59b6")

    Label(right, text="\nTop Services", bg="white", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)

    Label(right,text="• Office Buildings\n"
               "• Shopping Malls\n"
               "• Hotels\n"
               "• IT Parks\n"
               "• Hospitals\n"
               "• Restaurants",
          justify=LEFT,
          bg="white",
          font=("Arial", 10)).pack(anchor="w", padx=25)

    # ================= CLOSE BUTTON =================
    Button(win,text="Close Window",bg="#2c3e50",fg="white",font=("Arial", 11, "bold"),command=win.destroy).pack(pady=10)


#=============================================================================================================================
# interior_design
#=============================================================================================================================

def interior_design_window():
    win = Toplevel()
    win.title("Interior Design")
    win.geometry("1000x650")
    win.configure(bg="#f8f5f2")

    # ================= HEADER =================
    header = Frame(win, bg="#6d4c41", height=80)
    header.pack(fill=X)

    Label( header, text="INTERIOR DESIGN", font=("Georgia", 28, "bold"), bg="#6d4c41", fg="white" ).pack(pady=18)

    # ================= MAIN FRAME =================
    main_frame = Frame(win, bg="#f8f5f2")
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # =====================================================
    #                 LEFT SECTION
    # =====================================================

    left_frame = Frame(main_frame, bg="#ffffff")
    left_frame.place(x=10, y=10, width=460, height=500)

    Label( left_frame, text="🛋 Modern Interior Solutions", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#6d4c41"  ).pack(pady=20)

    interior_text = """
We create elegant and modern
interior designs that enhance
comfort, beauty, and functionality.

Our interior design services include:

• Living Room Designs
• Bedroom Interior Setup
• Modular Kitchen Designs
• Office Interior Decoration
• False Ceiling & Lighting
• Furniture & Space Planning

We focus on luxury, creativity,
smart space utilization, and
customer satisfaction.
"""

    Label(left_frame, text=interior_text,  font=("Calibri", 12),bg="#ffffff",fg="#444444",   justify=LEFT,   wraplength=400 ).pack(padx=25, pady=10)

    # =====================================================
    #                 RIGHT SECTION
    # =====================================================

    right_frame = Frame(main_frame, bg="#ede0d4")
    right_frame.place(x=500, y=10, width=460, height=500)

    Label(  right_frame,  text="✨ Interior Features",  font=("Helvetica", 20, "bold"),  bg="#ede0d4",  fg="#5d4037" ).pack(pady=20)

    features = [
        "✔ Luxury & Modern Interior Designs",
        "✔ Premium Furniture & Decoration",
        "✔ Smart Lighting Solutions",
        "✔ Stylish False Ceiling Designs",
        "✔ Space Saving Concepts",
        "✔ Customized Color Themes",
        "✔ Elegant Wall & Floor Designs",
        "✔ Comfortable & Functional Layouts",
        "✔ Affordable Interior Packages",
        "✔ Professional Interior Experts"
    ]

    for item in features:
        Label( right_frame, text=item,  font=("Arial", 11),  bg="#ede0d4",fg="#5d4037", anchor="w"  ).pack(anchor="w", padx=30, pady=7)

    # =====================================================
    #                 DETAILS FUNCTION
    # =====================================================

    def design_details():

        details = Toplevel()
        details.title("Interior Design Details")
        details.geometry("520x450")
        details.configure(bg="#ffffff")

        top = Frame(details, bg="#6d4c41", height=70)
        top.pack(fill=X)

        Label( top, text="Interior Design Details", font=("Georgia", 22, "bold"), bg="#6d4c41", fg="white").pack(pady=15)

        detail_text = """
🏠 Interior Services

• Living Room Decoration
• Bedroom & Wardrobe Design
• Modular Kitchen Setup
• Office Interior Planning
• Lighting & Ceiling Work
• Wall Texture & Painting

📌 Why Choose Our Interior Design?

• Elegant and modern designs
• Smart and space-saving solutions
• Premium quality materials
• Customized decoration themes
• Experienced interior designers

📞 Contact Information

Phone : +91 98765 43210
Email : interior@construction.com
        """

        Label(details, text=detail_text, font=("Calibri", 12), bg="#ffffff", fg="#333333", justify=LEFT, wraplength=450).pack(padx=25, pady=25)

        Button(  details,  text="Close",  font=("Arial", 11, "bold"),  bg="#e63946",  fg="white",  relief=FLAT,  padx=18,  pady=5,  cursor="hand2",  command=details.destroy  ).pack(pady=10)

    # =====================================================
    #                 DETAILS BUTTON
    # =====================================================

    Button( win, text="View Design Details", font=("Arial", 12, "bold"), bg="#6d4c41", fg="white", relief=FLAT, padx=20, pady=8, cursor="hand2", command=design_details ).place(x=395, y=560)

    # ================= FOOTER =================

    footer = Frame(win, bg="#6d4c41", height=55)
    footer.pack(side=BOTTOM, fill=X)

    Label( footer, text="Luxury Interiors • Smart Spaces • Elegant Designs", font=("Arial", 11, "italic"), bg="#6d4c41", fg="white" ).pack(side=LEFT, padx=20, pady=15)

    Button( footer, text="Close", font=("Arial", 10, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=15, pady=4, cursor="hand2",
    command=win.destroy ).pack(side=RIGHT, padx=20)


    
#=============================================================================================================
#renovation_window
#=============================================================================================================

def renovation_window():

    win = Toplevel()
    win.title("Renovation Services")
    win.geometry("1000x650")
    win.configure(bg="#eef4ed")

    # ================= HEADER =================
    header = Frame(win, bg="#264653", height=85)
    header.pack(fill=X)

    Label( header,   text="RENOVATION SERVICES",   font=("Times New Roman", 30, "bold"),   bg="#264653",   fg="#ffffff" ).pack(pady=20)

    # ================= LEFT PANEL =================
    left_panel = Frame(win, bg="#2a9d8f")
    left_panel.place(x=5, y=110, width=350, height=470)

    Label( left_panel, text="🔨 Upgrade Your Space", font=("Georgia", 20, "bold"),bg="#2a9d8f",fg="white").pack(pady=25)

    renovation_text = """
Transform old spaces into modern,
stylish, and comfortable living areas.

We provide renovation solutions for:

• Homes & Apartments
• Villas & Bungalows
• Offices & Commercial Buildings
• Kitchens & Bathrooms
• Flooring & Ceiling Upgrades
• Exterior & Interior Remodeling

Our renovation experts focus on
quality, creativity, and durability.
"""

    Label( left_panel, text=renovation_text, font=("Calibri", 12), bg="#2a9d8f", fg="white", justify=LEFT, wraplength=250).pack(padx=20)

    # ================= RIGHT PANEL =================
    right_panel = Frame(win, bg="#ffffff")
    right_panel.place(x=350, y=110, width=620, height=470)

    Label( right_panel, text="✨ Renovation Highlights", font=("Helvetica", 22, "bold"), bg="#ffffff", fg="#264653" ).pack(pady=20)

    # ==================================================
    #                 FEATURE CARDS
    # ==================================================

    features = [
        ("🏠", "Modern Remodeling",
         "Stylish renovation with modern architecture and elegant designs."),

        ("🎨", "Interior Makeover",
         "Creative wall textures, lighting, and premium decoration themes."),

        ("🪟", "Space Optimization",
         "Smart utilization of available space for comfort and functionality."),

        ("🛠", "Durable Materials",
         "High-quality materials used for long-lasting renovation projects.")
    ]

    y_position = 80

    for icon, title, text in features:

        card = Frame(right_panel, bg="#f1faee", highlightbackground="#d9d9d9", highlightthickness=1)
        card.place(x=35, y=y_position, width=550, height=80)

        Label( card, text=icon, font=("Arial", 28), bg="#f1faee" ).place(x=15, y=15)

        Label(card,text=title,font=("Arial", 15, "bold"), bg="#f1faee", fg="#1d3557" ).place(x=80, y=12)

        Label( card,  text=text,  font=("Calibri", 10),  bg="#f1faee",  fg="#444444",  justify=LEFT).place(x=80, y=40)

        y_position += 95

    # ================= DETAILS FUNCTION =================

    def renovation_details():

        details = Toplevel()
        details.title("Renovation Details")
        details.geometry("520x600")
        details.configure(bg="#ffffff")

        top = Frame(details, bg="#264653", height=70)
        top.pack(fill=X)

        Label(  top,  text="Renovation Project Details",  font=("Georgia", 22, "bold"),  bg="#264653",  fg="white" ).pack(pady=15)

        detail_text = """
🏡 Renovation Services Include

• Complete Interior & Exterior Remodeling
• Kitchen & Bathroom Renovation
• Flooring & False Ceiling Upgrades
• Wall Painting & Decoration
• Smart Lighting Installation
• Furniture & Space Planning

📌 Benefits of Our Renovation

• Modern and elegant appearance
• Increased property value
• Better comfort and functionality
• Durable and high-quality finishing
• Affordable renovation packages

📞 Contact Support

Phone : +91 98765 43210
Email : renovate@construction.com
        """

        Label( details, text=detail_text, font=("Calibri", 12), bg="#ffffff", fg="#333333", justify=LEFT, wraplength=450  ).pack(padx=25, pady=25)

        Button( details, text="Close", font=("Arial", 11, "bold"), bg="#e63946", fg="white", relief=FLAT, padx=18, pady=5 ,cursor="hand2", command=details.destroy).place(x=200,y=530)

    # ================= BUTTON =================

    Button(win,text="View Renovation Details",font=("Arial", 12, "bold"),bg="#264653",fg="white",relief=FLAT,padx=20,pady=8,cursor="hand2",
    command=renovation_details ).place(x=490, y=558)

    # ================= FOOTER =================

    footer = Frame(win, bg="#264653", height=50)
    footer.pack(side=BOTTOM, fill=X)

    Label( footer, text="Modern Renovation • Elegant Spaces • Quality Transformation", font=("Arial", 11, "italic"), bg="#264653", fg="white" ).pack(side=LEFT, padx=20, pady=12)

    Button(footer, text="Close",font=("Arial", 10, "bold"),  bg="#ef233c",  fg="white",  relief=FLAT,  padx=15,  pady=4,  cursor="hand2",  command=win.destroy).pack(side=RIGHT, padx=20)
    


#=============================================================================================================================
#design3d_window
#=============================================================================================================================

def design3d_window():

    win = Toplevel()
    win.title("3D Design")
    win.geometry("1000x650")
    win.configure(bg="#edf6f9")

    # ================= HEADER =================
    header = Frame(win, bg="#023047", height=70)
    header.pack(fill=X)

    Label( header, text="3D DESIGN SERVICES", font=("Times New Roman", 26, "bold"), bg="#023047", fg="white" ).pack(pady=15)

    # ================= LEFT PANEL =================
    left_panel = Frame(win, bg="#219ebc")
    left_panel.place(x=10, y=90, width=320, height=500)

    Label(left_panel,  text="🏗 Smart 3D Visualization",  font=("Georgia", 18, "bold"),  bg="#219ebc",  fg="white").pack(pady=18)

    design_text = """
Experience realistic and modern
3D building visualization before
construction begins.

Our 3D design services include:

• 3D Exterior Designs
• 3D Interior Visualization
• House & Villa Modeling
• Commercial Building Designs
• Landscape 3D Planning
• Furniture & Lighting Layouts

We provide innovative and
high-quality 3D presentations
for better project understanding.
"""

    Label(  left_panel,  text=design_text,  font=("Calibri", 10),  bg="#219ebc",  fg="white",  justify=LEFT,  wraplength=250).pack(padx=18)

    # ================= RIGHT PANEL =================
    right_panel = Frame(win, bg="#ffffff")
    right_panel.place(x=335, y=90, width=645, height=500)

    Label( right_panel, text="✨ 3D Design Features", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#023047" ).pack(pady=15)

    # =====================================================
    #                 FEATURE CARDS
    # =====================================================

    features = [
        ("🏠", "Realistic Exterior Views",
         "Modern and realistic 3D exterior building designs."),

        ("🛋", "Interior Visualization",
         "Detailed room layouts with furniture and lighting."),

        ("🌳", "Landscape Planning",
         "Beautiful outdoor planning with gardens and pathways."),

        ("💻", "Advanced Technology",
         "High-quality 3D rendering using modern software.")
    ]

    y_position = 70

    for icon, title, text in features:

        card = Frame(   right_panel,   bg="#f1f5f9",   highlightbackground="#cfd8dc",   highlightthickness=1 )
        card.place(x=30, y=y_position, width=580, height=78)

        Label(  card, text=icon, font=("Arial", 24), bg="#f1f5f9" ).place(x=10, y=15)

        Label(card, text=title, font=("Arial", 13, "bold"), bg="#f1f5f9", fg="#023047").place(x=70, y=12)

        Label( card, text=text, font=("Calibri", 9), bg="#f1f5f9", fg="#444444", justify=LEFT ).place(x=70, y=42)

        y_position += 92

    # ================= DETAILS FUNCTION =================

    def design_details():

        details = Toplevel()
        details.title("3D Design Details")
        details.geometry("500x550")
        details.configure(bg="#ffffff")

        top = Frame(details, bg="#023047", height=65)
        top.pack(fill=X)

        Label( top, text="3D Design Details", font=("Georgia", 20, "bold"), bg="#023047", fg="white" ).pack(pady=12)

        detail_text = """
🏗 3D Design Services

• Exterior & Interior 3D Modeling
• House & Villa Visualization
• Office & Commercial Layouts
• Landscape & Garden Planning
• Furniture & Lighting Placement

📌 Benefits

• Better project visualization
• Realistic modern presentation
• Easy design modifications
• Smart planning before construction

📞 Contact Information

Phone : +91 98765 43210
Email : design3d@construction.com
        """

        Label(details,  text=detail_text,  font=("Calibri", 11),  bg="#ffffff",  fg="#333333",  justify=LEFT,  wraplength=420 ).pack(padx=20, pady=20)

        Button(  details,  text="Close",  font=("Arial", 10, "bold"),  bg="#e63946",  fg="white",  relief=FLAT,  padx=15,  pady=4,  cursor="hand2",  command=details.destroy  ).pack(pady=10)

    # ================= BUTTON =================

    Button( win, text="View 3D Design Details", font=("Arial", 20, "bold"),    bg="#023047",    fg="white",    relief=FLAT,    padx=18,    pady=6,  cursor="hand2",
    command=design_details).place(x=410, y=520)

    # ================= FOOTER =================

    footer = Frame(win, bg="#023047", height=45)
    footer.pack(side=BOTTOM, fill=X)

    Label( footer, text="Creative Visualization • Smart Planning • Modern 3D Designs", font=("Arial", 10, "italic"), bg="#023047", fg="white").pack(side=LEFT, padx=15, pady=10)

    Button(  footer,  text="Close", font=("Arial", 9, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=12, pady=3, cursor="hand2", command=win.destroy ).pack(side=RIGHT, padx=15)



#=======================================================================================================
#project_management
#=========================================================================================================

def project_management_window():

    win = Toplevel()
    win.title("Project Management")
    win.geometry("1000x650")
    win.configure(bg="#fff8f0")

    # ================= HEADER =================
    header = Frame(win, bg="#6a040f", height=75)
    header.pack(fill=X)

    Label(header, text="PROJECT MANAGEMENT", font=("Georgia", 28, "bold"), bg="#6a040f", fg="white").pack(pady=18)

    # ================= LEFT SIDE =================
    left_frame = Frame(win, bg="#ffba08")
    left_frame.place(x=10, y=100, width=300, height=480)

    Label( left_frame, text="📊 Management Overview", font=("Helvetica", 18, "bold"), bg="#ffba08", fg="#370617").pack(pady=20)

    overview_text = """
Efficient project management
ensures smooth workflow,
quality control, and timely
project completion.

Our experts manage planning,
resources, budgeting, safety,
and communication throughout
the construction process.

We focus on productivity,
coordination, and successful
execution of every project.
"""

    Label( left_frame, text=overview_text, font=("Calibri", 11), bg="#ffba08", fg="#370617", justify=LEFT, wraplength=230 ).pack(padx=18)

    # ================= RIGHT SIDE =================
    right_frame = Frame(win, bg="#ffffff")
    right_frame.place(x=330, y=100, width=650, height=480)

    Label( right_frame, text="🚀 Core Management Services", font=("Helvetica", 22, "bold"), bg="#ffffff", fg="#6a040f").pack(pady=15)

    # ===================================================
    #                 SERVICE BOXES
    # ===================================================

    services = [
        ("📅 Planning & Scheduling",
         "Smart scheduling and workflow planning for timely execution.",
         "#ffe5ec"),

        ("💰 Budget Management",
         "Cost estimation and financial monitoring for every project.",
         "#e9f5db"),

        ("👷 Team Coordination",
         "Smooth communication between engineers, workers, and clients.",
         "#d9edff"),

        ("🛡 Quality & Safety",
         "Regular inspections and safety monitoring at construction sites.",
         "#fff1c1")
    ]

    x_pos = 30
    y_pos = 80

    for title, desc, color in services:

        box = Frame(  right_frame, bg=color, highlightbackground="#d0d0d0", highlightthickness=1 )
        box.place(x=x_pos, y=y_pos, width=270, height=140)

        Label( box, text=title, font=("Arial", 13, "bold"), bg=color, fg="#370617" ).pack(pady=12)

        Label(box,  text=desc,  font=("Calibri", 10),  bg=color,  fg="#333333",  justify=CENTER,  wraplength=220).pack(padx=10)

        # Position adjustment
        if x_pos == 30:
            x_pos = 340
        else:
            x_pos = 30
            y_pos += 170

    # ================= DETAILS FUNCTION =================

    def management_details():

        details = Toplevel()
        details.title("Management Details")
        details.geometry("520x550")
        details.configure(bg="#fffaf3")

        top = Frame(details, bg="#6a040f", height=65)
        top.pack(fill=X)

        Label( top, text="Project Management Details", font=("Georgia", 21, "bold"), bg="#6a040f", fg="white").pack(pady=12)

        detail_text = """
📋 Our Management Services

• Project Planning & Scheduling
• Resource & Workforce Management
• Budget & Cost Monitoring
• Site Supervision & Reporting
• Safety & Quality Assurance

✨ Advantages

• Timely project completion
• Better communication system
• Reduced project risks
• High productivity and efficiency
• Professional workflow management

📞 Contact Information

Phone : +91 98765 43210
Email : project@construction.com
        """

        Label(details,text=detail_text,font=("Calibri", 11),bg="#fffaf3",fg="#333333", justify=LEFT, wraplength=440 ).pack(padx=20, pady=20)

        Button(  details,  text="Close",font=("Arial", 10, "bold"),bg="#d62828",fg="white",relief=FLAT,padx=15,pady=4,cursor="hand2",command=details.destroy ).pack(pady=10)

    # ================= BUTTON =================

    Button( win, text="View Full Details", font=("Arial", 12, "bold"), bg="#6a040f", fg="white", relief=FLAT, padx=20, pady=7, cursor="hand2", command=management_details).place(x=480, y=538)

    # ================= FOOTER =================

    footer = Frame(win, bg="#6a040f", height=45)
    footer.pack(side=BOTTOM, fill=X)

    Label(footer, text="Planning • Coordination • Quality • Success", font=("Arial", 10, "italic"), bg="#6a040f", fg="white").pack(side=LEFT, padx=15, pady=10)

    Button( footer, text="Close", font=("Arial", 9, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=12, pady=3, cursor="hand2",
    command=win.destroy ).pack(side=RIGHT, padx=15)



#=============================================================================================================
#our_clients
#==============================================================================================================

def our_clients_window():

    win = Toplevel()
    win.title("Our Clients")
    win.geometry("1000x650")
    win.configure(bg="#0f172a")

    # =====================================================
    #                 VIEW PROFILE FUNCTION
    # =====================================================

    def view_profile(name, project, details, color):

        profile = Toplevel()
        profile.title(name)
        profile.geometry("550x450")
        profile.configure(bg="#f8f9fa")

        # ================= LEFT SIDE =================
        side = Frame(profile, bg=color, width=180)
        side.pack(side=LEFT, fill=Y)

        Label( side, text="CLIENT\nPROFILE", font=("Georgia", 20, "bold"), bg=color, fg="white", justify=CENTER ).place(x=10, y=40)

        Label( side, text="✔ Trusted\nPartner", font=("Arial", 10, "bold"), bg=color, fg="#ffe066", justify=CENTER ).place(x=22, y=180)

        # ================= MAIN CONTENT =================
        content = Frame(profile, bg="#f8f9fa")
        content.pack(fill=BOTH, expand=True)

        Label( content, text=name, font=("Helvetica", 22, "bold"), bg="#f8f9fa", fg="#1d3557" ).pack(pady=(30, 5))

        Label(  content,  text=project,  font=("Arial", 10, "italic"),  bg="#f8f9fa",  fg="#e76f51" ).pack()

        Frame(content,  bg=color,  height=3,  width=320 ).pack(pady=15)

        details_box = Frame( content, bg="white", highlightbackground="#d9d9d9",  highlightthickness=1)
        details_box.pack(padx=25, pady=10, fill=BOTH, expand=True)

        Label( details_box, text=details, font=("Calibri", 10), bg="white", fg="#444444", justify=LEFT, wraplength=340).pack(padx=20, pady=20)

        # ================= BUTTONS =================
        btn_frame = Frame(content, bg="#f8f9fa")
        btn_frame.pack(pady=10)

        Button(btn_frame,text="Contact",font=("Arial", 9, "bold"), bg="#2a9d8f", fg="white", relief=FLAT, padx=15, pady=4, cursor="hand2").pack(side=LEFT, padx=10)

        Button( btn_frame, text="Close", font=("Arial", 9, "bold"), bg="#e63946", fg="white", relief=FLAT, padx=15, pady=4, cursor="hand2", command=profile.destroy ).pack(side=LEFT, padx=10)

    # ================= HEADER =================
    header = Frame(win, bg="#111827", height=70)
    header.pack(fill=X)

    Label( header, text="OUR VALUABLE CLIENTS", font=("Georgia", 22, "bold"), bg="#111827", fg="#f8fafc" ).pack(pady=18)

    # ================= TAGLINE =================
    Label(win,text="Building Strong Relationships Through Quality & Trust",font=("Arial", 10, "italic"),bg="#0f172a",fg="#cbd5e1").place(x=320, y=82)

    # =====================================================
    #                 CLIENT PANELS
    # =====================================================

    clients = [

        (
            "🏢",
            "Skyline Group",
            "#1e293b",
            "Commercial Infrastructure Experts",

            """
• 80+ successful commercial projects
• Smart city development specialists
• Advanced office infrastructure

📞 Contact:
skyline@company.com
+91 98765 43210
            """
        ),

        (
            "🏠",
            "Dream Homes",
            "#14213d",
            "Luxury Residential Projects",

            """
• Premium villa construction experts
• Modern bungalow designs
• High-quality residential interiors

📞 Contact:
dreamhomes@company.com
+91 98765 12345
            """
        ),

        (
            "🏨",
            "Royal Hotels",
            "#283618",
            "Premium Hotel Construction",

            """
• Luxury hotel construction services
• Elegant room interior solutions
• Professional renovation experts

📞 Contact:
royal@company.com
+91 98765 67890
            """
        ),

        (
            "🏬",
            "Urban Builders",
            "#3c096c",
            "Modern Shopping Complexes",

            """
• Modern shopping mall development
• Commercial architecture specialists
• Smart infrastructure planning

📞 Contact:
urban@company.com
+91 98765 56789
            """
        )
    ]

    y_position = 120

    for icon, name, color, desc, details in clients:

        panel = Frame(win,bg=color,highlightbackground="#94a3b8",highlightthickness=1)
        panel.place(x=70, y=y_position, width=850, height=85)

        # ================= ICON =================
        Label( panel, text=icon, font=("Arial", 28), bg=color, fg="white" ).place(x=20, y=18)

        # ================= CLIENT NAME =================
        Label( panel, text=name, font=("Helvetica", 15, "bold"), bg=color, fg="#f8fafc").place(x=90, y=15)

        # ================= DESCRIPTION =================
        Label( panel, text=desc, font=("Calibri", 8), bg=color, fg="#d1d5db").place(x=92, y=45)

        # ================= STATUS =================
        Label(panel,text="✔ Trusted Partner",font=("Arial", 8, "bold"),bg=color,fg="#38b000").place(x=560, y=18)

        # ================= BUTTON =================
        Button( panel, text="View Profile", font=("Arial", 8, "bold"), bg="#f59e0b", fg="black", relief=FLAT, padx=10, pady=3, cursor="hand2",
         command=lambda n=name, d=details, c=color, p=desc:view_profile(n, p, d, c) ).place(x=650, y=42)

        y_position += 100

    # =====================================================
    #                 BOTTOM STATS SECTION
    # =====================================================

    stats_frame = Frame(win, bg="#111827")
    stats_frame.place(x=70, y=535, width=850, height=55)

    stats = [
        ("250+", "Projects"),
        ("120+", "Clients"),
        ("15+", "Experience"),
        ("98%", "Satisfaction")
    ]

    x_pos = 40

    for number, text in stats:

        Label( stats_frame, text=number, font=("Arial", 16, "bold"), bg="#111827", fg="#fbbf24"  ).place(x=x_pos, y=5)

        Label( stats_frame, text=text, font=("Calibri", 8), bg="#111827", fg="white" ).place(x=x_pos, y=32)

        x_pos += 190

    # ================= CLOSE BUTTON =================

    Button( win, text="Close Window", font=("Arial", 8, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=12, pady=3, cursor="hand2",
    command=win.destroy ).place(x=825, y=605)



#===================================================================================================================
#ongoing_projects
#===================================================================================================================

def ongoing_projects_window():

    win = Toplevel()
    win.title("Ongoing Projects")
    win.geometry("1000x700")
    win.configure(bg="#eef2f7")

    # ================= HEADER =================
    header = Frame(win, bg="#1b263b", height=75)
    header.pack(fill=X)

    Label( header, text="ONGOING PROJECTS", font=("Georgia", 28, "bold"), bg="#1b263b", fg="white" ).pack(pady=16)

    # ================= SUBTITLE =================
    Label(  win,  text="Current Construction Projects Under Development",  font=("Arial", 11, "italic"),  bg="#eef2f7",  fg="#555555").place(x=330, y=88)

    # =====================================================
    #            PROJECT STATUS WINDOW WITH IMAGES
    # =====================================================

    def show_project_status(project_name):

        status = Toplevel()
        status.title(project_name + " Status")
        status.geometry("720x580")
        status.configure(bg="#ffffff")

        # ================= HEADER =================
        top = Frame(status, bg="#1b263b", height=70)
        top.pack(fill=X)

        Label( top, text=project_name + " - Project Status", font=("Georgia", 22, "bold"), bg="#1b263b", fg="white" ).pack(pady=18)

        # ================= IMAGE FRAME =================
        image_frame = Frame(status, bg="#ffffff")
        image_frame.pack(pady=20)

        # =====================================================
        # Replace image names with your own images
        # =====================================================

        img1 = Image.open("image40.png")
        img1 = img1.resize((190, 130))
        img1 = ImageTk.PhotoImage(img1)
      

        img2 = Image.open("image42.png")
        img2 = img2.resize((190, 130))
        img2 = ImageTk.PhotoImage(img2)

        img3 = Image.open("image43.png")
        img3 = img3.resize((190, 130))
        img3 = ImageTk.PhotoImage(img3)

        


        # ================= IMAGE LABELS =================

        lbl1 = Label(image_frame, image=img1, bg="#ffffff")
        lbl1.image = img1
        lbl1.grid(row=0, column=0, padx=10)

        lbl2 = Label(image_frame, image=img2, bg="#ffffff")
        lbl2.image = img2
        lbl2.grid(row=0, column=1, padx=10)

        lbl3 = Label(image_frame, image=img3, bg="#ffffff")
        lbl3.image = img3
        lbl3.grid(row=0, column=2, padx=10)

        # ================= PROJECT DETAILS =================

        status_text = """
🏗 Construction Progress Report

• Foundation and structural work completed
• Interior decoration currently ongoing
• Electrical and safety installations active
• Exterior finishing work started

📅 Estimated Completion :
December 2026

👷 Overall Progress :
75% Completed
        """

        Label(status,text=status_text,font=("Calibri", 11),bg="#ffffff",fg="#333333",justify=LEFT ).pack(pady=15)

        # ================= BUTTONS =================

        btn_frame = Frame(status, bg="#ffffff")
        btn_frame.pack(pady=2)

        Button( btn_frame, text="Refresh Status", font=("Arial", 9, "bold"), bg="#2a9d8f", fg="white", relief=FLAT, padx=15,pady=4,cursor="hand2" ).pack(side=LEFT, padx=10)

        Button( btn_frame, text="Close", font=("Arial", 9, "bold"), bg="#e63946",
            fg="white", relief=FLAT, padx=15, pady=4, cursor="hand2", command=status.destroy ).pack(side=LEFT, padx=10)

    # =====================================================
    #                 PROJECT DETAILS FUNCTION
    # =====================================================

    def project_details(name, details, color):

        detail = Toplevel()
        detail.title(name)
        detail.geometry("520x430")
        detail.configure(bg="#ffffff")

        # ================= TOP BAR =================
        top = Frame(detail, bg=color, height=70)
        top.pack(fill=X)

        Label( top, text=name, font=("Georgia", 22, "bold"), bg=color, fg="white" ).pack(pady=18)

        # ================= CONTENT =================
        info = Frame(detail, bg="#ffffff")
        info.pack(fill=BOTH, expand=True, padx=20, pady=20)

        Label( info, text=details, font=("Calibri", 11), bg="#ffffff", fg="#333333", justify=LEFT, wraplength=430 ).pack(pady=10)

        # ================= BUTTONS =================
        btn_frame = Frame(detail, bg="#ffffff")
        btn_frame.pack(pady=10)

        Button( btn_frame, text="Project Status", font=("Arial", 9, "bold"), bg="#2a9d8f", fg="white", relief=FLAT, padx=14, pady=4, cursor="hand2",
         command=lambda: show_project_status(name)).pack(side=LEFT, padx=10)

        Button( btn_frame, text="Close", font=("Arial", 9, "bold"), bg="#e63946", fg="white", relief=FLAT, padx=14, pady=4, cursor="hand2", command=detail.destroy ).pack(side=LEFT, padx=10)

    # =====================================================
    #                 PROJECT CARDS
    # =====================================================

    projects = [

        (
            "🏢",
            "Skyline Tower",
            "#d8f3dc",
            "#2d6a4f",
            "Commercial Office Project",

            """
📍 Location : Mumbai

• 25-floor commercial office tower
• Smart parking and modern design
• Advanced security systems

📅 Completion : December 2026
👷 Progress : 70% Completed
            """
        ),

        (
            "🏠",
            "Green Villa Homes",
            "#ffe5ec",
            "#c9184a",
            "Luxury Residential Villas",

            """
📍 Location : Pune

• Premium luxury villa project
• Eco-friendly infrastructure
• Modern interior architecture

📅 Completion : March 2027
👷 Progress : 55% Completed
            """
        ),

        (
            "🏨",
            "Royal Palace Hotel",
            "#e0fbfc",
            "#0077b6",
            "5-Star Hotel Construction",

            """
📍 Location : Delhi

• Luxury hotel with 120 rooms
• Rooftop restaurant and pool
• Modern hospitality infrastructure

📅 Completion : August 2026
👷 Progress : 80% Completed
            """
        ),

        (
            "🏬",
            "Urban Shopping Mall",
            "#fff3bf",
            "#f77f00",
            "Modern Shopping Complex",

            """
📍 Location : Bangalore

• Large-scale shopping mall project
• Smart energy management system
• Premium entertainment zone

📅 Completion : January 2027
👷 Progress : 60% Completed
            """
        )
    ]

    x_pos = 45
    y_pos = 130

    for icon, name, bg_color, title_color, desc, details in projects:

        card = Frame( win, bg=bg_color, highlightbackground="#d0d0d0",highlightthickness=1 )
        card.place(x=x_pos, y=y_pos, width=420, height=170)

        Label(card, text=icon, font=("Arial", 32), bg=bg_color ).place(x=15, y=15)

        Label( card, text=name, font=("Helvetica", 16, "bold"), bg=bg_color, fg=title_color ).place(x=85, y=20)

        Label( card, text=desc, font=("Calibri", 9), bg=bg_color, fg="#444444" ).place(x=87, y=55)

        Label(card, text="✔ Active Project", font=("Arial", 8, "bold"), bg=bg_color, fg="#2d6a4f" ).place(x=87, y=82)

        progress_bg = Frame(card, bg="#d9d9d9")
        progress_bg.place(x=20, y=115, width=250, height=12)

        progress_fill = Frame(card, bg=title_color)
        progress_fill.place(x=20, y=115, width=180, height=12)

        Label( card, text="Progress",  font=("Arial", 7), bg=bg_color, fg="#444444" ).place(x=280, y=112)

        Button( card, text="View Details", font=("Arial", 8, "bold"), bg=title_color, fg="white", relief=FLAT, padx=10, pady=3, cursor="hand2",
         command=lambda n=name, d=details, c=title_color:project_details(n, d, c) ).place(x=300, y=135)

        if x_pos == 45:
            x_pos = 525
        else:
            x_pos = 45
            y_pos += 200

    # ================= FOOTER =================

    stats_frame = Frame(win, bg="#1b263b")
    stats_frame.place(x=45, y=560, width=900, height=50)

    stats = [

        ("12", "Active Projects", "#ffb703"),
        ("8", "Cities", "#8ecae6"),
        ("350+", "Workers", "#90be6d"),
        ("95%", "Safety Rate", "#f28482")
    ]

    x = 50

    for number, text, color in stats:

        Label( stats_frame, text=number, font=("Arial", 16, "bold"), bg="#1b263b", fg=color ).place(x=x, y=5)

        Label( stats_frame, text=text, font=("Calibri", 8), bg="#1b263b", fg="white" ).place(x=x, y=30)

        x += 210

    Button( win, text="Close Window", font=("Arial", 8, "bold"), bg="#e63946", fg="white", relief=FLAT, padx=12, pady=3, cursor="hand2",
    command=win.destroy ).place(x=835, y=618)



#============================================================================================================
#completed_projects
#============================================================================================================

def completed_projects_window():

    win = Toplevel()
    win.title("Completed Projects")
    win.geometry("1000x650")
    win.configure(bg="#edf6f9")

    # =====================================================
    #                     HEADER
    # =====================================================

    header = Frame(win, bg="#023047", height=80)
    header.pack(fill=X)

    Label( header, text="COMPLETED PROJECTS", font=("Georgia", 30, "bold"), bg="#023047", fg="#ffffff"  ).pack(pady=16)

    Label( win, text="Successfully Delivered Modern Construction Projects", font=("Arial", 11, "italic"), bg="#edf6f9", fg="#555555").place(x=300, y=92)

    # =====================================================
    #               PROJECT REPORT FUNCTION
    # =====================================================

    def project_report(name, color):

        report = Toplevel()
        report.title(name + " Report")
        report.geometry("660x650")
        report.configure(bg="#ffffff")

        # ================= TOP SECTION =================

        top = Frame(report, bg=color, height=75)
        top.pack(fill=X)

        Label( top, text=name + " - Project Report", font=("Georgia", 22, "bold"), bg=color, fg="white" ).pack(pady=18)

        # ================= REPORT BOX =================

        report_box = Frame( report, bg="#f8f9fa", highlightbackground="#d6d6d6", highlightthickness=1)
        report_box.pack(padx=25, pady=25, fill=BOTH, expand=True)

        report_text = """
🏗 PROJECT SUMMARY

• Project completed successfully
• High-quality materials used
• Safety inspections passed
• Delivered before deadline

📊 PERFORMANCE DETAILS

✔ Construction Quality : Excellent
✔ Safety Rating : 98%
✔ Client Satisfaction : 100%
✔ Structural Stability : Verified

👷 TEAM INVOLVED

• 120 Skilled Workers
• 15 Engineers
• 8 Interior Designers

📅 Final Completion :
March 2025

🏆 ACHIEVEMENT

Awarded as one of the best
modern infrastructure projects.
        """

        Label( report_box,text=report_text,font=("Calibri", 11), bg="#f8f9fa", fg="#333333", justify=LEFT ).pack(padx=20, pady=20)

        # ================= BUTTONS =================

        btn_frame = Frame(report, bg="#ffffff")
        btn_frame.place(x=450, y=430)

        Button(btn_frame, text="Close", font=("Arial", 9, "bold"), bg="#e63946", fg="white", relief=FLAT, padx=14, pady=4, cursor="hand2",
       command=report.destroy).pack(side=LEFT, padx=10)
    # =====================================================
    #               PROJECT DETAILS FUNCTION
    # =====================================================

    def project_details(name, details, color):

        detail = Toplevel()
        detail.title(name)
        detail.geometry("580x550")
        detail.configure(bg="#ffffff")

        # ================= TOP HEADER =================

        top = Frame(detail, bg=color, height=75)
        top.pack(fill=X)

        Label( top, text=name, font=("Georgia", 22, "bold"), bg=color, fg="white" ).pack(pady=18)

        # ================= DETAILS SECTION =================

        details_frame = Frame( detail, bg="#f8f9fa", highlightbackground="#d6d6d6", highlightthickness=1 )
        details_frame.pack(padx=25, pady=25, fill=BOTH, expand=True)

        Label( details_frame, text=details, font=("Calibri", 11), bg="#f8f9fa", fg="#333333", justify=LEFT, wraplength=430 ).pack(padx=20, pady=20)

        # ================= BUTTONS =================

        btn_frame = Frame(detail, bg="#ffffff")
        btn_frame.pack(pady=10)

        Button( btn_frame, text="Project Report", font=("Arial", 9, "bold"), bg="#219ebc", fg="white", relief=FLAT, padx=14, pady=4, cursor="hand2",
        command=lambda: project_report(name, color) ).pack(side=LEFT, padx=10)

        Button( btn_frame, text="Close", font=("Arial", 9, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=14, pady=4, cursor="hand2", command=detail.destroy).pack(side=LEFT, padx=10)

    # =====================================================
    #                  PROJECT DATA
    # =====================================================

    projects = [

        (
            "🏢",
            "Skyline Corporate Tower",
            "#caf0f8",
            "#0077b6",
            "Commercial Office Project",

            """
📍 Mumbai

• 30-floor smart office tower
• Advanced security systems
• Premium office infrastructure

📅 Completed :
March 2025

🏆 Status :
Successfully Delivered
            """
        ),

        (
            "🏠",
            "Green Valley Villas",
            "#ffe5ec",
            "#c9184a",
            "Luxury Residential Villas",

            """
📍 Pune

• Modern eco-friendly villas
• Luxury interior design
• Smart home technology

📅 Completed :
December 2024

🏆 Status :
Successfully Delivered
            """
        ),

        (
            "🏨",
            "Royal Heritage Hotel",
            "#e0fbfc",
            "#0077b6",
            "5-Star Hotel Project",

            """
📍 Delhi

• Rooftop swimming pool
• Modern hospitality services
• Premium room interiors

📅 Completed :
June 2025

🏆 Status :
Successfully Delivered
            """
        ),

        (
            "🏬",
            "Urban Shopping Plaza",
            "#fff3bf",
            "#f77f00",
            "Shopping Mall Construction",

            """
📍 Bangalore

• Entertainment zone included
• Smart parking facilities
• Large-scale shopping complex

📅 Completed :
January 2025

🏆 Status :
Successfully Delivered
            """
        )
    ]

    # =====================================================
    #                  PROJECT CARDS
    # =====================================================

    x_pos = 50
    y_pos = 140

    for icon, name, bg_color, title_color, desc, details in projects:

        card = Frame( win, bg=bg_color, bd=0, relief=RIDGE)
        card.place(x=x_pos, y=y_pos, width=420, height=185)

        # ================= TOP STRIP =================

        Frame( card, bg=title_color, height=8 ).pack(fill=X)

        # ================= ICON =================

        Label( card, text=icon, font=("Arial", 36), bg=bg_color ).place(x=18, y=20)

        # ================= TITLE =================

        Label(  card,  text=name,  font=("Helvetica", 15, "bold"),bg=bg_color, fg=title_color ).place(x=95, y=25)

        # ================= DESCRIPTION =================

        Label( card, text=desc, font=("Calibri", 9), bg=bg_color, fg="#444444").place(x=98, y=58)

        # ================= STATUS =================

        Label( card, text="✔ Completed Successfully", font=("Arial", 8, "bold"), bg=bg_color, fg="#2d6a4f" ).place(x=98, y=85)

        # ================= PROGRESS =================

        Frame( card, bg="#d9d9d9" ).place(x=20, y=125, width=250, height=12)

        Frame( card, bg=title_color ).place(x=20, y=125, width=250, height=12)

        Label( card, text="100% Finished", font=("Arial", 7), bg=bg_color, fg="#333333" ).place(x=285, y=123)

        # ================= BUTTON =================

        Button( card, text="View Details", font=("Arial", 8, "bold"), bg=title_color, fg="white", relief=FLAT, padx=10, pady=3, cursor="hand2",
       command=lambda n=name, d=details, c=title_color:project_details(n, d, c) ).place(x=300, y=148)

        # ================= POSITION =================

        if x_pos == 50:
            x_pos = 530
        else:
            x_pos = 50
            y_pos += 210

    # =====================================================
    #                     FOOTER
    # =====================================================

    footer = Frame(win, bg="#023047", height=55)
    footer.pack(side=BOTTOM, fill=X)

    Label( footer, text="250+ Projects Completed   •   120+ Happy Clients   •   15+ Years Experience", font=("Arial", 10, "bold"), bg="#023047", fg="white" ).pack(pady=16)

    # ================= CLOSE BUTTON =================

    Button( win, text="Close Window", font=("Arial", 8, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=12, pady=3, cursor="hand2", command=win.destroy ).place(x=840, y=610)



#==============================================================================================================
#residential_projects
#=============================================================================================================

def residential_projects_window():

    win = Toplevel()
    win.title("Residential Projects")
    win.geometry("1000x650")
    win.configure(bg="#f8f9fa")

    # =====================================================
    #                     HEADER
    # =====================================================

    header = Frame(win, bg="#5a189a", height=80)
    header.pack(fill=X)

    Label( header,text="RESIDENTIAL PROJECTS",font=("Georgia", 30, "bold"),bg="#5a189a", fg="white" ).pack(pady=18)

    # =====================================================
    #                    SUBTITLE
    # =====================================================

    Label( win, text="Luxury Villas • Smart Apartments • Modern Living", font=("Arial", 11, "italic"), bg="#f8f9fa", fg="#555555" ).place(x=310, y=90)

    # =====================================================
    #                PROJECT DETAILS FUNCTION
    # =====================================================

    def view_project(name, color, details):

        detail = Toplevel()
        detail.title(name)
        detail.geometry("520x420")
        detail.configure(bg="#ffffff")

        top = Frame(detail, bg=color, height=70)
        top.pack(fill=X)

        Label(  top,  text=name,  font=("Georgia", 22, "bold"), bg=color, fg="white" ).pack(pady=16)

        info = Frame(detail, bg="#ffffff")
        info.pack(fill=BOTH, expand=True, padx=20, pady=20)

        Label( info, text=details, font=("Calibri", 11), bg="#ffffff", fg="#333333", justify=LEFT, wraplength=430).pack(pady=10)

        Button( detail, text="Close", font=("Arial", 9, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=14, pady=4, cursor="hand2", command=detail.destroy ).pack(pady=10)

    # =====================================================
    #                 PROJECT CARDS
    # =====================================================

    projects = [

        (
            "🏡",
            "Green Valley Villas",
            "#ffe5ec",
            "#c9184a",
            "Luxury Villa Community",

            """
📍 Pune

• Smart luxury villas
• Private garden and parking
• Modern interior design

📅 Completed : 2025
🏆 Status : Premium Project
            """
        ),

        (
            "🏢",
            "Sky Heights Apartments",
            "#caf0f8",
            "#0077b6",
            "Modern Apartment Towers",

            """
📍 Mumbai

• 2BHK & 3BHK apartments
• Swimming pool and gym
• Smart security system

📅 Completed : 2024
🏆 Status : Best Seller
            """
        ),

        (
            "🏠",
            "Sunrise Residency",
            "#fff3bf",
            "#f77f00",
            "Affordable Family Homes",

            """
📍 Bangalore

• Spacious family homes
• Eco-friendly construction
• Children's play area

📅 Completed : 2025
🏆 Status : Family Choice
            """
        ),

        (
            "🌴",
            "Palm Residency",
            "#d8f3dc",
            "#2d6a4f",
            "Nature Inspired Villas",

            """
📍 Goa

• Nature-friendly architecture
• Premium landscape design
• Smart home automation

📅 Completed : 2025
🏆 Status : Luxury Living
            """
        )
    ]

    x_pos = 50
    y_pos = 140

    for icon, name, bg_color, title_color, desc, details in projects:

        # ================= CARD =================

        card = Frame(win, bg=bg_color, bd=0)
        card.place(x=x_pos, y=y_pos, width=420, height=190)

        # ================= TOP BAR =================

        Frame(card,bg=title_color,height=10).pack(fill=X)

        # ================= ICON =================

        Label( card, text=icon, font=("Arial", 38), bg=bg_color ).place(x=18, y=22)

        # ================= TITLE =================

        Label( card, text=name, font=("Helvetica", 16, "bold"), bg=bg_color, fg=title_color).place(x=100, y=28)

        # ================= DESCRIPTION =================

        Label( card, text=desc, font=("Calibri", 10), bg=bg_color, fg="#444444").place(x=102, y=62)

        # ================= FEATURES =================

        features = """
✔ Modern Design
✔ Premium Quality
✔ Smart Infrastructure
        """

        Label( card, text=features, font=("Arial", 8), bg=bg_color, fg="#333333", justify=LEFT).place(x=25, y=105)

        # ================= BUTTON =================

        Button( card, text="View Project", font=("Arial", 8, "bold"), bg=title_color, fg="white", relief=FLAT, padx=12, pady=4, cursor="hand2",
        command=lambda n=name, c=title_color, d=details: view_project(n, c, d)).place(x=285, y=145)

        # ================= POSITION =================

        if x_pos == 50:
            x_pos = 530
        else:
            x_pos = 50
            y_pos += 220

    # =====================================================
    #                     FOOTER
    # =====================================================

    footer = Frame(win, bg="#5a189a", height=55)
    footer.pack(side=BOTTOM, fill=X)

    Label( footer, text="Modern Living • Smart Homes • Luxury Lifestyle", font=("Arial", 11, "bold"), bg="#5a189a", fg="white").pack(pady=16)

    # =====================================================
    #                  CLOSE BUTTON
    # =====================================================

    Button( win, text="Close Window", font=("Arial", 8, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=12, pady=3, cursor="hand2", command=win.destroy).place(x=835, y=610)


#===================================================================================================================
#Commercial Projects
#===================================================================================================================

def commercial_projects_window():
    win = Toplevel()
    win.title("Commercial Projects")
    win.geometry("1000x650")
    win.configure(bg="#edf2fb")

    # =====================================================
    #                     HEADER
    # =====================================================

    header = Frame(win, bg="#14213d", height=80)
    header.pack(fill=X)

    Label( header, text="COMMERCIAL PROJECTS", font=("Georgia", 30, "bold"), bg="#14213d", fg="white" ).pack(pady=18)

    # =====================================================
    #                     SUBTITLE
    # =====================================================

    Label( win, text="Modern Business Infrastructure & Smart Commercial Spaces", font=("Arial", 11, "italic"), bg="#edf2fb", fg="#555555" ).place(x=260, y=92)

    # =====================================================
    #               VIEW DETAILS FUNCTION
    # =====================================================

    def view_details(name, color, details):

        detail = Toplevel()
        detail.title(name)
        detail.geometry("540x430")
        detail.configure(bg="#ffffff")

        # ================= TOP BAR =================

        top = Frame(detail, bg=color, height=75)
        top.pack(fill=X)

        Label( top, text=name, font=("Georgia", 22, "bold"), bg=color, fg="white" ).pack(pady=18)

        # ================= DETAILS BOX =================

        box = Frame( detail, bg="#f8f9fa", highlightbackground="#d6d6d6", highlightthickness=1)
        box.pack(padx=25, pady=25, fill=BOTH, expand=True)

        Label( box, text=details, font=("Calibri", 11), bg="#f8f9fa", fg="#333333", justify=LEFT, wraplength=430 ).pack(padx=20, pady=20)

        # ================= BUTTON =================

        Button( detail, text="Close", font=("Arial", 9, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=14, pady=4, cursor="hand2", command=detail.destroy ).pack(pady=10)

    # =====================================================
    #                  PROJECT DATA
    # =====================================================

    projects = [

        (
            "🏢",
            "Skyline Business Tower",
            "#d8f3dc",
            "#2d6a4f",
            "Corporate Office Complex",

            """
📍 Mumbai

• 35-floor office building
• Smart parking system
• Advanced business infrastructure

📅 Completed : 2025
🏆 Grade-A Commercial Project
            """
        ),

        (
            "🏬",
            "Urban Shopping Plaza",
            "#ffe5ec",
            "#c9184a",
            "Modern Shopping Mall",

            """
📍 Bangalore

• Multi-brand shopping complex
• Entertainment zone included
• Premium food court area

📅 Completed : 2024
🏆 Best Retail Infrastructure
            """
        ),

        (
            "🏨",
            "Royal Crown Hotel",
            "#caf0f8",
            "#0077b6",
            "Luxury Hotel Project",

            """
📍 Delhi

• 5-star hotel infrastructure
• Rooftop restaurant and pool
• Modern hospitality design

📅 Completed : 2025
🏆 Premium Hospitality Project
            """
        ),

        (
            "🏭",
            "Tech Industrial Hub",
            "#fff3bf",
            "#f77f00",
            "Industrial Business Park",

            """
📍 Pune

• Smart warehouse facilities
• Modern industrial setup
• Eco-friendly construction

📅 Completed : 2025
🏆 Smart Industry Award
            """
        )
    ]

    # =====================================================
    #                  PROJECT CARDS
    # =====================================================

    x_pos = 50
    y_pos = 145

    for icon, name, bg_color, title_color, desc, details in projects:

        # ================= CARD =================

        card = Frame( win, bg=bg_color, bd=0)
        card.place(x=x_pos, y=y_pos, width=420, height=190)

        # ================= SIDE BAR =================

        Frame(card, bg=title_color,width=10 ).place(x=0, y=0, height=190)

        # ================= ICON =================

        Label( card, text=icon, font=("Arial", 38), bg=bg_color ).place(x=25, y=25)

        # ================= PROJECT NAME =================

        Label( card,text=name, font=("Helvetica", 16, "bold"), bg=bg_color, fg=title_color ).place(x=105, y=30)

        # ================= DESCRIPTION =================

        Label(card, text=desc, font=("Calibri", 10), bg=bg_color, fg="#444444" ).place(x=108, y=65)

        # ================= FEATURES =================

        features = """
✔ Smart Infrastructure
✔ Premium Construction
✔ Modern Architecture
        """

        Label( card, text=features, font=("Arial", 8), bg=bg_color, fg="#333333", justify=LEFT ).place(x=30, y=110)

        # ================= STATUS =================

        Label( card, text="✔ Commercial Success", font=("Arial", 8, "bold"), bg=bg_color, fg="#2d6a4f").place(x=250, y=110)

        # ================= BUTTON =================

        Button( card, text="View Details", font=("Arial", 8, "bold"), bg=title_color, fg="white", relief=FLAT, padx=12, pady=4, cursor="hand2",
        command=lambda n=name, c=title_color, d=details: view_details(n, c, d)).place(x=285, y=145)

        # ================= POSITION =================

        if x_pos == 50:
            x_pos = 530
        else:
            x_pos = 50
            y_pos += 220

    # =====================================================
    #                     FOOTER
    # =====================================================

    footer = Frame(win, bg="#14213d", height=55)
    footer.pack(side=BOTTOM, fill=X)

    Label( footer,text="Corporate Excellence • Smart Business Spaces • Modern Commercial Design",font=("Arial", 10, "bold"),bg="#14213d",fg="white" ).pack(pady=16)

    # =====================================================
    #                  CLOSE BUTTON
    # =====================================================

    Button( win, text="Close Window", font=("Arial", 8, "bold"), bg="#ef233c", fg="white", relief=FLAT, padx=12, pady=3, cursor="hand2", command=win.destroy ).place(x=835, y=610)


#============================================================================================================================
                                                                            #villa_projects
#============================================================================================================================

def villa_projects_window():

    win = Toplevel()
    win.title("Luxury Villa Projects")
    win.geometry("1250x720")
    win.config(bg="#eef2f7")

    # ================= HEADER =================
    header = Frame(win, bg="#1f3b4d", height=70)
    header.pack(fill=X)

    Label(header, text="Luxury Villa Projects", bg="#1f3b4d", fg="white", font=("Arial", 24, "bold")).pack(pady=15)

    # ================= MAIN FRAME =================
    main_frame = Frame(win, bg="#eef2f7")
    main_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

    canvas = Canvas(main_frame, bg="#eef2f7", highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)

    scroll_frame = Frame(canvas, bg="#eef2f7")

    scroll_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # ======================================================
    # LOAD DIFFERENT IMAGES
    # ======================================================

    modern_img = Image.open("image29.png")
    modern_img = modern_img.resize((240, 150))
    modern_photo = ImageTk.PhotoImage(modern_img)

    mediterranean_img = Image.open("image38.png")
    mediterranean_img = mediterranean_img.resize((240, 150))
    mediterranean_photo = ImageTk.PhotoImage(mediterranean_img)

    tropical_img = Image.open("image39.png")
    tropical_img = tropical_img.resize((240, 150))
    tropical_photo = ImageTk.PhotoImage(tropical_img)

    indian_img = Image.open("image28.png")
    indian_img = indian_img.resize((240, 150))
    indian_photo = ImageTk.PhotoImage(indian_img)

    eco_img = Image.open("image30.png")
    eco_img = eco_img.resize((240, 150))
    eco_photo = ImageTk.PhotoImage(eco_img)

    # ======================================================
    # FUNCTION FOR PROJECT CARD
    # ======================================================

    def create_project_card(parent, title, features, bg_color, image):

        card = Frame(parent, bg=bg_color)
        card.pack(fill=X, padx=20, pady=15)

        # LEFT SIDE
        left = Frame(card, bg=bg_color)
        left.pack(side=LEFT, fill=BOTH, expand=True, padx=25, pady=20)

        Label(left,text=title,bg=bg_color, fg="white", font=("Arial", 18, "bold")).pack(anchor="w")

        Label(left,text=features,bg=bg_color,fg="white",justify=LEFT,font=("Arial", 11),pady=10 ).pack(anchor="w")

        # RIGHT SIDE IMAGE
        image_frame = Frame(card, bg="white", bd=3, relief=RIDGE)
        image_frame.pack(side=RIGHT, padx=20, pady=20)

        img_label = Label(image_frame, image=image, bg="white")
        img_label.image = image
        img_label.pack()

    # ======================================================
    # MODERN VILLA
    # ======================================================

    modern_features = """
• Open Floor Plans
• Large Glass Windows
• Infinity Swimming Pools
• Smart Home Automation
• Rooftop Lounge & Garden
"""

    create_project_card(scroll_frame, "Modern Luxury Villas", modern_features, "#264653", modern_photo )

    # ======================================================
    # MEDITERRANEAN VILLA
    # ======================================================

    mediterranean_features = """
• Arched Doors & Windows
• Terracotta Roofs
• Courtyard Gardens
• Wooden & Stone Finishes
• Elegant Balconies
"""

    create_project_card( scroll_frame,"Mediterranean Style Villas",mediterranean_features,"#e76f51",mediterranean_photo)

    # ======================================================
    # TROPICAL VILLA
    # ======================================================

    tropical_features = """
• Open-Air Living Spaces
• Natural Wood Interiors
• Private Swimming Pool
• Palm Tree Landscaping
• Eco-Friendly Structure
"""

    create_project_card(scroll_frame,"Tropical Resort Villas",tropical_features,"#2a9d8f",tropical_photo )

    # ======================================================
    # INDIAN VILLA
    # ======================================================

    indian_features = """
• Grand Entrance Design
• Marble Interiors
• Traditional + Modern Architecture
• Spacious Courtyard
• Decorative Lighting
"""

    create_project_card(scroll_frame,"Classic Indian Villas",indian_features,"#6a4c93",indian_photo)

    # ======================================================
    # ECO FRIENDLY VILLA
    # ======================================================

    eco_features = """
• Solar Energy Systems
• Rainwater Harvesting
• Green Roof Gardens
• Sustainable Materials
• Energy Efficient Design
"""

    create_project_card( scroll_frame, "Smart Eco-Friendly Villas", eco_features, "#588157", eco_photo)

    # ================= CLOSE BUTTON =================

    Button( win, text="Close", font=("Arial", 11, "bold"), bg="#d62828", fg="white", padx=20, pady=5, relief=FLAT, cursor="hand2", command=win.destroy ).pack(pady=10)



#==============================================================================================================
                                                               # interior_projects
#==============================================================================================================

def interior_projects_window():

    win = Toplevel()
    win.title("Interior Design Projects")
    win.geometry("1250x720")
    win.config(bg="#edf2f4")

    # ================= HEADER =================
    header = Frame(win, bg="#14213d", height=70)
    header.pack(fill=X)

    Label( header, text="Interior Design Projects", bg="#14213d", fg="white", font=("Arial", 24, "bold")).pack(pady=15)

    # ================= MAIN FRAME =================
    main_frame = Frame(win, bg="#edf2f4")
    main_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

    canvas = Canvas(main_frame, bg="#edf2f4", highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)

    scroll_frame = Frame(canvas, bg="#edf2f4")

    scroll_frame.bind( "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")) )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # ======================================================
    # LOAD DIFFERENT INTERIOR IMAGES
    # ======================================================

    living_img = Image.open("image47.png")
    living_img = living_img.resize((240, 150))
    living_photo = ImageTk.PhotoImage(living_img)

    bedroom_img = Image.open("image49.png")
    bedroom_img = bedroom_img.resize((240, 150))
    bedroom_photo = ImageTk.PhotoImage(bedroom_img)

    kitchen_img = Image.open("image50.png")
    kitchen_img = kitchen_img.resize((240, 150))
    kitchen_photo = ImageTk.PhotoImage(kitchen_img)

    office_img = Image.open("image51.png")
    office_img = office_img.resize((240, 150))
    office_photo = ImageTk.PhotoImage(office_img)

    cafe_img = Image.open("image52.png")
    cafe_img = cafe_img.resize((240, 150))
    cafe_photo = ImageTk.PhotoImage(cafe_img)

    # ======================================================
    # FUNCTION FOR PROJECT CARDS
    # ======================================================

    def create_project_card(parent, title, features, bg_color, image):

        card = Frame(parent, bg=bg_color)
        card.pack(fill=X, padx=20, pady=15)

        # LEFT SIDE
        left = Frame(card, bg=bg_color)
        left.pack(side=LEFT, fill=BOTH, expand=True, padx=25, pady=20)

        Label( left, text=title, bg=bg_color, fg="white", font=("Arial", 18, "bold")).pack(anchor="w")

        Label( left, text=features, bg=bg_color, fg="white", justify=LEFT, font=("Arial", 11), pady=10).pack(anchor="w")

        # RIGHT SIDE IMAGE
        image_frame = Frame(card, bg="white", bd=3, relief=RIDGE)
        image_frame.pack(side=RIGHT, padx=20, pady=20)

        img_label = Label(image_frame, image=image, bg="white")
        img_label.image = image
        img_label.pack()

    # ======================================================
    # LIVING ROOM INTERIORS
    # ======================================================

    living_features = """
• Elegant False Ceiling
• LED Ambient Lighting
• Modern Furniture Layout
• Wooden & Glass Finish
• Spacious Open Design
"""

    create_project_card( scroll_frame, "Modern Living Room Interiors", living_features, "#1d3557", living_photo)

    # ======================================================
    # BEDROOM INTERIORS
    # ======================================================

    bedroom_features = """
• Stylish Wall Panels
• Soft Designer Lighting
• Premium Wardrobes
• Wooden Flooring
• Luxury Bathroom Setup
"""

    create_project_card( scroll_frame, "Luxury Bedroom Interiors", bedroom_features, "#6d597a", bedroom_photo )

    # ======================================================
    # MODULAR KITCHENS
    # ======================================================

    kitchen_features = """
• Smart Storage Solutions
• Modular Cabinets
• Granite Countertops
• Modern Chimney Setup
• Space Saving Design
"""

    create_project_card(scroll_frame,"Modular Kitchen Designs",kitchen_features,"#bc6c25", kitchen_photo)

    # ======================================================
    # OFFICE INTERIORS
    # ======================================================

    office_features = """
• Professional Workspace Layout
• Conference Room Setup
• Creative Wall Decor
• Ergonomic Furniture
• Premium Lighting System
"""

    create_project_card( scroll_frame, "Office Interior Projects", office_features, "#3a5a40", office_photo )

    # ======================================================
    # CAFE & RESTAURANT INTERIORS
    # ======================================================

    cafe_features = """
• Decorative Lighting
• Stylish Seating Arrangements
• Artistic Wall Themes
• Comfortable Dining Space
• Attractive Ambience
"""

    create_project_card(scroll_frame,"Restaurant & Cafe Interiors",cafe_features, "#9d4edd", cafe_photo )

    # ================= CLOSE BUTTON =================

    Button( win, text="Close", font=("Arial", 11, "bold"), bg="#d62828", fg="white", padx=20, pady=5, relief=FLAT, cursor="hand2", command=win.destroy ).pack(pady=10)




#=====================================================================================================================
                                            # upcoming_projects
#=====================================================================================================================

def upcoming_projects_window():

    win = Toplevel()
    win.title("Upcoming Projects")
    win.geometry("1280x730")
    win.config(bg="#f4f7fb")

    # ================= HEADER =================
    header = Frame(win, bg="#0b132b", height=75)
    header.pack(fill=X)

    Label( header, text="Upcoming Construction Projects", bg="#0b132b", fg="#ffffff", font=("Arial", 25, "bold") ).pack(pady=16)

    # ================= MAIN FRAME =================
    main_frame = Frame(win, bg="#f4f7fb")
    main_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

    canvas = Canvas(main_frame, bg="#f4f7fb", highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)

    scroll_frame = Frame(canvas, bg="#f4f7fb")

    scroll_frame.bind( "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")) )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # ==========================================================
    # LOAD PROJECT IMAGES
    # ==========================================================

    smartcity_img = Image.open("image57.png")
    smartcity_img = smartcity_img.resize((250, 160))
    smartcity_photo = ImageTk.PhotoImage(smartcity_img)

    mall_img = Image.open("image58.png")
    mall_img = mall_img.resize((250, 160))
    mall_photo = ImageTk.PhotoImage(mall_img)

    metro_img = Image.open("image53.png")
    metro_img = metro_img.resize((250, 160))
    metro_photo = ImageTk.PhotoImage(metro_img)

    eco_img = Image.open("image60.png")
    eco_img = eco_img.resize((250, 160))
    eco_photo = ImageTk.PhotoImage(eco_img)

    resort_img = Image.open("image59.png")
    resort_img = resort_img.resize((250, 160))
    resort_photo = ImageTk.PhotoImage(resort_img)

    # ==========================================================
    # FUNCTION FOR PROJECT CARD
    # ==========================================================

    def create_project_card(parent, title, features, left_color, right_color, image):

        outer = Frame(parent, bg=right_color)
        outer.pack(fill=X, padx=25, pady=18)

        # LEFT SIDE
        left = Frame(outer, bg=left_color, width=700)
        left.pack(side=LEFT, fill=BOTH, expand=True)

        Label( left, text=title, bg=left_color, fg="white", font=("Arial", 19, "bold") ).pack(anchor="w", padx=25, pady=(20, 8))

        Label( left, text=features, bg=left_color, fg="#f1f1f1", justify=LEFT, font=("Arial", 11), pady=5 ).pack(anchor="w", padx=25, pady=(0, 20))

        # RIGHT SIDE IMAGE
        right = Frame(outer, bg=right_color, padx=18, pady=18)
        right.pack(side=RIGHT)

        img_label = Label(right, image=image, bd=4, relief=RIDGE)
        img_label.image = image
        img_label.pack()

    # ==========================================================
    # SMART CITY PROJECT
    # ==========================================================

    smartcity_features = """
• AI-Based Smart Infrastructure
• Green Energy Systems
• Smart Traffic Management
• Digital Security Monitoring
• Eco-Friendly Urban Planning
"""

    create_project_card( scroll_frame, "Future Smart City Project", smartcity_features, "#14213d", "#fca311", smartcity_photo )

    # ==========================================================
    # SHOPPING MALL PROJECT
    # ==========================================================

    mall_features = """
• Multi-Level Shopping Complex
• Entertainment Zone
• Premium Food Court
• Smart Parking System
• Modern Glass Architecture
"""

    create_project_card( scroll_frame, "Mega Shopping Mall", mall_features, "#3a0ca3", "#f72585", mall_photo )

    # ==========================================================
    # METRO STATION PROJECT
    # ==========================================================

    metro_features = """
• High-Speed Metro Connectivity
• Underground Platform Design
• Smart Ticketing System
• Passenger Safety Features
• Energy Efficient Structure
"""

    create_project_card( scroll_frame, "Modern Metro Station", metro_features, "#006d77", "#ffddd2", metro_photo)

    # ==========================================================
    # ECO TOWER PROJECT
    # ==========================================================

    eco_features = """
• Solar Powered Building
• Rainwater Harvesting
• Vertical Garden Design
• Energy Efficient Glass
• Sustainable Construction
"""

    create_project_card( scroll_frame, "Eco-Friendly Business Tower", eco_features, "#386641", "#f2e8cf", eco_photo )

    # ==========================================================
    # RESORT PROJECT
    # ==========================================================

    resort_features = """
• Luxury Beachside Resort
• Infinity Swimming Pool
• Premium Villa Suites
• Spa & Wellness Center
• International Hospitality Design
"""

    create_project_card( scroll_frame,  "Luxury Resort Project",  resort_features, "#5a189a", "#ffb703", resort_photo)

    # ================= CLOSE BUTTON =================

    Button( win, text="Close Window", bg="#d90429", fg="white", font=("Arial", 11, "bold"), padx=22, pady=6, relief=FLAT, cursor="hand2", command=win.destroy).pack(pady=12)


#=================================================================================================================
#Work_Showcase
#================================================================================================================

def Work_Showcase():

    win = Toplevel()
    win.title("Work Showcase - Eco Tower")
    win.geometry("1100x650")
    win.config(bg="#0b132b")

    # ================= HEADER =================
    header = Frame(win, bg="#1c2541", height=70)
    header.pack(fill=X)

    Label( header, text="Work Showcase - Eco Tower Project", bg="#1c2541", fg="white", font=("Arial", 22, "bold")).pack(pady=15)

    # ================= CONTENT FRAME =================
    content = Frame(win, bg="#0b132b")
    content.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # ================= LEFT TEXT SECTION =================
    left = Frame(content, bg="#0b132b")
    left.pack(side=LEFT, fill=BOTH, expand=True)

    Label( left, text="ECO TOWER PROJECT", bg="#0b132b", fg="#80ed99", font=("Arial", 20, "bold") ).pack(anchor="w", pady=10)

    description = """
• Sustainable green architecture design
• Fully solar-powered energy system
• Vertical gardens on every floor
• Smart water harvesting system
• Eco-friendly construction materials
• Energy efficient glass facade building
"""

    Label(  left,  text=description,  bg="#0b132b", fg="white", font=("Arial", 12), justify=LEFT ).pack(anchor="w", pady=10)

    # ================= RIGHT IMAGE SECTION =================
    right = Frame(content, bg="#0b132b")
    right.pack(side=RIGHT, padx=10)

    img = Image.open("image60.png")
    img = img.resize((520, 360))
    photo = ImageTk.PhotoImage(img)

    img_label = Label(right, image=photo, bg="#0b132b")
    img_label.image = photo
    img_label.pack()

    # ================= CLOSE BUTTON =================
    Button(win,  text="Close",  bg="#e63946",  fg="white",  font=("Arial", 11, "bold"),  padx=20,  pady=5,  command=win.destroy ).pack(pady=10)



#============================================================================================================
                                                                 # design_collection
#============================================================================================================

def design_collection_window():
    win = Toplevel()
    win.title("Design Collection")
    win.geometry("1100x700")
    win.config(bg="#f4f6f8")

    # ================= HEADER =================
    header = Frame(win, bg="#1e3a5f", height=70)
    header.pack(fill=X)

    Label( header, text="DESIGN COLLECTION", font=("Arial", 20, "bold"), bg="#1e3a5f", fg="white" ).pack(pady=18)

    # ================= DETAILS WINDOW =================
    def open_details(title, img_path):
        top = Toplevel(win)
        top.title(title)
        top.geometry("600x500")
        top.config(bg="white")

        Label(top, text=title,  font=("Arial", 18, "bold"),  bg="white", fg="#1e3a5f").pack(pady=10)

        try:
            img = Image.open(img_path)
            img = img.resize((450, 250))
            photo = ImageTk.PhotoImage(img)

            lbl = Label(top, image=photo, bg="white")
            lbl.image = photo
            lbl.pack(pady=10)

        except:
            Label(top, text="Image Not Found",  fg="red", bg="white").pack()

        Label(top,text="High-quality modern architectural design with premium finishing and smart layout.",wraplength=500, bg="white", font=("Arial", 11)).pack(pady=10)

        Button(top, text="Close",  command=top.destroy,bg="#c0392b", fg="white").pack(pady=10)

    # ================= MAIN FRAME =================
    main_frame = Frame(win, bg="#f4f6f8")
    main_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

    canvas = Canvas(main_frame, bg="#f4f6f8", highlightthickness=0)
    scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scroll_frame = Frame(canvas, bg="#f4f6f8")

    scroll_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # ================= DATA =================
    designs = [
        ("Modern Villas", "image39.png", "#ffdddd"),
        ("Eco Homes", "image37.png","#ddffdd"),
        ("Luxury Interiors", "image48.png","#dde5ff"),
        ("Smart Homes", "image36.png","#fff0cc"),
        ("Cafe Design", "image52.png","#e6e6fa"),
        ("Minimalist Designs", "image56.png", "#d0f0f0"),
        ("Commercial Towers", "image60.png","#ffe6f2"),
        ("Resort Villas", "image30.png","#f0f8ff"),
        ("Urban Apartments", "image17.png","#ddffdd"),
    ]

    images = []  # keep reference

    # ================= CARDS =================
    for i, (title, img_path,bg_color) in enumerate(designs):

        card = Frame(scroll_frame,  bg=bg_color, width=320, height=260, relief=RIDGE, bd=2)
        card.grid(row=i // 3, column=i % 3, padx=15, pady=15)
        card.pack_propagate(False)

        Label(card, text=title, font=("Arial", 12, "bold"), bg=bg_color).pack(pady=8)

        try:
            img = Image.open(img_path)
            img = img.resize((250, 140))
            photo = ImageTk.PhotoImage(img)
            images.append(photo)

            Label(card, image=photo, bg="white").pack()
        except:
            Label(card, text="Image Preview", bg="#ddd", width=30, height=8).pack()

        Button( card, text="View Details", bg="#1e3a5f", fg="white", font=("Arial", 9, "bold"), command=lambda t=title, p=img_path: open_details(t, p)).pack(pady=8)

    # ================= CLOSE =================
    Button(win,text="Close",command=win.destroy,bg="#c0392b",fg="white" ).pack(pady=10)

    win.mainloop()


#================================================================================================
                    # building_concepts
#================================================================================================

def building_concepts_window():
    win = Toplevel()
    win.title("Building Concepts")
    win.geometry("1100x700")
    win.config(bg="#eef2f3")

    win.images = []

    # ================= HEADER =================
    header = Frame(win, bg="#2c3e50", height=70)
    header.pack(fill=X)

    Label( header, text="BUILDING CONCEPTS", font=("Arial", 20, "bold"), fg="white", bg="#2c3e50").pack(pady=18)

    # ================= MAIN FRAME =================
    main_frame = Frame(win, bg="#eef2f3")
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

    concepts = [
        ("Modern Architecture", "image40.png", "#dff6ff"),
        ("Eco Buildings", "image60.png", "#e8f5e9"),
        ("Smart Buildings", "image57.png", "#fff3e0"),
        ("Skyscraper Design", "image20.png", "#ede7f6"),
        ("Luxury Villas", "image31.png", "#fce4ec"),
        ("Commercial Complex", "image22.png", "#e0f7fa"),
    ]

    def show_info(title):
        top = Toplevel(win)
        top.title("Concept Details")
        top.geometry("420x250")
        top.config(bg="white")

        Label(top, text=title, font=("Arial", 18, "bold"), bg="white", fg="#2c3e50").pack(pady=15)

        Label(top, text="This concept focuses on modern engineering,\narchitectural planning, and sustainable design principles.", font=("Arial", 11), bg="white",
        justify=CENTER).pack(pady=10)

        Button(top, text="Close", bg="#e74c3c", fg="white", command=top.destroy).pack(pady=15)

    row = 0
    col = 0

    for title, img_path, color in concepts:

        card = Frame(main_frame, bg=color, width=300, height=260, relief=RIDGE, bd=2)
        card.grid(row=row, column=col, padx=15, pady=15)
        card.pack_propagate(False)

        Label(card, text=title, font=("Arial", 12, "bold"),  bg=color).pack(pady=8)

        try:
            img = Image.open(img_path)
            img = img.resize((220, 140))
            photo = ImageTk.PhotoImage(img)
            win.images.append(photo)

            Label(card, image=photo, bg=color).pack()
        except:
            Label(card, text="No Image",  bg="#ddd", width=28, height=8).pack()

        Button(card, text="View Concept", bg="#2c3e50", fg="white", command=lambda t=title: show_info(t)).pack(pady=8)

        col += 1
        if col == 3:
            col = 0
            row += 1
    Button( win, text="Close", command=win.destroy, bg="#c0392b", fg="white").place(x=500,y=670)

    win.mainloop()

#==================================================================================================
                    # visual_gallery
#==================================================================================================

def visual_gallery_window():

    win = Toplevel()
    win.title("Visual Gallery")
    win.geometry("1100x700")
    win.config(bg="#f2f4f8")
    win.img_store = {}

    # ================= HEADER =================
    header = Frame(win, bg="#0f2d4a", height=70)
    header.pack(fill=X)

    Label( header, text="VISUAL GALLERY", font=("Arial", 22, "bold"), bg="#0f2d4a", fg="white").pack(pady=18)

    # ================= DETAILS POPUP =================
    def show_details(title, img_path, desc):
        pop = Toplevel(win)
        pop.title(title)
        pop.geometry("650x550")
        pop.config(bg="white")

        Label(pop, text=title, font=("Arial", 18, "bold"), bg="white", fg="#0f2d4a").pack(pady=10)

        try:
            img = Image.open(img_path)
            img = img.resize((500, 280))
            photo = ImageTk.PhotoImage(img)

            pop.photo_ref = photo  # keep reference

            Label(pop, image=photo, bg="white").pack(pady=10)

        except:
            Label(pop, text="Image Not Available",
                  fg="red", bg="white").pack()

        Label(  pop,  text=desc,  wraplength=580,  justify=LEFT, bg="white", font=("Arial", 11) ).pack(pady=10)

        Button( pop, text="Close", command=pop.destroy, bg="#c0392b", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

    # ================= MAIN AREA =================
    main = Frame(win, bg="#f2f4f8")
    main.pack(fill=BOTH, expand=True, padx=15, pady=15)

    canvas = Canvas(main, bg="#f2f4f8", highlightthickness=0)
    scroll = Scrollbar(main, orient=VERTICAL, command=canvas.yview)
    grid_frame = Frame(canvas, bg="#f2f4f8")

    grid_frame.bind( "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=grid_frame, anchor="nw")
    canvas.configure(yscrollcommand=scroll.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scroll.pack(side=RIGHT, fill=Y)

    # ================= DATA =================
    gallery = [
        ("Modern Villa", "image47.png",
         "Luxury modern villa with glass architecture and open space design."),

        ("Eco Home", "image49.png",
         "Sustainable eco home with green energy and natural materials."),

        ("Luxury Interior", "image50.png",
         "Premium interior design with modern lighting and furniture."),

        ("Smart Home", "image55.png",
         "AI-powered smart home with automation and smart security."),

        ("Cafe Design", "image52.png",
         "Stylish cafe interior with cozy and modern ambiance.")
    ]

    # ================= IMAGE GRID =================
    for i, (title, img_path, desc) in enumerate(gallery):

        card = Frame(grid_frame, bg="white", width=300, height=260, relief=RIDGE, bd=2)
        card.grid(row=i // 3, column=i % 3, padx=15, pady=15)
        card.pack_propagate(False)

        Label(card, text=title,font=("Arial", 12, "bold"), bg="white").pack(pady=8)

        try:
            img = Image.open(img_path)
            img = img.resize((260, 150))
            photo = ImageTk.PhotoImage(img)

            win.img_store[img_path] = photo

            lbl = Label(card, image=photo, bg="white")
            lbl.image = photo
            lbl.pack()

        except:
            Label(card, text="No Image",
                  bg="#ddd", width=30, height=8).pack()

        Button( card, text="View Details", bg="#0f2d4a", fg="white", font=("Arial", 9, "bold"), command=lambda t=title, p=img_path, d=desc: show_details(t, p, d)).pack(pady=8)

    # ================= CLOSE =================
    Button( win, text="Close Gallery", command=win.destroy, bg="#c0392b", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

    win.mainloop()


#===================================================================================================================
                     # creative_models
#===================================================================================================================

def creative_models_window():
    win = Tk()
    win.title("Creative Models Dashboard")
    win.geometry("1150x720")
    win.config(bg="#e9eff5")

    # ================= SIDEBAR =================
    sidebar = Frame(win, bg="#1e2a38", width=220)
    sidebar.pack(side=LEFT, fill=Y)

    Label(sidebar, text="CREATIVE\nMODELS", font=("Arial", 16, "bold"), fg="white", bg="#1e2a38", justify=LEFT).pack(pady=30)

    menu_items = ["Home", "Models", "Gallery", "Design Ideas", "Settings"]

    for item in menu_items:
        
        Button(sidebar, text=item, font=("Arial", 11), fg="white", bg="#2c3e50", activebackground="#34495e", relief=FLAT, cursor="hand2", width=20).pack(pady=5)

    # ================= MAIN AREA =================
    main = Frame(win, bg="#e9eff5")
    main.pack(side=LEFT, fill=BOTH, expand=True)

    
    header = Frame(main, bg="#ffffff", height=70)
    header.pack(fill=X)

    Label(header, text="Creative Architectural Models", font=("Arial", 18, "bold"), bg="#ffffff", fg="#2c3e50").pack(pady=18)

    # ================= CARDS AREA =================
    card_area = Frame(main, bg="#e9eff5")
    card_area.pack(pady=20)

    models = [
        ("Futuristic Smart Villa", "#ff7675"),
        ("Eco Green Home", "#00b894"),
        ("Sky Garden Apartment", "#0984e3"),
        ("Luxury Minimalist House", "#6c5ce7"),
        ("Smart Commercial Hub", "#fdcb6e"),
        ("Resort Style Villa", "#00cec9"),
    ]

    def open_details(name):
        top = Toplevel(win)
        top.title("Model Details")
        top.geometry("400x250")
        top.config(bg="white")

        Label(top, text=name, font=("Arial", 14, "bold"), bg="white").pack(pady=20)

        Label(top, text="Detailed design information coming soon...\n"
                        "• Architecture style\n• Materials\n• Features\n• Cost estimation", font=("Arial", 10), bg="white", justify=LEFT).pack(pady=10)

        Button(top, text="Close",bg="#e74c3c", fg="white",command=top.destroy).pack(pady=10)

    # CARD GRID
    r = 0
    c = 0

    for name, color in models:
        card = Frame(card_area, bg=color, width=320, height=140)
        card.grid(row=r, column=c, padx=15, pady=15)
        card.pack_propagate(False)

        Label(card, text=name, font=("Arial", 12, "bold"), fg="white", bg=color, wraplength=280).pack(pady=20)

        Button(card, text="View Details",font=("Arial", 9, "bold"),bg="white", fg="black",cursor="hand2",command=lambda n=name: open_details(n)).pack()

        c += 1
        if c == 2:
            c = 0
            r += 1

    # ================= FOOTER =================
    footer = Frame(main, bg="#ffffff", height=40)
    footer.pack(fill=X, side=BOTTOM)

    Button(footer, text="Close Window", bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), command=win.destroy).pack(pady=5)

    win.mainloop()


#=========================================================================================================
               # client_reviews
#========================================================================================================


def client_reviews_window():
    win = Tk()
    win.title("Client Reviews")
    win.geometry("1100x700")
    win.config(bg="#eef3f7")

    # ================= HEADER =================
    header = Frame(win, bg="#1f3b4d", height=70)
    header.pack(fill=X)

    Label(header, text="CLIENT REVIEWS", font=("Arial", 18, "bold"), fg="white", bg="#1f3b4d").pack(pady=18)

    # ================= MAIN FRAME =================
    main = Frame(win, bg="#eef3f7")
    main.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # ================= SAMPLE REVIEWS =================
    reviews = [
        ("Rahul Mehta", "Modern Villa Project",
         "Excellent design quality and timely delivery. Very professional team!", "★★★★★"),

        ("Anjali Sharma", "Eco Home Project",
         "Loved the green concept and eco-friendly materials used.", "★★★★☆"),

        ("Vikram Patil", "Luxury Interior",
         "Outstanding interior design work. Looks very premium and elegant.", "★★★★★"),

        ("Neha Desai", "Smart Office Building",
         "Very innovative smart system integration. Highly recommended!", "★★★★☆"),

        ("Amit Joshi", "Resort Villa",
         "Beautiful resort design with perfect landscape planning.", "★★★★★"),
    ]

    # ================= SCROLLABLE AREA =================
    canvas = Canvas(main, bg="#eef3f7", highlightthickness=0)
    scrollbar = Scrollbar(main, orient=VERTICAL, command=canvas.yview)
    scroll_frame = Frame(canvas, bg="#eef3f7")

    scroll_frame.bind( "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")) )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # ================= REVIEW CARDS =================
    for name, project, review, stars in reviews:
        card = Frame(scroll_frame, bg="white", width=900, height=120)
        card.pack(pady=10, fill=X)
        card.pack_propagate(False)

        
        left = Frame(card, bg="white")
        left.pack(side=LEFT, padx=15)

        Label(left, text=name, font=("Arial", 12, "bold"), bg="white", fg="#2c3e50").pack(anchor="w")

        Label(left, text=project, font=("Arial", 10), bg="white", fg="#7f8c8d").pack(anchor="w")

        
        right = Frame(card, bg="white")
        right.pack(side=RIGHT, padx=15)

        Label(right, text=stars, font=("Arial", 12), bg="white", fg="#f39c12").pack(anchor="e")

        Label(card, text=review,  font=("Arial", 10), bg="white", fg="#34495e", wraplength=600,  justify=LEFT).pack(pady=25)

    # ================= CLOSE BUTTON =================
    Button(win, text="Close", font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", command=win.destroy).pack(pady=10)

    win.mainloop()


#=============================================================================================================
        # testimonials
#=============================================================================================================

def testimonials_window():
    win = Tk()
    win.title("Testimonials")
    win.geometry("1100x720")
    win.config(bg="#f3f6fb")

    # ================= HEADER =================
    header = Frame(win, bg="#0f2a3d", height=75)
    header.pack(fill=X)

    Label(header, text="TESTIMONIALS", font=("Arial", 20, "bold"), fg="white", bg="#0f2a3d").pack(pady=18)

    # ================= MAIN FRAME =================
    main = Frame(win, bg="#f3f6fb")
    main.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # ================= TESTIMONIAL DATA =================
    testimonials = [
        ("Aarav Kulkarni", "Luxury Villa Project",
         "The design quality exceeded our expectations. The team delivered a world-class architectural solution.",
         "#ff6b6b"),

        ("Sneha Patil", "Eco Green Home",
         "Amazing eco-friendly concept with perfect execution. Truly sustainable and beautiful design.",
         "#2ecc71"),

        ("Rohan Deshmukh", "Smart Office Hub",
         "Highly innovative smart building features. Everything is automated and very efficient.",
         "#3498db"),

        ("Priya Sharma", "Modern Apartment",
         "Minimalist yet elegant interiors. The space utilization is absolutely perfect.",
         "#9b59b6"),

        ("Vikram Joshi", "Resort Villa",
         "The landscape and resort planning were stunning. A truly premium experience.",
         "#f39c12"),
    ]

    # ================= SCROLLABLE CANVAS =================
    canvas = Canvas(main, bg="#f3f6fb", highlightthickness=0)
    scrollbar = Scrollbar(main, orient=VERTICAL, command=canvas.yview)
    scroll_frame = Frame(canvas, bg="#f3f6fb")

    scroll_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # ================= TESTIMONIAL CARDS =================
    for name, project, text, color in testimonials:
        card = Frame(scroll_frame, bg="white", width=950, height=140)
        card.pack(pady=12, fill=X)
        card.pack_propagate(False)

        
        strip = Frame(card, bg=color, width=10)
        strip.pack(side=LEFT, fill=Y)

       
        content = Frame(card, bg="white")
        content.pack(side=LEFT, fill=BOTH, expand=True, padx=15)

        
        Label(content, text=name, font=("Arial", 12, "bold"), bg="white", fg="#2c3e50").pack(anchor="w")

        Label(content, text=project, font=("Arial", 10), bg="white", fg="#7f8c8d").pack(anchor="w")

      
        Label(content, text=text, font=("Arial", 10), bg="white", fg="#34495e", wraplength=750, justify=LEFT).pack(pady=8)

       
        Label(card, text="★★★★★", font=("Arial", 12), bg="white", fg="#f1c40f").pack(side=RIGHT, padx=15)

    # ================= CLOSE BUTTON =================
    Button(win, text="Close Window", font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", command=win.destroy).pack(pady=10)

    win.mainloop()
    

#=================================================================================================
           # happy_customers
#================================================================================================
    
def happy_customers_window():
    win = Tk()
    win.title("Happy Customers")
    win.geometry("1100x720")
    win.config(bg="#eef3f7")

    # ================= HEADER =================
    header = Frame(win, bg="#1a2c3a", height=75)
    header.pack(fill=X)

    Label(header, text="HAPPY CUSTOMERS", font=("Arial", 20, "bold"), fg="white", bg="#1a2c3a").pack(pady=18)

    # ================= STATS SECTION =================
    stats_frame = Frame(win, bg="#eef3f7")
    stats_frame.pack(pady=20)

    stats = [
        ("Projects Completed", "120+", "#3498db"),
        ("Satisfied Clients", "95%", "#2ecc71"),
        ("Ongoing Projects", "35", "#f39c12"),
        ("Repeat Customers", "80%", "#9b59b6"),
    ]

    for title, value, color in stats:
        card = Frame(stats_frame, bg=color, width=240, height=120)
        card.pack(side=LEFT, padx=10)
        card.pack_propagate(False)

        Label(card, text=value,  font=("Arial", 20, "bold"),  fg="white", bg=color).pack(pady=10)

        Label(card, text=title, font=("Arial", 11), fg="white", bg=color).pack()

    # ================= MAIN SECTION =================
    main = Frame(win, bg="#eef3f7")
    main.pack(fill=BOTH, expand=True, padx=20, pady=10)

    Label(main, text="Our Happy Customer Highlights", font=("Arial", 14, "bold"), bg="#eef3f7", fg="#2c3e50").pack(anchor="w")

    # ================= CUSTOMER DATA =================
    customers = [
        ("Rahul Mehta", "Villa Project", "Very professional and timely delivery."),
        ("Anjali Sharma", "Eco Home", "Loved the sustainable design approach."),
        ("Vikram Patil", "Luxury Interior", "Outstanding quality and finishing."),
        ("Neha Desai", "Smart Office", "Innovative and modern solutions."),
        ("Amit Joshi", "Resort Villa", "Beautiful landscape and architecture."),
        ("Priya Kulkarni", "Apartment Project", "Perfect space utilization."),
    ]

    # ================= CUSTOMER CARDS =================
    grid = Frame(main, bg="#eef3f7")
    grid.pack(pady=15)

    r = 0
    c = 0

    for name, project, msg in customers:
        card = Frame(grid, bg="white", width=330, height=140)
        card.grid(row=r, column=c, padx=12, pady=12)
        card.pack_propagate(False)

        
        avatar = Frame(card, bg="#3498db", width=40, height=40)
        avatar.place(x=10, y=10)
        Label(avatar, text=name[0], font=("Arial", 12, "bold"), fg="white", bg="#3498db").pack(expand=True)

        
        Label(card, text=name, font=("Arial", 11, "bold"), bg="white", fg="#2c3e50").place(x=60, y=10)

        
        Label(card, text=project, font=("Arial", 9), bg="white", fg="#7f8c8d").place(x=60, y=35)

       
        Label(card, text=msg, font=("Arial", 9), bg="white", fg="#34495e", wraplength=280, justify=LEFT).place(x=10, y=70)

        # STATUS
        Label(card, text="✔ Verified Customer",
              font=("Arial", 9, "bold"),
              bg="white", fg="#2ecc71").place(x=10, y=115)

        c += 1
        if c == 3:
            c = 0
            r += 1

    # ================= FOOTER =================
    Button(win, text="Close Window", font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", command=win.destroy).pack(pady=10)

    win.mainloop()


#=======================================================================================================
           # feedback
#=======================================================================================================

def feedback_window():
    win = Tk()
    win.title("Feedback")
    win.geometry("1100x720")
    win.config(bg="#eef3f7")

    # ================= HEADER =================
    header = Frame(win, bg="#1f3b4d", height=75)
    header.pack(fill=X)

    Label(header, text="FEEDBACK FORM", font=("Arial", 20, "bold"), fg="white", bg="#1f3b4d").pack(pady=18)

    # ================= MAIN FRAME =================
    main = Frame(win, bg="#eef3f7")
    main.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # ================= FORM FRAME =================
    form = Frame(main, bg="white", width=450, height=500)
    form.pack(side=LEFT, padx=20, pady=10)
    form.pack_propagate(False)

    Label(form, text="Share Your Feedback", font=("Arial", 14, "bold"), bg="white", fg="#2c3e50").pack(pady=15)

   
    Label(form, text="Name:", bg="white").pack(anchor="w", padx=20)
    name_entry = Entry(form, width=35)
    name_entry.pack(padx=20, pady=5)

    
    Label(form, text="Project:", bg="white").pack(anchor="w", padx=20)
    project_entry = Entry(form, width=35)
    project_entry.pack(padx=20, pady=5)

    
    Label(form, text="Category:", bg="white").pack(anchor="w", padx=20)
    category_var = StringVar()
    category_var.set("Select")

    OptionMenu(form, category_var, "Villa", "Apartment", "Commercial", "Interior", "Resort" ).pack(padx=20, pady=5, fill=X)

   
    Label(form, text="Rating:", bg="white").pack(anchor="w", padx=20)
    rating_var = StringVar()
    rating_var.set("★★★★★")

    OptionMenu(form, rating_var, "★★★★★", "★★★★☆", "★★★☆☆", "★★☆☆☆", "★☆☆☆☆" ).pack(padx=20, pady=5, fill=X)

    
    Label(form, text="Feedback:", bg="white").pack(anchor="w", padx=20)
    feedback_text = Text(form, height=5, width=30)
    feedback_text.pack(padx=20, pady=5)

    # ================= DISPLAY FRAME =================
    display = Frame(main, bg="#eef3f7")
    display.pack(side=LEFT, fill=BOTH, expand=True)

    Label(display, text="Submitted Feedback", font=("Arial", 14, "bold"), bg="#eef3f7", fg="#2c3e50").pack(anchor="w")

    list_frame = Frame(display, bg="#eef3f7")
    list_frame.pack(fill=BOTH, expand=True, pady=10)

    # ================= SUBMIT FUNCTION =================
    def submit_feedback():
        name = name_entry.get()
        project = project_entry.get()
        category = category_var.get()
        rating = rating_var.get()
        feedback = feedback_text.get("1.0", END).strip()

        if name == "" or feedback == "":
            messagebox.showerror("Error", "Please fill required fields!")
            return

        card = Frame(list_frame, bg="white", width=600, height=120)
        card.pack(pady=10, fill=X)
        card.pack_propagate(False)

        Label(card, text=f"{name} ({project})", font=("Arial", 11, "bold"), bg="white", fg="#2c3e50").pack(anchor="w", padx=10)

        Label(card, text=f"{category} | Rating: {rating}", font=("Arial", 10), bg="white", fg="#7f8c8d").pack(anchor="w", padx=10)

        Label(card, text=feedback, font=("Arial", 10), bg="white", fg="#34495e", wraplength=550, justify=LEFT).pack(padx=10, pady=5)

        # clear fields
        name_entry.delete(0, END)
        project_entry.delete(0, END)
        feedback_text.delete("1.0", END)

    # ================= BUTTONS =================
    Button(form, text="Submit Feedback", bg="#2ecc71", fg="white",  font=("Arial", 10, "bold"), command=submit_feedback).pack(pady=10)

    Button(form, text="Close Window",bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), command=win.destroy).pack()

    win.mainloop()


#===========================================================================================================
            # job_openings
#===========================================================================================================
    
def job_openings_window():
    win = Tk()
    win.title("Job Openings")
    win.geometry("1150x750")
    win.config(bg="#eef3f7")

    # ================= HEADER =================
    header = Frame(win, bg="#1f3b4d", height=75)
    header.pack(fill=X)

    Label(header, text="JOB OPENINGS", font=("Arial", 20, "bold"), fg="white", bg="#1f3b4d").pack(pady=18)

    # ================= FILTER BAR =================
    filter_frame = Frame(win, bg="#eef3f7")
    filter_frame.pack(fill=X, padx=20, pady=10)

    Label(filter_frame, text="Filter by Department:", font=("Arial", 11), bg="#eef3f7").pack(side=LEFT)

    dept_var = StringVar()
    dept_var.set("All")

    OptionMenu(filter_frame, dept_var,"All", "Architecture", "Engineering", "Interior Design","Site Supervisor", "Project Manager").pack(side=LEFT, padx=10)

    # ================= MAIN AREA =================
    main = Frame(win, bg="#eef3f7")
    main.pack(fill=BOTH, expand=True, padx=20, pady=10)

    # ================= JOB DATA =================
    jobs = [
        ("Architect", "Architecture", "Design modern residential & commercial buildings", "₹40,000 - ₹80,000"),
        ("Site Engineer", "Engineering", "Manage on-site construction activities", "₹25,000 - ₹50,000"),
        ("Interior Designer", "Interior Design", "Plan interior layouts and décor", "₹30,000 - ₹70,000"),
        ("Project Manager", "Project Manager", "Handle full project execution", "₹60,000 - ₹1,20,000"),
        ("Site Supervisor", "Site Supervisor", "Supervise daily site operations", "₹20,000 - ₹40,000"),
        ("Structural Engineer", "Engineering", "Design structural frameworks", "₹45,000 - ₹90,000"),
    ]

    # ================= JOB DETAILS POPUP =================
    def show_details(title, dept, desc, salary):
        top = Toplevel(win)
        top.title("Job Details")
        top.geometry("450x300")
        top.config(bg="white")

        Label(top, text=title, font=("Arial", 14, "bold"), bg="white", fg="#2c3e50").pack(pady=10)

        Label(top, text=f"Department: {dept}",font=("Arial", 11),bg="white").pack(anchor="w", padx=20)

        Label(top, text=f"Salary: {salary}", font=("Arial", 11), bg="white").pack(anchor="w", padx=20, pady=5)

        Label(top, text="Job Description:", font=("Arial", 11, "bold"), bg="white").pack(anchor="w", padx=20)

        Label(top, text=desc, font=("Arial", 10), bg="white", wraplength=400, justify=LEFT).pack(padx=20, pady=10)

        Button(top, text="Apply Now", bg="#2ecc71", fg="white",  font=("Arial", 10, "bold"), command=lambda: messagebox.showinfo("Applied", "Application Submitted!")).pack(pady=10)

        Button(top, text="Close", bg="#e74c3c", fg="white", command=top.destroy).pack()

    # ================= JOB CARDS =================
    card_frame = Frame(main, bg="#eef3f7")
    card_frame.pack()

    row = 0
    col = 0

    for title, dept, desc, salary in jobs:

        card = Frame(card_frame, bg="white", width=340, height=150, relief=RIDGE, bd=1)
        card.grid(row=row, column=col, padx=12, pady=12)
        card.pack_propagate(False)

        Label(card, text=title, font=("Arial", 12, "bold"), bg="white", fg="#2c3e50").pack(anchor="w", padx=10, pady=5)

        Label(card, text=dept, font=("Arial", 10), bg="white", fg="#7f8c8d").pack(anchor="w", padx=10)

        Label(card, text=salary, font=("Arial", 10, "bold"), bg="white", fg="#27ae60").pack(anchor="w", padx=10, pady=5)

        Button(card, text="View Details", bg="#3498db", fg="white", font=("Arial", 9, "bold"), command=lambda t=title, d=dept, ds=desc, s=salary: show_details(t, d, ds, s)).pack(pady=10)

        col += 1
        if col == 3:
            col = 0
            row += 1

    # ================= CLOSE BUTTON =================
    Button(win, text="Close Window",  bg="#e74c3c", fg="white",  font=("Arial", 10, "bold"),  command=win.destroy).pack(pady=10)

    win.mainloop()



#===============================================================================================================
              # apply_job
#===============================================================================================================

def apply_job(parent_window=None, title="Apply Job"):
    win = Toplevel(parent_window) if parent_window else Tk()
    win.title(title)
    win.geometry("500x450")
    win.config(bg="#f4f6f8")

    # ---------------- HEADER ----------------
    header = Frame(win, bg="#1e3a5f", height=60)
    header.pack(fill=X)

    Label(header, text="Job Application Form",bg="#1e3a5f", fg="white",font=("Arial", 16, "bold")).pack(pady=15)

    # ---------------- FORM ----------------
    form = Frame(win, bg="#f4f6f8")
    form.pack(pady=20)

    Label(form, text="Full Name", bg="#f4f6f8").grid(row=0, column=0, sticky=W, pady=5)
    name_entry = Entry(form, width=35)
    name_entry.grid(row=0, column=1)

    Label(form, text="Email", bg="#f4f6f8").grid(row=1, column=0, sticky=W, pady=5)
    email_entry = Entry(form, width=35)
    email_entry.grid(row=1, column=1)

    Label(form, text="Phone", bg="#f4f6f8").grid(row=2, column=0, sticky=W, pady=5)
    phone_entry = Entry(form, width=35)
    phone_entry.grid(row=2, column=1)

    Label(form, text="Position", bg="#f4f6f8").grid(row=3, column=0, sticky=W, pady=5)
    position_entry = Entry(form, width=35)
    position_entry.grid(row=3, column=1)

    # ---------------- SUBMIT FUNCTION ----------------
    def submit_application():
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        position = position_entry.get()

        if name == "" or email == "" or phone == "" or position == "":
            messagebox.showerror("Error", "Please fill all fields!")
        else:
            messagebox.showinfo(
                "Success",
                f"Application Submitted!\n\nName: {name}\nPosition: {position}"
            )
            win.destroy()

    # ---------------- BUTTON ----------------
    Button(win, text="Submit Application", bg="#2a9d8f", fg="white", font=("Arial", 11, "bold"), padx=10, pady=5, command=submit_application).pack(pady=20)

    # Close Button
    Button(win, text="Close", bg="#c0392b", fg="white", command=win.destroy).pack()

    win.mainloop()



#===============================================================================================================
      #join_our_team
#=================================================================================================================

def join_our_team(parent_window=None):
    win = Toplevel(parent_window) if parent_window else Tk()
    win.title("Join Our Team")
    win.geometry("520x520")
    win.config(bg="#f4f6f8")

    # ---------------- HEADER ----------------
    header = Frame(win, bg="#1e3a5f", height=70)
    header.pack(fill=X)

    Label(header, text="Join Our Team", bg="#1e3a5f", fg="white", font=("Arial", 18, "bold")).pack(pady=18)

    # ---------------- FORM FRAME ----------------
    form = Frame(win, bg="#f4f6f8")
    form.pack(pady=20)

    Label(form, text="Full Name", bg="#f4f6f8", font=("Arial", 10)).grid(row=0, column=0, sticky=W, pady=6)
    name_entry = Entry(form, width=35)
    name_entry.grid(row=0, column=1)

    Label(form, text="Email", bg="#f4f6f8", font=("Arial", 10)).grid(row=1, column=0, sticky=W, pady=6)
    email_entry = Entry(form, width=35)
    email_entry.grid(row=1, column=1)

    Label(form, text="Phone", bg="#f4f6f8", font=("Arial", 10)).grid(row=2, column=0, sticky=W, pady=6)
    phone_entry = Entry(form, width=35)
    phone_entry.grid(row=2, column=1)

    Label(form, text="Skills", bg="#f4f6f8", font=("Arial", 10)).grid(row=3, column=0, sticky=W, pady=6)
    skills_entry = Entry(form, width=35)
    skills_entry.grid(row=3, column=1)

    Label(form, text="Experience (Years)", bg="#f4f6f8", font=("Arial", 10)).grid(row=4, column=0, sticky=W, pady=6)
    exp_entry = Entry(form, width=35)
    exp_entry.grid(row=4, column=1)

    Label(form, text="Why Join Us?", bg="#f4f6f8", font=("Arial", 10)).grid(row=5, column=0, sticky=W, pady=6)
    reason_entry = Entry(form, width=35)
    reason_entry.grid(row=5, column=1)

    # ---------------- SUBMIT FUNCTION ----------------
    def submit_form():
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        skills = skills_entry.get()
        exp = exp_entry.get()
        reason = reason_entry.get()

        if name == "" or email == "" or phone == "":
            messagebox.showerror("Error", "Please fill required fields!")
        else:
            messagebox.showinfo(
                "Submitted",
                f"Welcome to Our Team!\n\n{name} your application is received."
            )
            win.destroy()

    # ---------------- BUTTONS ----------------
    Button(win, text="Submit Application", bg="#2a9d8f", fg="white", font=("Arial", 11, "bold"), padx=12, pady=6, command=submit_form).pack(pady=15)

    Button(win, text="Close", bg="#c0392b", fg="white", command=win.destroy).pack()

    win.mainloop()



#========================================================================================================
                    # internships
#==========================================================================================================


def internships_window(parent_window=None):
    win = Toplevel(parent_window) if parent_window else Tk()
    win.title("Internships")
    win.geometry("800x600")
    win.config(bg="#f4f6f8")

    # ---------------- HEADER ----------------
    header = Frame(win, bg="#1e3a5f", height=70)
    header.pack(fill=X)

    Label(header, text="Available Internships", bg="#1e3a5f", fg="white", font=("Arial", 18, "bold")).pack(pady=18)

    # ---------------- FORM FUNCTION ----------------
    def open_form(title):
        form = Toplevel(win)
        form.title(f"Apply - {title}")
        form.geometry("450x450")
        form.config(bg="#f4f6f8")

        header = Frame(form, bg="#1e3a5f", height=60)
        header.pack(fill=X)

        Label(header, text=f"{title} Application", bg="#1e3a5f", fg="white", font=("Arial", 14, "bold")).pack(pady=15)

        body = Frame(form, bg="#f4f6f8")
        body.pack(pady=20)

        Label(body, text="Full Name", bg="#f4f6f8").grid(row=0, column=0, sticky=W, pady=5)
        name = Entry(body, width=30)
        name.grid(row=0, column=1)

        Label(body, text="Email", bg="#f4f6f8").grid(row=1, column=0, sticky=W, pady=5)
        email = Entry(body, width=30)
        email.grid(row=1, column=1)

        Label(body, text="Phone", bg="#f4f6f8").grid(row=2, column=0, sticky=W, pady=5)
        phone = Entry(body, width=30)
        phone.grid(row=2, column=1)

        Label(body, text="Skills", bg="#f4f6f8").grid(row=3, column=0, sticky=W, pady=5)
        skills = Entry(body, width=30)
        skills.grid(row=3, column=1)

        def submit():
            if name.get() == "" or email.get() == "" or phone.get() == "":
                messagebox.showerror("Error", "Please fill all required fields!")
            else:
                messagebox.showinfo(
                    "Success",
                    f"Application submitted for {title}!"
                )
                form.destroy()

        Button(form, text="Submit Application", bg="#2a9d8f", fg="white", font=("Arial", 11, "bold"), command=submit).pack(pady=15)

        Button(form, text="Close", bg="#c0392b", fg="white", command=form.destroy).pack()

    # ---------------- CONTENT AREA ----------------
    content = Frame(win, bg="#f4f6f8")
    content.pack(pady=20, fill=BOTH, expand=True)

    internships = [
        ("Python Developer Intern", "Work on real Python projects and APIs."),
        ("Web Development Intern", "HTML, CSS, JS frontend & backend tasks."),
        ("UI/UX Design Intern", "Design modern app & website interfaces."),
        ("Data Analyst Intern", "Work with Excel, SQL, and dashboards."),
        ("AI/ML Intern", "Build simple machine learning models.")
    ]

    # ---------------- CARDS ----------------
    for i, (title, desc) in enumerate(internships):
        card = Frame(content, bg="white", bd=1, relief=SOLID)
        card.pack(pady=10, padx=20, fill=X)

        Label(card, text=title, bg="white", fg="#1e3a5f", font=("Arial", 12, "bold")).pack(anchor=W, padx=10, pady=5)

        Label(card, text=desc, bg="white", fg="#444", font=("Arial", 10)).pack(anchor=W, padx=10)

        Button(card, text="Apply Now", bg="#2a9d8f", fg="white", font=("Arial", 10, "bold"), command=lambda t=title: open_form(t)).pack(anchor=E, padx=10, pady=8)

    # ---------------- CLOSE BUTTON ----------------
    Button(win,  text="Close",  bg="#c0392b",  fg="white",  font=("Arial", 10, "bold"),  command=win.destroy).place(x=20,y=20)
    win.mainloop()


#=================================================================================================
  # employee_benefits
#=================================================================================================
    
def employee_benefits_window(parent_window=None):
    win = Toplevel(parent_window) if parent_window else Tk()
    win.title("Employee Benefits")
    win.geometry("850x600")
    win.config(bg="#f4f6f8")

    # ---------------- HEADER ----------------
    header = Frame(win, bg="#1e3a5f", height=70)
    header.pack(fill=X)

    Label(header, text="Employee Benefits", bg="#1e3a5f", fg="white", font=("Arial", 18, "bold")).pack(pady=18)

    # ---------------- CONTENT ----------------
    content = Frame(win, bg="#f4f6f8")
    content.pack(pady=20, fill=BOTH, expand=True)

    benefits = [
        ("💰 Competitive Salary", "Attractive salary packages based on skills & experience."),
        ("🏥 Health Insurance", "Medical coverage for employees and family."),
        ("📈 Career Growth", "Training programs and promotion opportunities."),
        ("🏖 Paid Leaves", "Annual paid leaves, sick leaves, and holidays."),
        ("🏠 Work Flexibility", "Hybrid and remote working options available."),
        ("🎓 Skill Development", "Free workshops, certifications, and learning support."),
        ("🏆 Performance Bonus", "Extra rewards for top-performing employees."),
        ("🤝 Friendly Environment", "Supportive and professional workplace culture.")
    ]

    # ---------------- CARDS ----------------
    for title, desc in benefits:
        card = Frame(content, bg="white", bd=1, relief=SOLID)
        card.pack(pady=10, padx=20, fill=X)

        Label(card, text=title, bg="white", fg="#1e3a5f", font=("Arial", 12, "bold")).pack(anchor=W, padx=10, pady=5)

        Label(card, text=desc, bg="white", fg="#444", font=("Arial", 10)).pack(anchor=W, padx=10, pady=5)

    # ---------------- CLOSE BUTTON ----------------
    Button(win, text="Close",  bg="#c0392b",  fg="white",  font=("Arial", 10, "bold"),  command=win.destroy).place(x=20,y=20)
    win.mainloop()


#================================================================================================
 # Phone number
#================================================================================================


def company_contact_window(parent_window=None):
    win = Toplevel(parent_window) if parent_window else Tk()
    win.title("Contact Us")
    win.geometry("400x300")
    win.config(bg="#f4f6f8")

    # ---------------- HEADER ----------------
    header = Frame(win, bg="#1e3a5f", height=70)
    header.pack(fill=X)

    Label(header, text="Contact Our Company", bg="#1e3a5f", fg="white", font=("Arial", 16, "bold")).pack(pady=18)

    # ---------------- CONTENT ----------------
    content = Frame(win, bg="#f4f6f8")
    content.pack(expand=True)

    Label(content, text="📞 Company Contact Number", bg="#f4f6f8", fg="#1e3a5f", font=("Arial", 12, "bold")).pack(pady=15)

    contact_number = "📱 +91 98765 43210"

    Label(content, text=contact_number, bg="#f4f6f8", fg="#2a9d8f", font=("Arial", 16, "bold")).pack(pady=10)

    Label(content, text="Call us for any inquiry related to jobs,\nprojects, internships or services.", bg="#f4f6f8", fg="#444", font=("Arial", 10), justify=CENTER).pack(pady=10)

    # ---------------- CLOSE BUTTON ----------------
    Button(win, text="Close", bg="#c0392b", fg="white", font=("Arial", 10, "bold"), command=win.destroy).pack(pady=15)

    win.mainloop()


#===================================================================================================
           # company_email
#===================================================================================================


def company_email_window(parent_window=None):
    win = Toplevel(parent_window) if parent_window else Tk()
    win.title("Email Us")
    win.geometry("520x500")
    win.config(bg="#f4f6f8")

    # ---------------- HEADER ----------------
    header = Frame(win, bg="#1e3a5f", height=70)
    header.pack(fill=X)

    Label(header,text="Contact via Email",bg="#1e3a5f",fg="white",font=("Arial", 16, "bold")).pack(pady=18)

    # ---------------- CONTENT ----------------
    content = Frame(win, bg="#f4f6f8")
    content.pack(expand=True)

    Label(content, text="📧 Official Email Address", bg="#f4f6f8", fg="#1e3a5f", font=("Arial", 12, "bold")).pack(pady=15)

    email_id = "📩 info@DwivediConstructionCompany.com"

    Label(content, text=email_id, bg="#f4f6f8", fg="#2a9d8f", font=("Arial", 14, "bold")).pack(pady=10)

    Label(content, text="Send us an email for inquiries,\nsupport, jobs, and project details.", bg="#f4f6f8", fg="#444", font=("Arial", 10), justify=CENTER).pack(pady=10)

    # ---------------- CLOSE BUTTON ----------------
    Button(win, text="Close", bg="#c0392b", fg="white", font=("Arial", 10, "bold"), command=win.destroy).pack(pady=15)

    win.mainloop()



#================================================================================================
            # office_locations
#================================================================================================

def office_locations_window(parent_window=None):
    win = Toplevel(parent_window) if parent_window else Tk()
    win.title("Office Locations")
    win.geometry("900x650")
    win.config(bg="#f4f6f8")

    # ================= HEADER =================
    header = Frame(win, bg="#1e3a5f", height=60)
    header.pack(fill=X)

    Label( header, text="Our Office Locations", bg="#1e3a5f", fg="white", font=("Arial", 15, "bold") ).pack(pady=15)

    # ================= MAIN CONTENT =================
    main_frame = Frame(win, bg="#f4f6f8")
    main_frame.pack(fill=BOTH, expand=True, padx=15, pady=10)

    # ================= MAIN BRANCH =================
    main_branch = Frame(main_frame, bg="white", bd=1, relief=SOLID)
    main_branch.pack(fill=X, pady=8)

    Label(main_branch,text="🏢 Head Office / Main Branch",bg="white",fg="#1e3a5f",font=("Arial", 11, "bold")).pack(anchor=W, padx=10, pady=5)

    Label( main_branch, text="Global Construction Pvt. Ltd.\n""Business Tower, MG Road,\n""Pune, Maharashtra, India",bg="white", fg="#444",
    justify=LEFT, font=("Arial", 8)).pack(anchor=W, padx=15, pady=3)

    # ================= OTHER OFFICES =================
    Label(  main_frame,  text="🌍 Other Office Locations",  bg="#f4f6f8",  fg="#1e3a5f",  font=("Arial", 11, "bold")).pack(anchor=W, pady=8)

    offices = [
        ("Mumbai Office", "Mumbai, Maharashtra, India"),
        ("Delhi Office", "New Delhi, India"),
        ("Bangalore Office", "Bangalore, Karnataka, India"),
        ("Dubai Branch", "Dubai, UAE"),
        ("New York Branch", "New York, USA"),
        ("London Branch", "London, UK"),
        ("Singapore Branch", "Singapore"),
        ("Tokyo Branch", "Tokyo, Japan")
    ]

    for office, location in offices:
        card = Frame(main_frame, bg="white", bd=1, relief=SOLID)
        card.pack(fill=X, pady=4)

        Label( card, text=office, bg="white", fg="#1e3a5f", font=("Arial", 9, "bold")).pack(anchor=W, padx=10, pady=3)

        Label( card, text=location, bg="white", fg="#555", font=("Arial", 8) ).pack(anchor=W, padx=18, pady=2)

    # ================= OPERATING AREAS =================
    countries_frame = Frame(main_frame, bg="white", bd=1, relief=SOLID)
    countries_frame.pack(fill=X, pady=10)

    Label( countries_frame, text="🌎 Countries & States Where We Operate", bg="white", fg="#1e3a5f", font=("Arial", 10, "bold") ).pack(anchor=W, padx=10, pady=5)

    operation_text = (
        "Countries: India, USA, UK, UAE, Singapore, Japan\n\n"
        "Indian States: Maharashtra, Karnataka, Delhi,\n"
        "Gujarat, Tamil Nadu"
    )

    Label( countries_frame, text=operation_text, bg="white", fg="#444", justify=LEFT, font=("Arial", 8)).pack(anchor=W, padx=15, pady=5)

    # ================= CLOSE BUTTON =================
    Button(win, text="Close", bg="#c0392b", fg="white", font=("Arial", 9, "bold"), padx=10, pady=4, command=win.destroy).place(x=20,y=20)

    win.mainloop()




#=====================================================================================================================
               # whatsapp
#=====================================================================================================================

def whatsapp_window(parent_window=None):
    win = Toplevel(parent_window) if parent_window else Tk()
    win.title("WhatsApp Support")
    win.geometry("600x600")
    win.config(bg="#eef7f2")

    # ================= HEADER =================
    header = Frame(win, bg="#075E54", height=70)
    header.pack(fill=X)

    Label( header,  text="WhatsApp Support", bg="#075E54", fg="white", font=("Arial", 18, "bold")).pack(pady=18)

    # ================= MAIN CONTENT =================
    content = Frame(win, bg="#eef7f2")
    content.pack(expand=True, fill=BOTH, padx=20, pady=20)

    # ================= CARD =================
    card = Frame(content, bg="#ffffff", bd=2, relief=RIDGE)
    card.pack(fill=BOTH, expand=True)

    Label( card, text="💬 Chat With Our Team", bg="#ffffff", fg="#128C7E", font=("Arial", 14, "bold") ).pack(pady=15)

    Label( card, text="For project inquiries, internships,\njob applications, and support.", bg="#ffffff", fg="#555555", font=("Arial", 9), justify=CENTER ).pack(pady=5)

    # ================= WHATSAPP NUMBER =================
    number_frame = Frame(card, bg="#DCF8C6", bd=1, relief=SOLID)
    number_frame.pack(pady=15, padx=20, fill=X)

    Label( number_frame, text="📱 WhatsApp Number", bg="#DCF8C6", fg="#075E54", font=("Arial", 10, "bold")).pack(pady=5)

    Label(number_frame,text="+91 98765 43210",bg="#DCF8C6",fg="#25D366",font=("Arial", 16, "bold")).pack(pady=8)

    # ================= OFFICE TIMING =================
    timing = Frame(card, bg="#E8F5E9")
    timing.pack(pady=10, padx=20, fill=X)

    Label(timing,text="🕒 Available Timing",bg="#E8F5E9",fg="#1B5E20",font=("Arial", 10, "bold") ).pack(pady=4)

    Label( timing, text="Monday - Saturday\n9:00 AM to 7:00 PM", bg="#E8F5E9", fg="#444444", font=("Arial", 8)).pack(pady=4)

    # ================= BUTTONS =================
    btn_frame = Frame(card, bg="#ffffff")
    btn_frame.pack(pady=15)

    Button(btn_frame,text="Chat Now",bg="#25D366",fg="white",font=("Arial", 10, "bold"),padx=12,pady=5,relief=FLAT).grid(row=0, column=0, padx=10)

    Button( btn_frame, text="Close", bg="#d62828", fg="white", font=("Arial", 10, "bold"), padx=12, pady=5, relief=FLAT, command=win.destroy).grid(row=0, column=1, padx=10)

    win.mainloop()
    



# =================================================
# Main Page
# =================================================

def main_page(root):
    root.withdraw()

    main = Toplevel()

    main.geometry("1500x900")

    main.title("Main Page")

    bg2 = Image.open("image15.jpg")

    bg2 = bg2.resize((1500, 900))

    photo2 = ImageTk.PhotoImage(bg2)

    label2 = Label(main, image=photo2)

    label2.image = photo2

    label2.place(x=0, y=0, relwidth=1, relheight=1)

    
  
#====================================================
                         #Menu Bar#

    menu = Menu(main)
    main.config(menu=menu)
    #===========================================
                      #Homa#
    Home_menu = Menu(menu)
    menu.add_cascade(label="Home",menu=Home_menu)

    Home_menu.add_command(label="Dashboard",command=dashboard)
    Home_menu.add_command(label="Overview",command= overview_window)
    Home_menu.add_command(label="Latest Updates",command=latest_updates_window)
   
    Home_menu.add_command(label="Recent Projects",command=recent_projects_window)
    Home_menu.add_command(label="Site Progress",command=site_progress_window)
    Home_menu.add_command(label="Testimonials",command=testimonials_window)
    Home_menu.add_command(label="Quality Assurance",command=quality_assurance_window)
   #===========================================
                    #About Us#

    About_menu = Menu(menu)
    menu.add_cascade(label="About Us",menu=About_menu)

    About_menu.add_command(label="Company Profile",command=company_profile_window)
    About_menu.add_command(label="Our Mission",command= our_mission_window)
    About_menu.add_command(label="Our Vision",command=OUR_VISION_window)
    About_menu.add_command(label="Our Team",command=our_team_window)
    About_menu.add_command(label="Why Choose Us",command=why_choose_us_window)

     #===========================================
                    #Our Services#

    Our_Services_menu = Menu(menu)
    menu.add_cascade(label="Our Services",menu=Our_Services_menu)

    Our_Services_menu.add_command(label="Residential Construction",command=residential_construction_window)
    Our_Services_menu.add_command(label="Commercial Construction",command=commercial_construction_window)
    Our_Services_menu.add_command(label="Interior Design",command= interior_design_window)
    Our_Services_menu.add_command(label="Renovation",command=renovation_window)
    Our_Services_menu.add_command(label="3D Design",command=design3d_window)
    Our_Services_menu.add_command(label="Project Management",command=project_management_window)
    
     #===========================================
                    #Projects#

    Projects_menu = Menu(menu)
    menu.add_cascade(label="Projects",menu=Projects_menu)

    Projects_menu.add_command(label="Ongoing Projects",command=ongoing_projects_window)
    Projects_menu.add_command(label="Completed Projects",command=completed_projects_window)
    Projects_menu.add_command(label="Residential Projects",command=residential_projects_window)
    Projects_menu.add_command(label="Commercial Projects",command=commercial_projects_window)
    Projects_menu.add_command(label="Villa Projects",command=villa_projects_window)
    Projects_menu.add_command(label="Interior Projects",command=interior_projects_window)
    Projects_menu.add_command(label="Upcoming Projects",command=upcoming_projects_window)
    

 #===========================================
                    #Portfolio#

    Portfolio_menu = Menu(menu)
    menu.add_cascade(label="Portfolio",menu=Portfolio_menu)
    Portfolio_menu.add_command(label="Work Showcase",command=Work_Showcase)
    Portfolio_menu.add_command(label="Design Collection" , command=design_collection_window)
    Portfolio_menu.add_command(label="Building Concepts",command= building_concepts_window)
    Portfolio_menu.add_command(label="Visual Gallery",command=visual_gallery_window)
    Portfolio_menu.add_command(label="Creative Models",command=creative_models_window)
    
 #===========================================
                    #Clients#

    Clients_menu = Menu(menu)
    menu.add_cascade(label="Clients",menu=Clients_menu)
    Clients_menu.add_command(label="Our Clients",command=our_clients_window)
    Clients_menu.add_command(label="Client Reviews",command=client_reviews_window)
    Clients_menu.add_command(label="Testimonials",command=testimonials_window)
    Clients_menu.add_command(label="Happy Customers",command= happy_customers_window)
    Clients_menu.add_command(label="Feedback",command=feedback_window)

      
 #===========================================
                    #Careers#

    Careers_menu = Menu(menu)
    menu.add_cascade(label="Careers",menu=Careers_menu)
    Careers_menu.add_command(label="Job Openings",command=job_openings_window)
    Careers_menu.add_command(label="Apply Now",command=apply_job)
    Careers_menu.add_command(label="Join Our Team",command=join_our_team)
    Careers_menu.add_command(label="Internships",command=internships_window)
    Careers_menu.add_command(label="Employee Benefits",command=employee_benefits_window)

 #===========================================
                    #Contact Us#

    Contact_Us_menu = Menu(menu)
    menu.add_cascade(label="Contact Us",menu=Contact_Us_menu)
    Contact_Us_menu.add_command(label="Phone Number",command=company_contact_window)
    Contact_Us_menu.add_command(label="Email Address",command=company_email_window)
    Contact_Us_menu.add_command(label="Office Location",command=office_locations_window)
    Contact_Us_menu.add_command(label="WhatsApp",command=whatsapp_window)
    
 #==========================================
                 #Button 1 #
    p=Button(main,text="OPEN APARTMENTS", font=("Arial", 15, "bold"), bg="orange", fg="white", command=lambda: apartment1(main))

    p.place(x=20, y=180,width=250)
    
#==========================================
                 #Button 2 #
    button2 = Button( main, text="Row_Houses  Designs", font=("Arial Black", 15, "bold"), bg="orange", fg="white",command=lambda: Row_Houses1(main))

    button2.place(x=20, y=280,width=250)
    
#==========================================
                 #Button 3 #
    button3 = Button( main, text=" Villa designss", font=("Arial Black", 15, "bold"), bg="orange", fg="white" ,command= lambda:Villa1(main))

    button3.place(x=20, y=380,width=250)
    
#==========================================
                 #Button 4 #
    button4 = Button( main, text=" Hotal Designs", font=("Arial Black", 15, "bold"), bg="orange", fg="white" ,command=lambda:Hotal1(main))

    button4.place(x=20, y=480,width=250)

#==========================================
                 #Button 5 #
    button5 = Button( main, text="Modern Homes ", font=("Arial Black", 15, "bold"), bg="orange", fg="white",command=lambda: Homes1(main))

    button5.place(x=20, y=580,width=250)
 #==========================================
                 #Button 6 #
    button6 = Button( main, text="Office Designs ", font=("Arial Black", 15, "bold"), bg="orange", fg="white" ,command=lambda: Office1(main))

    button6.place(x=20, y=680,width=250)
# =========================================
 # SMALL COMPANY LOGO
 # =========================================

    img = PhotoImage(file="image16.png")

    small_logo = img.subsample(8, 8)

    logo_label = Label(main, image=small_logo, bg="white")
    logo_label.image = small_logo

    logo_label.place(x=800, y=20)

    # =========================================

   # =========================================
    # BACK BUTTON
    # =========================================

    back_button = Button(main,text="BACK",font=("Arial", 15, "bold"),bg="blue", fg="white", padx=20, pady=10, command=lambda: back_to_first(main, root) )

    back_button.place(x=1100, y=20)

    # =========================================
    # CLOSE BUTTON
    # =========================================

    close_button = Button( main, text="CLOSE",font=("Arial", 15, "bold"),bg="red", fg="white", padx=20,pady=10,command=main.destroy)

    close_button.place(x=1300, y=20)

   
# ====================================================
# BACK FUNCTION
# ====================================================

def back_to_first(main, root):

    main.destroy()

    root.deiconify()
      
    





                    

first_page()
