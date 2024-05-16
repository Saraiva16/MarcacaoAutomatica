import bibtexparser
import pandas as pd # type: ignore
from tabulate import tabulate 

# Carrega o arquivo BibTeX
with open('020.bib', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Extraia as entradas do BibTeX
bib_entries = bib_database.entries

# Converta as entradas para um DataFrame do Pandas
df = pd.DataFrame(bib_entries)

df['id'] = df.index

df_selected = df[['id', 'author', 'year']]

# Exibir a tabela
print(tabulate(df_selected, headers='keys', tablefmt='grid'))
