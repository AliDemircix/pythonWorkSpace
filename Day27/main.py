from tkinter import *

window = Tk()
window.title("My First GUI App")
window.minsize(width=500,height=300)


#Label

my_label=Label(text="I am a label",font=("Arial",24,"bold"))
my_label.pack() # automaticly center
# my_label.pack(side="left") # align left

my_label["text"]="Updated Text" # update text of my_label

#Buttons

def button_clicked():
    print("I got clicked")
    input_value=input.get()
    my_label["text"]=input_value

button = Button(text="Click me ",command=button_clicked) # command fetch button_clicked function
button.pack()

#Entry
input = Entry(width=10)
input.pack()




window.mainloop()