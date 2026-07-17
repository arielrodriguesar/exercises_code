import pandas as pd
from tabulate import tabulate
import tkinter as tk
from tkinter import ttk

'''--Tabulate: Importei o tabulate, pois achei péssima a vizualização dos dados na impressão final, assim a biblioteca importa formatações para o terminal--
   --Tkinter: Ainda achando a vizualização péssima, busquei uma forma de ter certa interface, nesta intenção pesquisei e encontrei essa biblioteca--'''

'''--Leitura do excel com os dados básicos-- 
   --Pesquisei uma função do pandas para que não precisasse fazer a conta por código, visando o encurtamento do código, usei, assim, o ,mean
    colocando alguns parâmetros; axis=1 para leitura occorer na horizontal, skipna e numeric only para ignorar os nulos e usar só os númericos--'''

df = pd.read_excel('tarefa_python.xlsx')
df['Media'] = df.mean(axis=1, skipna=True, numeric_only=True)

'''--Aqui criei um valor Status para marcar o aluno como aprovado ou reprovado; pesquisei uma forma mais sintérica e achei a forma com o .apply.
   O .apply é uma função que busca cada valor individual aplicando a uma função específica dentro do parênteses, isso facilita,
   pois não preciso fazer uma retrutura de repetição(for). E o mais interessante o lambda x opera como se fosse uma linha de código descartável,
   que puxa o valor x da coluna média, ele manda operar um código rápido, enquanto entrar um valor x e o apply vai devolvendo ao df Status 
   cada valor de acordo com o if. O comprendi como uma forma curta de um for dentro de outro for--'''

df['Status'] = df['Media'].apply(lambda x: 'Aprovado' if x >= 6 else 'Reprovado')
df_final = df[['Nome', 'Media', 'Status']]

'''Essa é a parte final usando o tabulate, para que o dado saia com formatação'''

print(tabulate(df_final, headers='keys', tablefmt='fancy_grid', showindex=False, numalign="center"))

'''

#--Essa parte do código, foi pela intenção de deixar a interface de vizualização maelhor--

app = tk.Tk()
app.title("Media Alunos")
app.geometry("1000x1000")

tv = ttk.Treeview(app, columns=('Nome','Media', 'Status'), show= 'headings')
tv.column('Nome', minwidth=0, width=50)
tv.column('Media', minwidth=0, width=50)
tv.column('Status', minwidth=0, width=50)
tv.heading('Nome', text='Nome')
tv.heading('Media', text='Média')
tv.heading('Status', text='Status')

#--Nesta parte, descobri que o Tkinter não tem interação com o pandas, assim teria de transformar os dados do df numa lista, 
#  que deve separar cada elemento seguindo a ordem da coluna, o '' faz com que o primeiro elemento seja o pai que herda o restante, 
#  asim, a cada final de linha do df, fecha-se já endereçados ao nome. O end força a próxima linha ser sempre jogada para baixo, 
#  não invertendo a tabela fora da ordem original. O values força os elementos serem igual a lista, mantendo a estrutura de 3 em 3 e na ordem certa,
#  pois o tk lerá da esquerda para direita. Assim, eu entendi--

for index, linha in df_final.iterrows():
    tv.insert('', 'end', values=list(linha))
    
# fill faz com que tudo do x e y seja preenchido. Expand permite que ao expandir a tela todo os elmentos tenham permissão de se ajustar ao espaço ganhado.
tv.pack(fill='both', expand=True)

app.mainloop()
'''

