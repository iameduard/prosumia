#Librerias....
import os
import glob
import shutil


BASE="E:\\Descargas\\truncated-csv-uploads"

os.chdir(BASE)

origen=os.getcwd()+'\\'

list1 = glob.glob("*.csv")

listaCampos=[]

for dir in list1:
	f1=open(dir,"r")
	lineas=f1.readline()
	campos=lineas.split(';')
	for c in campos:
		if c not in listaCampos:
			listaCampos.append(c)
	f1.close()

print listaCampos


