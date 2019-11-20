#! /usr/bin/python3

from sys import argv
import os
import sys
import subprocess
import imageio

CONV_LETTER = {
    'a': 'A', 'A': 'A', '1': 'A',
    'b': 'B', 'B': 'B', '2': 'B',
    'c': 'C', 'C': 'C', '3': 'C',
    'd': 'D', 'D': 'D', '4': 'D',
    'e': 'E', 'E': 'E', '5': 'E',
    'f': 'F', 'F': 'F', '6': 'F',
    'g': 'G', 'G': 'G', '7': 'G',
    'h': 'H', 'H': 'H', '8': 'H',
    'i': 'I', 'I': 'I', '9': 'I',
    'j': 'J', 'J': 'J',
    'k': 'K', 'K': 'K', '0': 'K',
    'l': 'L', 'L': 'L',
    'm': 'M', 'M': 'M',
    'n': 'N', 'N': 'N',
    'o': 'O', 'O': 'O',
    'p': 'P', 'P': 'P',
    'q': 'Q', 'Q': 'Q',
    'r': 'R', 'R': 'R',
    's': 'S', 'S': 'S',
    't': 'T', 'T': 'T',
    'u': 'U', 'U': 'U',
    'v': 'V', 'V': 'V',
    'w': 'W', 'W': 'W',
    'x': 'X', 'X': 'X',
    'y': 'Y', 'Y': 'Y',
    'z': 'Z', 'Z': 'Z',
    'alpha': 'J',
    'num': '0'
}

DEFAULT_DELAY = 1.5


class GifMaker():

    def __init__(self, sentence, delay, inputdir, outputdir):
        self.__sentence = ""
        self.__delay = delay

        previous_letter = "0"
        numeric = False

        for letter in sentence:
            if letter.isdigit():
                if not numeric:
                    self.__sentence += CONV_LETTER['num']
                    numeric = True
                previous_letter = CONV_LETTER[letter]
                self.__sentence += previous_letter

            elif letter.isalpha():
                if numeric:
                    self.__sentence += CONV_LETTER['alpha']
                    numeric = False
                elif previous_letter == CONV_LETTER[letter]:
                    continue
                previous_letter = CONV_LETTER[letter]
                self.__sentence += previous_letter

            elif letter == "?":
                if previous_letter != '+':
                    self.__sentence += '+'
                self.__sentence += 'AR'
                previous_letter = 'question'

            else:
                if previous_letter == '+':
                    continue
                previous_letter = '+'
                self.__sentence += previous_letter

        self.__sentence += '++'

        self.__location = '%s/%s.gif' % (outputdir, self.__sentence)
        with imageio.get_writer(self.__location,
                                mode='I', duration=self.__delay) as gif:
            for letter in self.__sentence:
                image = imageio.imread('%s/%s.png' % (inputdir, letter))
                gif.append_data(image)

    def display(self):
        if sys.platform == "win32":
            os.startfile(self.__location)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, self.__location])
        print(self.__location)


if __name__ == "__main__":
    if len(argv) > 2:
        delay = argv[2] if argv[2].isdigit() else DEFAULT_DELAY
    else:
        delay = DEFAULT_DELAY
    sentence = argv[1]
    gif = GifMaker(sentence, delay, 'resources', 'cache')
    gif.display()
