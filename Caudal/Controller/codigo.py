import xlwings as xw
import pandas as pd
import seaborn as sns
import matplotlib as plt
import numpy as np
from Caudal.Model.funciones import Qo

#Definir la hoja
SHEET = 'sheet1'

#Definir las columnas
DF_DATA = 'df_datos'
DF_DATOS = 'valores'
DF_PWF = 'datos_pwf'
DF_Qo = 'valores_qo'
DF_Pr = 'df_pr'
DF_Qmax = 'df_qmax'

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[SHEET]
    df_data =sheet[DF_DATOS].options(np.array, transpose=True).value

    #Llamar e imprimir los resultados
    sheet[DF_Qo].options(np.array, transpose=True).value = Qo(*df_data)

    #Crear la gráfica


if __name__ == "__main__":
    xw.Book("examen.xlsm").set_mock_caller()
    main()
