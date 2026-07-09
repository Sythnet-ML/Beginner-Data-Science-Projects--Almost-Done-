import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

sns.set_style("whitegrid")
plt.rcParams.update({'figure.figsize': (10, 6)})

import warnings

warnings.filterwarnings("ignore")



# ------------------------------------------------------------------------------------------
# Data Loading
# ------------------------------------------------------------------------------------------

def load_data(path= 'data\\bankrupt.csv'):
    df = pd.read_csv(path)
    df['Bankrupt'] = df['Bankrupt'].map({'Yes': 1, 'No': 0})
    
    return df

