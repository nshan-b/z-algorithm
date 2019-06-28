# Z Algorithm : the simplest linear-time exact matching algorithm

def z_algorithm(text):
    Z = [0] * len(text) # Stores Z_k values
    l = 0  # Updates for left-most Z-box
    r = 0  # Updates for right-most Z-box
    for k in range(1, len(text)):
        if k > r:
            l = r = k
            # Continue to increment r while we compare both character ends after r for matches
            while(r < len(text) and text[r] == text[r - l]):
                r += 1
            Z[k] = r - l
            r -= 1
        else:
            # Inside a Z-box, conditions 2a and 2b
            k_prime = k - l
            # Condition 2a => Zk = Zk', copy values
            # Condition 2b => May be more matches, use direct comparison
            if(Z[k_prime] < r - k + 1):
                Z[k] = Z[k_prime]
            else:
                l = k
                while(r < len(text) and text[r] == text[r - l]):
                    r += 1
                Z[k] = r - l
                r -= 1
    return Z



# Quick Testing
'''
print(z_algorithm("abxyzq$qabxyzqabxyz"))
my_list = z_algorithm("abxyzq$qabxyzqabxyz")
list2 = list("abxyzq$qabxyzqabxyz")
for x in my_list:
    if x == len("abxyzq"):
        print(list2[x+1:x+len("abxyzq")+1])
print(list2)
'''