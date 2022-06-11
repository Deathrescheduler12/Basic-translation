import math
import numpy as np
class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates
    @property
    def change_coordinate(self):
        return self.coordinates
    @change_coordinate.setter
    def change_coordinate(self, prop: np.ndarray):
        self.coordinates = prop
        return True
    def rotate(self, angle: int):
        coordinates = self.coordinates
        for x in range(1, int(angle/90) + 1):
            mat = [round(math.cos(90)), -round(math.sin(90)), round(math.sin(90)), round(math.cos(90))]
            coordinates = (np.array(mat) * np.array((*coordinates, *coordinates)))[1:3]
        self.change_coordinate = coordinates
        return
    def translate(self, vector: np.ndarray):
        coordinate = np.array(self.coordinates) + vector
        self.change_coordinate = coordinate
        return
    def enlarge(self, point: np.ndarray, factor: np.ndarray =2):
        distance = (np.array(self.coordinates) - point) * factor
        self.change_coordinate = point + distance
        return
    def reflect(self, mirror: np.ndarray):
        distance = ((np.array(self.coordinates)[0] - mirror[0]) * -1)
        self.change_coordinate = (distance, self.coordinates[1])
        return


