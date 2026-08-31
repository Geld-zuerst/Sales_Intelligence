import numpy as np
import pandas as pd
import data.load_data as load_data 
import os
import sys


# import os
# import sys

# root = os.path.dirname(os.path.dirname(__file__)) 

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(root, 'data'))

# app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 

# import load_data

from pathlib import Path
import sys


# data_dir = Path(__file__).resolve().parent / 'data'
# sys.path.append(str(data_dir))

import load_data

# product = pd.read_csv("")

# product()

