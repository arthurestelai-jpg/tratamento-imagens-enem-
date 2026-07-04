from PIL import Image
import os


class RemoverEspacoBranco:

    def __init__(self):
        self.pasta_origem = "finalizadas"
        self.pasta_destino = "finalizadass"

        # Quanto maior, mais "branco" a linha precisa ser
        self.limite_branco = 245

        # Quantos pixels abaixo do último conteúdo cortar
        self.margem = 8

        os.makedirs(self.pasta_destino, exist_ok=True)


    def linha_esta_branca(self, pixels, largura, y):

        brancos = 0

        for x in range(largura):

            r, g, b = pixels[x, y][:3]

            if (
                r >= self.limite_branco and
                g >= self.limite_branco and
                b >= self.limite_branco
            ):
                brancos += 1

        return brancos >= largura * 0.995


    def encontrar_fim(self, imagem):

        largura, altura = imagem.size

        pixels = imagem.load()

        for y in range(altura - 1, -1, -1):

            if not self.linha_esta_branca(pixels, largura, y):

                corte = min(y + self.margem, altura)

                return corte

        return altura


    def processar_imagem(self, caminho_origem, caminho_destino):

        imagem = Image.open(caminho_origem)

        y = self.encontrar_fim(imagem)

        imagem = imagem.crop((0, 0, imagem.width, y))

        imagem.save(caminho_destino)

        print(f"✓ {os.path.basename(caminho_origem)}")


    def executar(self):

        arquivos = sorted(

            [
                arquivo
                for arquivo in os.listdir(self.pasta_origem)
                if arquivo.lower().endswith(".png")
            ]

        )

        print(f"{len(arquivos)} imagens encontradas.\n")

        for arquivo in arquivos:

            origem = os.path.join(self.pasta_origem, arquivo)

            destino = os.path.join(self.pasta_destino, arquivo)

            self.processar_imagem(origem, destino)

        print("\nProcessamento concluído!")


if __name__ == "__main__":

    remover = RemoverEspacoBranco()

    remover.executar()