
# 5) Inverter caracteres de uma string sem usar funções prontas
def inverte_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string_original = "Distribuidora"  # Altere a string conforme desejado
string_invertida = inverte_string(string_original)

print(f"5) String original: {string_original}")
print(f"   String invertida: {string_invertida}")
