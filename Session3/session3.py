def fibonacci(max_num):
    seq_1 = 0
    seq_2 = 1
    F = [0, 1]
    while True:
        new_seq = seq_1 + seq_2
        seq_1 = seq_2
        seq_2 = new_seq
        if seq_2 < max_num:
            F.append(new_seq)
        else:
            break
    return F

def rem_dup_loop(input_list):
    output_list = []
    for num in input_list:
        if num not in output_list:
            output_list.append(num)
    return output_list
            


def rem_dup_set(input_list):
    output_list = set(input_list)
    return(output_list)