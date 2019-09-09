def get_mean(n):
    return sum(n)/len(n)
    
def convert_n(n):
    cn = []
    
    for i in n.split():
        cn.append(i)
        
    return cn
    
def compute_standard_deviation(cn, mean):
    d = 0
    for n in cn:
        d+= (n-mean)^2
    
    return d/len(cn)
    
n = int(input())
numbers = input()

cn = convert_n(numbers)
mean = get_mean(cn)

print(compute_standard_deviation(cn, mean))

"{:.1f}".format(number)