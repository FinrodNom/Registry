import os
import re
import csv
from collections import namedtuple

PATH_TO_REGISTRY = 'data\\registry.csv'
zag = namedtuple('Client', 'Name Phone Date Server')


def read_from_file():
    registry = []
    with open(PATH_TO_REGISTRY, 'r', encoding='utf-8') as file:
        src = csv.reader(file)
        for x in src:
            if x :
                print(x)
                registry.append(zag(x[0], x[1], x[2], x[3]))

    print(registry)


def 


def main():
    read_from_file()


if __name__ == '__main__':
    main()