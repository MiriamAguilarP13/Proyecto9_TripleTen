# %% [markdown]
# # Contar una historia utilizando datos
# 
# **Descripción del proyecto**  
# Has decidido abrir un pequeño café regentado por robots en Los Ángeles. El proyecto es prometedor pero caro, así que tú y tus compañeros decidís intentar atraer inversionistas. Están interesados en las condiciones actuales del mercado.

# %% [markdown]
# # Contenido
# 
# * [Objetivos](#objetivos)
# * [Diccionario de Datos](#diccionario)
# * [Inicialización](#inicio)
# * [Cargar datos](#carga_datos)
# * [Análisis de datos](#analisis)
# * [Conclusión General](#end)
# * [Recomendaciones Generales](#recom)
# * [Enlace de Presentación](#link)

# %% [markdown]
# # Objetivos <a id='objetivos'></a>  
# 
# * Obtener una comprensión general de los datos.  
# * Identificar tendencias y patrones importantes.  
# * Preparar los datos para el análisis.   
# * Contar una historia con los datos.   

# %% [markdown]
# # Diccionario de Datos <a id='diccionario'></a>  
# 
# Tabla `rest_data`:  
# `object_name` — nombre del establecimiento  
# `chain` — establecimiento que pertenece a una cadena (TRUE/FALSE)  
# `object_type` — tipo de establecimiento  
# `address` — dirección  
# `number` — número de asientos  

# %% [markdown]
# # Inicialización <a id='inicio'></a>

# %%
# Cargar todas las librerías
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px

# %% [markdown]
# # Cargar datos <a id='carga_datos'></a>

# %%
# Carga del archivo de datos 
rest_data_us = pd.read_csv('files/datasets/rest_data_us.csv')

# %%
# se muestra la información del DataFrame con info()
rest_data_us.info()

# %%
# se imprimen las 5 primeras filas del DataFrame
rest_data_us.head()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Observaciones:**  
# Los tipo de datos para cada columna es correcto, por lo tanto, se dejarán así. Se buscarán valores ausentes y duplicados para procesarlos.     
#     
# </span>
#     
# </div>

# %%
# se buscan valores ausentes con isna() y sum()
rest_data_us.isna().sum()

# %%
# se eliminan los valores nulos
rest_data_us.dropna(inplace= True)

# %%
# se buscan valores duplicados con duplicated() y sum()
rest_data_us.duplicated().sum()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Observaciones:**  
# Solo una columna (`chain`) tenía valores nulos, los cuales se eliminaron. No se encontraron valores duplicados.       
#     
# </span>
#     
# </div>

# %% [markdown]
# # Análisis de datos <a id='analisis'></a>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Se calcula la cantidad para cada tipo de establecimiento, columna `object_type`, con `groupby()` y se contabilizan con `count()`. El resultado se guarda como un DataFrame.  
# 
# </span>
#     
# </div>

# %%
# se agrupan los datos de la columna 'object_type'
object_type_qty = rest_data_us.groupby('object_type')[['object_type']].count()
# se cambia el nombre de la columna
object_type_qty = object_type_qty.rename(columns= {'object_type': 'count_object_type'})
# se reinicia el índice
object_type_qty.reset_index(inplace= True)
object_type_qty

# %%
# se grafica un gráfico de pastel con la ayuda de ploty para representar las proporciones
fig1 = px.pie(object_type_qty, 
              values='count_object_type', 
              names='object_type', 
              title='Proporciones de los distintos tipos de establecimientos',
              color_discrete_sequence= px.colors.sequential.Aggrnyl
             )

# se muestra el gráfico
fig1.show()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Observaciones:**  
# El tipo de estableciomiento que tiene una mayor proporción es Restaurant, seguido de Fast Food y café.  
# 
# </span>
#     
# </div>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# ****
# Se muestran la proporción de establecimientos que pertenecen a una cadena en un gráfico de pastel.  
# 
# </span>
#     
# </div>

# %%
# se agrupan los datos de la columna 'chain' y se contabilizan los establecimientos para las agrupaciones
chain_qty = rest_data_us.groupby('chain')[['object_type']].count()
# se cambia el nombre de la columna
chain_qty = chain_qty.rename(columns= {'object_type': 'count_chains'})

# se reinicia el índice
chain_qty.reset_index(inplace= True)

