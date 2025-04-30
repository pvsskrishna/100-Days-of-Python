from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx= 50,pady=50) # Increase or create the extra space around the component,
# we can create this padding for individual components too

#Label

my_label = Label(text='I am Label', font=("Arial", 24, "bold"))
my_label.pack() # we should not use pack() and grid() methods together in same code

my_label["text"] = "New text"
my_label.config(text= "New text") #we can use either above line of code or this to configure label
my_label.grid(column=0,row=0)
my_label.config(padx= 10,pady=10)

#Button

def button_clicked():
    print("I got clicked")
    #my_label.config(text= "Button Got Clicked")
    my_label.config(text=input.get())


button = Button(text="Click me",command=button_clicked)
button.grid(column=1,row=1)
button.config(padx= 10,pady=10)


new_button = Button(text="New Button",command=button_clicked)
new_button.grid(column=2,row=0)
new_button.config(padx= 10,pady=10)

#Entry

input = Entry(width=50)
input.grid(column=3,row=2)





window.mainloop()
