import data as data
from playsound import playsound
import json

CLEAN = 'c'
NOISY = 'n'

media_src = ['./Media/sound1.mp3', './Media/sound2.mp3',  './Media/sound3.mp3', './Media/sound4.mp3',
             './Media/sound5.mp3']


def play(src, idx=0):
    if idx == len(src):
        print('All finished!!')
        return None
    playsound(src[idx])
    print("Is the sound noisy or clean? Please type 'n' for noisy and 'c' for clean !")
    value = input()
    while not (value == CLEAN or value == NOISY):
        print("Please type 'n' or 'c' !")
        value = input()
    else:
        print('Thank You, Your answer is saved as ' + value)
        play(src, idx + 1)


play(media_src)

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
