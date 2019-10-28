def check_symbols(restricted_symbols, s):
    for symb in restricted_symbols:
        if symb in s:
            return True
        return False