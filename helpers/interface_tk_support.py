#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Jan 23, 2019 02:06:03 PM -03  platform: Linux
#    Jan 23, 2019 06:20:32 PM -03  platform: Linux

import sys
import tkinter as tk
def set_Tk_var():
    global che86
    che86 = tk.StringVar()
    global combobox
    combobox = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None




