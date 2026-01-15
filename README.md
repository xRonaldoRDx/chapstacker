# 📚 Chapstacker

O **Chapstacker** é um utilitário desenvolvido em Python para automatizar a organização de capítulos de HQs em volumes. Ele resolve o problema de pastas desorganizadas, agrupando capítulos automaticamente com base na numeração identificada em seus nomes, facilitando o processo para leitores de HQs digitais.

## 🚀 Funcionalidades

- **Identificação via Regex:** Scaneia nomes de pastas e identifica o número do volume automaticamente.
- **Nomenclatura Flexível:** Permite ao usuário definir padrões de nomes para os volumes usando o placeholder `{#n}`.
- **Movimentação Robusta:** Utiliza `shutil` para garantir a integridade dos dados, permitindo mover arquivos entre diferentes unidades de disco.
- **Validação de Segurança:** Verifica se os diretórios existem, se estão vazios e solicita confirmação final antes de qualquer alteração física nos arquivos.
- **Interface Limpa:** Console interativo com comandos de limpeza de tela e pausas estratégicas para melhor experiência do usuário (UX).

## 🛠️ Tecnologias e Conceitos Aplicados

- **Linguagem:** Python 3
- **Bibliotecas Nativas:**
    - `pathlib`: Manipulação moderna de sistemas de arquivos.
    - `re`: Expressões Regulares para extração de padrões de texto.
    - `shutil`: Movimentação de alto nível de diretórios.
    - `os`: Integração com comandos do sistema operacional.
- **Arquitetura:** Programação modular (Separação entre lógica de negócio e interface).

## 📋 Como utilizar

1. Execute o arquivo `main.py`.
2. Informe o caminho da pasta onde estão os capítulos originais.
3. Defina a máscara de nome para os volumes (ex: `HQ Exemplo - Vol.{#n}`).
4. Informe o caminho de destino.
5. Revise o resumo da operação e confirme com `S` para iniciar a organização.

---
Desenvolvido por **Ronaldo Rossetti Dearo**