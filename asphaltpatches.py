
def solution(S):
    i = 0
    patches = 0

    while(i<len(S)):
        segment = S[i]
        if segment == 'X':
            i+=3
            patches+=1
        else:
            i+=1
    return patches

def verify_input(S):
    allowed_inputs = [ 'X', '.']
    for seg in S:
        if not (seg in allowed_inputs):
            raise Exception("Invalid inputs in the String")


def help_message():
    print("Valid inputs for the String are:")
    print("\t\t X \t\t")
    print("\t\t . \t\t")

if __name__ == "__main__":
    help_message()
    input_string = input("Enter input string representing potholes and good segment:")
    formated_input = str(input_string)
    verify_input(formated_input)
    print("Number of patches required for  the given input {}".format(solution(formated_input)))

