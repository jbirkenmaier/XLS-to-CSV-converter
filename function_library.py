import xlrd
import os
import xlrd


def find_XLS_files():
    xls_file_list = []
    for element in os.listdir():
        file_object = os.path.isfile(element)

        if file_object == True and element.endswith('.XLS'):
            xls_file_list.append(str(element))
    xls_file_list = [element.strip('.XLS') for element in xls_file_list]
    return xls_file_list

def read_data(names_of_sheets):
    contents=[]
    for sheet in names_of_sheets:
        book= xlrd.open_workbook('%s.XLS'%sheet)
        sh = book.sheet_by_index(0)
        len_of_file = sh.nrows
        num_of_cols = sh.ncols

        for i in range(num_of_cols):
            contents.append([sh.cell_value(rowx=j, colx=i) for j in range(len_of_file)])

        with open('%s.csv'%sheet, "w") as datafile:
            datafile.close()
        
        for row in range(len_of_file):
            with open('%s.csv'%sheet, "a+") as datafile:
                for i in range(num_of_cols):
                    datafile.write(str(contents[i][row])+',')
                datafile.write('\n')
