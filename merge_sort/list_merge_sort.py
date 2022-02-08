# Variables to count recursive function calls
merge_sort_cntr  = 0
split_cntr = 0
merge_cntr = 0

def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    Takes O(kn log n) time
    """
    # Count number of times this recursive function is called
    global merge_sort_cntr
    merge_sort_cntr += 1

    print('merge_sort_cntr is ', merge_sort_cntr)
    print('> merge_sort(', end = "")
    print(list, end = "")
    print(')')
    
    if len(list) <= 1: # true until we either have single or empty list
        print('single item merge_sort list is ', list)
        return list

    left_half, right_half = split(list)

    left = merge_sort(left_half)
    print('left merge_sort ', left)
    right = merge_sort(right_half)
    print('right merge_sort ', right)
    
    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Called as many times as needed to get to single element lists
    Takes overall O(k log n) time which is logarithmic time.  The k is due to Python's split operations
    """

    # Count number of times this recursive function is called
    global split_cntr
    split_cntr += 1

    print('>>> split(', end = "")
    print(list, end = "")
    print(')')

    mid = len(list)//2 # divide by 2 and round down
    # print('midpoint for split ', list[mid])
    left = list[:mid] # slice from begining up to midpoint of list but not including the midpoint
    print('>>> split return left ', left, end = " ")
    right = list[mid:] # slice from midpoint up to end of list
    print('>>> split return right ', right)

    # print('Length of list processed ', len(list))

    return left, right
    

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    Performs comparison ops against single element lists and
    merges them back in the correct order
    Runs in overall O(n) time which is linear time
    """

    # Count number of times this recursive function is called
    global merge_cntr
    merge_cntr += 1

    l = []
    i = 0 # indexes in left list
    j = 0 # indexes in right list
    print('>>>>>> merge() called with', left, right)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            print('>>>>>> left merge 1 is ', l)
            i += 1
        else:
            l.append(right[j])
            print('>>>>>> right merge 1 is ', l)
            j += 1

    while i < len(left):
        l.append(left[i])
        print('>>>>>> left merge 2 is ', l)
        i += 1

    while j < len(right):
        l.append(right[j])
        print('>>>>>> right merge 2 is', l)
        j += 1

    print('>>>>>> merge() returned ', l)
    return l

alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]

l = merge_sort(alist)

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

print('Original list  ', alist)
#print('verify_sorted equals ', verify_sorted(alist))
print('Sorted list ', l)
#print('verify_sorted equals ', verify_sorted(l))
print('Number of merge_sort operations ', merge_sort_cntr)
print('Number of split operations ', split_cntr)
print('Number of merge operations ', merge_cntr)
