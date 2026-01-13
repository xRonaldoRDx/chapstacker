import utils

validated_path = utils.user_path_validation() # --- Solicita ao usuário o caminho de input e verifica se é válido.

origin_chapters = utils.get_chapters_list(validated_path) # --- Insere todos os capítulos encontrados em um vetor.

# --- Lista todos os capítulos encontrados presentes no origin_chapters.
print(f"\nForam encontrados {len(origin_chapters)} capítulos:")
print("\n".join(origin_chapters))