import collections
import copy


class LifeGame(object):
    """
    Class for Game life
    """

    def __init__(self, ocean: list[list[int]]) -> None:
        self.ocean = ocean

    def _get_neighbours(self, cell: tuple[int, int, int]) -> list[int]:
        may_neighbours_coordinates = [[cell[0], cell[1] + 1], [cell[0] + 1, cell[1] + 1],
                                      [cell[0] - 1, cell[1] + 1], [cell[0], cell[1] - 1],
                                      [cell[0] + 1, cell[1]], [cell[0] + 1, cell[1] - 1],
                                      [cell[0] - 1, cell[1]], [cell[0] - 1, cell[1] - 1]]
        return [self.ocean[neighbour[0]][neighbour[1]] for neighbour in may_neighbours_coordinates
                if (0 <= neighbour[0] < len(self.ocean)) and (0 <= neighbour[1] < len(self.ocean[0]))]

    def _get_cell_next_generation(self, cell_value: int, neighbours: list[int]) -> int:
        neighbour_counter = collections.Counter(neighbours)
        if cell_value == 0:
            if neighbour_counter[2] == 3:
                return 2
            elif neighbour_counter[3] == 3:
                return 3
            else:
                return 0
        elif cell_value == 1:
            return 1
        else:
            if neighbour_counter[cell_value] in [0, 1, 4, 5, 6, 7, 8]:
                return 0
            else:
                return cell_value

    def get_next_generation(self) -> list[list[int]]:
        new_ocean = copy.deepcopy(self.ocean)
        for i in range(len(self.ocean)):
            for j in range(len(self.ocean[0])):
                cell = (i, j, self.ocean[i][j])
                neighbours = self._get_neighbours(cell)
                new_value = self._get_cell_next_generation(cell[2], neighbours)
                new_ocean[cell[0]][cell[1]] = new_value
        self.ocean = new_ocean
        return self.ocean