# se cambian los nombres de False por No y True Si, sólo para cuetiones del gráfico
chain_qty.loc[0, 'chain'] = 'No'
chain_qty.loc[1, 'chain'] = 'Si'

chain_qty

# %%
# se grafica un gráfico de pastel con la ayuda de ploty para representar las proporciones para las cadenas
fig2 = px.pie(chain_qty, 
              values='count_chains', 
              names='chain',
              title='Proporciones de establecimientos que pertenecen a una cadena y de los que no',
              color_discrete_sequence= px.colors.sequential.Aggrnyl
             )

# se muestra el gráfico
fig2.show()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# Se filtra el DataFrame `rest_data_us` si el establecimiento que pertenece a una cadena (TRUE) o no pertenece (FALSE).
# </span>
#     
# </div>

# %%
# se filtra el DataFrame para los establecimientos que pertenecen a una cadena y se guarda el resultado en chain_true
chain_true = rest_data_us[rest_data_us['chain'] == True]
chain_true.head()

# %%
# se agrupan los datos de la columna 'object_type' del DataFrame 'chain_true'
chain_true_type = chain_true.groupby('object_type')[['object_type']].count()
# se cambia el nombre de la columna
chain_true_type = chain_true_type.rename(columns= {'object_type': 'count_object_type'})
# se reinicia el índice
chain_true_type.reset_index(inplace= True)
chain_true_type

# %%
# se grafica un gráfico de pastel con la ayuda de ploty para representar las proporciones de establecimientos que
# pertencen a una cadena
fig3 = px.pie(chain_true_type, 
              values='count_object_type', 
              names='object_type', 
              title='Proporciones de los tipos de establecimientos que pertenecen a una cadena',
              color_discrete_sequence= px.colors.sequential.Aggrnyl
             )

# se muestra el gráfico
fig3.show()

# %%
# se filtra el DataFrame para los establecimientos que no pertenecen a una cadena y se guarda el resultado en chain_false
chain_false = rest_data_us[rest_data_us['chain'] == False]
chain_false.head()

# %%
# se agrupan los datos de la columna 'object_type' del DataFrame 'chain_false'
chain_false_type = chain_false.groupby('object_type')[['object_type']].count()
# se cambia el nombre de la columna
chain_false_type = chain_false_type.rename(columns= {'object_type': 'count_object_type'})
# se reinicia el índice
chain_false_type.reset_index(inplace= True)
chain_false_type

# %%
# se grafica un gráfico de pastel con la ayuda de ploty para representar las proporciones de establecimientos que
# no pertencen a una cadena
fig3 = px.pie(chain_false_type, 
              values='count_object_type', 
              names='object_type', 
              title='Proporciones de los tipos de establecimientos que no pertenecen a una cadena',
              color_discrete_sequence= px.colors.sequential.Aggrnyl
             )

# se muestra el gráfico
fig3.show()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Conclusiones:**  
# El 61.9 % de establecimientos no pertenecen a una cadena, mientras que los lugares que forman parte de una cadena son el 38.1 %.  
# 
# Para los establecimientos que forman parte de una cadena el 62.4 % son restaurantes, el 16.5 % son del sector de la comida rápida y el 7.7 % son pastelerías. En cambio, los establecimientos que no pertencen a una cadena, los 3 principales son restaurantes ocupando el 83.2 %, seguido con un 7.7 % de establecimientos de comida rápida y un 3.6 % de bares.  
# 
# A diferencia de los lugares que pertencen a una cadena los restaurantes tienen un mayor porcentaje, la comida rápida tiene un menor porcentaje y los bares entran en el top 3 de los establecimientos que no forman parte de una cadena.  
#     
# Es evidente que, en comparación con los establecimientos asociados a cadenas, la proporción de restaurantes es aún más grande en los establecimientos independientes, mientras que la representación de comida rápida disminuye. Además, los bares aparecen como uno de los tres tipos de establecimientos más comunes en este último grupo, lo cual puede marcar o inidicar una diferencia en las preferencias y modelos de propiedad.
# 
# </span>
#     
# </div>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# ****  
# Se calcula la cantidad de asientos para los establecimientos que pertencen a una cadena, se emplea el DataFrame `chain_true`.  
# 
# </span>
#     
# </div>

# %%
# se configura el tamaño y el estilo de color para el gráfico
plt.figure(figsize=(14, 10))
plt.style.use('seaborn-pastel')

