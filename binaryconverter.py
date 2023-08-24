# init variables

binary_key = []

for power in range(32):
    binary_key.append(2**(31-power))

# declare functions

def calculate_binary(input):
    sum = 0
    input_length = len(input)
    for place in range(input_length):
        if input[input_length-1-place] == "1":
            sum += binary_key[31-place]
    print("Your binary number represents " + str(sum) + "!")

# input & output

while True:
    print("Enter the binary number to be converted: ")
    user_input = str(input())
    calculate_binary(user_input)