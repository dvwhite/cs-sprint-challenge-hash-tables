def get_indices_of_item_weights(weights, length, limit):
    """
    Return a tuple of weights that when summed equal limit. The
    solution runs in linear time by utilizing hash tables to
    store the complement of each weight in weights and
    returning the two weights that sum to the limit
    """
    # Create a dict of weights mapped to their index
    weight_pos = {}
    for idx, weight in enumerate(weights):
        weight_pos[weight] = idx

    # Check if the complement exists in the dictionary
    # The complement is the difference between the limit and the weight
    counter = 0
    for weight in weights:
        complement = limit - weight
        weight_pos[complement] = weight_pos.get(complement, None)
        pos = weight_pos[complement]
        if pos != None and pos != counter:
            valid_weights = [pos, counter]
            valid_weights.sort(reverse=True)
            # Return the tuple containing the weights that sum to limit
            return tuple(valid_weights)
        counter += 1

    # If no compatible weights found, return None
    return None


# Manual testing
weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(answer_4)
