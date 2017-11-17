11111
12221
12321
12221
11111

side_length = char_length * 2 - 1
row0 = characters[0:0] + characters[0] * (side_length - 0) + "".join(reversed(characters[0:0]))
row1 = characters[0:1] + characters[1] * (side_length - 2) + "".join(reversed(characters[0:1]))
row2 = characters[0:2] + characters[2] * (side_length - 4) + "".join(reversed(characters[0:2]))
row3 = characters[0:3] + characters[3] * (side_length - 6) + "".join(reversed(characters[0:3]))


rowk = characters[0:k] + characters[k] * (side_length - 2k) + "".join(reversed(characters[0:k])) + "\n"

xx3xx
x222x
11111


row0 = " " * 0 + (side_length - 0) * characters[0] + " " * 0
row1 = " " * 1 + (side_length - 2) * characters[1] + " " * 1
row2 = " " * 2 + (side_length - 4) * characters[2] + " " * 2

rowk = " " * k + (side_length - 2 * k) * characters[k] + " " * k


(string_length - 1) * " " + characters[-1] + (string_length - 1) * " "