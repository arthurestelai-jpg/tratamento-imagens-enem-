from pathlib import Path


class RenomeadorQuestoes:

    def __init__(self, pasta, primeira_questao, ultima_questao):

        self.pasta = Path(pasta)
        self.primeira_questao = primeira_questao
        self.ultima_questao = ultima_questao

    def listar_imagens(self):

        if not self.pasta.exists():
            raise FileNotFoundError(
                f"A pasta '{self.pasta}' não foi encontrada."
            )

        imagens = sorted(
            self.pasta.glob("parte_*.png"),
            key=lambda arquivo: int(
                arquivo.stem.replace("parte_", "")
            )
        )

        return imagens

    def validar_quantidade(self, quantidade):

        esperado = (
            self.ultima_questao
            - self.primeira_questao
            + 1
        )

        print(f"Imagens encontradas : {quantidade}")
        print(f"Imagens esperadas   : {esperado}")

        if quantidade != esperado:
            print("\nAviso:")
            print(
                "A quantidade de imagens não corresponde "
                "à quantidade de questões.\n"
            )

    def renomear(self):

        imagens = self.listar_imagens()

        self.validar_quantidade(len(imagens))

        numero = self.primeira_questao

        for imagem in imagens:

            if numero > self.ultima_questao:
                break

            novo_nome = self.pasta / f"questao-{numero}.png"

            if novo_nome.exists():
                novo_nome.unlink()

            imagem.rename(novo_nome)

            print(
                f"{imagem.name}  →  {novo_nome.name}"
            )

            numero += 1

        print("\nRenomeação concluída!")

    def executar(self):

        self.renomear()


if __name__ == "__main__":

    renomeador = RenomeadorQuestoes(
        pasta="155-180",
        primeira_questao=155,
        ultima_questao=180
    )

    renomeador.executar()