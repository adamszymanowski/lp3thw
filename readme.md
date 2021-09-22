# Learn Python 3 The Hard Way
Me doing exercises from the book. That's it for now.

### Exercise 23 Python Session
> python3
>
> a_pl = "ą"
> a_pl.encode()
> import sys
> sys.byteorder
> int.from_bytes(a_pl.encode(), byteorder="little")
> int.from_bytes(a_pl.encode(), byteorder="big")
> (0xc4 << 8) + 0x85
> (0x85 << 8) + 0xc4
> int.from_bytes(a_pl.encode(), byteorder="little") == (0x85 << 8) + 0xc4
> int.from_bytes(a_pl.encode(), byteorder="big") == (0xc4 << 8) + 0x85
> bin((0x85 << 8) + 0xc4)
> 0b1000010111000100
>
> int.from_bytes(a_pl.encode(), byteorder="little") # I don't get this part bellow
> chr(int.from_bytes(a_pl.encode(), byteorder="little"))
> ord(chr(int.from_bytes(a_pl.encode(), byteorder="little")))
> ord(a_pl)
> chr(261)

Maybe read [this thing about python3 unicode](https://docs.python.org/3/howto/unicode.html) and try to understand it