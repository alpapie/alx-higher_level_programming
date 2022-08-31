#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if a_dictionary:
        fst_key = list(a_dictionary.keys())[0]
        fst_value = a_dictionary[fst_key]

        for k, v in a_dictionary.items():
            if v > fst_value:
                fst_value = v
                fst_key = k
        return (fst_key)
