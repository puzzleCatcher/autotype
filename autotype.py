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

def insert_from_right(text, ch, num):
    index = len(text) - num
    if index < 0:
        index = 0
    return text[:index] + ch + text[index:]




#text = input("Input the text you want to type.\n")
#wpm = float(input("Input the WPM speed you want.\n"))


wpm = 150

cps = wpm * 5 / 60
delay = 1 / cps

pyautogui.PAUSE = 0



print("You got 5 seconds to get to your doc!")



sentences = text.split(".")
sentences.pop()
sentences = [s.strip() for s in sentences]
print(sentences)

len_sentences = [len(i) for i in sentences]
print(len_sentences)

s_order = [4, 7, 6, 9, 5, 8, 10, 1, 3, 2]
completed_sentences = []
completed_index = 0

left_shift = 0

reordered_text = ""
for i in range(len(s_order)):
    reordered_text += sentences[s_order[i] - 1].strip()
    reordered_text += ". "


text = reordered_text
print(text)
time.sleep(5)


i = 0
while i < len(text):
    time.sleep(delay)
    pyautogui.PAUSE = 0

    char = text[i]

    # Check for typos
    # if not text.startswith(curText):
    #     pyautogui.press('backspace')
    #     curText = curText[:-1]
    #     i -= 1
    #     continue


    # every sentence
    if i != 0 and text[i - 1] == ".":
        if left_shift > 0:
            for right in range(left_shift):
                pyautogui.press('right')
            left_shift = 0

        completed_sentences.append(s_order[completed_index])
        print(f"Completed sentences {completed_sentences}")

        completed_index += 1

        next_sentence = s_order[completed_index]
        print(f"Next sentence {next_sentence}")
        time.sleep(1)

        later_sentences = []
        for s in completed_sentences:
            if s > next_sentence:
                later_sentences.append(s)
                print()
        print(f"later sentences {later_sentences}")



        len_later_sentences = [(len_sentences[_ - 1] + 2) for _ in later_sentences]
        num_hit_left = sum(len_later_sentences)

        if num_hit_left != 0:

            for left in range(num_hit_left):
                pyautogui.press('left')
                left_shift += 1

        time.sleep(1)



    if i != 0 and curText[-1] == " ":
        if random.random() <= 0.02:
            next_word = get_next_word(text, curText)
            wrong_word = typo_word(next_word)

            # type the wrong word
            for letter in wrong_word:
                pyautogui.press(letter)
                curText = insert_from_right(curText, letter, left_shift)
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
                curText = insert_from_right(curText, letter, left_shift)
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
        curText = insert_from_right(curText, typoKey(char), left_shift)

    else:
        if char.isupper():
            pyautogui.keyDown('shift')
            pyautogui.press(char.upper())
            pyautogui.keyUp('shift')
        else:
            pyautogui.press(char)
        curText = insert_from_right(curText, char, left_shift)

    i += 1