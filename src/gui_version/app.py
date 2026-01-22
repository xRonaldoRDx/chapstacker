import customtkinter as ctk
import utils

class ChapstackerApp(ctk.CTk):
    
    def select_origin(self):
        path = ctk.filedialog.askdirectory()
        
        if path:
            self.origin_path = path
            print(f"Path selected: {self.origin_path}")

            self.origin_content.configure(text=path)
            
            # Muda a cor do botão para indicar sucesso.
            self.btn_origin.configure(fg_color="green")

    def select_destination(self):
        path = ctk.filedialog.askdirectory()

        if path:
            self.destination_path = path
            print(f"Path selected: {self.destination_path}")

            self.destination_content.configure(text=path)
            
            # Muda a cor do botão para indicar sucesso.
            self.btn_destination.configure(fg_color="green")

    def run_process(self):
        print("Starting organization...")


    def __init__(self):
        super().__init__()

        self.origin_path = ""
        self.destination_path = ""

        self.title("Chapstacker")
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