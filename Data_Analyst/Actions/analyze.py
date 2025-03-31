import matplotlib.pyplot as plt   
import pandas as pd              
import numpy as np               
import seaborn as sns            
import os                        

def analysis(path, folder):
    data = pd.read_csv(path)

    os.makedirs(folder, exist_ok=True)

    # Gráfico de líneas
    data.plot(
        x='Timestamp',
        y=['Temperature', 'Temperature_error', 'Extruder_RPM'],
        kind='line',
        figsize=(10, 5),
        title='Variables seleccionadas'
    )
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.xlabel('Timestamp (s)')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.legend(title='Variables')
    plt.savefig(os.path.join(folder, 'variables_seleccionadas.png'), dpi=300, bbox_inches='tight') 
    plt.close()

    # Heatmap de correlación
    subset = data[['Temperature', 'Spooler_RPM', 'Diameter']]
    corr_matrix = subset.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Matriz de correlación')
    plt.savefig(os.path.join(folder, 'heatmap_correlacion.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # Boxplot
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data['Diameter'])
    plt.title('Boxplot')
    plt.xlabel('Temperature (C)')
    plt.savefig(os.path.join(folder, 'boxplot_temperature.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # Cross-correlation
    def cross_correlation(series1, series2, max_lag):
        lags = range(-max_lag, max_lag + 1)
        corr_values = []
        for lag in lags:
            if lag < 0:
                shifted_corr = series1.shift(-lag).corr(series2)
            else:
                shifted_corr = series1.corr(series2.shift(lag))
            corr_values.append(shifted_corr)
        return list(lags), corr_values

    serie_temp = data['Temperature']
    serie_diam = data['Diameter']

    lags, corr_values = cross_correlation(serie_temp, serie_diam, max_lag=50)
    plt.figure(figsize=(10,5))
    plt.plot(lags, corr_values, marker='o')
    plt.xlabel('Lag (segundos)')
    plt.ylabel('Coeficiente de correlación')
    plt.title('Cross-correlation entre Spooler Rpm y Diámetro')
    plt.grid(True)
    plt.savefig(os.path.join(folder, 'cross_correlation.png'), dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Example usage
    path = r"C:\Users\lench\Desktop\Data_Analyst\CSV\ControlSystemsData_Clean.csv"
    folder = r"C:\Users\lench\Desktop\Data_Analyst\Images"
    analysis(path,folder)