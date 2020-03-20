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

import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox

import os

import config
from converter import Converter


class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=tk.BOTH, expand=1)

        # champ input
        self.sentence = tk.StringVar()

        tk.Label(
            self,
            text="text",
            font=("Helvetica", 12)
        ).grid(row=1, sticky=tk.W, padx=10)

        tk.Entry(
            self,
            font=("Helvetica", 12),
            textvariable=self.sentence,
            width=60
        ).grid(row=2, columnspan=3, sticky=tk.W, padx=10)

        self.display = tk.IntVar()

        # champ save
        self.destinationFile = tk.StringVar()
        self.destinationFile.set("{}/new.gif".format(config.DEFAULT_OUTPUT))

        tk.Label(
            self,
            text="destination",
            font=("Helvetica", 12)
        ).grid(row=4, column=0, sticky=tk.W, padx=10)

        tk.Entry(
            self,
            font=("Helvetica", 12),
            textvariable=self.destinationFile,
            justify=tk.LEFT,
            width=38,
            state="readonly"
        ).grid(row=4, column=1, sticky=tk.W)

        tk.Button(
            self,
            text="Browse",
            font=("Helvetica", 12),
            command=self.clickSaveButton
        ).grid(row=4, column=2, padx=10)

        # champ modèle
        tk.Label(
            self,
            text="model",
            font=("Helvetica", 12)
        ).grid(row=5, column=0, sticky=tk.W, padx=10)

        models = os.listdir("resources")
        self.modelDir = tk.StringVar(self)
        self.modelDir.set(config.DEFAULT_INPUT)
        tk.OptionMenu(
            self,
            self.modelDir,
            *models
        ).grid(row=5, column=1, padx=10)

        # champ délai

        self.delay = tk.DoubleVar()
        self.delay.set(1.4)
        tk.Label(
            self,
            text="frame time (s)",
            font=("Helvetica", 12)
        ).grid(row=6, column=0, padx=10)

        tk.Scale(
            self,
            from_=0.2,
            to=4.2,
            resolution=0.2,
            variable=self.delay,
            orient=tk.HORIZONTAL,
            font=("Helvetica", 12),
            length=300
        ).grid(row=6, column=1, columnspan=2)

        # bouton d'activation

        tk.Checkbutton(
            self,
            text="Display after creation",
            font=("Helvetica", 12),
            variable=self.display
        ).grid(row=7, columnspan=2, sticky=tk.E)

        tk.Button(
            self,
            text="go",
            font=("Helvetica", 12),
            command=self.convertText
        ).grid(row=7, column=2, columnspan=2, padx=10, pady=10, sticky=tk.E)

    def clickSaveButton(self):
        self.destinationFile.set(filedialog.asksaveasfilename(
            initialdir=config.DEFAULT_OUTPUT,
            title="Select destination file",
            filetypes=(("gif files", "*.gif"), ("all files", "*.*"))
        ))

    def convertText(self):
        converter = Converter()
        converter.convert(
            self.sentence.get(),
            self.delay.get(),
            'resources/{}'.format(self.modelDir.get()),
            self.destinationFile.get()
        )
        if self.display.get() == 1:
            converter.display()
        else:
            messagebox.showinfo("GIF maker", "GIF created with success")


if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.wm_title("GIF en sémaphore !")
    root.mainloop()
