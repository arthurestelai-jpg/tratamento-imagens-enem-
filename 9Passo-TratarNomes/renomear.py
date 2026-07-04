import os


def renomear_questoes():

    pasta = "155-180"

    inicio = 155
    fim = 180

    if not os.path.isdir(pasta):
        print("Pasta não encontrada.")
        return

    imagens = [
        arquivo for arquivo in os.listdir(pasta)
        if arquivo.endswith(".png") and arquivo.startswith("parte_")
    ]

    imagens.sort(key=lambda arquivo: int(arquivo.replace("parte_", "").replace(".png", "")))

    esperado = fim - inicio + 1

    if len(imagens) != esperado:
        print(f"Foram encontradas {len(imagens)} imagens.")
        print(f"O esperado era {esperado}.\n")

    indice = 0

    for numero in range(inicio, fim + 1):

        if indice >= len(imagens):
            break

        origem = os.path.join(pasta, imagens[indice])

        destino = os.path.join(
            pasta,
            f"questao-{numero}.png"
        )

        os.rename(origem, destino)

        print(f"Questão {numero} criada.")

        indice += 1

    print("\nProcesso finalizado.")


if __name__ == "__main__":
    renomear_questoes()