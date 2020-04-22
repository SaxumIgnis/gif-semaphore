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

from sys import argv

from config import DEFAULT_DELAY
from converter import Converter

if __name__ == "__main__":
    if len(argv) > 1:
        if argv[1] == "show":
            with open("resources/LICENSE.md") as license:
                print(license.read())
        else:
            print(
                """
    GIF-semaphor  Copyright (C) 2020 Silvère du Gardin
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show' for details.
            """
            )
            if len(argv) > 2:
                delay = argv[2] if argv[2].isdigit() else DEFAULT_DELAY
            else:
                delay = DEFAULT_DELAY
            sentence = argv[1]
            gif = Converter()
            gif.convert(sentence, delay, "resources/basic", "gif/temp.gif")
            gif.display()
