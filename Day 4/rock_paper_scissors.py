from random import randint

arts = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """,
]

players_choice = int(
    input("What do you choose? Type 0 for Rock, "
          "1 for Paper or 2 for Scissors\n"))
computers_choice = randint(0, 2)

print(f"Your choice: {arts[players_choice]}")
print(30 * "-")
print(f"computer's choices {arts[computers_choice]}")


if players_choice == computers_choice:
    print("Tie")
elif players_choice == 0 and computers_choice == 2:
    print("You Win!!")
elif players_choice == 0 and computers_choice == 1:
    print("You lose.")
elif players_choice == 1 and computers_choice == 0:
    print("You Win!!")
elif players_choice == 0 and computers_choice == 2:
    print("You lose.")
elif players_choice == 2 and computers_choice == 1:
    print("You Win!!")
elif players_choice == 2 and computers_choice == 0:
    print("You lose.")
