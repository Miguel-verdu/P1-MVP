"""
Módulo para ejecución de tests y actualización automática del README.

Este módulo proporciona funciones para ejecutar tests de pytest y registrar
los resultados en el archivo README.md con un historial de ejecuciones.
"""

import subprocess
from datetime import datetime


def run_tests() -> str:
    """
    Ejecuta los tests del proyecto usando pytest.
    
    Esta función ejecuta todos los tests definidos en el proyecto mediante
    el comando pytest y retorna un mensaje indicando el resultado.
    
    Returns:
        str: Mensaje indicando el resultado de los tests:
            - "✅ Tests correctos" si todos los tests pasan
            - "❌ Tests fallidos" si algún test falla
            
    Raises:
        FileNotFoundError: Si pytest no está instalado o no se encuentra
        
    Example:
        >>> result = run_tests()
        >>> result in ["✅ Tests correctos", "❌ Tests fallidos"]
        True
    """
    try:
        subprocess.check_call(["python", "-m", "pytest", "-q"])
        return "✅ Tests correctos"
    except subprocess.CalledProcessError:
        return "❌ Tests fallidos"


def update_readme(status: str) -> None:
    """
    Actualiza el archivo README.md con el resultado de los tests.
    
    Añade una nueva entrada al historial de tests en el README, incluyendo
    la fecha y hora actual y el resultado de la ejecución. Si no existe
    una sección de historial, la crea automáticamente.
    
    Args:
        status (str): Resultado de los tests a registrar. Debe ser uno de:
            - "✅ Tests correctos"
            - "❌ Tests fallidos"
            
    Returns:
        None: La función no retorna valores, pero modifica el archivo README.md
        
    Raises:
        FileNotFoundError: Si el archivo README.md no existe
        PermissionError: Si no hay permisos para escribir en README.md
        
    Note:
        El formato de cada entrada en el historial es:
        - YYYY-MM-DD HH:MM:SS: [status]
        
    Example:
        >>> update_readme("✅ Tests correctos")
        # Añade al README: "- 2024-01-15 14:30:00: ✅ Tests correctos"
    """
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
    """
    Punto de entrada principal del script.
    
    Cuando se ejecuta directamente, esta función:
    1. Ejecuta los tests usando run_tests()
    2. Registra el resultado en el README usando update_readme()
    3. Imprime el resultado en la consola
    """
    status = run_tests()
    update_readme(status)
    print(f"Resultado añadido al historial: {status}")
