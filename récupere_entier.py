#  Programme retrieves the grades of a class. Subsequently, the algorithm must display grades above average.
n = int(input("Entrez un entier n : "))
p = []
for num in range(2, n):   
    is_p = True
    for i in range(2, num):
        if num % i == 0:
            is_p = False
            break    
p.append(num)
print(f"Les nombres premiers inférieurs à {n} sont : {p}")















