# Reversing an string

def reverse_string(s):
    c = list(s)
    l = len(c)
    if len(c) == 0:
        return c
    elif len(c) == 1:
        return c
    else:
        for i in range(l//2):
            temp = c[i]
            c[i] = c[l -i -1]
            c[l - i - 1]= temp
        return "".join(c)
    
r = reverse_string("Nafis")
print(r)

