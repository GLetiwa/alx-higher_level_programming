def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        new = str[:n] + str[n + 1:]
        return new
