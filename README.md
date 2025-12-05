# Documentación del proceso y preguntas (evidencias)

## Carta de presentación

  * Herramienta usada para generar documentación HTML y comandos ejecutados:
  La herrimienta que utilicé para la documentación fue pdoc.

  * Ejemplos de código documentado (enlace a la fuente) y fragmento con las etiquetas/estructura usadas: https://github.com/Miguel-verdu/P1-MVP/blob/main/src/main.py El fragmento es todo lo de en medio entre """, por ejemplo el Returns:

  * Enlace público a GitHub Pages donde se puede ver la documentación HTML: 
  https://miguel-verdu.github.io/P1-MVP/index.html

  * Cómo clonar/usar el repositorio:
  El repositorio está configurado para uso público, si se quiere clonar o usar este será necesario instalar los archivos mediante la interfaz de github o mediante el uso de comandos en Git.

## Explicación del Workflow

Cada vez que se sube un código, el workflow automáticamente genera y publica documentación web.

## 📅 ¿Cuándo se activa?
Al hacer push a la rama main o manualmente desde la web de GitHub

## 🔧 ¿Qué hace?:

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
**a) Identificación de herramientas de generación de documentación.**
La herramienta utilizada para la generación de documentación fue pdoc version 13 o superior.

**b) Documentación de componentes.**
Un breve ejemplo en el archivo main.py sería lo siguiente: 
      Returns:
        str: Saludo formateado, por ejemplo "Hola, Mundo!"."""
        
**c) Publicación en GitHub Pages.**

```name: 🚀 Publicar en GitHub Pages
  uses: peaceiris/actions-gh-pages@v3
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    publish_dir: docs_html/
    force_orphan: true
```
## Pasos clave:

-Acción peaceiris/actions-gh-pages@v3: Sube contenido a la rama gh-pages

-force_orphan: true: Limpia la rama gh-pages en cada despliegue

-GITHUB_TOKEN: Token automático con permisos de escritura

-Configuración en Settings → Pages:

-Source: Deploy from a branch

-Branch: gh-pages (creada automáticamente)

-Folder: / (root)




**d) Colaboración. Explica cómo GitHub Pages facilita compartir documentación actualizada con el equipo y usuarios externos.**


## Ventajas de GitHub Pages frente a archivos HTML en el repo:
 * URL pública permanente
 * Actualización automática	
 * Acceso desde cualquier dispositivo	
 * Índice automático y navegación	

 
**e) Control de versiones. Muestra mensajes de commit que evidencien la configuración del workflow de publicación.**

### Mensajes de commit generados por el workflow:

```"Update README y documentación [skip ci]"```
Análisis:

✅ Claro: Indica qué se actualizó

✅ Descriptivo: Menciona ambos elementos modificados

❌ Mejorable: Podría ser más específico:

"📚 Actualiza docs con pdoc - v1.0.0"

"🔧 CI: Actualiza README con resultados de tests"

✅ [skip ci]: Previene bucles infinitos de ejecución
 
**f) Accesibilidad y seguridad. ¿Cómo garantizas que la documentación en GitHub Pages es accesible públicamente pero el código fuente solo es accesible para personal autorizado?**

```
┌─────────────────────────────────────┐
│     Repositorio PRIVADO/PÚBLICO     │
│  (código fuente con control acceso) │
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│     GitHub Pages PÚBLICO SIEMPRE    │
│  (documentación HTML accesible)     │
└─────────────────────────────────────┘
```
### Mecanismos:

* Repositorio puede ser privado: Solo equipo autorizado ve código

* GitHub Pages siempre público: Documentación accesible globalmente

* GITHUB_TOKEN con scope limitado: Solo puede modificar el repo actual

* Separación ramas: main (código) ≠ gh-pages (docs)


**g) Instalación/uso documentados. Indica dónde en el README.md explicas cómo acceder a la documentación publicada en GitHub Pages y dónde detallas las herramientas y comandos usados para generarla.**


**h) Integración continua y despliegue continuo (CI/CD). Justifica por qué el workflow utilizado implementa CI/CD.**


**Justificación de CI/CD:**

### **CI (Integración Continua):**
- ✅ **Tests automáticos**: `pytest` se ejecuta en cada push
- ✅ **Build automático**: Generación de docs con cada cambio
- ✅ **Validación**: README se actualiza con resultados

### **CD (Despliegue Continuo):**
- ✅ **Despliegue automático**: Docs se publican sin intervención
- ✅ **Consistencia**: Docs siempre sincronizadas con código
- ✅ **Disponibilidad**: Última versión siempre online

**Evento disparador:**
```yaml
on:
  push:
    branches: [main]  # ← Se dispara con CADA push a main
  workflow_dispatch:   # ← También manualmente


### README.md inicial   

Una posible versión base del fichero README.md sería el siguiente (aunque finalmente será mas completo): 


```

# Mi Proyecto con GitHub Actions

Este proyecto sirve para aprender a usar GitHub Actions 🚀

## Estado de los tests
✅ Tests correctos


## Historial de tests
- 2025-12-05 20:05:07: ✅ Tests correctos
- 2025-12-05 20:03:21: ✅ Tests correctos
- 2025-12-05 20:02:42: ✅ Tests correctos
- 2025-12-05 20:01:32: ✅ Tests correctos
- 2025-12-05 20:00:36: ✅ Tests correctos
- 2025-12-05 19:59:36: ✅ Tests correctos
- 2025-12-05 19:50:58: ✅ Tests correctos
- 2025-12-05 19:50:09: ✅ Tests correctos
- 2025-12-05 19:43:01: ✅ Tests correctos
- 2025-12-05 19:41:42: ✅ Tests correctos
- 2025-12-05 19:41:05: ✅ Tests correctos
- 2025-12-05 19:39:19: ✅ Tests correctos
- 2025-12-05 19:33:34: ✅ Tests correctos
- 2025-12-05 19:30:07: ✅ Tests correctos
- 2025-12-05 19:26:16: ✅ Tests correctos
- 2025-12-05 19:16:40: ✅ Tests correctos
- 2025-12-05 19:14:47: ✅ Tests correctos
- 2025-12-05 19:14:13: ✅ Tests correctos
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
