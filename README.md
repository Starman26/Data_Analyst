🤖📊 Automatización de Reportes de Análisis de Datos para Sistemas Robóticos
Este proyecto automatiza de forma completa el proceso de análisis, visualización y generación de reportes sobre el funcionamiento de un robot industrial. Integra procesamiento de datos, análisis estadístico, generación de gráficos y razonamiento automático con modelos de lenguaje multimodal (LLM), culminando en un reporte profesional en formato .docx.

🧠 ¿Qué hace este proyecto?
Procesamiento de Datos

Se cargan datos limpios del sistema de control del robot.

Se procesan columnas clave como temperatura, velocidad del extrusor, diámetro, etc.

Análisis Exploratorio Automatizado

Se generan automáticamente:

Boxplots para detección de outliers.

Heatmaps de correlación entre variables.

Gráficos de líneas para visualizar comportamiento a lo largo del tiempo.

Análisis de correlación cruzada entre señales clave.

Generación de Imágenes

Todos los gráficos se guardan en una carpeta local (Images) para su uso posterior.

Razonamiento con un LLM (BLIP)

Las imágenes generadas se interpretan usando un modelo LLM de Hugging Face.

El modelo proporciona una descripción automática del contenido visual (captioning).

Creación de Reporte Word

Se genera un archivo .docx profesional que incluye:

Título personalizado con estilo.

Imagen de portada.

Todas las gráficas generadas.

Descripciones automáticas generadas por el modelo.

Las imágenes se eliminan automáticamente de la carpeta después de insertarse.

⚙️ Tecnologías utilizadas
pandas, matplotlib, seaborn → Análisis de datos y visualización

transformers, BLIP (Hugging Face) → Razonamiento multimodal

python-docx → Generación de documentos Word

Pillow → Manipulación de imágenes

🚀 Cómo usar
Coloca tu archivo CSV en la carpeta correspondiente.

Ejecuta el script principal (analyze.py o Create_Doc.py).

El reporte se generará automáticamente en la carpeta reportes/.

