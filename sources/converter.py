#! /usr/bin/python3

"""Copyright (C) 2020  Silvère du Gardin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import os
import subprocess
import sys
from glob import glob

import imageio

CONV_LETTER = {
    "a": "A",
    "A": "A",
    "à": "A",
    "1": "A",
    "b": "B",
    "B": "B",
    "2": "B",
    "c": "C",
    "C": "C",
    "ç": "C",
    "3": "C",
    "d": "D",
    "D": "D",
    "4": "D",
    "e": "E",
    "E": "E",
    "é": "E",
    "è": "E",
    "ê": "E",
    "5": "E",
    "f": "F",
    "F": "F",
    "6": "F",
    "g": "G",
    "G": "G",
    "7": "G",
    "h": "H",
    "H": "H",
    "8": "H",
    "i": "I",
    "I": "I",
    "î": "I",
    "9": "I",
    "j": "J",
    "J": "J",
    "k": "K",
    "K": "K",
    "0": "K",
    "l": "L",
    "L": "L",
    "m": "M",
    "M": "M",
    "n": "N",
    "N": "N",
    "o": "O",
    "O": "O",
    "ô": "O",
    "p": "P",
    "P": "P",
    "q": "Q",
    "Q": "Q",
    "r": "R",
    "R": "R",
    "s": "S",
    "S": "S",
    "t": "T",
    "T": "T",
    "u": "U",
    "U": "U",
    "ù": "U",
    "v": "V",
    "V": "V",
    "w": "W",
    "W": "W",
    "x": "X",
    "X": "X",
    "y": "Y",
    "Y": "Y",
    "z": "Z",
    "Z": "Z",
    "alpha": "J",
    "num": "0",
}


class Converter:
    """Convertisseur d'une phrase (sous forme de string)
    en sémaphore (au format gif)"""

    def __init__(self):
        self.__sentence = ""

    def convert(self, sentence: str, delay: float, inputdir, outputfile):
        """Convertit sentence en gif

        sentence : la phrase à convertir
        delay: le temps d'affichage de chaque lettre en secondes
        inputdir: le répertoire où se trouvent les lettres sémaphore
        outputfile: le fichier de destination
        """
        self.__delay = delay

        # on a besoin de connaître la lettre précédente
        # pour supprimer les lettres doubles
        previous_letter = "0"

        # on veut savoir si on est en numérique ou en alphabétique
        numeric = False

        for letter in sentence:
            if letter.isdigit():
                if not numeric:
                    # pour le premier chiffre d'une séquence
                    # on bascule en numérique
                    self.__sentence += CONV_LETTER["num"]
                    numeric = True
                previous_letter = CONV_LETTER[letter]
                self.__sentence += previous_letter

            elif letter.isalpha():
                if numeric:
                    # après le dernier chiffre, on repasse en alphabétique
                    self.__sentence += CONV_LETTER["alpha"]
                    numeric = False
                elif previous_letter == CONV_LETTER[letter]:
                    # pas de double lettre en sémaphore
                    continue
                previous_letter = CONV_LETTER[letter]
                self.__sentence += previous_letter

            elif letter == "?":
                if previous_letter != "+":
                    # toujours un espace avant le ?
                    # en sémaphore
                    self.__sentence += "+"
                self.__sentence += "AR"
                previous_letter = "question"

            else:
                if previous_letter == "+":
                    continue
                previous_letter = "+"
                self.__sentence += previous_letter

        self.__sentence += "--"

        self.__location = (
            outputfile if outputfile.endswith(".gif") else "{}.gif".format(outputfile)
        )

        with imageio.get_writer(
            self.__location, mode="I", duration=self.__delay
        ) as gif:
            for letter in self.__sentence:
                for image in glob("{}/{}.*".format(inputdir, letter)):
                    try:
                        image = imageio.imread(image)
                    except ValueError:
                        continue
                    else:
                        break
                else:
                    raise FileNotFoundError(
                        "pas de fichier valide pour la lettre {}".format(letter)
                    )
                gif.append_data(image)

    def display(self):
        if sys.platform == "win32":
            os.startfile(self.__location)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, self.__location])
