import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def deposit():
    while True:
        amount = input("What would you like to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a valid number")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Pick a number of lines (1-" + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines ")
        else:
            print("Please enter a number ")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a valid number")
    
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You don't have enough money to bet this number. Your current balance is ${balance} ")
        else:
            break

    print(f"You're betting ${bet} on {lines} lines. Your total bet is ${total_bet}")


main()