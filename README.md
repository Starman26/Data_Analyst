# Automated Data Analysis Report Generation for Robotic Systems

This project fully automates the process of **data analysis, visualization, and report generation** for monitoring the performance of a robotic system. It integrates data processing, statistical analysis, graph generation, and visual reasoning using a multimodal large language model (LLM), resulting in a professional `.docx` report.

---

## Features

- Automated processing of system data from `.csv` files
- Auto-generation of insightful visualizations:
  - Line plots (time-based signal tracking)
  - Boxplots (outlier detection)
  - Correlation heatmaps
  - Cross-correlation plots between key signals
- Visual reasoning powered by Hugging Face's `BLIP` model:
  - Automatically generates image captions from the charts
- Professional `.docx` report creation:
  - Custom cover image and title styling
  - Visualizations inserted with captions
  - All generated images are automatically deleted after insertion

---
Data_Analyst/
├── analyze.py                 
├── Create_Doc.py              
├── Images/                    
├── reportes/                 
├── FrED_Factory.png           
└── ControlSystemsData_Clean.csv  





## Technologies Used

- [`pandas`](https://pandas.pydata.org/) for data processing  
- [`matplotlib`](https://matplotlib.org/) & [`seaborn`](https://seaborn.pydata.org/) for data visualization  
- [`transformers`](https://huggingface.co/docs/transformers) + [`BLIP`](https://huggingface.co/Salesforce/blip-image-captioning-base) for image captioning  
- [`python-docx`](https://python-docx.readthedocs.io/) for Word report generation  
- [`Pillow`](https://pillow.readthedocs.io/) for image handling

---

## How to Use

1. Place your clean data file (`.csv`) into the project directory.
2. Run the main script:  
   ```bash
   python pipeline.py
