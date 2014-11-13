import re

def url_check(url):
    regex = re.compile(r'^ftps?://(?:\w+(?:\w+)@)?\S+$')
    if regex.match(url):
        return True
    return False
