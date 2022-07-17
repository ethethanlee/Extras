x = {"Gfg" : 5, "is" : 5, "Best" : 5}
y = {"Gfg" : 5, "is" : 5, "Best" : 5}

shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
print(len(x))
print(len(shared_items))