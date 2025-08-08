""" rot13 rotate letters by 13 place. """

from string import ascii_uppercase, ascii_lowercase

_rot13 = str.maketrans(
        ascii_uppercase + ascii_lowercase,

        ascii_uppercase[13:] + ascii_uppercase[:13] +
        ascii_lowercase[13:] + ascii_lowercase[:13]
)

def rot13(s: str) -> str:
    return s.translate(_rot13)
