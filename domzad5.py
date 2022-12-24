a = int(input('Введите число последовательностей: '))
negofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,a):
    new_list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(new_list)
    ne_list = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(ne_list)

negofibonacci.reverse()
negofibonacci.append(0)

print(f'  {a} = {negofibonacci+fibonacci}')