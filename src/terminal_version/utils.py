from pathlib import Path
from re import search
from shutil import move
from os import system, name



# --- Validações de caminho
def is_valid_directory(inserted_path):
    return inserted_path.exists() and inserted_path.is_dir() and any(inserted_path.iterdir())

def user_input_path_validation():
    while True:
        input_path = Path(input('Digite o caminho da pasta dos capítulos: '))

        if is_valid_directory(input_path) and input_path:
            print(f'\nO caminho digitado é válido. Iremos trabalhar na pasta {input_path}.')
            return input_path
        else:
            print('\nErro: O caminho é inválido, não é uma pasta ou está totalmente vazia.')
            print('Verifique e tente novamente.\n')

def user_output_path_validation():
    while True:
        output_path = Path(input('Digite o caminho de destino para os volumes: '))

        # --- Verifica se o local é gravável.
        if output_path.parent.exists():
            
            # --- Se a pasta não existe, confirma se o usuário deseja criá-la.
            if not output_path.exists():
                user_confirmation = input(f"A pasta {output_path} não existe. Deseja criá-la? (S/N): ").upper()
                if user_confirmation == 'S':
                    try:
                        output_path.mkdir(parents=True, exist_ok=True)
                        return output_path
                    except Exception as e:
                        print(f"Erro ao criar pasta: {e}")
                else:
                    print("Por favor, digite outro caminho.")
            else:
                return output_path
        else:
            print("O caminho pai não existe. Verifique o drive ou a pasta principal.")

def user_final_confirmation(final_volumes, validated_input_path, volumes_folder):
    print('\nOs seguintes volumes: ')

    for volume, chapters in final_volumes.items():
        print(f'\n {volume}:')
        for chapter in chapters:
            print(f'\t{chapter}')

    print(f'\nSerão movidos de {validated_input_path}')
    print(f'para {volumes_folder}.')
    
    while True:
        user_confirmation = input('\nDeseja continuar [S/N]? Após isso o processo não poderá ser parado: ').upper() 
        if user_confirmation == 'S':
            print('\nTerminando manipulação...')
            return
        elif user_confirmation == 'N':
            print('\nOperação cancelada, nenhum arquivo foi movido.')
            exit()
        else:
            print(f'Entrada inválida! Digite apenas "S" para Sim ou "N" para não.')
            continue



# --- Organização de volumes e capítulos

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

    match = search(pattern, chapter_name)

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



# --- Manipulação de Volumes e Capítulos

def volumes_folder_creator(input_path, output_path, volumes):
    for volume_name, chapters in volumes.items():
        volume_path = output_path/volume_name
    
        volume_path.mkdir(parents=True, exist_ok=True) 
        if volume_path.exists():
            print(f'\nPasta {volume_name} criada com sucesso!')

        for chapter in chapters:
            origin = input_path/chapter
            destination = volume_path/chapter

            move(str(origin), str(destination))
            print(f'\t└─ {chapter} movido com sucesso!')

    print('\nTodos os capítulos foram movidos com sucesso!')



# --- User Experience

def clear_console():
    input('\nPressione [Enter] para continuar...')
    
    # Verifica o sistema operacional e então limpa a tela de acordo.
    if name == 'nt':
        system('cls')
    else:
        system('clear')