r"""Kata: String Pyramid.

#1 Best Practices Solution by Bilnd4Basics

def watch_pyramid_from_the_side(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( ' '*(i) + characters[i]*(baseLen-2*i) + ' '*(i) for i in range(len(characters)-1,-1,-1) )


def watch_pyramid_from_above(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( characters[0:min(i,baseLen-1-i)] + characters[min(i,baseLen-1-i)]*(baseLen-2*min(i,baseLen-1-i)) + characters[0:min(i,baseLen-1-i)][::-1] for i in range(baseLen) )


def count_visible_characters_of_the_pyramid(characters):
    return -1 if not characters else (len(characters)*2-1)**2


def count_all_characters_of_the_pyramid(characters):
    return -1 if not characters else sum( (2*i+1)**2 for i in range(len(characters)) )
"""


def get_side_length(chars):
    """Calculate the side length for a number of characters."""
    return 2 * len(chars) - 1


def watch_pyramid_from_the_side(characters):
    """Produce side view of pyramid."""
    if characters is None:
        return None
    side_length = get_side_length(characters)
    accumulator = ""
    for k in range(len(characters) - 1, -1, -1):
        accumulator += " " * k + (side_length - 2 * k) * characters[k] + " " * k + "\n"
    return accumulator[:-1]


def watch_pyramid_from_above(characters):
    """Produce top view of pyramid."""
    if characters is None:
        return None
    side_length = get_side_length(characters)
    accumulator = ""
    for k in range(len(characters)):
        accumulator += characters[0:k] + characters[k] * (side_length - 2 * k) + "".join(reversed(characters[0:k])) + "\n"
    for k in range(len(characters) - 2, -1, -1):
        accumulator += characters[0:k] + characters[k] * (side_length - 2 * k) + "".join(reversed(characters[0:k])) + "\n"
    return accumulator[:-1]


def count_visible_characters_of_the_pyramid(characters):
    """Count of visible chars in pyramid by squaring side length."""
    if characters is None or characters == "":
        return -1
    side_length = get_side_length(characters)
    return side_length ** 2


def count_all_characters_of_the_pyramid(characters):
    """Count of all chars in pyramid by summing odd squares from 0 to 2n-1."""
    if characters is None or characters == "":
        return -1
    str_length = len(characters)
    sum_odd_squares = (4 * str_length ** 3 - str_length) // 3
    return sum_odd_squares
