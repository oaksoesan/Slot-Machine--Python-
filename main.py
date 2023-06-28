MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("How much would you like to depost: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{str(MAX_LINES)}?)")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines

def get_bet():
    while True:
        bets = input(f"What would like to bet on each line? $")
        if bets.isdigit():
            bets = int(bets)
            if MIN_BET <= bets <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number")

    return bets
    




def main():
    balance = deposit()
    lines = get_number_of_lines()
    bets = get_bet()
    print(balance, lines, bets)
main()