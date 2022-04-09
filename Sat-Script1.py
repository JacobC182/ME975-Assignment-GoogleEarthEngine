#ME975 - Assignment - Jacob Currie - 201718558
#---------------------------------------------
#Plotting/Graphing Script
import matplotlib.pyplot as plt
import numpy as np

DistrictNamesList = ['Borders', 'Central', 'Dumfries and Gal', 'Fyfe', 'Grampian', 'Highland', 'Lothian', 'Orkney', 'Shetland Islands', 'Strathclyde', 'Tayside', 'Western Isles']
Data2019 = [2.2122008554262085e-05,2.3609144718329626e-05,2.2920205749643354e-05,2.996572421056435e-05,1.7438069491396237e-05,1.6123909193907615e-05,
            2.978613519760064e-05,1.2591065901324445e-05,1.2150154708114013e-05,2.2034038841374178e-05,1.916083730769428e-05,1.2717830142645274e-05]
Data2020 = [2.0716044129793837e-05,2.184295374201366e-05,2.0838283314443245e-05,2.7177963032354258e-05,1.8644532261182567e-05,1.5392865174184957e-05,
            2.5521300512970897e-05,1.227162058641417e-05,9.72305618677271e-06,2.04907429503703e-05,1.9815419902427874e-05,1.0717729418158482e-05]
Data2021 = [2.210136053056543e-05,2.207590961163332e-05,2.0215835905095158e-05,3.0077168762210414e-05,1.9320790396829416e-05,1.439016460944674e-05,
            3.158178579266714e-05,1.1731656606566475e-05,1.0305211852537112e-05,2.0276745580832056e-05,1.9620622300899496e-05,1.0706163989725942e-05]
LegendLabels = ['2019', '2020', '2021']            
PopDensity = [0.17426138278757503,0.7882225176754679,0.1657262549941687,1.8709740668009556,0.44117151972967555,0.058451959776377994,
            3.289956581898585,0.1320787293067459,0.07400979504997422,1.0977339910833979,0.3546662688716222,0.055960752561892306]

N = len(DistrictNamesList)
xIndex = np.arange(N) * 4

def NO2_Plot(data):
    f1, ax = plt.subplots()
    for i in range(len(data)):
        ax.bar(xIndex + i, data[i])

    ax.set_xticks(xIndex + 1)
    ax.set_xticklabels(DistrictNamesList)
    ax.legend(LegendLabels)
    ax.set_ylabel('tropospheric NO2 column number density (mol/m^2)')
    
rawData = [Data2019, Data2020, Data2021]
NO2_Plot(rawData)

#normalData = [np.divide(Data2019,PopDensity), np.divide(Data2020,PopDensity), np.divide(Data2021,PopDensity)]
#NO2_Plot(normalData)

plt.show()