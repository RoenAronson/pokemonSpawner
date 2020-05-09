import Pokemon
import os
import random
import math
from pathlib import Path
from PIL import Image

pCoords = []  # Previous Coordinates


def generateCoordinate():
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    available = True
    if not pCoords:
        pCoords.append([x, y])
    else:
        for c in pCoords:
            if math.fabs(c[0] - x) < 30 and math.fabs(c[1] - y) < 30:
                available = False
    if available:
        pCoords.append([x, y])


for i in range(10):
    generateCoordinate()

if __name__ == '__main__':
    generateCoordinate()
    print(pCoords)
