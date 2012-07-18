#!/usr/bin/env python

import os.path
from ftplib import FTP


class Buffo(object):
    _ftp = None

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    @property
    def ftp(self):
        if self._ftp:
            return self._ftp
        ftp = FTP(self.host)
        ftp.login(self.username, self.password)
        self._ftp = ftp
        return self._ftp

    def upload(self, filepath, destination, overwrite=False):
        diretory, name = os.path.split(destination)
        files = self.list(diretory)
        if not files:
            self.ftp.mkd(diretory)
        elif name in files and not overwrite:
            raise ValueError('%s exits, set overwrite=True')

        ret = self.ftp.storbinary('STOR %s' % destination, open(filepath))
        return ret

    def delete(self, destination):
        pass

    def exists(self, destination):
        pass

    def list(self, *directory):
        try:
            return self.ftp.nlst(directory)
        except:
            return None
