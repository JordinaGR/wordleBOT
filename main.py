from selenium import webdriver
import pyautogui as auto
import time
import pandas as pd
from pynput.keyboard import Controller

keyboard = Controller()

driver = webdriver.Firefox(executable_path="/home/jordina/Desktop/new_programming/wordleBOT/geckodriver")
driver.get("https://gelozp.com/games/elmot/")
time.sleep(.5)

auto.moveTo(781,824)
auto.click()
auto.moveTo(1071, 329)
auto.click()

word = 'gutxo'
newword = ''
keyboard.type(word)
auto.press('enter')
time.sleep(1)

sol = []
lletres_verdes = []
lletres_grises = []
lletres_grises_pos = []
lletres_grogues = []
lletres_grogues_pos = []
xpos = [542, 610, 679, 746, 814]

def check_row(row, word):
    y = 364 + row*68
    for i in range(5):
        im = auto.screenshot()
        r, g, b = im.getpixel((xpos[i], y))
        if r == 60:
            lletres_verdes.append(word[i])
            sol.append([word[i], i])
        elif r == 214:
            lletres_grogues.append(word[i])
            lletres_grogues_pos.append([word[i], i])
        elif r == 120:
            lletres_grises.append(word[i])
            lletres_grises_pos.append([word[i], i])

def discard_words(sol):
    global df, lletres_grogues, lletres_grises, lletres_verdes
    
    # df = df[~df.paraules.str.contains('1')]
    for i in lletres_grises:
        if i in lletres_verdes:
            lletres_grises.remove(i)

            pos = []
            for j in range(len(sol)):
                letter = sol[j][0]
                index = sol[j][1]
                if letter == i:
                    pos.append(index)
            
            for k in range(5):
                if k not in pos:
                    df = df[~df.paraules.str[k].eq(i)]
    
    for i in lletres_grogues:
        if i in lletres_verdes:
            lletres_grogues.remove(i)

    for i in lletres_grises:
        df = df[~df.paraules.str.contains(i)]
    
    for i in lletres_grogues:
        df = df[df.paraules.str.contains(i)]
        for j in range(len(lletres_grogues_pos)):
            letter = lletres_grogues_pos[j][0]
            index = lletres_grogues_pos[j][1]
            if i == letter:
                df = df[~df.paraules.str[index].eq(letter)]

    for i in range(len(sol)):
        letter = sol[i][0]
        index = sol[i][1]
        df = df[df.paraules.str[index].eq(letter)]

def new_word(row):
    global df, newword
    for ind, w in df.iterrows():
        word = w['paraules']

        for i in range(6):
            auto.press('backspace')

        keyboard.type(word)
        auto.press('enter')
        time.sleep(.5)
        # auto.write(word)
        # auto.press('enter')
        # time.sleep(.5)

        im = auto.screenshot()
        r, g, b = im.getpixel((542, 364+row*68))
        if r != 255:
            newword = word
            break


check_row(0, word)
df = pd.read_csv('newdicc.csv')
discard_words(sol)
new_word(1)

check_row(1, newword)
discard_words(sol)
new_word(2)

check_row(2, newword)
discard_words(sol)
new_word(3)

check_row(3, newword)
discard_words(sol)
new_word(4)

check_row(4, newword)
discard_words(sol)
new_word(5)
