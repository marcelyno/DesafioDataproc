with open("resultado_part-00000.txt", encoding="utf8") as file:
    data = file.read().split('\n')
    data = data[:10]
    output = ""
    output = '\n'.join(data)
    print(output)

with open('resultado.txt', 'w') as file:
    file.write(output)