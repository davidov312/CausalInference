###################
# Author: David Dov
# Date: 2/1/2023
###################


import pathmagic
from src.utils import my_operator


def test_my_operator():
    assert my_operator(2, 3) == 8


def main():
    test_my_operator()
    print('done')


if __name__ == "__main__":
    main()
