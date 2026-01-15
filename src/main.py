import utils

validated_input_path = utils.user_input_path_validation() # --- Solicita ao usuário o caminho de input e verifica se é válido.
utils.clear_console()

origin_chapters = utils.get_chapters_list(validated_input_path) # --- Insere todos os capítulos encontrados em um vetor.



volumes = utils.chapters_volume_identification(origin_chapters) # --- Identifica o número do volume presente em cada capitulo e o anexa em um dicionário (chave e valor).



# --- Exibe os volumes identificados e seus respectivos capítulos.
print(f'Foram encontrados {len(origin_chapters)} capítulos, os quais foram organizados em {len(volumes)} volumes da seguinte forma:')
for volume, chapters in volumes.items():
    print(f'\nVolume {volume}:')
    for chapter in chapters:
        print(f'\t{chapter}')
utils.clear_console()




final_volumes = utils.user_volumename_organization(volumes) # --- Solicita ao usuário o nome que deseja para os volumes e os organiza com o devido nome.
utils.clear_console()



volumes_folder = utils.user_output_path_validation() # --- Solicita ao usuário o caminho de destino dos volumes.



utils.user_final_confirmation(final_volumes, validated_input_path, volumes_folder) # --- Solicita ao usuário a autorização final para mover os volumes.
utils.clear_console()



utils.volumes_folder_creator(validated_input_path, volumes_folder, final_volumes) # --- Cria e move os volumes autorizados pelo usuário.