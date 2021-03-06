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
#colN = []

#Open File and split into columns

with open('path', "r+") as f:
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
        col0n.append(line.strip().split("|")[n-1]) #n is however many columns you are dealing, change the split dilineator situationally
        
#Create Pandas df from columns  
        
panda = pd.DataFrame(list(zip(col01,col02,col03,col04,col05,col06,col07,col0n)),
              columns=['name_1','name_2', 'name_3','name_4',
                       'name_5', 'name_6','name_7', 'name_n')
    
#clear the text titles
    
panda_sliced = panda.drop(list([0]))

#Export to excel
writer = ExcelWriter('destination of save')
panda_sliced.to_excel(writer) #can add sheets here if needed
writer.save()
