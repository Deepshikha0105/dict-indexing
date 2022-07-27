data2 = {"aa" : {"bb" : "cc" , "dd" : "ee"}, "ff" : [{"gg" : "hh"}, "ii"] }
'''1. Parse for ii
2. Parse for hh
3. Replace ee with "new"'''
#2.1
print(data2["ff"][1])

#2.2
ans2= data2["ff"][0]
print(ans2["gg"])

#2.3
(data2["aa"]["dd"])="new"
print(data2["aa"]["dd"])
