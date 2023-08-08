#!/usr/bin/python3
for ord_ in range(97, 123):
    if chr(ord_) in ['q', 'e']:
        continue
    print("{}".format(chr(ord_)), end="")
