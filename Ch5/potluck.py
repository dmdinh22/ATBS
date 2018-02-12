all_guests = {'Alice':
                {'apples': 5, 'pretzels': 12},
              'Bob':
                {'ham sandwiches': 3, 'apples': 2},
              'Carol':
                {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    num_brought = 0
    # k to guest, v to dictionary of items
    for k, v in guests.items():
        # if it does not exist, get() method to add 0 to number brought
        num_brought = num_brought + v.get(item, 0)
    return num_brought

print('Number of things being brought:')
print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))
