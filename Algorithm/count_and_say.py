def countAndSay(n):
    seq = "1"
    for i in range(n-1):
        seq = getNext(seq)
    return seq

def getNext(seq):
    i, next_seq = 0, ""
    while i < len(seq):
        count = 1
        while i < len(seq)  -1 and seq[i] == seq[i+1]:
            count += 1
            i += 1
        next_seq += str(count) + seq[i]
        i += 1
    return next_seq
