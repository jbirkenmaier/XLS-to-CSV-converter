import numpy as np
import xlrd

def read_data(names_of_sheets, column_x=1,column_y=2):
    for sheet in names_of_sheets:
        book= xlrd.open_workbook('%s.XLS'%sheet)
        sh = book.sheet_by_index(0)

        print('Reading ', str(sh.cell_value(rowx=0, colx=column_x)), 'as x, and', str(sh.cell_value(rowx=0, colx=column_y)), 'as y')
        drehzahl =[]
        torque = []
        len_of_file = sh.nrows
        #read rotational velocity
        drehzahl = [sh.cell_value(rowx=i, colx=1) for i in range(len_of_file)][1:]
        #read torque
        torque = [sh.cell_value(rowx=i, colx=2) for i in range(len_of_file)][1:]

        with open('%s.csv'%sheet, "w") as datafile:
            datafile.close()
        
        for row in range(len_of_file-1):
            with open('%s.csv'%sheet, "a+") as datafile:
                datafile.write(str(f'{drehzahl[row]:.2f}') + ", " + str(f'{torque[row]:.2f}'+'\n'))
