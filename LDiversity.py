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
    
    
def get_full_l_diversity_report(df, quasi_identifiers, sensitive_attribute):
    """
        Function to find the minimum value of l for which each equivalence class of the given quasi_identifiers satisfies l- Diversity, and return each equivalence class and corresponding value of l. 
    
    Params:
        df: Pandas DataFrame which is to be tested 
        quasi_identifiers: List of attributes; must be a subset of the columns of df
        sensitive_attribute: string; must be a column in the dataframe
        
    Returns:
        Two lists; equivalence clases and corresponding l-values

       
    """
    # Check that quasi_identifiers is a subset of dataframe columns
    assert set(quasi_identifiers).issubset(set(df.columns)), "One or more quasi identifiers is not in the data frame columns"
    assert sensitive_attribute in df.columns, "The sensitive attribute is not present in dataframe"
    assert sensitive_attribute not in quasi_identifiers, "The sensitive attribute cannot be a quasi identifier"
    
    # Make a copy for local manipulation
    df_local = df.copy()
    
    # Add a summy column used for aggregation
    # This is needed to access the aggregate in case quasi_identifiers are all of the dataframe columns
    
    
    # Group by quasi identifiers 
    df_grouped = df_local.groupby(quasi_identifiers).nunique()
    df_grouped.drop(quasi_identifiers,inplace=True,axis=1)
    df_grouped = df_grouped.reset_index()
    equivalence_classes = []
    l_values = []
    
    for i in range(df_grouped.shape[0]):
        record = df_grouped.iloc[i]
        equivalence_class = tuple(record[quasi_identifiers])
        l = record[sensitive_attribute]
        equivalence_classes.append(equivalence_class)
        l_values.append(l)
        
    return equivalence_classes, l_values
        