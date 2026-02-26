import time
import random


def animate():
    width = 40
    pos = random.randint(0, width - 1)
    direction = 1
    # Generate a random ID
    container_id = f"ID-{random.randint(100, 999)}"

    while True:
        # Create the visual line
        line = [" "] * width
        line[pos] = "●"
        display = "".join(line)

        # Print to terminal (clear line and print)
        print(f"\r{container_id} |{display}|", end="", flush=True)

        # bounce the ball
        pos += direction
        if pos >= width - 1 or pos <= 0:
            direction *= -1

        time.sleep(0.05)


if __name__ == "__main__":
    animate()
