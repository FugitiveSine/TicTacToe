import tkinter
from tkinter import ttk

#gameBoard = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
gameBoard1 = {}


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
        gameBoard1[specButton] = "X" #Sets value of specific button to X or O
    else:
        specButton.configure(text = "O")
        gameBoard1[specButton] = "O"
    counter += 1
    checkWinner()
    lockButton(specButton)
    

#test


buttons = []
counta = 0
for i in range(3):
    row_buttons = []
    for x in range(3):
        button = ttk.Button(window, text=" ")
        button.grid(row = i, column = x, padx=1, pady=1)
        button.bind('<Button-1>', lambda event, i = i, j = x:  changeText(i, j))
        row_buttons.append(button)
        counta = counta + 1
        gameBoard1[button] = ""#puts all buttons inside dictionary
        

    buttons.append(row_buttons)




def lockButton(specButton):
    specButton.config(state=tkinter.DISABLED)


def checkWinner():
    tie = True
    for i in range(3):
        #checks vertical
        if all(buttons[j][i]["text"] == "X" for j in range(3)):
            print("X is the winner")
            tie = False
        if all(buttons[j][i]["text"] == "O" for j in range(3)):
            print("O is the winner")
            tie = False
        #checks horizontal
        if all(buttons[i][j]["text"] == "O" for j in range(3)):
            print("O is the winner")
            tie = False
        if all(buttons[i][j]["text"] == "X" for j in range(3)):
            print("X is the winner")
            tie = False
        #check diagonal
    if buttons[0][0]["text"] == "X" and buttons[1][1]["text"] == "X" and buttons[2][2]["text"] == "X":
        print("X is the winner")
        tie = False
    if buttons[0][0]["text"] == "O" and buttons[1][1]["text"] == "O" and buttons[2][2]["text"] == "O":
        print("O is the winner")
        tie = False
    if buttons[0][2]["text"] == "O" and buttons[1][1]["text"] == "O" and buttons[2][0]["text"] == "O":
        print("O is the winner")
        tie = False
    if buttons[0][2]["text"] == "X" and buttons[1][1]["text"] == "X" and buttons[2][0]["text"] == "X":
        print("X is the winner")
        tie = False
    if all(button["state"] == tkinter.DISABLED for row in buttons for button in row)  and tie:
        print("It is a tie")
    

    
    #print(gameBoard1[specButton00])
    #print(gameBoard1[specButton11])
    #print(gameBoard1[specButton22])
    
    #if gameBoard1[specButton00] == "X" and:
        #print("Its an X")
    



            

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