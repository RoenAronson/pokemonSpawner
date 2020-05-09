import Pokemon
import os
import random
import math
from pathlib import Path
from PIL import Image

pokemonImages = 'D:\PycharmProjects\PokemonRandomizer\pokemon_sprites';
pokemonList = []  # List of all of the pokemon objects, they have a weight for random encounter,
# name, and associated image.

weightList = []  # List of all of the pokemon's weights, this is only used to actually choose
# a pokemon, the weights are generated when the list of pokemon is generated
# at the start of the program.

coordinateList = []  # Coordinates that a pokemon has already spawned at, used to make sure they don't

canvasSize = 600

# spawn on top of each other

def generatePokemonList():
    for pokemon in os.listdir(pokemonImages):
        p = Pokemon.Pokemon()
        p.name = Path(pokemon).stem
        p.image = Image.open(os.path.join('D:\PycharmProjects\PokemonRandomizer\pokemon_sprites', pokemon))
        p.weight = random.random()
        pokemonList.append(p)


# def calculatePreviousCoords(x, y, sizeOfSprite):
#     new = True
#     print(len(coordinateList))
#     for coord in coordinateList:
#         if coord is None:
#             return False
#         new = True
#         if x in range(coord[0] - sizeOfSprite, coord[0] + sizeOfSprite) and \
#            y in range(coord[1] - sizeOfSprite, coord[1] + sizeOfSprite):
#             new = False
#             return new
#     return new


def generateCoordinate(canvasSize, distance):
    x = random.randint(0, canvasSize)
    y = random.randint(0, canvasSize)
    available = True
    if not coordinateList:
        coordinateList.append([x, y])
        return [x, y]
    else:
        for c in coordinateList:
            if math.fabs(c[0] - x) < distance and math.fabs(c[1] - y) < distance:
                available = False
        if available:
            coordinateList.append([x, y])
            return [x, y]
        else:
            generateCoordinate(canvasSize, distance)

def choosePokemon():
    imageX = canvasSize
    imageY = canvasSize
    combinedPokemonImage = Image.new('RGB', (imageX, imageY))
    for p in pokemonList:
        weightList.append(p.weight)
    for choice in random.choices(population=pokemonList, weights=weightList, k=10):
        imageCoordinate = generateCoordinate(canvasSize, 50)
        combinedPokemonImage.paste(choice.image, imageCoordinate)
    combinedPokemonImage.show()


def printPokemonList():
    for p in pokemonList:
        print(p.name)
        print(p.weight)


if __name__ == '__main__':
    generatePokemonList()
    choosePokemon()
    print(len(coordinateList))
    print(coordinateList)