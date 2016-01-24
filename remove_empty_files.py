# -*- coding: utf-8 -*-

''' Used to clear empty crdownload files in attachment folder caused by unknown bugs '''

import os

for i in os.listdir():
    if 'crdownload' in i:
        os.remove(i)
