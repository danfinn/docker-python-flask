# Docker + Flask

A simple webapp that takes an integer and a character as input and builds a pyramid out of it.  For example, 5 and "a" would get you:

```
a
aa
aaa
aaaa
aaaaa
aaaa
aaa
aa
a
```

This is built using python + flask + docker + docker-compose.  It also uses redis as a web counter.

If you'd like to run this locally you can clone this repo, `cd docker-python-flask` and `docker-compose up`.  You'll then be able to access the webapp at http://127.0.0.1/.
