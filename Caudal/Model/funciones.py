#Funciones

#%%
def Qo(Pwf,pr,Qmax):
    """Función que nos permite calulcar el Qo, mediante el uso de los parámetros:
    pr, Qmax y Pwf"""
    x = (Pwf/pr)
    y = (Pwf/pr)**2

    caudal = (1 - 0.2*x - 0.8*y)*Qmax

    return caudal

#print(Qo(2400,250,2400))