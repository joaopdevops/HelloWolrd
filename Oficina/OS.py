# OI. OS COMENTÁRIOS AQUI PRESENTES SÃO MINHAS DIFICULDADES E APRENDIZADOS. VAMOS LÁ!!
# -----------------------------------------------------------------------------------------------------------------------------
# A FUNÇÃO print("") FOI A PRIMEIRA QUE APRENDI E LOGO DEPOIS A input(""). ABAIXO EU AS UTILIZEI BASTANTE PARA COLETA DE DADOS

print("=== ORDEM DE SERVIÇO BATALHÃO X ===")
data_chegada = input("Data de chegada (DD/MM/AAAA): ")
om_origem = input("OM de origem: ")
equipe = input("Número da quipe: ")
sargento = input("Sargento responsável: ")
viatura_marca_modelo = input("Marca/Modelo da viatura: ")
viatura_ident = input("Placa/EB da viatura: ")


# -----------------------------------------------------------------------------------------------------------------------------------------
# AQUI EU PERDI MUITAS HORAS PARA APRENDER A RODAR A LISTA, ATÉ PEGAR AS ASSOCIAÇÕES LÓGICAS QUE A LINGUAGEM NOS EXIGE.


tipos_servico = ['mecanica', 'borracharia', 'lanternagem',
                 'pintura', 'eletrica', 'capotaria', 'empresa civil']


print("\nTipos de servicos disponíveis:")
for servico in tipos_servico:
    print("-", servico)

# AO RODAR O CÓDIGO INICIALMENTE, EU PERCEBI QUE EU SÓ CONSEGUIA ESCOLHER UM TIPO DE SERVIÇO DA LISTA, ACHO QUE DEVO USAR O ".split", ENTÃO TENHO QUE PESQUISAR COMO MELHORAR ISSO
# CREIO QUE COM A PRÁTICA VOU EVOLUINDO ESSE PROJETO.
# ----------------------------------------------------------------------------------------------------------------------------------------


while True:
    tipo_servico = input("Tipo de servico: ").lower().strip()
    if tipo_servico in tipos_servico:
        break
    else:
        print("Digite um dos servicos da lsita acima para prosseguir.")


while True:
    tem_avarias = input(
        "A viatura chegou com avarias? (s/n): ").lower().strip()
    if tem_avarias in ["s", "n"]:
        break
    else:
        print("Digite apenas 's' para sim ou 'n' para não.")

avarias = []
if tem_avarias == "s":
    texto = input("Descreva as avarias (separe com vígula): ")
    avarias = [item.strip() for item in texto.split(",") if item.strip()]

print("\n=== RESUMO DA OS ===")
print("Data de chegada:", data_chegada)
print("OM/Origem:", om_origem)
print("Número da quipe", equipe)
print("Sargento responsável:", sargento)
print("Viatura:", viatura_marca_modelo)
print("Placa/EB", viatura_ident)
print("Tipo de serviço: ", tipo_servico)

print("\nAvarias:")
if not avarias:
    print("- (nenhuma)")
else:
    for item in avarias:
        print("-" + item)

print("\n... Fim da versão simples. Vou modificando conforme meu aprendizado. ")



