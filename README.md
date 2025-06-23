# Studio dei casi Covid-19 e Inquinamento in Umbria

Questo progetto analizza i dati epidemiologici relativi alla diffusione del Covid-19 nei comuni dell'Umbria e li confronta con fattori ambientali, geografici e demografici (inquinamento da PM10, densità abitativa, indice di deprivazione sociale).

##  Obiettivi

- Normalizzazione e pulizia del dataset
- Analisi visiva interattiva (Plotly, Folium)
- Clustering (K-Means) e PCA per riduzione dimensionale
- Regressione supervisionata (Linear Regression, Decision Tree)
- Modellazione interpretabile con pruning e cross-validation
- Costruzione di mappe interattive per insight territoriali

##  Tecnologie

- **Python 3.13.1**
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
- `plotly`, `folium`, `ipywidgets`
- `statsmodels`, `geopandas`
- Notebook Jupyter `.ipynb`

##  File del progetto
- dataset_exam.csv
- limits_R_10_municipalities.geojson
- Dockerfile
- covid_umbria_analysis.ipynb
- README.md
- requirements.txt


I dati usati sono stati raccolti da fonti pubbliche e aperte. Questo progetto ha scopo esclusivamente didattico ed esplorativo.

## Esecuzione con Docker

Al fine di eseguire la pipeline in ambiente isolato e riproducibile è disponibile un'immagine Docker.

### Build

Basta clonare **questa** repository e poi spostarsi nella cartella: 
git clone https://github.com/MarcoTamburi/covid.git
cd covid

Costruire l'immagine: 
docker build -t covid-analysis .

### Avvio del container

Run del container:
docker run -p 8888:8888 covid-analysis

L'interfaccia Jupyter Notebook sarà accessibile all'indirizzo indicato nel terminale, solitamente simile a:

http://127.0.0.1:8888/?token.....