# se realiza el gráfico con seaborn (sns) a partir del DataFrame 'chain_true'
fig4 = sns.barplot(x='object_type', y='number', data= chain_true)

# se le asigan un título y nombres de los ejes al gráfico
fig4.set_title('Cantidad de Asientos para los Establecimientos que Pertencen a una Cadena', fontsize= 18)
fig4.set_xlabel('Tipo de Establecimiento', fontsize= 14)
fig4.set_ylabel('Promedio del Número de Asientos', fontsize= 14)

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Conclusiones:**  
# Los 3 establecimientos con un mayor número de asientos que forman parte de una cadena son los restaurantes, seguido de los bares y el sector de comida rápida; los tres sitios tienen en promedio un mayor número de asientos.  
# 
# </span>
#     
# </div>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# ****  
# Se separan los nombres de las calles de la columna `address` en una nueva columna llamada `street`. Para lo anterior se emplea el método `str.extract` con una expresión regular para extraer sólo la calle.  
# 
# </span>
#     
# </div>

# %%
# se separan los nombres de las calles con str.extract y la expresión regular '\s(.+)'
rest_data_us['street'] = rest_data_us['address'].str.extract(r'\s(.+)')
rest_data_us.head()

# %%
# se agrupan los datos por la calle y el número de establecimientos y se reinicia el índice con reset_index()
# el resultado se guarda en 'num_rest_by_streets'
num_rest_by_streets = rest_data_us.groupby('street')[['object_type']].count().reset_index()
# se cambia el nombre de la columna
num_rest_by_streets = num_rest_by_streets.rename(columns= {'object_type': 'count_rest'})
num_rest_by_streets.head()

# %%
# del DataFrame 'num_rest_by_streets' se ordenan de mayor a menor con sort_values()  y se guardan solo el top 10 empleando head()
# el resultado se guarda en 'top_10_streets'
top_10_streets = num_rest_by_streets.sort_values(by= 'count_rest', ascending= False).head(10)

# %%
# se configura el tamaño y el estilo de color para el gráfico
plt.figure(figsize=(12, 8))

# se grafica el top 10 de las calles con más establecimientos con seaborn (sns) a partir del DataFrame 'top_10_streets'
fig5 = sns.barplot(x='street', y='count_rest', data= top_10_streets)

# se le asigan un título y nombres de los ejes al gráfico
fig5.set_title('Top 10 de Calles con más Establecimientos', fontsize= 16)
fig5.set_xlabel('Calle', fontsize= 12)
fig5.set_ylabel('Número de Establecimientos', fontsize= 12)
plt.xticks(rotation= 45)
plt.show()

# %%
# se filtra el DataFrame 'num_rest_by_streets' en donde la columna 'count_rest' sea 1
# se selecciona la columna 'count_rest' y se emplea sum(), el resultado se guarda en 'total_streets_one_rest'
total_streets_one_rest = num_rest_by_streets[num_rest_by_streets['count_rest'] == 1]['count_rest'].sum()
print(f'Total de calles con un sólo establecimiento: {total_streets_one_rest}')

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# ****  
# Para analizar la distribución del número de asientos del top 10 de las calles con más establecimientos, se hace una lista del nombre de las calles del top 10 y se filtra el DataFrame `rest_data_us` con `isin()`. Después se grafica un histograma, un violinplot y stripplot con la librería ploty para analizar la distribución del número de asientos.  
# 
# </span>
#     
# </div>

# %%
# se guarda una lista con los nombres de las calles del top 10
list_top_10_streets = list(top_10_streets['street'])
list_top_10_streets

# %%
# se filtra el DataFrame 'rest_data_us' donde sólo tenga los datos de las calles del top 10 con isin()
# el resultado se guarda en 'df_top_10'
df_top_10 = rest_data_us[rest_data_us['street'].isin(list_top_10_streets)]
df_top_10.head()

# %%
# se grafica un histograma para el número de asientos para el top 10 de calles con más establecimientos
fig6 = px.histogram(df_top_10, x="number", nbins= 80)
fig6.show()

# %%
# con numpy se calculan los percentiles 95 y 99
print(np.percentile(df_top_10['number'], [90, 95, 99]))

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Observaciones:**  
# Al calcular los percentiles del número de asientos para el top 10 de las calles con más establecimientos se observa que no más del 5 % tuvieron más de 174 asientos y no más del 1 % de los establecimientos tienen más de 217 asientos.  
# 
# </span>
#     
# </div>

