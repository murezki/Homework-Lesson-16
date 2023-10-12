import imp
import os
import csv

os.mkdir("watch_me")
os.mkdir("list")

file_name = os.path.basename('C:\Homework os library\sub\Nina_Stoletova.jfif')
a = file_name.split(".")
b = a[0].split("_")
os.rename('C:\Homework os library\sub\Nina_Stoletova.jfif', f'C:\Homework os library\sub\{b[1]}_{b[0]}')

file_name2 = os.path.basename('C:\Homework os library\video\Misha_Perlman.jfif')
c = file_name2.split(".")
d = c[0].split("_")
os.rename('C:\Homework os library\sub\Nina_Stoletova.jfif', f'C:\Homework os library\sub\{d[1]}_{d[0]}')

f = open('C:\Homework os library\list.csv', 'w')
writer = csv.writer(f)
writer.writerow("sadsadsadsad")
f.close()