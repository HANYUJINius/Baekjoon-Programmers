def solution(operations):
    num_list = []
    for i in operations:
        if(i[0] == "I"): # 숫자 추가
            num = int(i[2:])
            num_list.append(num)
        else:
            if(i[2] == "-"): # 최소값 삭제
                if(len(num_list) <= 1): # List 크기가 1 이하이면 List 비우기
                    num_list.clear()
                else:
                    min_num = min(num_list)
                    num_list.remove(min_num)
            else: # 최대값 삭제
                if(len(num_list) <= 1): # List 크기가 1 이하이면 List 비우기
                    num_list.clear()
                else:
                    max_num = max(num_list)
                    num_list.remove(max_num)
    if (len(num_list) == 0):
        return [0,0]
    return [max(num_list), min(num_list)]