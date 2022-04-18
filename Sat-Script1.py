#ME975 - Assignment - Jacob Currie - 201718558
#---------------------------------------------
#Plotting/Graphing Script
import matplotlib.pyplot as plt
import numpy as np

DistrictNamesList = ['Borders', 'Central', 'Dumfries & Gal', 'Fyfe', 'Grampian', 'Highland', 'Lothian', 'Orkney', 'Shetland Islands', 'Strathclyde', 'Tayside', 'Western Isles']
Data2019 = [2.2122008554262085e-05,2.3609144718329626e-05,2.2920205749643354e-05,2.996572421056435e-05,1.7438069491396237e-05,1.6123909193907615e-05,
            2.978613519760064e-05,1.2591065901324445e-05,1.2150154708114013e-05,2.2034038841374178e-05,1.916083730769428e-05,1.2717830142645274e-05]
Data2020 = [2.0716044129793837e-05,2.184295374201366e-05,2.0838283314443245e-05,2.7177963032354258e-05,1.8644532261182567e-05,1.5392865174184957e-05,
            2.5521300512970897e-05,1.227162058641417e-05,9.72305618677271e-06,2.04907429503703e-05,1.9815419902427874e-05,1.0717729418158482e-05]
Data2021 = [2.210136053056543e-05,2.207590961163332e-05,2.0215835905095158e-05,3.0077168762210414e-05,1.9320790396829416e-05,1.439016460944674e-05,
            3.158178579266714e-05,1.1731656606566475e-05,1.0305211852537112e-05,2.0276745580832056e-05,1.9620622300899496e-05,1.0706163989725942e-05]
LegendLabels = ['2019', '2020', '2021']            
PopDensity = [2.49289177832715e-05,0.00011463267606779667,2.3413799137766673e-05,0.0002722375960673222,6.604844414118531e-05,8.820244062438711e-06,
            0.0004746136196991526,2.0756991266692525e-05,1.2111503364635487e-05,0.00015828110200027238,5.21235078302237e-05,8.524820130842963e-06]

sortIndex = np.argsort(PopDensity)  #Getting sorted list indices for population density

def argSort(data, indices): #sort list with given list or indices
    newList = []
    for i in indices:
        newList.append(data[i])
    return newList

PopDensitySorted = argSort(PopDensity, sortIndex)
Data2019Sorted = argSort(Data2019, sortIndex)
Data2020Sorted = argSort(Data2020, sortIndex)
Data2021Sorted = argSort(Data2021, sortIndex)
DistrictsSorted = argSort(DistrictNamesList, sortIndex)

#Saving to Excel doc
import xlwt
W = xlwt.Workbook()
Ws = W.add_sheet("Results")

Ws.write(2,1,"District")
Ws.write(3,1,"2019")
Ws.write(4,1,"2020")
Ws.write(5,1,"2021")
Ws.write(6,1,"Pop Density")

for i in range(0, len(DistrictNamesList)):
    Ws.write(2, i + 2, DistrictNamesList[i])
    Ws.write(3, i + 2, Data2019[i])
    Ws.write(4, i + 2, Data2020[i])
    Ws.write(5, i + 2, Data2021[i])
    Ws.write(6, i + 2, PopDensity[i])

Wa = W.add_sheet("Results2")

Wa.write(1,2,"District")
Wa.write(1,3,"2019")
Wa.write(1,4,"2020")
Wa.write(1,5,"2021")
Wa.write(1,6,"Pop Density")


for i in range(0, len(DistrictNamesList)):
    Wa.write(i + 2,2, DistrictNamesList[i])
    Wa.write(i + 2,3, Data2019[i])
    Wa.write(i + 2,4, Data2020[i])
    Wa.write(i + 2,5, Data2021[i])
    Wa.write(i + 2,6, PopDensity[i])

#W.save("Result.xls")

N = len(DistrictNamesList)
xIndex = np.arange(N) * 4

def NO2_Plot(data, labels):
    f1, ax = plt.subplots()
    c=['#66c2a5', '#fc8d62', '#8da0cb']
    for j in range(len(data)):
        ax.bar(xIndex + j, data[j], color=c[j])

    ax.set_xticks(xIndex + 1)
    ax.set_xticklabels(labels)
    ax.legend(LegendLabels)
    ax.set_ylabel('tropospheric NO2 column number density (mol/m^2)')
    ax.set_title('Annual average Tropospheric NO2 Column density per District in Scotland')
    
rawData = [Data2019, Data2020, Data2021]
NO2_Plot(rawData, DistrictNamesList)

rawDataSorted = [Data2019Sorted, Data2020Sorted, Data2021Sorted]
NO2_Plot(rawDataSorted, DistrictsSorted)

def NO2_stack():
    f1, ax = plt.subplots()
    c = ['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00','#cab2d6','#6a3d9a','#ffff99','#b15928']
    DistrictData = []
    for i in range(len(Data2019)):
        DistrictData.append([Data2019Sorted[i], Data2020Sorted[i], Data2021Sorted[i]])

    for i in range(len(DistrictsSorted)):
        ax.plot([2019, 2020, 2021], DistrictData[i], '-o', color=c[i])

    ax.set_xticks([2019,2020,2021])
    ax.legend(DistrictsSorted, bbox_to_anchor=(1,1), loc="upper left")
    ax.grid()
    ax.set_xlabel('Year')
    ax.set_ylabel('Tropospheric NO2 Column number Density (mol/m^2)')
    ax.set_title('Annual Average Tropospheric NO2 Column density Per Year')

NO2_stack()

plt.show()