###################
# Author: David Dov
# Date: 25/7/2023
###################

from pathlib import Path
import sys
sys.path.append(str(Path().resolve()))
from src.utils import get_args, get_hyperparams
    
def main():
    args = get_args()
    hyperparams = get_hyperparams(Path('config', args.hyperparams_path))
    print(hyperparams.example_param)
    return

if __name__ == "__main__":
    main()
