import eyed3
from datetime import date
import os


def check_dupes(cur_file: str) -> bool:
    cur_file = cur_file + '.mp3'
    result = False
    directory = os.listdir()
    for item in directory:
        if item == cur_file:
            result = True
    return result


filename = input('What is the name of the file?')
mp3file = eyed3.load(filename)

current_date = str(date.today())

mp3file.tag.title = current_date

new_name = current_date[5:] + '-' + current_date[0:4]
diff = 1
while check_dupes(new_name):
    new_name = new_name + f'({diff})'
    diff += 1

os.rename(filename, new_name + '.mp3')
