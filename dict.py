Nestle_roducts={"KitKat" : "34,456,432","Nescafe" : "14,106,132","Maggi" : "9,960,312","Nido" : "44,506,003"}
Unilever_products={"Lipton" : "23,456,000","Breyers" : "1,235,891","HellManns" : "17,241,412","Marmite" : "11,715,324"}

for key ,value in Unilever_products.items():
    print(key,value)
for key ,value in Nestle_roducts.items():
    print(key,value)

print("Nestle products are {}".format(len(Nestle_roducts)),"Unilever products are {}".format(len(Unilever_products)))

max_key = max(Nestle_roducts, key=Nestle_roducts.get)

print("the top selling in Nestle_roducts is",max_key)
max_key2 = max(Unilever_products, key=Unilever_products.get)

print("the top selling in Unilever_products is",max_key)




Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for items in Nestle:
    print(items)

for element in (Nestle & Unilever):
    print(Nestle & Unilever)

for element in (Nestle & Unilever):
    print(Nestle - Unilever)