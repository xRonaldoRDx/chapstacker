import utils

validated_path = utils.user_path_validation() # --- Solicita ao usuário o caminho de input e verifica se é válido.

origin_chapters = utils.get_chapters_list(validated_path) # --- Insere todos os capítulos encontrados em um vetor.



# --- Lista todos os capítulos encontrados presentes no origin_chapters.
print(f"\nForam encontrados {len(origin_chapters)} capítulos:")
print("\n".join(origin_chapters))



# --- Verifica o nome de cada pasta de capítulo em busca do número de volume e então a anexa num padrão chave(volume) e valor(capítulo)
volumes = {} 

# --- Verifica cada capítulo encontrado
for chapter_name in origin_chapters:
    num_vol = utils.get_volume_number(chapter_name)

    if num_vol is not None:
        # Se a a chave do volume não existir, é criada.
        if num_vol not in volumes:
            volumes[num_vol] = [] 

        # Atribui o caítulo na chave certa
        volumes[num_vol].append(chapter_name)


# --- Exibe os volumes identificados e seus respectivos capítulos
print(f'\nOs capítulos indicados foram organizados em {len(volumes)} volumes da seguinte forma:')
for volume, chapters in volumes.items():
    print(f'\nVolume {volume}:')
    for chapter in chapters:
        print(f'\t{chapter}')
