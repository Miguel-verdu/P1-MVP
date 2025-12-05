import subprocess
from datetime import datetime

def run_tests():
    try:
        subprocess.check_call(["python", "-m", "pytest", "-q"])
        return "✅ Tests correctos"
    except subprocess.CalledProcessError:
        return "❌ Tests fallidos"

def update_readme(status: str):
    # Obtener fecha y hora actual
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history_entry = f"- {timestamp}: {status}\n"
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Buscar la sección de historial
    history_header = "## Historial de tests"
    
    if history_header in content:
        # Insertar nueva entrada después del encabezado
        parts = content.split(history_header, 1)
        # Dividir en líneas después del encabezado
        lines = parts[1].split('\n', 1)
        # Reconstruir con la nueva entrada
        new_content = parts[0] + history_header + "\n" + history_entry + (lines[1] if len(lines) > 1 else "")
    else:
        # Si no existe la sección, buscar "## Estado de los tests"
        if "## Estado de los tests" in content:
            # Insertar después de "## Estado de los tests"
            parts = content.split("## Estado de los tests", 1)
            # Buscar el final de esa sección (próximo encabezado o fin de archivo)
            next_section = parts[1].find('\n##')
            if next_section != -1:
                insert_pos = parts[0] + "## Estado de los tests" + parts[1][:next_section]
                remaining = parts[1][next_section:]
                new_content = insert_pos + "\n\n" + history_header + "\n" + history_entry + remaining
            else:
                new_content = content + "\n\n" + history_header + "\n" + history_entry
        else:
            # Si no existe ninguna sección, añadir al final
            new_content = content + "\n\n" + history_header + "\n" + history_entry
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    status = run_tests()
    update_readme(status)
    print(f"Resultado añadido al historial: {status}")
