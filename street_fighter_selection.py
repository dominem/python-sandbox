def street_fighter_selection_v1(fighters, initial_position, moves):
    hovered = []
    position = initial_position
    min_position = (0, 0)
    max_position = (len(fighters) - 1, len(fighters[0]) - 1)
    move_to_gain = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    for move in moves:
        gain = move_to_gain[move]
        position = tuple(map(sum, zip(position, gain)))
        if position[0] < min_position[0]:
            position = (min_position[0], position[1])
        elif position[0] > max_position[0]:
            position = (max_position[0], position[1])
        if position[1] < min_position[1]:
            position = (position[0], max_position[1])
        elif position[1] > max_position[1]:
            position = (position[0], min_position[1])
        hovered.append(fighters[position[0]][position[1]])
    return hovered


def get_x_position(x, x_min, x_max):
    if x < x_min:
        return x_max
    elif x > x_max:
        return x_min
    return x


def get_y_position(y, y_min, y_max):
    if y < y_min:
        return y_min
    elif y > y_max:
        return y_max
    return y


def get_next_position(position, gain, min_position, max_position):
    y, x = tuple(map(sum, zip(position, gain)))
    min_y, min_x = min_position
    max_y, max_x = max_position
    return get_y_position(y, min_y, max_y), get_x_position(x, min_x, max_x)


def street_fighter_selection_v2(fighters, initial_position, moves):
    hovered = []
    position = initial_position
    min_position = (0, 0)
    max_position = (len(fighters) - 1, len(fighters[0]) - 1)
    move_to_gain = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    for move in moves:
        position = get_next_position(position, move_to_gain[move], min_position, max_position)
        hovered.append(fighters[position[0]][position[1]])
    return hovered


fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
opts = ["up", "down", "right", "left"]


street_fighter_selection = street_fighter_selection_v2


moves = []
solution = []
assert street_fighter_selection(fighters, (0, 0), moves) == solution

moves = ["left"] * 8
solution = ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']
assert street_fighter_selection(fighters, (0, 0), moves) == solution

moves = ["right"] * 8
solution = ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka']
assert street_fighter_selection(fighters, (0, 0), moves) == solution

moves = ["up"] * 4
solution = ['Ryu', 'Ryu', 'Ryu', 'Ryu']
assert street_fighter_selection(fighters, (0, 0), moves) == solution

moves = ["down"] * 4
solution = ['Ken', 'Ken', 'Ken', 'Ken']
assert street_fighter_selection(fighters, (0, 0), moves) == solution

moves = ["down", "right", "up", "left"] * 2
solution = ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu']
assert street_fighter_selection(fighters, (0, 0), moves) == solution
