# Take the first input from user
loop_flag = True
input_msg = "Please input an integer"
while loop_flag:
    try:
        n_input = int(input(input_msg))
        loop_flag = False
    except:
        input_msg = "Your input is invalid, please input an integer"

# Once we get the n_input, we ask the user to input n_input numbers again
input_list = []
for i in range(n_input):
    loop_flag = True
    input_msg = f"Please input No.{i+1} integer"
    while loop_flag:
        try:
            input_list.append(int(input(input_msg)))
            loop_flag = False
        except:
            input_msg = "Your input is invalid, please input an integer"

# Ask user to input again and check if it has been input before

loop_flag = True
input_msg = "Please input an integer for the system to check"
while loop_flag:
    try:
        rs_input = int(input(input_msg))
        if rs_input in input_list:
            print(input_list.index(rs_input)+1)
        else:
            print("-1")
        loop_flag = False
    except:
        input_msg = "Your input is invalid, please input an integer"
