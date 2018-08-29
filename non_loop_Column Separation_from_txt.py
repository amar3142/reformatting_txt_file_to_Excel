#This program is helpful for fixing formating issues from .txt to excel
import pandas as pd
from pandas import ExcelWriter

#Define n number of column variables 

col01 = []
col02 = []
col03 = []
col04 = []
col05 = []
col06 = []
col07 = []
col08 = []
col09 = []
col10 = []
col11 = []
col12 = []

#Open File and split into columns

with open('C:/Users/HundleyT/Documents/short.txt', "r+") as f:
    data = f.readlines()

    for line in data:
        col01.append(line.strip().split("|")[0])
        
    for line in data:
        col02.append(line.strip().split("|")[1])

    for line in data:
        col03.append(line.strip().split("|")[2])

    for line in data:
        col04.append(line.strip().split("|")[3])

    for line in data:
        col05.append(line.strip().split("|")[4])

    for line in data:
        col06.append(line.strip().split("|")[5])

    for line in data:
        col07.append(line.strip().split("|")[6])

    for line in data:
        col08.append(line.strip().split("|")[7])
        
    for line in data:
        col09.append(line.strip().split("|")[8])

    for line in data:
        col10.append(line.strip().split("|")[9])

    for line in data:
        col11.append(line.strip().split("|")[10])

    for line in data:
        col12.append(line.strip().split("|")[11]) 
        
#Create Pandas df from columns  
        
panda = pd.DataFrame(list(zip(col01,col02,col03,col04,col05,col06,col07,col08,col09,
                              col10,col11,col12)),
              columns=['ID','Report_Date', 'Account_Number_Prior_Servicer','Date_of_Message',
                       'Teller_ID', 'Trans_Type_code','Transaction Message', 'Fieldman_code',
                       'Load_Date','Account_Number', 'Account_Number_Investor', 'Pool_ID'])
    
#clean up data
    
panda_sliced = panda.drop(list([0]))

#Export to excel
writer = ExcelWriter('C:/Users/HundleyT/Documents/Test_Folde/PythonExport_test.xlsx')
panda_sliced.to_excel(writer) #can add sheets here if needed
writer.save()

