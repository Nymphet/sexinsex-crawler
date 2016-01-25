from urllib import request, parse

from config import URLS_PREFIX



def generate_thread_url(tid,pid=1):
    return ''.join([URLS_PREFIX, 'thread-', str(tid), '-', str(pid), '-1.html'])

def generate_attachment_url(aid):
    return ''.join([URLS_PREFIX, 'attachment.php?aid=', aid])

def download_html(url):
    r = request.Request(url)
    r.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
    with request.urlopen(r) as f:
        with open('%s/html/%s'%(path,parse.quote_plus(url)), 'w') as s:
            s.write(f.read().decode(encoding=encoding,errors='ignore'))
