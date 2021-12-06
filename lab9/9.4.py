def replace(d,v,e):
    for key in d.keys():
        if d[key] == v:
            d[key]=e
    return d

d={'1':3, '2':3, "5":3, '6':5}
print(replace(d,3,9))