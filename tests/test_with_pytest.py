###################
# Author: David Dov
# Date: 2/1/2023
###################

from pathlib import Path
import sys
sys.path.append(str(Path().resolve()))
from src.utils import get_hyperparams

global_params: dict = {'hyperparams_path': 'config/hyperparams.yml'}


def test_alwayas_true():
    """
    Function that should always pass if pytest is configured properly
    """
    assert True

def test_hyperparams_loading():
    """
    test the loading of hyperparams
    """
    hyperparams = get_hyperparams(Path(global_params['hyperparams_path']))
    pass

