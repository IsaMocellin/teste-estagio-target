# 3) Faturamento diário (usando JSON como fonte)
import json

faturamento_json = '''
{
    "faturamento_diario": [200, 450, 0, 0, 320, 600, 0, 780, 0, 420, 520, 0, 330, 0, 550, 0, 610, 700, 800, 430, 340, 0, 900, 0, 0, 500, 430, 0, 670, 350]
}
'''

dados_faturamento = json.loads(faturamento_json)["faturamento_diario"]

faturamentos_validos = [x for x in dados_faturamento if x > 0]
menor_faturamento = min(faturamentos_validos)
maior_faturamento = max(faturamentos_validos)
media_faturamento = sum(faturamentos_validos) / len(faturamentos_validos)
dias_acima_media = len([x for x in faturamentos_validos if x > media_faturamento])

print(f"3) Menor faturamento: R${menor_faturamento}")
print(f"   Maior faturamento: R${maior_faturamento}")
print(f"   Dias com faturamento acima da média mensal: {dias_acima_media} dias")
