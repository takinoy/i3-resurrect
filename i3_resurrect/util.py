import sys
import string

def eprint(*args, **kwargs):
    """
    Function for printing to stderr.
    """
    print(*args, file=sys.stderr, **kwargs)


def filename_filter(filename):
    """
    Take a string and return a valid filename constructed from the string.
Uses a whitelist approach: any characters not present in valid_chars are
removed. Also spaces are replaced with underscores.
"""
    # whitelist = "-_.() %s%s" % (string.ascii_letters, string.digits)
    blacklist = '/\:*"<>|'

    if filename is None:
        return filename

    for char in filename:
        # Check it char is in whitelist
        if char in blacklist:
            # Replace the string
            filename = filename.replace(char, '')

    return filename
