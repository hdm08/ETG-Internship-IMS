# ETG-Internship-IMS
Inventory Management System:
There 3 basic functionality :
1. Add Product to the Inventory
2. Manage the Sales of product
3. Displaying all transaction

It consist of 4 python file Record.py, sales.py, Update_Inventory.py and sales_list.py and 2 JSON file record.json which store all the products available in inventory and sales.json which store all transaction done by customer along with all product purchased by them  and customer information.

dumps method from json library is used to dump python objects to json object and 
loads method is used to load json object to python object.

Update Inventory.py: this file can be used to add new products to the inventory and it will also display all product present in inventory.
Sales.py: This file handles bill creation, record updation, creation of sales.json file all puchases are handle in this file.
SalesList: Using this we can see all the transaction done.

fields for record/product:
Product_id: { name,
              category,
              Cost_each,
              quantity,
              unit_sold,
              last_updated
        }

fields for sales:
Transaction id:{
                  customer_name,
                  mob_no,
                  date_of_purchase,
                  total_item,
                  total_quantity,
                  total_cost,
                  products :{ 
                              Product_id: { name,
                                            quantity,
                                            price_each,
                                            total_cost_per_Product,
                                      }
                            }
                }
      
 Product available in Inventory:
![Screenshot (1)](https://user-images.githubusercontent.com/65184650/131949918-89e9fc26-1e39-474d-869f-bf59517e4710.png)

Sales list:
![Screenshot (2)](https://user-images.githubusercontent.com/65184650/131949908-2a39a2e1-e64c-4c3f-9bfb-6011159f3d9b.png)

