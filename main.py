import tkinter
from tkinter import ttk

gameBoard = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]


window = tkinter.Tk()
window.geometry("800x500")
window.title("TicTacToe")
#menuTitle = tkinter.Label(window, text="Welcome to TicTacToe!", font=('Arial', 18))
#menuTitle.grid()
def button_clicked(row, col):
    print(f"Button clicked at row {row}, column {col}")

counter = 0
def changeText(row, col):
    global counter
    specButton = buttons[row][col]
    if counter % 2 == 0:
        specButton["text"] = "X"
    else:
        specButton.configure(text = "O")
    counter += 1
    print(counter)

#test


buttons = []

for i in range(3):
    row_buttons = []
    for x in range(3):
        button = ttk.Button(window, text=" ")
        button.grid(row = i, column = x, padx=1, pady=1)
        button.bind('<Button-1>', lambda event, i = i, j = x: changeText(i, j))
        row_buttons.append(button)
    buttons.append(row_buttons)



            

#createMenu()



#selectionFrame = tkinter.Frame(root)
#selectionFrame.columnconfigure(0, weight = 1)
#selectionFrame.columnconfigure(1, weight = 1)


#playComputer = tkinter.Checkbutton(selectionFrame, text="Play against computer", font=('Arial', 12))
#playComputer.grid(row=0, column=0, sticky=tkinter.W+tkinter.E)

#play2P = tkinter.Checkbutton(selectionFrame, text="Play 2 Player locally", font=('Arial', 12))
#play2P.grid(row=0, column=1, sticky=tkinter.W+tkinter.E)

#selectionFrame.pack(padx=20, pady=0)
#btn1 = tkinter.Button(root, text="Here")
#btn1.pack(padx=10, pady=10)




window.mainloop()