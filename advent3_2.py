with open("adventdata3.txt", 'r') as f:
    binlistraw = f.readlines()
binlist = [x.strip() for x in binlistraw]
binlist.sort()
sumbinlist = []
print(binlist)

# I will be building two recursive functions. The first one will get the binary digit with the most common numbers,
# The second the least. This will be done by passing in the above list with all the binary numbers. Then I will check
# The first digit of every number and figure out whether there are more ones or zeros by adding and subtracting one
# Respectively from a temporary variable. If the variable is positive, there are more ones. Negative, more zeros. In the
# First function, the digits from the list that include the most common number in that place will be added to a new
# List. So if there are five numbers, and three of them have a one in the second place and two have a zero, I will
# Append to a new list all the numbers that have one in the second place. In the second program, I will do the same but
# For the least common numbers. So in the above case, I would append to a new list the numbers that have zero in the
# Second place. If there's an equal number of ones and zeros, then in the first case I pick one, and in the second zero


def get_most_common(list1, b):
    if len(list1) > 1:
        if b < len(list1[0]):
            templist = []
            sumtemp = 0
            for n in list1:
                if n[b] == "1":  # Figure out if there are more 1s or 0s, if there are more 1s then number is positive
                    sumtemp += 1
                elif n[b] == "0":
                    sumtemp -= 1
            for v in list1:
                if sumtemp >= 0:  # Getting rid of numbers with zero or one in bth place by appending to list numbers
                    if v[b] == "1":  # w/o zero or on in bth place
                        templist.append(v)
                elif sumtemp < 0:
                    if v[b] == "0":
                        templist.append(v)
            if sumtemp >= 0:
                print(f'Getting rid of 0 in the {b+1} place')
            elif sumtemp < 0:
                print(f'Getting rid of 1 in the {b+1} place')
            print(templist)
            return get_most_common(templist, b + 1)
        else:
            return list1
    else:
        return list1


def get_least_common(list2, b2):
    if len(list2) > 1:
        if b2 < len(list2[0]):
            templist = []
            sumtemp1 = 0
            for n in list2:
                if n[b2] == "1":  # Figure out if there are more 1s or 0s, if there are more 1s then number is positive
                    sumtemp1 += 1
                elif n[b2] == "0":
                    sumtemp1 -= 1
            # print(sumtemp1)
            for v in list2:
                if sumtemp1 >= 0:
                    if v[b2] == "0":
                        templist.append(v)
                elif sumtemp1 < 0:
                    if v[b2] == "1":
                        templist.append(v)
            if sumtemp1 <= 0:
                print(f'Getting rid of 1 in the {b2+1} place')
            elif sumtemp1 > 0:
                print(f'Getting rid of 0 in the {b2+1} place')
            print(templist)
            return get_least_common(templist, b2 + 1)
        else:
            return list2
    else:
        return list2


ogr = get_most_common(binlist, 0)[0]
print(binlist)
csr = get_least_common(binlist, 0)[0]
print(int(ogr, 2))
print(int(csr, 2))
print(int(csr, 2) * int(ogr, 2))
