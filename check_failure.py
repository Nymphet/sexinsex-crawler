import os, re
from urllib import parse

failcnt = 0
successcnt = 0
path = os.path.abspath('.')

for htmlfile in os.listdir(path+'/html/'):
    flag = True
    with open(path+'/html/'+htmlfile,'r',errors='ignore') as f:
        for line in f.readlines():
            p = re.search('<title> SexInSex! Board </title>', line)
            if p:
                print(parse.unquote_plus(htmlfile))
                flag = False
                failcnt += 1
                break
    if flag:
        print(parse.unquote_plus(htmlfile),'OK')
        successcnt += 1

print('Failed:',failcnt)
print('Succeeded:',successcnt)
