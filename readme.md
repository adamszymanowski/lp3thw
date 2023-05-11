# Learn Python 3 The Hard Way
Me doing exercises from the book.

**IMPORTANT NOTE** `projects/` should be run using Docker (the reason why is explained in *Exercise 46* section of this document). Any other exercise can be run from the docker too.

To build Docker image just run:
- `docker build -t lp3thw .`

To enter interactive environment run:
- `docker run -it -v ${PWD}:/usr/src/lp3thw lp3thw /bin/bash`

## Exercise Notes
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
Instead of `venv` virtual environment I'm using a Docker image for running the `projects/` as `python 3.10` and above breaks things. 


I'm leaving instruction for `venv` anyway, for sake of it:

**OBSOLETE**

Under Windows (PowerShell):
1. `cd projects`
2. `mkdir venv`
2. `virtualenv --system-site-packages venv/lp3thw`
3. `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
4. `venv/lp3thw/Scripts/activate`
5. `pip install nose`
6. `cd skeleton`
7. `nosetests`

Linux is probably:
1. `cd projects`
2. `mkdir venv`
2. `virtualenv --system-site-packages venv/lp3thw`
3. `venv/lp3thw/bin/activate`
4. `pip install nose`
5. `cd skeleton`
6. `nosetests`

### Exercise 48, 49
are combined and are in `/projects/ex48`


# Useful tips, commands and references
- `git status -uall`
- PowerShell downloading:
  * `Invoke-WebRequest -Uri https://learnpythonthehardway.org/python3/languages.txt -OutFile languages.txt`
  * `Invoke-WebRequest -Uri https://learnpythonthehardway.org/python3/exercise26.txt -OutFile ex26.py`


- **OBSOLETE**
- `$VIRTUAL_ENV` to check your virtualenv [Determine if Python is running inside virtualenv](https://stackoverflow.com/questions/1871549/determine-if-python-is-running-inside-virtualenv)
- activate/dectivate virtualenv
  - Windows Powershell:
    - `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
    - activate: `. projects/bin/activate` **NOTE** after it will add `(lp3thw)` to console prompt 
    - deactivate: `deactivate` **NOTE** added `(lp3thw)` will disappear from console prompt
  - Linux (probably)
  - activate: `. projects/bin/activate` **NOTE** after it will add `(lp3thw)` to console prompt 
  - deactivate: `deactivate` **NOTE** added `(lp3thw)` will disappear from console prompt

- Error while running `nosetests`: `AttributeError: module 'collections' has no attribute 'Callable'`
- Caused (as described in link below) by 3.10 moving `collections.Callable` to `collections.abc.Callable`
- [AttributeError: module 'collections' has no attribute 'Callable'](https://stackoverflow.com/questions/69515086/error-attributeerror-collections-has-no-attribute-callable-using-beautifu)