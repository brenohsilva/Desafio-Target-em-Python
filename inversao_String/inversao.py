string = input("Digite a palavra que você deseja inverter: ")
string_invertida = ''

for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

print("a String invertida é: ", string_invertida)