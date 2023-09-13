import random

MAX_LINES = 3
MAX_BETS = 200
MIN_BETS = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def redeposit(balance):
    if balance == 0:
        redeposit = input("Your balance is NIL, Would you like to deposit more?(No to discontinue.)")
        if redeposit != "No" or "NO" or "no":
            deposit()
        if redeposit == "No" or "NO" or "no":
            exit()


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)

    return winnings, winning_lines


def slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        # makes a copy of the all symbols list so as not to alter the all_symbols
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for _, column in enumerate(columns):
            if _ != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="\n")


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            # changing string to int for comparison.
            if amount > 0:
                break
            else:
                print("Amount must be greater then 0")
        else:
            print("Please enter a number.")

    return amount


def number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bets():
    while True:
        bets = input("What would you like to bet? $")
        if bets.isdigit():
            bets = int(bets)
            if MIN_BETS <= bets <= MAX_BETS:
                break
            else:
                print(f"Amount must be between ${MIN_BETS} - ${MAX_BETS}")
        else:
            print("Please enter a number.")

    return bets


def spin(balance):
    lines = number_of_lines()
    while True:
        bets = get_bets()
        total_bet = bets * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")

        else:
            break

    print(f"You are betting ${bets} on {lines} lines amounting to ${total_bet} ")

    slots = slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bets, symbol_values)
    print(f"You won ${winnings}!!")
    print(f"You won on lines : ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        s_pin = input("Press Enter to play (q to quit).")
        if s_pin == "q":
            break
        balance += spin(balance)
    print(f"You are left with ${balance}")


main()
