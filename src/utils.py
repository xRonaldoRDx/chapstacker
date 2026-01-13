from pathlib import Path

def is_valid_directory(inserted_path):
    return inserted_path.exists() and inserted_path.is_dir()

def user_path_validation():
    while True:
        input_path = Path(input('Digite o caminho da pasta dos capítulos: '))

        if is_valid_directory(input_path):
            print(f'O caminho digitado é válido. Iremos trabalhar na pasta {input_path}.')
            return input_path
        else:
            print('O caminho digitado não é válido, verifique a escrita e tente novamente.')

def get_chapters_list(validated_path):

    chapters = []
    for item in validated_path.iterdir():
        if item.is_dir():
            chapters.append(item.name)
    
    chapters.sort()    
    return chapters