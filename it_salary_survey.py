import pandas as pd
import matplotlib.pyplot as plt

survey = pd.read_csv('./IT-Salary-Survey.csv')

#visualizar datos (primeras filas)
first10 = survey.head(10)
# print(first10)
for col in survey.columns:
    print(col)

#tamaño
size = survey.size

#informacion de las columnas 
# info = survey.info()


#estadisticas descriptivas de los datos
desc = survey.describe()


#Valores nulos por columna
n_values = survey.isna().sum()


############
# 1.
ages = survey.groupby('Gender')['Age'].hist()
plt.show()

# 2.
cities = survey.groupby('Gender')['City'].head(10).hist()
plt.show()

# 3.
language = survey.groupby('Company type')['Main language at work'].head(10).hist()
# print(language)
plt.show()

# 4.
status_l = survey.groupby('Gender')['Employment status'].hist()
plt.show()

# 5.

# # s_avrg = pd.Series(salary_avrg)
# # s_avrg_df = pd.DataFrame({'Salary':s_avrg})

# # answ = s_avrg_df.groupby('Position')['Employment status'].hist()
# # plt.show()

