.POSIX:

PREFIX = /usr/local

all: install

lttwitter-cli:

install:
        mkdir -p ${DESTDIR}${PREFIX}/bin
        cp twitter.py ${DESTDIR}${PREFIX}/bin/twitter.py

uninstall:
        rm -f ${DESTDIR}${PREFIX}/bin/twitter.py

.PHONY: all install uninstall
