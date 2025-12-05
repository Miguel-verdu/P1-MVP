# Documentación del proceso y preguntas (evidencias)

## Carta de presentación



  * Herramienta usada para generar documentación HTML y comandos ejecutados:
  La herrimienta que utilicé para la documentación fue pdoc.

  * Ejemplos de código documentado (enlace a la fuente) y fragmento con las etiquetas/estructura usadas:

  * Enlace público a GitHub Pages donde se puede ver la documentación HTML: 
  https://miguel-verdu.github.io/P1-MVP/index.html

  * Mensajes de commit:

  * Cómo clonar/usar el repositorio:
  El repositorio está configurado para uso público, si se quiere clonar o usar este será necesario instalar los archivos mediante la interfaz de github o mediante el uso de comandos en Git.

## Explicación del Workflow

Cada vez que se sube un código, el workflow automáticamente genera y publica documentación web.

📅 ¿Cuándo se activa?
Al hacer push a la rama main o manualmente desde la web de GitHub

🔧 ¿Qué hace?:

1️⃣ Prepara el entorno
Descarga el código

Instala Python y demás herramientas necesarias

2️⃣ Ejecuta los tests
Corre pytest para verificar que todo funciona

Actualiza el README.md con los resultados

3️⃣ Genera documentación
Convierte los comentarios de tu código ("""docstrings""") a páginas web

4️⃣ Publicación online
Sube las páginas generadas a GitHub Pages

Quedan disponibles en el enlace dado anteriormente

🌐 Resultado final:
Documentación siempre actualizada sin que tengas que hacer nada manualmente.

## Cuestionario a responder




### README.md inicial   

Una posible versión base del fichero README.md sería el siguiente (aunque finalmente será mas completo): 


```markdown
# Mi Proyecto con GitHub Actions

Este proyecto sirve para aprender a usar GitHub Actions 🚀

## Estado de los tests
✅ Tests correctos


## Historial de tests
- 2025-12-05 19:02:37: ✅ Tests correctos
- 2025-12-05 19:01:42: ✅ Tests correctos
- 2025-12-05 18:59:49: ✅ Tests correctos
- 2025-12-05 18:40:26: ✅ Tests correctos
- 2025-12-05 18:13:11: ✅ Tests correctos
- 2025-12-05 18:04:16: ✅ Tests correctos
- 2025-12-05 18:03:57: ✅ Tests correctos
- 2025-12-05 16:40:57: ✅ Tests correctos
- 2025-12-05 16:38:03: ✅ Tests correctos
- 2025-12-05 05:34:43: ✅ Tests correctos
- 2025-12-05 05:34:19: ❌ Tests fallidos
- 2025-12-05 05:33:37: ❌ Tests fallidos
- 2025-12-05 05:33:25: ❌ Tests fallidos
- 2025-12-05 04:54:10: ✅ Tests correctos
