from pathlib import Path

def is_valid_directory(inserted_path):
    return inserted_path.exists() and inserted_path.is_dir()

def user_path_validator():
    while True:
        input_path = Path(input('Digite o caminho da pasta dos capítulos: '))

        if is_valid_directory(input_path):
            print(f'O caminho digitado é válido. Iremos trabalhar na pasta {input_path}.')
            return input_path
        else:
            print('O caminho digitado não é válido, verifique a escrita e tente novamente.')

