# MarcacaoAutomatica

Usei o seguinte código para conseguir extrair apenas os dados essenciais do arquivo bib:

--------------------------------------------------------------------------------------------
import bibtexparser
import pandas as pd 
from tabulate import tabulate 

with open('020_completo.bib', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)


bib_entries = bib_database.entries


df = pd.DataFrame(bib_entries)

df['id'] = df.index

df_selected = df[['id', 'author', 'year']]

print(tabulate(df_selected, headers='keys', tablefmt='grid'))

--------------------------------------------------------------------------------------------

Agora precismos criar um jeito de ler o arquivo md e substituir citações fechadas automaticamente

Para fins didáticos vou mostrar como serão as citações que iremos substituir:

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis blandit, ligula ut feugiat tincidunt, eros nibh imperdiet enim, vulputate condimentum est dolor id massa. Morbi feugiat tortor nec dui pretium porta. Phasellus vel dapibus nunc. Pellentesque sed facilisis neque. Fusce nisl metus, condimentum hendrerit tellus ac, **(Saraiva, 2001)**. Quisque quis laoreet diam. Etiam Mateus Saraiva (2001). Viverra dignissim vitae sed nisl. Nulla ac odio lacinia, laoreet odio sed, euismod est. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed a nisl volutpat ante scelerisque tempus. Maecenas feugiat justo ut lectus gravida facilisis. Pellentesque habitant **(Silva, 2024)** senectus et netus et malesuada fames ac turpis egestas. Donec porttitor sed ex sit amet volutpat. Phasellus vehicula purus eget metus facilisis, sed ullamcorper erat gravida. Praesent lacinia purus massa, et sollicitudin est eleifend eu.

Apenas as duas citações em **negrito** serão substituídas, por enquanto
