from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Cargar modelo
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Cargar imagen local
img_path = r"C:\Users\lench\Desktop\Data_Analyst\Images\heatmap_correlacion.png"
raw_image = Image.open(img_path).convert("RGB")

# Preprocesar e inferir
inputs = processor(raw_image, return_tensors="pt")
out = model.generate(**inputs)
caption = processor.decode(out[0], skip_special_tokens=True)

print(" Descripción:", caption)
