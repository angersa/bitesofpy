"""Color class

The following sites were consulted:
    http://www.99colors.net/
    https://www.webucator.com/blog/2015/03/python-color-constants-module/
"""
import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join('/tmp', 'color_values.py')
urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
                           color_values_module)
sys.path.append('/tmp')

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(self.color.upper())

    @classmethod
    def hex2rgb(cls, hex):
        """Class method that converts a hex value into an rgb one"""
        valid_char = '#1234567890abcdef'
        conditions = (hex[0] == '#',
                      len(hex) == 7,
                      all(c in valid_char for c in hex))
        if not all(conditions):
            raise ValueError
        return int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:], 16)

    @classmethod
    def rgb2hex(cls, rgb):
        """Class method that converts an rgb value into a hex one"""
        if not type(rgb) == tuple or not all(255 >= v >= 0 for v in rgb):
            raise ValueError
        r, g, b, = rgb
        return f'#{r:02x}{g:02x}{b:02x}'

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return str(self.rgb) if self.rgb else "Unknown"
