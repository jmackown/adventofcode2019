

test1 = [1,9,10,3,2,3,11,0,99,30,40,50]
test2= [1,0,0,0,99]
test3 = [2,3,0,3,99]
test4 = [2,4,4,5,99,0]
test5 = [1,1,1,4,99,5,6,0,99]

real_input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,9,19,23,2,13,23,27,1,6,27,31,2,6,31,35,2,13,35,39,1,39,10,43,2,43,13,47,1,9,47,51,1,51,13,55,1,55,13,59,2,59,13,63,1,63,6,67,2,6,67,71,1,5,71,75,2,6,75,79,1,5,79,83,2,83,6,87,1,5,87,91,1,6,91,95,2,95,6,99,1,5,99,103,1,6,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]

op_codes = [1,2,99]

def perform_operation(op, int1, int2):
    result = None
    if op == 1:
        result = int1 + int2
    if op == 2:
        result = int1 * int2

    return result


def loopy(input):

    for x, value in enumerate(input):
        if x % 4 == 0:
            if value == 99:
                break
            pos = x
            input_val_1 = input[pos+1]
            input_val_2 = input[pos+2]
            output = input[pos+3]
            if input_val_1 and input_val_2:
                operation_result = perform_operation(op=value, int1=input[input_val_1], int2=input[input_val_2])
                input[output] = operation_result

    return input


def replace_vals(input):

    j = 0
    for i in range(100):
        for j in range(100):
            this_input = list(input)
            this_input[1] = i
            this_input[2] = j
            result = loopy(this_input)[0]

            if result == 19690720:
                print(i)
                print(j)
                print(this_input)
                print(100*i+j)
                break


print(replace_vals(real_input))