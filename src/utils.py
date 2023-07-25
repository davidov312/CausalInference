###################
# Author: David Dov
# Date: 25/7/2023
###################
import argparse
from pathlib import Path
import yaml
from pydantic import BaseModel
from typing import Literal


def read_yaml(file_path: Path) -> dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


class Hyperparams(BaseModel):
    """
    This class defines the schema for hyperparameters using pydantic library
    """

    example_param: Literal['A', 'B']


def get_hyperparams(file_path: Path) -> Hyperparams:
    """
    This function loads the hyperparameters from yaml file into the schema defined using pydantic library
    Input file_path - path to yaml file with the hyperparameter
    Output - a dictionary that allows hinting
    """
    hyperparams = read_yaml(file_path)
    hyperparams = Hyperparams(**hyperparams)
    return hyperparams


def get_args() -> argparse.Namespace:
    """
    This function defines the arguments need to be passed to fetch_data
    Output: args - an object that contains all collected arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--hyperparams_path', nargs='?', type=str)
    args = parser.parse_args()
    hyperparams = get_hyperparams(Path('config', args.hyperparams_path))
    return args

