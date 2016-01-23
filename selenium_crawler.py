from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import parse
from time import sleep

from config import username as cred_username
from config import password as cred_password
from config import sleeptime, start_tid, path
from crawler import generate_url, download, page

# download the start page
print('Downloading the first page...')
download(generate_url(start_tid,1))

print('OK. Extracting tids from the page')
start_page = page(start_tid,1)
start_page.extract_tids()

print('Extracted tids:')
print(start_page.extracted_tids)

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

# download html files

success_count = 0
failure_count = 0
t_count = len(start_page.extracted_tids)

print('Download started. Kill process to terminate. Ctrl-C to skip current task')

for tid in start_page.extracted_tids:
    try:
        url = generate_url(tid,1)
        if sleeptime:
            print('sleeping...')
            sleep(sleeptime)
        print('Downloading from:',url)
        browser.get(url)
        with open('%s/html/%s'%(path,parse.quote_plus(url)), 'w') as s:
            s.write(browser.page_source)
        success_count += 1
        print('OK',success_count,'/',t_count)
    except Exception as inst:
        print('There is an error:')
        print type(inst)
        print inst.args
        failure_count += 1

print('Download finished,', success_count, 'succeeded,', failure_count, 'failed. Files saved in html folder, run extractor.py to extract the main content of downloaded files.')
browser.close()
