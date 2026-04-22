from collections import Counter
from .lib import get_list_from_ids_mapping, increment_by_custom_base, freq_in_range

# To permutate the list with some custom options, such as we don't want `c` to be at first option.


def custom_permutate_by_options(item_list, item_options=[]):

    # The total item count
    slot_count = len(item_list)

    # Create the item sorted set to have distinct items
    item_set = sorted(set(item_list))

    # Set an id for each distinct item
    ids_by_item = {v: i for i, v in enumerate(item_set)}
    items_by_id = {i: v for i, v in enumerate(item_set)}

    # Create a list of ids for the each distinct item
    id_list = list(ids_by_item.values())

    item_id_list = [ids_by_item[item] for item in item_list]

    # The actual frequency by id needed for the result
    needed_freq_by_id = Counter(item_id_list)

    if item_options:
        the_choices = [[ids_by_item[item] for item in option] for option in item_options]
    else:
        the_choices = [id_list[:] for i in range(slot_count)]

    # The base for the position that should be limited
    item_bases = [len(the_choices[i]) for i in range(slot_count)]

    iter_count = 1921

    initial = [0] * slot_count
    current = initial

    for i in range(iter_count):
        next_one = increment_by_custom_base(current, item_bases)
        if next_one == initial:
            # EOCP
            return

        next_ids = [the_choices[i][next_one[i]] for i in range(len(the_choices))]
        currentCtr = Counter(next_ids)
        if freq_in_range(currentCtr, needed_freq_by_id):
            if next_one == current:
                # EOCP
                return
            next_item_list = get_list_from_ids_mapping(next_ids, items_by_id)
            yield next_item_list
        current = next_one
