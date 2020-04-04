import pandas as pd 
import numpy as np 

def get_k_anonymity(df,quasi_identifiers):
    """
    
    Function to return the minimum value of k for which a table satisfies k-Anonymity
    
    Params:
        df: Pandas DataFrame which is to be tested 
        quasi_identifiers: List of attributes; must be a subset of the columns of df
        
    Returns:
        A python dictionary which consists of two items:
            k: The minimum value of k for which df satisfies k-Anonymity
            equivalence_classes: List of tuples; each tuple represents the equivalence class that satisfies k-Anonymity
    
    """
    
    # Check that quasi_identifiers is a subset of dataframe columns
    assert set(quasi_identifiers).issubset(set(df.columns)), "One or more quasi identifiers is not in the data frame columns"
    
    # Make a copy for local manipulation
    df_local = df.copy()
    
    # Add a summy column used for aggregation
    # This is needed to access the aggregate in case quasi_identifiers are all of the dataframe columns
    df_local['DUMMY_COUNTER'] = df_local[quasi_identifiers[0]].apply(lambda x: 1)
    
    # Group by quasi identifiers 
    df_grouped = df_local.groupby(quasi_identifiers).count()
    
    # Get different values of k
    # Minimum value is the one we want
    group_k = df_grouped['DUMMY_COUNTER'].tolist()
    k = np.min(group_k)
    
    # After group by, indices represent the equivalence classes
    # Obtain index values for those which satisfy the k-Anonymity for the k obtained above
    df_grouped_index = df_grouped.index[df_grouped['DUMMY_COUNTER']==k].tolist()
    
    # Construct response
    response = {'k':k, 
                'equivalence_classes':df_grouped_index}
    
    return response


def get_k_reverse_membership(df,equivalence_class):
    """
    
    Function to compute reverse membership map and find how many tuples in the class
    
    Params:
        df: Pandas DataFrame which is to be tested 
        equivalence_class: Dictionary object denoting the value of quasi_identifiers
                           For example:
                           {'Age': 30, 'Gender':'F'}
        
        
    Returns:
        Integer that denotes the size of the equivalence class in df 
    
    """
    
    # Check that the QI are in columns 
    assert set(equivalence_class.keys()).issubset(set(df.columns)), "One or more quasi identifiers is not in the data frame columns"
    
    # Make a copy for local manipulation
    df_local  = df.copy()
    
    # Subset the dataframe to obtain the dataframe corresponding to the equivalence class
    for qi in equivalence_class.keys():
        df_local = df_local[df_local[qi]==equivalence_class[qi]]
    
    # Number of records in the resulting dataframe is the size of the equivalence class
    return df_local.shape[0]

