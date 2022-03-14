def solution(S):
    a = 0
    mod_S = S

    length = len(S)

    if (len(S) < 2 ):
        return -1

    if( mod_S[0] == 'H'):
        if mod_S[1] == 'H':
            return -1
        else:
            mod_S[1]='T'
    
    if mod_S[length-1] == 'H':
        if mod_S[length-2] == 'H':
            return -1
        else:
            mod_S[length-2]='T'

    i = 1
    while i < length-1:
        if mod_S[i] == 'H':
            if mod_S[i-1] == 'H' and mod_S[i+1] == 'H':
                return -1
            if mod_S[i-1] != 'T' and mod_S[i+1] != 'T':
                if mod_S[i+1] == '-' :
                    mod_S[i+1] = 'T'
                else:
                    mod_S[i-1] = 'T'
        i+=1

    i = 0
    while i < length:
        if mod_S[i] == 'T':
            a+=1
        i+=1

    if a == 0:
        a = -1

    print("Modified String is {}".format(mod_S))
    return a

def help_message():
    print("Allowed chars for the input string are:" )
    print("\t\t H \t\t")
    print("\t\t - \t\t")

def verify_input(S):
    allowed_input = [ "H", "-" ]
    for char in S:
        if not (char in allowed_input):
            raise Exception("Input string has invalid inputs")

def Convert(string):
    list1 = []
    list1[:0] = string
    return list1



if __name__ == "__main__":
    help_message()
    input_string = input("Enter input string with H and -:")
    formated_input = str(input_string)
    verify_input(formated_input)
    formated_list = Convert(formated_input)
    num_of_insert = solution(formated_list)
    print("Min number of insertion required are {}".format(num_of_insert))


