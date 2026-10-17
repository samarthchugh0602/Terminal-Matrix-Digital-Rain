import os
import random
import sys
import time

GREEN = "\033[32m"
LIGHT_GREEN = "\033[92m"
WHITE = "\033[97m"
RESET = "\033[0m"


def run_matrix():
    try:
        cols, rows = os.get_terminal_size()
    except OSError:
        cols, rows = 80, 24

    # Katakana characters combined with ASCII
    characters = [chr(i) for i in range(0x30A0, 0x30FF)] + list(
        "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*"
    )

    drops = [0] * cols

    # Hide cursor and clear screen
    sys.stdout.write("\033[?25l\033[2J")

    try:
        while True:
            # Move cursor back to top-left
            sys.stdout.write("\033[1;1H")
            buffer = []

            for r in range(rows - 1):
                row_chars = []
                for c in range(cols):
                    dist = r - drops[c]
                    if dist == 0:
                        row_chars.append(f"{WHITE}{random.choice(characters)}{RESET}")
                    elif dist == -1:
                        row_chars.append(f"{LIGHT_GREEN}{random.choice(characters)}{RESET}")
                    elif -12 < dist < 0:
                        row_chars.append(f"{GREEN}{random.choice(characters)}{RESET}")
                    else:
                        row_chars.append(" ")
                buffer.append("".join(row_chars))

            sys.stdout.write("\n".join(buffer))
            sys.stdout.flush()

            for i in range(cols):
                if drops[i] == 0:
                    if random.random() > 0.96:
                        drops[i] = 1
                else:
                    drops[i] += 1
                    if drops[i] > rows + 15:
                        drops[i] = 0

            time.sleep(0.04)

    except KeyboardInterrupt:
        # Restore cursor and clear screen on exit
        sys.stdout.write("\033[?25h\033[0m\033[2J\033[1;1H")
        print("Simulation ended.")


if __name__ == "__main__":
    run_matrix()
