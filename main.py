import xlrd
import function_library as fl
import os

#transform a csv copy version of any .XLS file in the directory

xls_file_list = []

for element in os.listdir():
    file_object = os.path.isfile(element)

    if file_object == True and element.endswith('.XLS'):
        xls_file_list.append(str(element))

xls_file_list = [element.strip('.XLS') for element in xls_file_list]

print(xls_file_list)       

fl.read_data(xls_file_list)
