import utils

validated_input_path = utils.user_path_validation() # --- Solicita ao usuário o caminho de input e verifica se é válido.

origin_chapters = utils.get_chapters_list(validated_input_path) # --- Insere todos os capítulos encontrados em um vetor.



# --- Lista todos os capítulos encontrados presentes no origin_chapters.
print(f"\nForam encontrados {len(origin_chapters)} capítulos:")
print("\n".join(origin_chapters))


volumes = utils.chapters_volume_identification(origin_chapters) # --- Identifica o número do volume presente em cada capitulo e o anexa em um dicionário (chave e valor).



# --- Exibe os volumes identificados e seus respectivos capítulos.
print(f'\nOs capítulos indicados foram organizados em {len(volumes)} volumes da seguinte forma:')
for volume, chapters in volumes.items():
    print(f'\nVolume {volume}:')
    for chapter in chapters:
        print(f'\t{chapter}')



final_volumes = utils.user_volumename_organization(volumes) # --- Solicita ao usuário o nome que deseja para os volumes e os organiza com o devido nome.



# --- Exibe os volumes com seus respetivos nomes finais e capítulos.
for volume, chapters in final_volumes.items():
    print(f'\n {volume}:')
    for chapter in chapters:
        print(f'\t{chapter}')