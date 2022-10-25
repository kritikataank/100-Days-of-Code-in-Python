from tkinter import *

def miles_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result.config(text=f"{km}")

#Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometer converter")
window.minsize()
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilomerter_label = Label(text="Km")
kilomerter_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_km)
calculate_button.grid(column=1, row=2)

window.mainloop()