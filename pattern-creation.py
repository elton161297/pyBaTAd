import re
s="HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandallt heKingsmenCouldntputHumptyDumptyinhisplaceagain. 22 27 97 102"
pattern1=re.search(r'Humpty Dumpty',s,re.I|re.M)
pattern2="[H]+[u]+[m]+[p]+[t]+[y]+[]+[D]+[u]+[m]+[p]+[t]+[y]"
com=re.compile(pattern2)
com2=com.findall(pattern2)
print(com2)

