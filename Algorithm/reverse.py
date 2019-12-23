# V.01
def reverse(integer):
    str_int = str(integer)
    if integer < 0:
        integer = integer * -1
        return int(str(integer)[::-1])*-1
    elif str_int[-1] == '0':
        return int(str_int.rstrip('0')[::-1])       
    else:
        return int(str_int[::-1])
