def converter_moeda(valor, moeda):
    """Converte um valor para a moeda especificada."""
    taxas_cambio = {
        "real": 1.00,
        "dolar": 5.89,
        "libra": 7.79
    }
    moeda_limpa = moeda.lower().replace('ó', 'o')
    if moeda_limpa in taxas_cambio:
        return valor / taxas_cambio[moeda_limpa]
    else:
        return "\033[91mMoeda não suportada.\033[0m"  # Vermelho para erro

frutas_data = [
    {"nome": "Banana (dúzia)", "valor": 8.00},
    {"nome": "Maracujá", "valor": 5.50},
    {"nome": "Manga", "valor": 6.00},
]

nomes_frutas = ["\033[93m" + fruta["nome"] + "\033[0m" for fruta in frutas_data]

print("Lista de Frutas Disponíveis:")
for i, nome in enumerate(nomes_frutas):
    print(f"{i + 1} - {nome} (\033[94mR$ {frutas_data[i]['valor']:.2f}\033[0m)")

moeda_desejada = input("\nEscolha a moeda para conversão (real, dolar ou libra): ").strip()
moeda_formatada = moeda_desejada.capitalize()

print(f"\n--- Lista de Frutas em {moeda_formatada} ---")
for i, nome in enumerate(nomes_frutas):
    valor_convertido = converter_moeda(frutas_data[i]['valor'], moeda_desejada)
    if isinstance(valor_convertido, str):
        print(f"{i + 1} - {nome}: {valor_convertido}")
    else:
        print(f"{i + 1} - {nome}: \033[94m{moeda_formatada} {valor_convertido:.2f}\033[0m")

carrinho = []
total_compra = 0.0

while True:
    try:
        escolha = input("\nDigite o número da fruta que deseja adicionar ao carrinho (ou 'fim' para finalizar): ").lower()
        if escolha == 'fim':
            break

        indice_fruta = int(escolha) - 1
        if 0 <= indice_fruta < len(frutas_data):
            quantidade = int(input(f"Quantas unidades de {nomes_frutas[indice_fruta]} você quer? "))
            if quantidade > 0:
                fruta_selecionada = frutas_data[indice_fruta]
                carrinho.append({"nome": nomes_frutas[indice_fruta], "quantidade": quantidade, "valor_unitario_real": fruta_selecionada["valor"]})
            else:
                print("A quantidade deve ser maior que zero.")
        else:
            print("Opção inválida. Por favor, digite o número da fruta na lista.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

print("\n--- Carrinho de Compras ---")
for item in carrinho:
    valor_unitario_convertido = converter_moeda(item["valor_unitario_real"], moeda_desejada)
    total_item = valor_unitario_convertido * item["quantidade"]
    total_compra += total_item
    print(f"{item['nome']} ({item['quantidade']}): {moeda_formatada} {valor_unitario_convertido:.2f}, Total: {moeda_formatada} {total_item:.2f}")

print(f"\nTotal da Compra: \033[92m{moeda_formatada} {total_compra:.2f}\033[0m")