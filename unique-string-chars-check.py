def isStringCharsUnique(incoming_string):
    for i in range(0, len(incoming_string)):
        for j in range(0, len(incoming_string)):
            if (i != j) and (incoming_string[i] == incoming_string[j]):
                print('Match Found - Positions: ' + str(i + 1) + ' & ' + str(j + 1)) # "+ 1" to avoid 0 position for readability
                return False
    
    return True

incoming_string = str(input())

if isStringCharsUnique(incoming_string) is True:
    print('Your string has all unique characters.')
else:
    print('Your string does not have all unique characters.')