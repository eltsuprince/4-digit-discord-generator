import random
import string
import pyperclip
from pynput import keyboard

def generate_code():
    chars = string.ascii_lowercase + string.digits
    code = random.choices(chars, k=4)
    if random.choice([True, False]):
        code[random.randrange(4)] = "."

    return "".join(code)

def on_press(key):
    if key == keyboard.Key.enter:
        code = generate_code()
        pyperclip.copy(code)
        print(f"copied: {code}")

print("injected")
print("esc for exit")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()