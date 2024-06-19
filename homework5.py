# Homework5

# Пример результата выполнения программы:
# Immutable tuple: (1, 2, 'a', 'b')
# Mutable list: [1, 2, 'a', 'b', 'Modified']

immutable_var = (1, 2, 'a', 'b')
print('Immutable tuple: ',immutable_var)
#immutable_var [0] = 3 ошибка так как кортеж является неизменяемым списком
#print(immutable_var)
mutable_list = [1, 2, 'a', 'b']
mutable_list.append('Modified')
print('Mutable list: ',mutable_list)