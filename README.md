# 📚 Chapstacker

O **Chapstacker** é uma aplicação desenvolvida em Python para automatizar a organização de capítulos de HQs em volumes. Ele resolve o problema de pastas desorganizadas, agrupando capítulos automaticamente com base na numeração de volume identificada em seus nomes, facilitando o processo para leitores de HQs digitais.

## 🚀 Funcionalidades

- **Identificação via Regex:** Scaneia nomes de pastas e identifica o número do volume automaticamente.
- **Nomenclatura Flexível:** Permite ao usuário definir padrões de nomes para os volumes usando o placeholder `{#n}`.
- **Movimentação Robusta:** Utiliza `shutil` para garantir a integridade dos dados, permitindo mover arquivos entre diferentes unidades de disco.
- **Validação de Segurança:** Verifica se os diretórios existem, se estão vazios e solicita confirmação final antes de qualquer alteração física nos arquivos.
- **Interface Limpa:** Console interativo com comandos de limpeza de tela e pausas estratégicas para melhor experiência do usuário (UX), além de uma versão com GUI intuitivo.
- **Processamento Assíncrono (Multithreading):** Interface responsiva que permite acompanhar o progresso em tempo real sem travamentos durante a movimentação de arquivos.
- **Log de Operações:** Registro histórico com timestamps de cada ação realizada pelo sistema.

## 🛠️ Tecnologias e Conceitos Aplicados

- **Linguagem:** Python 3
- **Bibliotecas Nativas:**
    - `pathlib`: Manipulação moderna de sistemas de arquivos.
    - `re`: Expressões Regulares para extração de padrões de texto.
    - `shutil`: Movimentação de alto nível de diretórios.
    - `os`: Integração com comandos do sistema operacional.
    - `threading`:Gerenciamento de processos em segundo plano para garantir a estabilidade da GUI.
    - `datetime`: Formatação de registros cronológicos para auditoria de processos.
- **Bibliotecas Não Nativas:**
    Necessária instalação prévia, podendo utilizar o comando `pip install customtkinter`.
    - `customtkinter`: Interface moderna, responsiva e com suporte a temas (Dark/Light Mode).
- **Arquitetura:** Programação modular (Separação entre lógica de negócio e interface) utilizando arquitetura de camadas.


## 📁 Estrutura do Projeto
```text
chapstacker/
└── src/
    ├── gui_version/       # Versão moderna com interface gráfica (app.py)
    |    ├──app.py
    |    └──utils.py
    └── terminal_version/  # Versão clássica via console (main.py)
        ├──main.py
        └──utils.py
```

## 📋 Como utilizar

O projeto mantém as duas versões para compatibilidade e histórico. Ambas podem ser acessadas dentro da pasta `src`.

1. Escolha a versão navegando até `src/terminal_version` ou `src/gui_version`.
2. Execute o arquivo `main.py` (terminal) ou `app.py` (GUI).
3. Informe o caminho da pasta onde estão os capítulos originais.
4. Defina a máscara de nome para os volumes (ex: `HQ Exemplo - Vol.{#n}`).
5. Informe o caminho de destino.
6. Revise o resumo da operação e confirme para iniciar a organização.

---
Desenvolvido por **Ronaldo Rossetti Dearo**