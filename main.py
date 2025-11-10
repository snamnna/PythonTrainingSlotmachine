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

#Multiplier values, A is the most valuable
symbol_value = { 
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] #First check the row, then which line we're on
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = [] # columns not rows
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #copies the list
        for _ in range (rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) # delete the value so you don't use it again
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns): #transposing, matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): #enumerate gives 
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
       # print()


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

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You don't have enough money to bet this number. Your current balance is ${balance} ")
        else:
            break

    print(f"You're betting ${bet} on {lines} lines. Your total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings} on line(s)", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin, q to quit.")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")

main()