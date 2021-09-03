# displaying all transaction
import json
from tabulate import tabulate

op=open("sales.json","r")
sales=json.loads(op.read())

p=[]
for i in sales.keys():
    x=sales[i]
    l=[i]
    for j in x.keys():
        if j=="products":
            pass
        else:
            l.append(x[j])

    p.append(l)
header=["Transaction_id", "Customer Name", "Contact", "Date of Purchase", "Total Item","Total Quantity","Total Cost"]
print(tabulate(p, headers=header, tablefmt='orgtbl'))

