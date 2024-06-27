import random
import time
# import winsound  # Uncomment if you want to add sound effects on Windows

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def get_winnings(columns, lines, values, bet_amount):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol_to_match = columns[0][line]
        for col in columns:
            curr_symbol = col[line]
            if symbol_to_match != curr_symbol:
                break
        else:
            winnings += values[symbol_to_match] * bet_amount
            winning_lines.append(line + 1)

    return winnings, winning_lines

def slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(f"\033[1;33m{col[row]}\033[0m", end=" | ")
            else:
                print(f"\033[1;33m{col[row]}\033[0m")
    print()

def deposit():
    while True:
        amount = input("Enter the deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a valid amount.")

def get_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Enter a valid number of lines between 1 and {MAX_LINES}.")
        else:
            print("Please enter a number.")

def get_bet():
    while True:
        bet = input(f"How much do you want to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Enter a valid bet amount between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not enough balance. Your current balance is ${balance}.")
        else:
            break
    
    print(f"\nYou are betting ${bet} on each line. Total lines: {lines}. Total bet: ${total_bet}.")
    
    # Simulate spinning
    print("Spinning...", end="")
    for _ in range(3):
        time.sleep(2.0)
        print(".", end="")
    print("\n")
    
    # winsound.PlaySound("spin.wav", winsound.SND_ASYNC)  # Uncomment if you have a spin sound file
    slots = slot_machine(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    winnings, winning_lines = get_winnings(slots, lines, symbol_value, bet)
    print(f"\nCongratulations!!! You won ${winnings}.\nYou won on lines: ", *winning_lines)
    if winnings > 0:
        print("\033[1;32mYou win!\033[0m")
        # winsound.PlaySound("win.wav", winsound.SND_ASYNC)  # Uncomment if you have a win sound file
    else:
        print("\033[1;31mBetter luck next time!\033[0m")

    return winnings - total_bet

def main():
    balance = deposit()
    total_spins = 0
    total_winnings = 0
    total_bets = 0

    while True:
        print(f"Your current balance: ${balance}")
        ans = input("Press any key to spin (q to quit): ")
        if ans.lower() == 'q':
            break
        
        total_spins += 1
        result = spin(balance)
        balance += result
        total_winnings += max(result, 0)
        total_bets += abs(result) if result < 0 else 0
    
    print(f"\nYou exited with a balance of ${balance}.")
    print(f"Total spins: {total_spins}, Total winnings: ${total_winnings}, Total bets: ${total_bets}")

if __name__ == "__main__":
    main()
