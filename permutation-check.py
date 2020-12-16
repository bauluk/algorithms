def isPermutation(string_1, string_2):
    string_1 = list(string_1)
    string_2 = list(string_2)
    for i in range(0, len(string_1)):
        for j in range(0, len(string_2)):
            if string_1[i] == string_2[j]:
                del string_2[j]
                break
    
    if len(string_2) == 0:
        return True
    else:
        return False

string_1 = str(input())
string_2 = str(input())

if isPermutation(string_1, string_2):
    print('Your strings are permutations of each other.')
else:
    print('Your strings are not permutations of each other.')