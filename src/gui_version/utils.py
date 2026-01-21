from pathlib import Path
from re import search
from shutil import move



def is_valid_directory(inserted_path):
    return inserted_path.exists() and inserted_path.is_dir() and any(inserted_path.iterdir())

def is_writable_path(output_path):
    return output_path.parent.exists()

def apply_volume_custom_names(volumes, base_name_pattern):
    final_volumes_organization = {}
    for volume, chapters in volumes.items():
        new_volume_name = base_name_pattern.replace('{#n}', str(volume))
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



def volumes_folder_creator(input_path, output_path, volumes_dict):
    process_log = []

    for volume_name, chapters in volumes_dict.items():
        volume_path = output_path / volume_name
        try:
            volume_path.mkdir(parents=True, exist_ok=True)
            process_log.append(f'Pasta {volume_name} criada.')
            for chapter in chapters:
                origin = input_path / chapter
                destination = volume_path / chapter
                move(str(origin), str(destination))
                process_log.append(f'   └─ {chapter} movido.')
        except Exception as e:
            process_log.append(f'Erro ao criar {volume_name}: {e}')

    return process_log

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
        return int(match.group(1)) # Transforma "01" em "1"
    return None