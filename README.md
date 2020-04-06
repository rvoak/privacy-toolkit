# privacy-toolkit

This is an open source library which helps examine datasets for important privacy related properties. You can use data you have in CSV format, and examine k-Anonymity, l-diversity, etc. To the best of my knowledge, this is the first library which provides off-the-shelf methods to conveniently calculate these properties.

# Features
Presently it supports:
- _k_-Anonymity
- _l_-Diversity

I am working on adding the following features:
- t-Closeness
- delta-presence
- Differential Privacy

# Usage

## _k_-Anonymity
This module currently supports the following methods:
- `get_k_anonymity()`: This function takes in a DatFrame and the set of quasi identifiers. It computes the value of _k_ for which the table satisfies _k_-Anonymity with respect to those quasi identifiers.
- `get_full_k_anonymity_report()`: This function takes in a DatFrame and the set of quasi identifiers. It finds the minimum value of _k_ for which each equivalence class of the given quasi_identifiers satisfies _k_-Anonymity, and return each equivalence class and corresponding value of _k_.
- `get_k_summary()`: This function takes in a DataFrame and examines _k_-Anonymity for every possible combination of quasi identifiers. Returns lists of quasi identifier combinations and corresponding _k_-value.

## _l_-Diversity
This module currently supports the following methods:
- `get_l_diversity()`: This function takes in a DatFrame, the sensitive attribute and the set of quasi identifiers. It computes the value of _l_ for which the table satisfies _l_-Diversity with respect to those quasi identifiers.
- `get_full_l_diversity_report()`: This function takes in a DatFrame, the sensitive attribute and the set of quasi identifiers. It finds the minimum value of _l_ for which each equivalence class of the given quasi identifiers satisfies _l_-Diversity, and return each equivalence class and corresponding value of _l_.
- `get_l_summary()`: This function takes in a DataFrame and examines _l_-Diversity for every possible combination of quasi identifiers. Returns lists of quasi identifier combinations and corresponding _l_-value.



## Demo
For sample usage, please see the demo in `Sample_Usage.ipynb`.
