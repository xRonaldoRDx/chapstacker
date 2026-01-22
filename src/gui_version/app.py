import customtkinter as ctk
from datetime import datetime
from pathlib import Path
import threading
import utils

class ChapstackerApp(ctk.CTk):
    
    def select_origin(self):
        path = ctk.filedialog.askdirectory()
        
        if path:
            self.origin_path = path
            print(f"Path selected: {self.origin_path}")
            self.origin_content.configure(text=path)

            # --- Muda a cor do botão para indicar sucesso.
            self.btn_origin.configure(fg_color="green")

            # --- Atualiza o Log
            self.update_log(f"Origin folder selected: {path}")

    def select_destination(self):
        path = ctk.filedialog.askdirectory()

        if path:
            self.destination_path = path
            print(f"Path selected: {self.destination_path}")
            self.destination_content.configure(text=path)
            
            # --- Muda a cor do botão para indicar sucesso.
            self.btn_destination.configure(fg_color="green")

            # --- Atualiza o Log
            self.update_log(f"Destination folder selected: {path}")

    def update_log(self, message):
        # Obtém o horário atual para o log
        timestamp = datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"

        # 1. Habilita a caixa para escrita
        self.log_textbox.configure(state="normal")
        
        # 2. Insere a mensagem no final
        self.log_textbox.insert("end", full_message)
        
        # 3. Faz o scroll automático para a última linha
        self.log_textbox.see("end")
        
        # 4. Desabilita novamente para o usuário não editar
        self.log_textbox.configure(state="disabled")

    def run_process(self):
        pattern = self.entry_name_pattern.get().strip()

        # --- Verifica falta de dados do usuário
        if not self.origin_path:
            self.update_log("ERROR: Select an origin folder first.")
            return
        if not self.destination_path:
            self.update_log("ERROR: Select a destination folder first.")
            return
        if "{#n}" not in pattern:
            self.update_log("ERROR: Invalid pattern! Use '{#n}' for numbering.")
            return
        
        # --- Desativa o botão START para evitar cliques enquanto processa os dados
        self.btn_run.configure(state="disabled", text="PROCESSING...")

        # --- Cria e inicia o Thread
        # --- daemon=True garante que a thread morra se a janela principal fechar
        thread = threading.Thread(target=self.execute_task, args=(pattern,), daemon=True)
        thread.start()

    def execute_task(self, pattern):
        p_origin = Path(self.origin_path)
        p_dest = Path(self.destination_path)

        self.update_log("--- Starting Organization Process ---")

        try:
            # --- Verifica os capítulos presentes na origem.
            chapters = utils.get_chapters_list(p_origin)
            self.update_log(f"Found {len(chapters)} folders in origin.")

            # --- Identifica os volumes presentes nas pastas dos capítulos.
            volumes_found = utils.chapters_volume_identification(chapters)
            if not volumes_found:
                self.update_log("WARNING: No volume numbers identified in chapter names.")

            self.update_log(f"Identified {len(volumes_found)} different volumes.")
                
            # --- Aplica o nome escolhido para cada volume.
            organized_volumes = utils.apply_volume_custom_names(volumes_found, pattern)

            # --- Executa a movimentação e recebe os logs do utils
            results = utils.volumes_folder_creator(p_origin, p_dest, organized_volumes)

            for line in results:
                self.update_log(line)

            self.update_log("SUCCESS: Organization completed!")

        except Exception as e:
            self.update_log(f"CRITICAL ERROR: {str(e)}")
        
        finally:
            # Reativa o botão na interface principal
            self.btn_run.configure(state="normal", text="START")

    def __init__(self):
        super().__init__()

        self.origin_path = ""
        self.destination_path = ""

        self.title("ChapStacker")
        self.geometry("900x500")

        self.grid_columnconfigure(0, weight=1) # --- Coluna da Esquerda
        self.grid_columnconfigure(1, weight=1) # --- Coluna da Direita
        self.grid_rowconfigure(0, weight=1)    # --- Linha única


        # --- Frame da Esquerda
        self.frame_config = ctk.CTkFrame(self, corner_radius=0)
        self.frame_config.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.frame_config.grid_columnconfigure((0, 1), weight=1)

        self.frame_config_title = ctk.CTkLabel(
            self.frame_config,
            text='HQs Configuration',
            text_color='white',
            font=("Roboto", 14, "bold")
        )
        self.frame_config_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # --- Botão e Caminho de Input
        self.btn_origin = ctk.CTkButton(
            self.frame_config, 
            text="Select Origin Folder",
            font=("Roboto", 12, "bold"),
            fg_color="#1f538d",
            hover_color="#14375e",
            width=160,
            command=self.select_origin
        )
        self.btn_origin.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.origin_content = ctk.CTkLabel(
            self.frame_config,
            text="No Folder Selected.",
            font=("Roboto", 12, "italic"),
            text_color="gray"
        )
        self.origin_content.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # --- Botão e Caminho de Output
        self.btn_destination = ctk.CTkButton(
            self.frame_config,
            text="Select Output Folder",
            font=("Roboto", 12, "bold"),
            fg_color="#1f538d",
            hover_color="#14375e",
            width=160,
            command=self.select_destination
        )
        self.btn_destination.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.destination_content = ctk.CTkLabel(
            self.frame_config,
            text="No Folder Selected.",
            font=("Roboto", 12, "italic"),
            text_color="gray"
        )
        self.destination_content.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # --- Seletor de Base para o Nome
        self.label_pattern = ctk.CTkLabel(
            self.frame_config, 
            text="Volume Pattern (use {#n} for numbering):",
            font=("Roboto", 12, "bold")
        )
        self.label_pattern.grid(row=3, column=0, columnspan=2, padx=20, pady=(10, 0), sticky="w")

        self.entry_name_pattern = ctk.CTkEntry(
            self.frame_config, 
            placeholder_text="Ex: HQ Exemplo - Volume {#n}",
            width=600
        )
        self.entry_name_pattern.grid(row=4, column=0, columnspan=2, padx=20, pady=(0, 10), sticky="ew")

        # --- Botão de Execução
        self.btn_run = ctk.CTkButton(
            self.frame_config,
            text="START",
            font=("Roboto", 13, "bold"),
            fg_color="#1f538d",
            hover_color="#14375e",
            height=40,
            command=self.run_process
        )
        self.btn_run.grid(row=5, column=0, columnspan=2, padx=20, pady=20, sticky="ew")
        
        

        # --- Frame da Direita
        self.frame_log = ctk.CTkFrame(self, corner_radius=0)
        self.frame_log.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.frame_log.grid_columnconfigure(0, weight=1)
        self.frame_log.grid_rowconfigure(1, weight=1)

        self.frame_log_title = ctk.CTkLabel(
            self.frame_log,
            text='Operation Log',
            text_color='white',
            font=("Roboto", 14, "bold")
        )
        self.frame_log_title.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # --- Caixa de Log
        self.log_textbox = ctk.CTkTextbox(
            self.frame_log,
            font=("Consolas", 12),
            text_color="#A9A9A9",
            state="disabled"
        )
        self.log_textbox.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")

if __name__ == "__main__":
    app = ChapstackerApp()
    app.mainloop()