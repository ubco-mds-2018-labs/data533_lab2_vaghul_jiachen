import numpy as np
import missingno

def show_nulls(input_df):
    input_df.replace("None", np.nan, inplace = True)
    missingno.matrix(input_df)