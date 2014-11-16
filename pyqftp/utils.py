import re
from enum import Enum

def url_check(url):
    regex = re.compile(r'^ftps?://(?:\w+(?:\w+)@)?\S+$')
    if regex.match(url):
        return True
    return False

class FileType(Enum):
    FILE = 0
    DIR = 1
    LINK = 2

class FtpFile:
    def __init__(self):
        self.filename = None
        self.filetype = FileType.FILE
        self.permission = 0o644

filetypes = {'-': FileType.FILE, 'd': FileType.DIR, 'l': FileType.LINK}
permissions = {
    '---': 0,
    '--x': 1,
    '-w-': 2,
    '-wx': 3,
    'r--': 4,
    'r-x': 5,
    'rw-': 6,
    'rwx': 7
}

def parse_ftp(filelist):
    files = []
    for line in filelist:
        f = FtpFile()
        linep = line.split()
        linep = linep[0:9]  # ignore space in file name
        linep[8] = line[line.index(linep[8]):]
        f.filetype = filetypes[linep[0][0]]
        f.filename = linep[8].encode('iso-8859-1').decode('utf-8')
        f.permission = (permissions[linep[0][1:4]]*8+permissions[linep[0][4:7]])*8+permissions[linep[0][7:10]]
        files.append(f)

    return files
