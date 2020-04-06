import pandas as pd
import numpy as np 

def get_l_diversity(df,quasi_identifiers, sensitive_attribute):
    """
    Function to return the minimum value of l for which a table satisfies l-Diversity
    
    @Params:
        df: Pandas DataFrame which is to be tested 
        quasi_identifiers: List of attributes; must be a subset of the columns of df
        sensitive_attribute: string; must be a column in the dataframe
        
    Returns:
        A python dictionary which consists of two items:
            l: The minimum value of l for which df satisfies l-diversity
            equivalence_classes: List of tuples; each tuple represents the equivalence class that satisfies l-diversity

    """
    assert set(quasi_identifiers).issubset(set(df.columns)), "One or more quasi identifiers is not in the data frame columns"
    assert sensitive_attribute in df.columns, "The sensitive attribute is not present in dataframe"
    assert sensitive_attribute not in quasi_identifiers
    df_local = df.copy()
    
    df_grouped = df_local.groupby(quasi_identifiers).nunique()
    
    group_l = df_grouped[sensitive_attribute].tolist()
    l = np.min(group_l)
    
    df_grouped_index = df_grouped.index[df_grouped[sensitive_attribute]==l].tolist()
    
    response = {'l':l, 
                'equivalence_classes':df_grouped_index}
    
    return response
    