import requests
import pandas as pd
from bs4 import BeautifulSoup

# Definir la URL
url = "https://www.nba.com/stats/teams/traditional?dir=A&sort=GP"

# Realizar solicitud
response = requests.ge(url)

# Verificar exito en la solicitud
if response.status_code == 200:
    # Usar soup para analizar el contenido
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar todas las tablas en la pagina
    tables = soup.find_all('table')
    dfs = []
    
    for i, table in enumerate(tables):
        df = pd.read_html(str(table))[0]
        dfs.append((df))
        
        df.to_csv(f'table_{i}.csv', index=False)
    print((f'Se han extraido y guardado {len(dfs)} tablas'))
else:
    print('No se han podido extrar tablas.')