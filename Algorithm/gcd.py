# Greatest Common Divisor

def finding_gcd(a,b):
    wile(b!=0):
        result = b
        a, b = b, a%b
    return result

