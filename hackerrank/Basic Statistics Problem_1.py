def compute_mean(arr):
    if len(arr) < 1:
        return None
    else:
        return sum(arr)/len(arr)

def compute_median(arr):
    if len(arr) < 1:
        return None
    elif len(arr) == 1:
        return arr
    else:
        return sorted(arr)[len(arr)//2] if len(arr) % 2 == 1 else (sorted(arr)[len(arr)//2-1] + sorted(arr)[len(arr)//2])/2

def get_mode(arr):
    d = {}
    for i in sorted(arr):
        d[i] = d.get(i,0) + 1
    
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))] if max(v) !=1 else k[0]
    
print(get_mode(arr))

def get_numbers(n, values):
    arr = []
    for n in values.split():
        arr.append(int(n))
    return arr
	
n = input()
values = input()

numbers = get_numbers(n, values)

print(compute_mean(numbers))
print(compute_median(numbers))
print(get_mode(numbers))