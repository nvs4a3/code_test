
#Solution for number of arrow turns

def solution(S):
    #Define a default map that stores the count of each direction count
    arrow_dict = {'<':0, '>':0, '^':0, 'v':0 }

    for char in S: 
        if char == '<':
            arrow_dict['<']+=1
        elif char == '>':
            arrow_dict['>']+=1
        elif char == '^':
            arrow_dict['^']+=1
        elif char == 'v':
            arrow_dict['v']+=1

    count_of_arrows = arrow_dict.values()
    max_arrow_count = max(count_of_arrows)
    if max_arrow_count == len(S):
        return 0
    else:
        return len(S)-max_arrow_count

def help_message():
    print("Below Characters represent arrows in different directions")
    print("\t\t < \t\t")
    print("\t\t > \t\t")
    print("\t\t v \t\t")
    print("\t\t ^ \t\t")


def verify_input(S):
    allowed_input=[ '<', '>', 'v' ,'^']
    #verifying whether all the charaters in string are valid or not
    for char in S:
        if not (char in allowed_input):
            raise Exception("Input string has invalid inputs")

if __name__ == "__main__":
    help_message()
    input_string = input("Enter string input:")
    formated_string = str(input_string)
    verify_input(formated_string)
    arrows_to_turn=solution(formated_string)
    print("No.of arrows to turn are {}".format(arrows_to_turn))
