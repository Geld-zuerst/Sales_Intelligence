import numpy as np
import pandas as pd
import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(root, 'data'))

import load_data
load_data.product()