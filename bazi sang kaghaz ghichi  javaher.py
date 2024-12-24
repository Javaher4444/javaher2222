import turtle
import random

screen = turtle.Screen()
screen.title("Rock, Paper, Scissors Game")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(5)

def draw_rock():
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.circle(50)
    pen.write("Rock", align="center", font=("Arial", 16, "bold"))

def draw_paper():
    pen.clear()
    pen.penup()
    pen.goto(-30, 30)
    pen.pendown()
    for _ in range(2):
        pen.forward(60)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.penup()
    pen.goto(0, -50)
    pen.write("Paper", align="center", font=("Arial", 16, "bold"))

def draw_scissors():
    pen.clear()
    pen.penup()
    pen.goto(-20, 0)
    pen.pendown()
    pen.goto(20, 50)
    pen.penup()
    pen.goto(-20, 50)
    pen.pendown()
    pen.goto(20, 0)
    pen.penup()
    pen.goto(0, -60)
    pen.write("Scissors", align="center", font=("Arial", 16, "bold"))

choices = ["rock", "paper", "scissors"]

def play_game(user_choice):
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == "rock":
        draw_rock()
    elif user_choice == "paper":
        draw_paper()
    elif user_choice == "scissors":
        draw_scissors()
    
    pen.goto(0, -100)
    if user_choice == computer_choice:
        pen.write("It's a Tie!", align="center", font=("Arial", 16, "bold"))
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        pen.write("You Win!", align="center", font=("Arial", 16, "bold"))
    else:
        pen.write("You Lose!", align="center", font=("Arial", 16, "bold"))

while True:
    user_input = screen.textinput("Rock, Paper, Scissors", "Enter rock, paper, scissors, or exit:").lower()
    if user_input == "exit":
        print("Game Over!")
        break
    elif user_input in choices:
        play_game(user_input)
    else:
        print("Invalid choice. Try again.")

screen.bye()