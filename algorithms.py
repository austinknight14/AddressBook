def insertion_sort(contact_list):
    for i in range(1, len(contact_list)):
        key = contact_list[i]
        position = i - 1
        while position >= 0 and contact_list[position]> key :
            contact_list[position + 1] = contact_list[position]
            position -= 1
        contact_list[position + 1] = key
def binary_search(contact_list, target_contact):
    low = 0
    high = len(contact_list)
    while low <= high:
        midpoint = (low + high)//2
        if contact_list[midpoint] == target_contact:
            return midpoint
        elif contact_list[midpoint] < target_contact:
            low = midpoint + 1
        else:
            high = midpoint - 1
    return -1