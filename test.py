# import re
# txt = '14. SUSPECT DRUG(S) (include generic name) #1 ) Synacthen Depot (TETRACOSACTIDE) \n Suspension for Injection, 1 mg/ml {Lot # Unknown}; Regimen #1 15. DAILY DOSE(S);'
# 
# 
# stuff=re.search('14. SUSPECT(.*?)15. DAILY DOSE',txt,re.DOTALL).group(1)
# if 'Synacthen' in stuff:
#     print('Found')
# print(stuff)
PathFile = open('./Paths.txt')
PVpath = PathFile.read()
print(type(PVpath))
print(PVpath)