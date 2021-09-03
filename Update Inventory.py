#updating inventory
import json
from datetime import date
from tabulate import tabulate
record_file = open("record.json",'r')
load_data = json.loads(record_file.read())
p=[]
for i in load_data.keys():
    x=load_data[i]
    l=[i]
    for j in x.keys():
        l.append(x[j])
    p.append(l)
header = ["Product_id", "Name", "Category", "Cost_each", "quantity", "unit_sold","Last Updated"]
print(tabulate(p, headers=header, tablefmt='orgtbl'))

old_inventory = open("record.json",'r')
load_data = json.loads(old_inventory.read())
print("Welcome to IMS")
product_id = str(int(input("Enter Product ID: ")))


if product_id not in load_data.keys():
    Name = input("Enter Name: ")
    Category = input("Enter Category: ")
    Cost = int(input("Enter Cost: "))
    Quantity = int(input("Enter Quantity: "))
    p={product_id: {"name": Name,"category":Category ,"Cost_each":Cost,"quantity":Quantity ,"unit_sold":0,"last_updated":str(date.today())},}
    load_data.update(p)
    print(product_id + " is added to inventory")

else:
    Cost = int(input("Enter Cost: "))
    Quantity = int(input("Enter Quantity: "))
    old_product = load_data[product_id]
    old_product['Cost_each']=Cost
    old_product['quantity']+= Quantity
    old_product['last_updated'] = str(date.today())
    print("product id: "+product_id + " is updated")


open_record = open("record.json","w")
product=json.dumps(load_data)
open_record.write(product)
open_record.close()
old_inventory.close()




