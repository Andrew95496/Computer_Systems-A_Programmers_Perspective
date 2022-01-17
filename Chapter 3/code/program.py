import dis

def sum(x, y):
    accum = 0
    t = x + y
    accum += t
    return t

dis.dis(sum)