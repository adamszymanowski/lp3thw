# Learn Python 3 The Hard Way
Me doing exercises from the book.

### Exercise 23 Python Session

```
python3

a_pl = "ą"
a_pl.encode()
import sys
sys.byteorder
int.from_bytes(a_pl.encode(), byteorder="little")
int.from_bytes(a_pl.encode(), byteorder="big")
(0xc4 << 8) + 0x85
(0x85 << 8) + 0xc4
int.from_bytes(a_pl.encode(), byteorder="little") == (0x85 << 8) + 0xc4
int.from_bytes(a_pl.encode(), byteorder="big") == (0xc4 << 8) + 0x85
bin((0x85 << 8) + 0xc4)
0b1000010111000100

int.from_bytes(a_pl.encode(), byteorder="little") # I don't get this part bellow
chr(int.from_bytes(a_pl.encode(), byteorder="little"))
ord(chr(int.from_bytes(a_pl.encode(), byteorder="little")))
ord(a_pl)
chr(261)
```

Maybe read [this thing about python3 unicode](https://docs.python.org/3/howto/unicode.html) and try to understand it

### Exercise 26 - how to run
`python3 ex26.py test.txt`

### Exercise 46 - setup virtual environment - check skeleton directory
1. make sure you're at `lp3thw/projects` directory
2. `virtualenv --system-site-packages .`
3. `. bin/activate`
4. `pip install nose`
5. `cd skeleton`
6. `nosetests`

### Exercise 48, 49
are combined and are in `/projects/ex48`


# useful things
- `git status -uall`
- `$VIRTUAL_ENV` to check your virtualenv [Determine if Python is running inside virtualenv](https://stackoverflow.com/questions/1871549/determine-if-python-is-running-inside-virtualenv)
- activate/dectivate virtualenv
  -  activate: `. projects/bin/activate` **NOTE** after it will add `(projects)` to console prompt 
  - deactivate: `deactivate` **NOTE** added `(projects)` will disappear from console prompt