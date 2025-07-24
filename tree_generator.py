import os
import sys

IGNORE_DIRS = {'__pycache__', '.git', '.idea', '.vscode', 'env', '.venv'}
IGNORE_EXTENSIONS = {'.pyc', '.log', '.sqlite3', '.DS_Store'}
OUTPUT_FILE = 'tree.txt'

def should_ignore(name):
    if name in IGNORE_DIRS:
        return True
    _, ext = os.path.splitext(name)
    return ext in IGNORE_EXTENSIONS

def print_tree(start_path, prefix=""):
    entries = [e for e in os.listdir(start_path) if not should_ignore(e)]
    entries.sort()
    lines = []
    pointers = ['├── '] * (len(entries) - 1) + ['└── '] if entries else []

    for pointer, entry in zip(pointers, entries):
        path = os.path.join(start_path, entry)
        lines.append(prefix + pointer + entry)
        if os.path.isdir(path):
            extension = '│   ' if pointer == '├── ' else '    '
            lines.extend(print_tree(path, prefix + extension))
    return lines

if __name__ == "__main__":
    # Captura argumento opcional
    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
        target_path = os.path.abspath(target_folder)

        if os.path.exists(target_path) and os.path.isdir(target_path):
            print(f"📂 Exibindo estrutura de: '{target_folder}'\n")
        else:
            print(f"⚠️ Pasta '{target_folder}' não encontrada. Mostrando estrutura do projeto completo.\n")
            target_path = os.path.abspath(os.path.dirname(__file__))
    else:
        # Sem argumento: usa a pasta atual
        target_path = os.path.abspath(os.path.dirname(__file__))

    root_name = os.path.basename(target_path)
    tree_lines = [f"{root_name}/"] + print_tree(target_path)

    # Mostrar no terminal
    print("\n".join(tree_lines))

    # Salvar no arquivo tree.txt dentro da pasta analisada
    output_path = os.path.join(target_path, OUTPUT_FILE)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(tree_lines))

    print(f"\n📄 Estrutura salva em '{output_path}'")
