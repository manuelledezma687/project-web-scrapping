import pandas as pd
import requests
from bs4 import BeautifulSoup

# Obtener títulos de artículos
response = requests.get('https://blazedemo.com/reserve.php')
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find_all('h3')
for headline in headlines:
    print(headline.text.strip())

# Crear un DataFrame a partir de listas de titulares
# data = {'Title': [headline.text for headline in headlines]}
# df = pd.DataFrame(data)
# print(df)

# # Guardar el DataFrame en un archivo CSV
# df.to_csv('headlines.csv', index=False)


# # Extraer todas las filas de una tabla
# table = soup.find('table')
# rows = table.find_all('tr')
# for row in rows:
#     columns = row.find_all('td')
#     print([column.text for column in columns])

# # Eliminar caracteres extraños y limpiar los datos
# df['Title'] = df['Title'].str.strip()

