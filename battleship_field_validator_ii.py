# https://www.codewars.com/kata/571ec81d7e8954ce1400014f


class BattleFieldValidator:
    out_of_battlefield = (-1, 10)
    max_submarines = 4
    max_destroyers = 3
    max_cruisers = 2
    max_battleships = 1
    submarine_size = 1
    destroyer_size = 2
    cruiser_size = 3
    battleship_size = 4
    max_occupied_fields = (
        max_submarines * submarine_size +
        max_destroyers * destroyer_size +
        max_cruisers * cruiser_size +
        max_battleships * battleship_size
    )
    # The ship cannot overlap, but can be contact with any other ship.

    def __init__(self, battlefield):
        self.battlefield = battlefield
        self.submarines = 0
        self.destroyers = 0
        self.cruisers = 0
        self.battleships = 0

    def validate(self):
        try:
            self.check_occupied_fields()
            # self.check_separated_submarines()
        except ValueError:
            return False
        return True

    def check_occupied_fields(self):
        occupied_fields = 0
        for y in range(len(self.battlefield)):
            for x in range(len(self.battlefield[0])):
                occupied_fields += self.battlefield[y][x]
        if occupied_fields > self.max_occupied_fields:
            raise ValueError

    def check_separated_submarines(self):
        for y in range(len(self.battlefield)):
            for x in range(len(self.battlefield[0])):
                if self.battlefield[y][x] and not self.is_submarine_in_contact(x, y):
                    self.battlefield[y][x] = 0
                    self.submarines += 1
        if self.submarines > 4:
            raise ValueError

    def is_submarine_in_contact(self, x, y):
        fields_to_check = [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),             (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)
        ]
        for fx, fy in fields_to_check:
            if fx not in self.out_of_battlefield and fy not in self.out_of_battlefield:
                if self.battlefield[fy][fx]:
                    return True
        return False

    def check_for_more_than_one_separated_battleships(self):
        pass


def validate_battlefield(battlefield):
    return BattleFieldValidator(battlefield).validate()


assert validate_battlefield(
    [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
     [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) is True, "Must return true for valid field"

assert validate_battlefield(
    [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
     [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) is True, "Must return true if ships are in contact"


assert validate_battlefield(
    [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
     [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]) is False, "Must return false for invalid field"
