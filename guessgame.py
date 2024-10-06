import tkinter
import tkinter.font as f
import random
import tkinter.messagebox
root = tkinter.Tk()
root.title("Guessing Game")
root.geometry("350x250")
number= random.randint(1,20)

def buttonconfirm():
    myName=textName.get()
    tkinter.messagebox.showinfo("hello","well"+"I am thinking of a number between 1 and 20 "+myName)

def checknumber():
    guess=textGuess.get()
    guess=int(guess)
    if guess == number:
        tkinter.messagebox.showinfo("Nice!","you guessed it right, good job!")
    elif guess>number:
        tkinter.messagebox.showinfo("almost","that number is too high")
    elif guess<number:
        tkinter.messagebox.showinfo("almost","that number to too low")




label=tkinter.Label(root,text="welcome to Akshay's guessing game")
label.pack()

labelName=tkinter.Label(root,text="what is your name")
labelName.place(x=10,y=60)

textName=tkinter.Entry(root,width=25)
textName.place(x=10,y=85)

btnOk = tkinter.Button(root,text="Ok",command=buttonconfirm)
btnOk.place(x=200,y=85,height=25,width=28)

labelGuess=tkinter.Label(root,text="Take a guess!")
labelGuess.place(x=10,y=150)

textGuess=tkinter.Entry(root,width=10)
textGuess.place(x=90,y=150)

btnCheck = tkinter.Button(root,text="Guess",command=checknumber)
btnCheck.place(x=200,y=150,height=25,width=35)



root.mainloop()
