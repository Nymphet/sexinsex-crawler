# -*- coding:utf-8 -*-

''' Used to download html files directly (without login) from the board.
    This program will download threads with tid in the tids_list.
    tids list is loaded from ./pickle folder '''

import pickle

from config import path, sleeptime, start_tid
from utils import download_html, generate_thread_url

tids_list = pickle.load('%s/pickle/tids_from_thread_%s.p'%(path,start_tid))

for tid in tids_list:
    try:
        if sleeptime:
            print('sleeping...')
            sleep(sleeptime)
        print('downloading:',tid)
        download_html(generate_thread_url(tid,1))
    except Exception as inst:
        print('There is an error:')
        print(type(inst),inst.args)
