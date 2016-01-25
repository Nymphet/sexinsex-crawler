# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import parse
from time import sleep
import pickle

from config import username as cred_username
from config import password as cred_password
from config import sleeptime, start_tid, path
from thread_tids_extractor import page
from utils import generate_thread_url, generate_attachment_url

# todo: add exception handling
print('Loading tids from thread %s'%start_tid)

with open('%s/pickle/aids_list.p'%path,'rb') as p:
    aids_list = pickle.load(p)

# start Chrome
browser = webdriver.Chrome()

# try to login
if cred_password and cred_username:
    browser.get('http://www.sexinsex.net/forum/logging.php?action=login')
    assert 'SexInSex' in browser.title

    username = browser.find_element_by_name('username')
    username.send_keys(cred_username)

    password = browser.find_element_by_name('password')
    password.send_keys(cred_password + Keys.RETURN)

print('Download started. Kill process to terminate. Ctrl-C to skip current task')

# download attachments
success_count = 0
failure_count = 0
a_count = len(aids_list)
for aid in aids_list:
    try:
        url = generate_attachment_url(aid)
        if sleeptime:
            print('sleeping...')
            sleep(sleeptime)
        print('Downloading from:',url)
        browser.get(url)
        success_count += 1
    except Exception as inst:
        print('There is an error:')
        print(type(inst))
        print(inst.args)
        failure_count += 1
print('Download finished,', success_count, 'succeeded,', failure_count, 'failed. Files saved in html folder.')

browser.close()