# %%
# se configura el tamaño y el estilo de color para el gráfico
plt.figure(figsize=(14, 8))

# se gra
fig7 = sns.violinplot(x="street", y="number", data= df_top_10)

# se le asigan un título y nombres de los ejes al gráfico
fig7.set_title('Top 10 de Calles con más Establecimientos', fontsize= 16)
fig7.set_xlabel('Calle', fontsize= 12)
fig7.set_ylabel('Cantidad de Asientos', fontsize= 12)
plt.xticks(rotation= 45)
plt.show()

# %%
# se configura el tamaño y el estilo de color para el gráfico
plt.figure(figsize=(14, 8))

fig8 = sns.stripplot(x="street", y="number", data= df_top_10)

# se le asigan un título y nombres de los ejes al gráfico
fig8.set_title('Top 10 de Calles con más Establecimientos', fontsize= 16)
fig8.set_xlabel('Calle', fontsize= 12)
fig8.set_ylabel('Cantidad de Asientos', fontsize= 12)
plt.xticks(rotation= 45)
plt.show()

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# **Conlusiones:**  
# En el histograma se observa que los datos no tienen una distribución normal, hay establecimientos que tienen más de 50 asientos, lo cuál hace que el gráfico tenga un sesgo a la derecha.  
# 
# En los gráficos de violin para cada calle se observa que los datos no están distribuidos de forma simétrica, lo cuál indica un sesgo en la distribución y que hay valores muy grandes. Lo anterior se puede corroborar con el gráfico `stripplot`, ya que la mayoría de los datos se encuentran concentrados entre 0 y 50 asientos para los establecimientos de las calles que conforman el top 10.  
#     
# </span>
#     
# </div>

# %% [markdown]
# # Resumen y Conclusión General <a id='end'></a>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# • El top 3 de los establecimientos con mayor presencia son:  
#     1.  Restaurantes (75.2 %)  
#     2. Sector de comida rápida (11 %)  
#     3. Cafeterías (4.5 %)  
#     
# • El 61.9 % de los establecimientos pertenecen a una cadena.  
#     
# • El top 3 de los establecimientos que pertenecen a una cadena son:  
#       1. Restaurantes (62.4 %)  
#       2. Sector de comida rápida (16.5 %)  
#       3. Pastelerías (7.7 %)  
#     
# • El top 3 de los establecimientos que no pertenecen a una cadena son:  
#       1. Restaurantes (83.1 %)  
#       2. Sector de comida rápida (7.7 %)  
#       3. Bares (3.6 %)  
#     
# • El top 3 de los establecimientos con un mayor número de asientos que forman parte de una cadena son los restaurantes, los bares y el sector de comida rápida; los tres sitios tienen en promedio más de 35 de asientos.  
#     
# •  El top 10 de las calles con más establecimientos son: W SUNSET BLVD, W PICO BLVD, HOLLYWOOD BLVD,  WILSHIRE BLVD, S VERMONT AVE, SANTA MONICA BLVD, W 3RD ST, BEVERLY BLVD, S FIGUEROA ST y  MELROSE AVE.  
#     
# • Los establecimientos en su  mayoría tienen entre 0 y 50 asientos para los establecimientos de las calles que conforman el top 10, no más del 10 % tuvieron más de 124 asientos.  
# 
#     
# </span>
#     
# </div>

# %% [markdown]
# # Recomendaciones Generales <a id='recom'></a>

# %% [markdown]
# <div style="background-color: lightyellow; padding: 10px;">
# 
# <span style="color: darkblue;">  
#     
# • El sector con mayor presencia es el restaurantero, por tanto, es una opción factible a elegir para el tipo de establecimiento. En su defecto, podría ser del sector de comida rápida.
# 
# • No necesariamente el establecimiento tiene que pertenecer a una cadena, ya que en su mayoría los establecimientos no forman parte de una cadena.
# 
# • Además, no se requiere de un lugar grande con muchos asientos, dado que los establecimientos actuales en su mayoría tienen menos de 100 asientos. Por lo tanto, se puede comenzar con un lugar pequeño.  
#     
# </span>
#     
# </div>

# %% [markdown]
# # Enlace de Presentación <a id='link'></a>
# 
# Presentation: <https://drive.google.com/file/d/1vNhIBHCkmgELI_-J02f3kU_DE1203Qnc/view?usp=drive_link> 

# %%



