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

        self.frame_config_title = ctk.CTkLabel(
            self.frame_config,
            text='Volume Configuration',
            text_color='white'
        )
        self.frame_config_title.grid(row=0, column=0, padx=20, pady=10)

        self.btn_origin = ctk.CTkButton(
            self.frame_config, 
            text="Select Origin Folder",
            command=self.select_origin
        )
        self.btn_origin.grid(row=1, column=0, padx=20, pady=10)

        self.origin_content = ctk.CTkLabel(
            self.frame_config,
            text="Nenhuma pasta selecionada"
        )
        self.origin_content.grid(row=2, column=0, padx=20, pady=10)

        self.btn_destination = ctk.CTkButton(
            self.frame_config,
            text="Select Output Folder",
            command=self.select_destination
        )
        self.btn_destination.grid(row=3, column=0, padx=20, pady=10)

        self.destination_content = ctk.CTkLabel(
            self.frame_config,
            text="Nenhuma pasta selecionada"
        )
        self.destination_content.grid(row=4, column=0, padx=20, pady=10)

        # --- Frame da Direita
        self.frame_log = ctk.CTkFrame(self, corner_radius=0)
        self.frame_log.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.frame_log_title = ctk.CTkLabel(
            self.frame_log,
            text='Operation Log',
            text_color='white'
        )

        self.frame_log_title.grid( row=0, column=0, padx=20, pady=10)



if __name__ == "__main__":
    app = ChapstackerApp()
    app.mainloop()