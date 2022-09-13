import pandas as pd

month_list = ['janeiro', 'fevereiro', 'março']

for month in month_list:
    table = (pd.read_excel(f'assets/{month}.xlsx'))
    if (table['Vendas'] > 55000).any():
        seller = table.loc[table['Vendas'] > 55000, 'Vendedor'].values[0]
        sales = table.loc[table['Vendas'] > 55000, 'Vendas'].values[0]

        print(f'{month}: {seller} with {sales}')
