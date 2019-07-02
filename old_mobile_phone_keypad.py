layout = [
    '1',     'abc2', 'def3',
    'ghi4',  'jkl5', 'mno6',
    'pqrs7', 'tuv8', 'wxyz9',
    '*',     ' 0',   '#',
]


def presses(phrase):
    return sum(1 + b.index(c) for c in phrase.lower() for b in layout if c in b)


if __name__ == '__main__':
    assert presses('LOL') == 9
    assert presses('HOW R U') == 13
