import pyautogui
import time
import random

text = ""
try:
    with open('input.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        text = content
except FileNotFoundError:
    print(f"Error: The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


keys = [
  ["q","w","e","r","t","y","u","i","o","p"],
  ["a","s","d","f","g","h","j","k","l"],
  ["z","x","c","v","b","n","m"]
]

curText = ""

def typoKey(key):
    lKey = key.lower()

    for row in keys:
        if lKey in row:
            if (len(row) == row.index(lKey) + 1):
                return row[row.index(lKey) - 1]
            else:
                return row[row.index(lKey) + 1]

    return key

def typo_word(word):
    lWord = word.lower()
    finalWord = ""

    for letter in lWord:
        finalWord += typoKey(letter)

    return finalWord

def jumble_word(word):

    chars = list(word)
    random.shuffle(chars)
    jumbled_word = ''.join(chars)
    return jumbled_word

def get_next_word(full, typed):
    start = len(typed)
    rest = full[start:].lstrip()
    space = rest.find(" ")
    if space == -1:
        return rest
    return rest[:space]



#text = input("Input the text you want to type.\n")
#wpm = float(input("Input the WPM speed you want.\n"))


wpm = 150

cps = wpm * 5 / 60
delay = 1 / cps

pyautogui.PAUSE = 0



print("You got 5 seconds to get to your doc!")

time.sleep(2)

i = 0


while i < len(text):
    time.sleep(delay)
    pyautogui.PAUSE = 0

    char = text[i]

    print(curText, text)
    # Check for typos
    if not text.startswith(curText):
        pyautogui.press('backspace')
        curText = curText[:-1]
        i -= 1
        continue

    # stop a bit every sentence
    # if i != 0 and curText[i - 1] == ".":
    #     time.sleep(random.randint(2, 10))


    if i != 0 and curText[-1] == " ":
        if random.random() <= 0.02:
            next_word = get_next_word(text, curText)
            wrong_word = typo_word(next_word)

            # type the wrong word
            for letter in wrong_word:
                pyautogui.press(letter)
                curText += letter
                time.sleep(delay)


            time.sleep(1)
            i += len(next_word)
            continue
        elif random.random() <= 0.04:
            next_word = get_next_word(text, curText)
            wrong_word = jumble_word(next_word)

            # type the wrong word
            for letter in wrong_word:
                pyautogui.press(letter)
                curText += letter
                time.sleep(delay)

            time.sleep(1)
            i += len(next_word)

            continue

    if random.random() <= 0.08:
        if char.isupper():
            pyautogui.keyDown('shift')
            pyautogui.press(typoKey(char.lower()))
            pyautogui.keyUp('shift')
        else:
            pyautogui.press(typoKey(char))
        curText += typoKey(char)

    else:
        if char.isupper():
            pyautogui.keyDown('shift')
            pyautogui.press(char.upper())
            pyautogui.keyUp('shift')
        else:
            pyautogui.press(char)
        curText += char

    i += 1