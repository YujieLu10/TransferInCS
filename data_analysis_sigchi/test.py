def get_patentid(x):
    x = x[x.index("-")+1:]
    if "-" in x:
        return x[:x.index("-")]
    else:
        return x
    
print(get_patentid("US-123-23"))