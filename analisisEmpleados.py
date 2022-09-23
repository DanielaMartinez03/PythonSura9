import pandas as pd

tablaEmpleados=pd.read_csv('./BD/empleados.csv')
#print(tablaEmpleados)

#print(tablaEmpleados.to_string())

#Filtro 1 quiero que solo me muestre los datos de los analistas uno
'''tablaAnalistas1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)

archivoHTML=tablaAnalistas1.to_html()
archivoTEXTO=open('datosanalistas1.html',"w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''

'''tablaAnalistas2=tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)

archivoHTML2=tablaAnalistas2.to_html()
archivoTEXTO2=open('datosanalistas2.html',"w")
archivoTEXTO2.write(archivoHTML2)
archivoTEXTO2.close()
'''
tablaAnalistas3=(tablaEmpleados[(tablaEmpleados["edad"]<30)&(tablaEmpleados["salario"]>5500000)])
print(tablaAnalistas3)


archivoHTML3=tablaAnalistas3.to_html()
archivoTEXTO3=open('datosanalistas3.html',"w")
archivoTEXTO3.write(archivoHTML3)
archivoTEXTO3.close()
