# managing Sales
import random
from datetime import date
from tabulate import tabulate
import json

f = open('record.json','r')

load_data = json.loads(f.read())
final_file = open("sales.json", 'r')
final_sale=json.loads(final_file.read())


while True:
    customer_name = input("Enter Name of Customer : ")
    mob_no = int(input("Enter Mobile Number : ")[0:10])

    while True:

        # selecting random transaction id which in not taken previously
        l = "0123456789"
        t = "".join(random.sample(l, len(l)))
        if str(t) not in final_sale.keys():
            tid = t
            break

    # it will keep track of product purchased by customer
    sale = {}


    sale["customer_name"]=customer_name
    sale["mob_no"] = mob_no
    sale["date_of_purchase"] = str(date.today())


    # initializing varibale
    total_items=0
    total_cost=0
    total_quantity=0

    # dictionary to keep track of product purchased by a Customer
    product = {}

    while True:

        # product id either entered manually or by bar-code scanner
        product_id = int(input("Enter Product id : "))

        #quantity of product will be entered
        quant = int(input("Enter Quantity : "))

        # product is fetched from record based on product id
        sale_pro = load_data[str(product_id)]

        # checking product is available in inventory or not
        if sale_pro["quantity"]-quant>=0:
            sale_pro["quantity"]-=quant
            if sale_pro["quantity"]-quant==0:
                del load_data[str(product_id)]
        else:
            print("Product out of stock")
            continue

        # incrementing unit_sold in record
        sale_pro["unit_sold"] += quant

        # dictionary to store single product at a time
        single_prod = {product_id :{"name" : sale_pro["name"], "quantity": quant,"price_each":sale_pro["Cost_each"],"total_cost_per_Product":quant*sale_pro["Cost_each"] }}

        # evaluating total item, total cost, total quantity
        total_items+=1
        total_cost+=(quant*sale_pro["Cost_each"])
        total_quantity+=quant

        # single product is updated to main dictionary product
        product.update(single_prod)

        # checking if more product want to add to bill or checkout
        while True:
            AC = input("Enter A to add another item to bill or C to checkout")[0]
            if AC in ["C", "c", "A", "a"]:
                break
            else:
                print("enter correct character")
        if AC == "C" or AC == "c": break

    # inserting values to sale dictionary
    sale["total_item"]=total_items
    sale["total_quantity"]=total_quantity
    sale["total_cost"]=total_cost
    sale["products"] = product

    #creating table of products purchases
    p = []
    for i in sale.keys():
        if i=="products":
            x=sale["products"]

            for j in x.keys():
                l=[]
                y=x[j]
                l.append(j)
                l.append(y["name"])
                l.append(y["quantity"])
                l.append(y["price_each"])
                l.append(y["total_cost_per_Product"])
                p.append(l)

        else:
            print(str(i)+" : ", str(sale[i]),end="\t|")
    print()
    print(tabulate(p, headers=["pid", "Name", "Quantity", "price", "Total price"], tablefmt='orgtbl'))

    print("Total bill of Mr."+customer_name +" is Rs"+str(total_cost) )
    print()



    # updating sales.json file
    sales_file = open("sales.json", 'r')
    load_sales = json.loads(sales_file.read())
    load_sales[tid] = sale
    dump_sale = json.dumps(load_sales)
    write_sales = open("sales.json", "w")
    write_sales.write(dump_sale)
    write_sales.close()
    sales_file.close()


    while True:
        Cus = input("Enter A to make another bill or E to exit")[0]
        if Cus  in ["E","e","A","a"]:break
        else:print("enter correct character")
    if Cus == "E" or Cus == "e": break


# updating changes to record.json file
record_dumps = json.dumps(load_data)
open_record = open("record.json","w")
open_record.write(record_dumps)
open_record.close()


f.close()


