lista = [1,2,3,4,5,6,7,8,9,10]

for number in range(len(lista)+1):
    print(number)
    if number > 5:
        lista.remove(number)
    
print(lista)