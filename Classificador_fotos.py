#pip install pyheif
import os
from PIL import Image
import pyheif

# Definir o diretório que contém as imagens originais
diretorio = "/Users/jeffersonforti/Library/CloudStorage/OneDrive-Pessoal/Pessoais/MESTRADO/Dados_coletados/Fotos_mineradas"

# Extensões de arquivo consideradas para conversão (exceto PNG, já que queremos mantê-las)
extensoes_validas = {'.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.heic', '.JPG', '.JPEG', '.GIF', '.BMP', '.TIFF', '.HEIC'}

# Lista para armazenar os caminhos das imagens que serão verificadas
arquivos_para_processar = []

# Listar arquivos no diretório
for arquivo in os.listdir(diretorio):
    # Verificar se o arquivo é uma imagem com base na extensão
    if os.path.splitext(arquivo)[1].lower() in extensoes_validas or os.path.splitext(arquivo)[1].lower() == '.png':
        arquivos_para_processar.append(arquivo)

# Ordenar a lista de arquivos (opcional, dependendo de como deseja numerar as imagens)
arquivos_para_processar.sort()

# Processar arquivos
for idx, nome_arquivo in enumerate(arquivos_para_processar, start=1):
    # Caminho completo para o arquivo original
    caminho_arquivo_original = os.path.join(diretorio, nome_arquivo)
    
    # Definir o novo nome do arquivo, mantendo o formato .png
    novo_nome_arquivo = f"imagem_{idx}.png"
    caminho_arquivo_novo = os.path.join(diretorio, novo_nome_arquivo)
    
    # Verificar se a imagem já está em formato .png
    if os.path.splitext(nome_arquivo)[1].lower() == '.png':
        # Simplesmente renomear se já for .png
        os.rename(caminho_arquivo_original, caminho_arquivo_novo)
    else:
        # Carregar a imagem para conversão
        if os.path.splitext(nome_arquivo)[1].lower() == '.heic':
            # Carregar a imagem HEIC
            heif_file = pyheif.read_heif(caminho_arquivo_original)
            imagem = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data, 
                "raw", 
                heif_file.mode, 
                heif_file.stride,
            )
        else:
            imagem = Image.open(caminho_arquivo_original)
        
        # Salvar a imagem no formato .png
        imagem.save(caminho_arquivo_novo, 'PNG')
        
        # Apagar o arquivo original após a conversão
        os.remove(caminho_arquivo_original)

    print(f"Processado: '{nome_arquivo}' para '{novo_nome_arquivo}'")

print("Conclusão do processamento de arquivos.")