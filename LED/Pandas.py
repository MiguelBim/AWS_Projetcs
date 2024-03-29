from pandas import Series, DataFrame
import pandas as pd

# Clases primarias de la librería
    # DataFrame: Imagen de una tabla relacional, con filas y columnas
    # Series: Una sola columna
# Un DataFrame contiene mas de una Series

# SERIES
ser_1 = Series([1, 1, 2,-3,-5, 8, 13])
print(ser_1)
# cada series, dataframe va a tener índices: objetos inmutables que etiquetan las filas de mis estructuras (columna o tabla)

print(ser_1.values)
print(ser_1.index)

# Indices personalizados
ser_2 = Series([1, 1, 2,-3,-5], index=['a', 'b', 'c', 'd', 'e'])
print(ser_2)

# Acceso a valores por medio del índice
print(ser_2['e'])
# Condiciones
print(ser_2[ser_2 > 0])
# Operaciones algebraicas
print(ser_2 * 2)

# Crear una serie a partir de un diccionario
dict_1 = {'matematicas':100, 'quimica':200, 'logica':300}
ser_3 = Series(dict_1)
print(ser_3)

# DATAFRAMES
# Un dataframe es una estructura tabular que va a contener una colección ordenada de columnas
# estas estructuras van a tener índices tanto en las filas como en las columnas

# Crear una dataframe a partir de un diccionario
data_1 = {'estado': ['JA', 'CO', 'MX', 'JA', 'LA'],
          'año': [2012, 2013, 2014, 2014, 2015],
          'versión': [5.0, 5.1, 5.2, 4.0, 4.1]}
print(data_1)
df_1 = DataFrame(data_1)
print(df_1)

# Agregar columna nueva (sin elementos)
df_2 = DataFrame(data_1, columns=['año', 'estado', 'versión', 'NewColumn'])
print(df_2)

# Renombrar una columna
df_3 = df_2.rename(columns={'NewColumn': 'rank'})
print(df_2)
print(df_3)

# Usando el parámetro inplace para aplicar cambios en el mismo dataframe
df_2.rename(columns={'NewColumn': 'rank'}, inplace=True)
print(df_2)

# Agregando elementos a una Series (columna)
ranks_df3 = Series([1,2,3], index=[2,3,4])
df_3['rank'] = ranks_df3
print(df_3)

# Agregando elementos por medio de un arreglo
ranks_df4 = [1,1,2,3,4]
df_3['rank'] = ranks_df4
print(df_3)

# Ingresar a Series (columnas)
print(df_3['estado'])

# Ingresar a una fila
print(df_3.iloc[0])

# Ingresar a una celda de la tabla
print(df_3.at[1,'estado'])

# 3 Series nuevas
ser_nombre = Series(["María", "Lupe", "Omar", "Antonia", "Checo"])
ser_edad = Series([21,20,22,19,20])
ser_estado = Series(["Jalisco", "Michoacan", "Puebla", "Guanajuato", "Tabasco"])

frame = {'Nombre': ser_nombre, 'Edad': ser_edad, 'Estado':ser_estado}
print(frame)

estudiantes_df = pd.DataFrame(frame)
print(estudiantes_df)

edad = [11,9,9,8,7]
estudiantes_df['Edad 2'] = edad
print(estudiantes_df)

# Eliminar columnas
estudiantes_df.drop(columns=['Edad 2'], inplace=True)
print(estudiantes_df)

# Ingresando a mas de una columna
print(estudiantes_df[['Nombre', 'Estado']])

# Iterando sobre Dataframes
for index, row in estudiantes_df.iterrows():
    print(index, row)
    print()

for index, row in estudiantes_df.iterrows():
    for column_name, value in row.iteritems():
        print(column_name)
        print(value)
        print()