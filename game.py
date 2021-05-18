from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title("Tic Tac Toe")
root.geometry("600x600")

# top_frame = Frame(root, )
# top_frame.place(relw)

########## PLAYER 1 === X  ########### PLAYER 2 ==== 0 ZER0

def random_values():
      global entry_list
      entry_list = [a_1, a_2, a_3, b_1, b_2, b_3, c_1, c_2, c_3]
      entry_list[0].set("x")
      # while True:
      #       computer_input = random.randint(0, 8)
      #       if entry_list[computer_input].get() == " " :
      #             entry_list[computer_input].set("x")
      #             break
      
      
      return

def stop_game():
      a_1 = Entry(game_frame, font=("bold", 35), state=DISABLED)
      b_1 = Entry(game_frame, font=("bold", 35), state = DISABLED)
      c_1 = Entry(game_frame, font=("bold", 35), state = DISABLED)
      a_1.place(relwidth = 0.3, relheight = 0.3, relx = 0, rely =0)
      b_1.place(relwidth = 0.3, relheight = 0.3, relx = 0.35, rely =0)
      c_1.place(relwidth = 0.3, relheight = 0.3, relx = 0.7, rely =0)


def vertical_win():

      if str(a_1.get()) == str(a_2.get()) and str(a_1.get()) == str(a_3.get() and a_1 != "x" or a_1 =="o"):
            return 1
      elif str(b_1.get()) == str(b_2.get()) and str(b_2.get()) == str(b_3.get() and b_1 != "x" or b_1 =="o"):
            return 1
      elif str(c_1.get()) == str(c_2.get()) and str(c_1.get()) == str(c_3.get() and c_1 != "x" or c_1 =="o"):
            return 1
      return 0
def horizontal_win():
      
      if str(a_1.get()) == str(b_1.get()) and str(a_1.get()) == str(c_1.get()) and a_1 == str('X') or a_1 == str('O'):
            return 1
      elif str(a_2.get()) == str(b_2.get()) and str(a_2.get()) == str(c_2.get() and a_2 != "x" or a_2 =="o"):
            return 1
      elif str(c_3.get()) == str(b_3.get()) and str(a_3.get()) == str(c_3.get() and c_3 != "x" or c_3 =="o"):
            return 1
      return 0
def digonal_win():
      if str(a_1.get()) == str(b_2.get()) and str(a_1.get()) == str(c_3.get() and a_1 != "x" or a_1 =="o"):
            return 1
      return 0

def result():
      if horizontal_win() == 1:
            messagebox.showinfo("win", "player won")
            print("horizontal win")
            stop_game()
            return
      elif vertical_win() == 1:
            messagebox.showinfo("win", "player won")
            print("vertical win")
            return 
      elif digonal_win() == 1:
            print("Diagonal win")
            messagebox.showinfo("win", "player won")
            return
      else:
            random_values()
            print("No win")
            return

Label(root, text="tic tac toe", font=("Bradley Hand ITC", 30) ).place(
      relwidth = 0.5, relheight=0.15, relx = 0.25, rely = 0.01
)
Label(root, text="Player 1: X", font=("bold", 12)).place(
      relwidth=0.2, relheight = 0.1, relx= 0.02, rely= 0.1
)
Label(root, text="Player 2: O", font=("bold", 12)).place(
      relwidth=0.2, relheight = 0.1, relx=0.78, rely= 0.1
)

game_frame = Frame(root, bg="black", bd=2)
game_frame.place(relwidth=0.6, relheight = 0.6, rely=0.2, relx=0.2)

###################### POSITION ENTRIES ###########################################

######## (A, B, C) HORIZONTAL ENTRIES COLUMNS ##########
######## (1, 2, 3) VERTICAL ENTRIES ROWS #########
a_1 = Entry(game_frame, font=("bold", 35))
b_1 = Entry(game_frame, font=("bold", 35))
c_1 = Entry(game_frame, font=("bold", 35))

a_1.place(relwidth = 0.3, relheight = 0.3, relx = 0, rely =0)
b_1.place(relwidth = 0.3, relheight = 0.3, relx = 0.35, rely =0)
c_1.place(relwidth = 0.3, relheight = 0.3, relx = 0.7, rely =0)

a_2 = Entry(game_frame, font=("bold", 35))
b_2 = Entry(game_frame, font=("bold", 35))
c_2 = Entry(game_frame, font=("bold", 35))

a_2.place(relwidth = 0.3, relheight = 0.3, relx = 0, rely =0.35)
b_2.place(relwidth = 0.3, relheight = 0.3, relx = 0.35, rely =0.35)
c_2.place(relwidth = 0.3, relheight = 0.3, relx = 0.7, rely =0.35)

a_3 = Entry(game_frame, font=("bold", 35))
b_3 = Entry(game_frame, font=("bold", 35))
c_3 = Entry(game_frame, font=("bold", 35))

a_3.place(relwidth = 0.3, relheight = 0.3, relx = 0, rely =0.7)
b_3.place(relwidth = 0.3, relheight = 0.3, relx = 0.35, rely =0.7)
c_3.place(relwidth = 0.3, relheight = 0.3, relx = 0.7, rely =0.7)

play_button = Button(root, text="play", font=("bold", 18), bd=2, command=result)
play_button.place(relwidth = 0.3, relheight = 0.1, relx = 0.35, rely =0.82)



root.mainloop()