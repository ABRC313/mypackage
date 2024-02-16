def top_n (items, n):
    """Return the top n items in and array, in decending order
    
    Args:
        items (array): list or array-like object
        n (int): number of items to return
        
    Restun:
        array: top n items, in desc order

    Egs:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8,7,3]
    """
      # Sort the items in descending order
    sorted_items = sorted(items, reverse=True)
    
    # Slice the list to get the top n items
    top_n_items = sorted_items[:n]
    
    return top_n_items

# Example usage
result = top_n([8, 3, 2, 7, 4], 3)
print(result)