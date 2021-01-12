def is_degenerated(line):
    (x1, y1), (x2, y2) = line
    if x1 == x2 and y1 == y2:
        return True
    return False


def is_vertical(line):
    (x1, y1), (x2, y2) = line
    if x1 == x2 and not is_degenerated(line):
        return True
    return False


def is_horizontal(line):
    (x1, y1), (x2, y2) = line
    if y1 == y2 and not is_degenerated(line):
        return True
    return False


def is_inclined(line):
    if (not is_vertical(line) and not is_horizontal(line) and
            not is_degenerated(line)):
        return True
    return False


assert is_degenerated(((1, 4), (1, 4))) is True
assert is_degenerated(((1, 4), (4, 1))) is False
