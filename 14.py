#import random
#random.seed(111)
#print (random.randint(1,15))
#14, 7
name='myfirastfile.txt'
ssum = 0
with open(name, 'r') as file:
    text = file.read()
    words = text.split()
    for i in words:
        if i.isdigit():
            n = int(i)
            if 1 <= n <= 10:
                ssum += n
# Выводим результат
print("Сумма чисел от 1 до 10 в файле:", ssum)
