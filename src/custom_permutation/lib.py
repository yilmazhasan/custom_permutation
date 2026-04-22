# helpers from custom lib
from typing import List

# Check if the number items freq is a subset of needed freq


def freq_in_range(the_new_freq, the_freq):
    for k, v in the_new_freq.items():
        if k == -1:
            continue

        if k not in the_freq or the_new_freq[k] > the_freq[k]:
            return False
    return True

# Get the item list from the ids mapping


def get_list_from_ids_mapping(the_next, the_items_by_id):
    return [the_items_by_id[id] for id in the_next]

# Incremenet a number based on a specific custom base


def increment_by_custom_base(the_input_number, the_base_limit):
    the_number = the_input_number[:]
    carry = 1  # initialize by 1 initially to increment by one

    for i in range(len(the_number)-1, -1, -1):
        if the_number[i] + carry < the_base_limit[i]:
            the_number[i] += carry
            break
        else:
            the_number[i] = the_number[i] + carry - the_base_limit[i]

    return the_number

# Initiate the options based on the items


def initiate_options(items):
    options = []

    for i in range(len(items)):
        options.append(items[:])

    return options

# Remove an item from the options previously created


def remove_from_options(options, item, option_index):
    options[option_index].remove(item)

# Set the items as the options at a specific index


def set_as_options(options: List[List[str]], items: List, option_index):
    if option_index >= len(options):
        raise IndexError(
            f"option_index {option_index} is out of range for options of length {len(options)}")

    options[option_index] = items

# Get options by cli arguments


def get_options(items, includes, excludes, separator=","):
    initial_options = initiate_options(items)

    by_indexes = {}

    for include in includes:
        item, idx = include.split(separator)
        idx = int(idx)
        by_indexes.setdefault(idx, {"include": [], "exclude": []})
        by_indexes[idx]["include"].append(item)

    for exclude in excludes:
        item, idx = exclude.split(separator)
        idx = int(idx)
        by_indexes.setdefault(idx, {"include": [], "exclude": []})
        by_indexes[idx]["exclude"].append(item)

    for idx, options in by_indexes.items():
        if options["include"]:
            set_as_options(initial_options, options["include"], idx)
        elif options["exclude"]:
            for item in options["exclude"]:
                remove_from_options(initial_options, item, idx)

    return initial_options
