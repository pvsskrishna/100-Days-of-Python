import tkinter
from tkinter import *
window = tkinter.Tk()
window.minsize(width=50,height=50)
window.title("Mile to Km Converter")
window.config(padx=50,pady=50)

#TODO 7: Create a mile to Km convertion function
def miles_to_km():
    mile = float(miles_input.get())
    km = round(mile * 1.609,2)
    output_label.config(text=f"{km}")

#TODO 1: Create "is equal to" Label
is_equal_label = Label(text="is equal to",font=("Arial",10,"bold"))
is_equal_label.grid(column=0,row=3)
is_equal_label.config(padx=10,pady=10)

#TODO 2: Create "input" or "Entry" field
miles_input = Entry(width=10)
miles_input.grid(column=1,row=2)

#TODO 3: Create "Output display" field
output_label = Label(text='0.0',font=("Arial",10,"bold"))
output_label.grid(column=1,row=3)

#TODO 4: Create "Calculate" button
calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=1,row=4)

#TODO 5: Create "Miles" Label
miles_label = Label(text='Miles',font=("Arial",8,"bold"))
miles_label.grid(column=2,row=2)


#TODO 6: Create "Km" Label
km_label = Label(text='Km',font=("Arial",8,"bold"))
km_label.grid(column=2,row=3)


window.mainloop()