import crypt
import os
import random


def salt():
    znaki = 'abcdefghijklmnopqrstuvwxyz' \
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
            '0123456789/.'
    return random.choice(znaki) + random.choice(znaki)


class HtpasswdFile:

    def __init__(self, filename, create=False):
        self.entries = []
        self.filename = filename
        if not create:
            if os.path.exists(self.filename):
                self.load()
            else:
                raise Exception("nie istnieje plik")

    def load(self):
        lines = open(self.filename, 'r').readlines()
        self.entries = []
        for line in lines:
            username, pwhash = line.split(':')
            entry = [username, pwhash.rstrip()]
            self.entries.append(entry)

    def save(self):
        open(self.filename, 'w').writelines(["%s:%s\n" % (entry[0], entry[1]) for entry in self.entries])

    def update(self, username, pwhash):
        # pwhash = crypt.crypt(pwhash, salt())
        matching_entries = [entry for entry in self.entries
                            if entry[0] == username]

        if matching_entries:
            matching_entries[0][1] = pwhash
        else:
            self.entries.append([username, pwhash])

    def delete(self, username):
        self.entries = [entry for entry in self.entries
                        if entry[0] != username]


if __name__ == "__main__":
    htp = HtpasswdFile('db')
    htp.update('adam', 'dupa')
    htp.save()
