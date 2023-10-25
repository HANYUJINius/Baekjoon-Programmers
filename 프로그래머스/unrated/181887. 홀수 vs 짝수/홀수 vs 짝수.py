def solution(num_list):
    o_sum = 0
    e_sum = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            o_sum += num_list[i]
        else:
            e_sum += num_list[i]
        
    return max(o_sum, e_sum)