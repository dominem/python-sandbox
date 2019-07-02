def race_verbose(v1, v2, g):
    if v1 >= v2:
        return None

    # d - distance
    # t1, t2 - times

    # d = (v1 * t1) + g
    # d = (v2 * t2)

    # d - g = v1 * t1
    # d = v2 * t2

    # t1 = (d - g) / v1
    # t2 = d / v2

    # t1 = d/v1 - g/v1
    # t2 = d/v2

    # t1 = t2
    # d/v1 - g/v1 = d/v2
    # d/v1 - d/v2 = g/v1
    # (d*v2)/(v1*v2) - (d*v1)/(v1*v2) = g/v1
    # (d*v2 - d*v1) / (v1*v2) = g/v1
    # (d * (v2 - v1)) / (v1*v2) = g/v1
    # d = g / (v1 * ((v2 - v1) / (v1 * v2)))
    # d = g / ((v2 - v1) / v2)
    # t1 = t2 = t
    # t = d / (v2 / 3600)
    # t = (g / ((v2 - v1) / v2)) / (v2 / 3600)
    # t = (g * (v2 / (v2 - v1)) * (3600 / v2)
    # t = g * (3600 / (v2 - v1))
    # t = g * 3600 / (v2 - v1)

    time = g * 3600 / (v2 - v1)
    hours = int(time // 3600)
    minutes = int((time % 3600) // 60)
    seconds = int(time % 60)
    return [hours, minutes, seconds]


def race(v1, v2, g):
    if v1 >= v2:
        return None
    t = g * 3600 / (v2 - v1)
    return list(map(int, [t // 3600, (t % 3600) // 60, t % 60]))


if __name__ == '__main__':
    assert race(720, 850, 70) == [0, 32, 18]
    assert race(80, 91, 37) == [3, 21, 49]
    assert race(80, 100, 40) == [2, 0, 0]
