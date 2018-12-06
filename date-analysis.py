import sys
from datetime import timedelta
import numpy as np
import pandas as pd

open_path = pd.read_csv(sys.argv[1], sep=",",header=0)
output_path = sys.argv[2]

open_path.StartTime = pd.to_datetime(open_path.StartTime)
open_path['DeltaTime'] = open_path.StartTime.diff().shift(0)
open_path.to_csv(output_path)




