def solution(N):
    binary = format(N, "b")
    binary_to_num = int(binary)
    length = len(binary)
    count  = 0
    num_list = []
    
    if binary_to_num % 10 is 0: #100 #1000
        return 0
    if N is 0:
        return 0
    
    for ele in range(length-1):
        if binary[ele] is '0' and binary[ele+1] is '0':
            count = count + 1
            if binary[ele+1] is not '1':
                num_list.append(count)
            else: 
                num_list.append(count)
        elif binary[ele] is '1' and binary[ele+1] is '0':
            count = count + 1            
        else:
            num_list.append(count)
            count = 0
    return max(num_list)
