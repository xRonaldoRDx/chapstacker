from pathlib import Path
import re

def is_valid_directory(inserted_path):
    return inserted_path.exists() and inserted_path.is_dir()

def user_path_validation():
    while True:
        input_path = Path(input('Digite o caminho da pasta dos capítulos: '))

        if is_valid_directory(input_path):
            print(f'\nO caminho digitado é válido. Iremos trabalhar na pasta {input_path}.')
            return input_path
        else:
            print('O caminho digitado não é válido, verifique a escrita e tente novamente.\n')

def get_chapters_list(validated_path):

    chapters = []
    for item in validated_path.iterdir():
        if item.is_dir():
            chapters.append(item.name)
    
    chapters.sort()    
    return chapters


def get_volume_number(chapter_name):
    # (?i) = ignorar maiúsculas/minúsculas
    # (?:vol|v|volume) = procurar por uma dessas palavras
    # [\s.]* = aceitar espaços ou pontos no meio
    # (\d+) = capturar um ou mais números
    pattern = r'(?i)(?:volume|vol|v)[\s.]*(\d+)'

    match = re.search(pattern, chapter_name)

    if match:
        # --- Recebe apenas o que estava dentro do parênteses (\d+)
        volume_number = match.group(1) 
        return int(volume_number) # Transforma "01" em "1"
    return None

def user_volumename_organization(volumes):
    volumes_base_name = input('Digite a base para os nomes dos volumes (digite "{#n}" onde deverão ficar o número do volume: ')

    final_volumes_organization = {}
    for volume, chapters in volumes.items():
        new_volume_name = volumes_base_name.replace('{#n}', str(volume))
        final_volumes_organization[new_volume_name] = chapters
    
    return final_volumes_organization

def chapters_volume_identification(origin_chapters):
    # --- Verifica o nome de cada pasta de capítulo em busca do número de volume e então a anexa num padrão chave(volume) e valor(capítulo)
    volumes = {} 

    # --- Verifica cada capítulo encontrado
    for chapter_name in origin_chapters:
        num_vol = get_volume_number(chapter_name)

        if num_vol is not None:
            # Se a a chave do volume não existir, é criada.
            if num_vol not in volumes:
                volumes[num_vol] = [] 

            # Atribui o caítulo na chave certa
            volumes[num_vol].append(chapter_name)

    return volumes