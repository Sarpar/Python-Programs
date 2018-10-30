# Program to merge 2 sorted array

L1 = [4,6,8,9,12,14]
L2 = [2,3,6,8,10,15,16,18]

def merge(L1, L2):
    temp = []
    n1 = n2 = 0

    while((n1 < len(L1)) and (n2 < len(L2))):
        if (L1[n1] < L2[n2]):
            temp.append(L1[n1])
            n1 = n1 + 1
        else:
            temp.append(L2[n2])
            n2 = n2 + 1

    while(n1 < len(L1)):
        temp.append(L1[n1])
        n1 = n1 + 1

    while(n2 < len(L2)):
        temp.append(L2[n2])
        n2 = n2 + 1

    return temp

print merge(L1, L2)
