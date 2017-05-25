# downloads a webpage or pulls from cache if exists
# input: url string
# output: content bytes

import os
import hashlib
import requests

CACHEDIR = 'CACHE'

# init

if not os.path.exists(CACHEDIR):
    os.makedirs(CACHEDIR)


def get(url):
#    urlhash = "".join(x for x in url if x.isalnum())    
    urlhash = hashlib.sha224(url.encode('utf-8')).hexdigest()
    if lookup(urlhash):
#        print('CACHE')
        return load(urlhash)
    else:
        print('DOWNLOAD')
        data = download(url)
        save(urlhash, data)
        return data
    
def download(url):
    r = requests.get(url)
#    print r.status_code
    return r.content
   
def lookup(urlhash):
    return os.path.exists(os.path.join(CACHEDIR, urlhash))

def save(urlhash, data):
    f = open(os.path.join(CACHEDIR, urlhash), 'wb')
    f.write(data)
    
def load(urlhash):
    f = open(os.path.join(CACHEDIR, urlhash), 'rb')
    return f.read()