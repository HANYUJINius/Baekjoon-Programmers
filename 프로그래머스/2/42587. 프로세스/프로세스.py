
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
def solution(priorities, location):

    answer = 0
    loc = []

    for i in range(len(priorities)):             
        for i in range(len(priorities)):
            if max(priorities) == priorities[i]:   
                loc.append(i)                     
                priorities[i] = 0              

            if len(loc) == len(priorities):        
                break

        if len(loc) == len(priorities):            
                break    

    answer = loc.index(location) + 1

    return answer