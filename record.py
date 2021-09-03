#inserting data to inventory
import json


record={
1000001 : {"name": "comb","category":"Personal" ,"Cost_each":20,"quantity":10 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000002 : {"name": "Hair dryer","category":"Personal" ,"Cost_each":200,"quantity":5 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000003 : {"name": "Towels","category":"Personal" ,"Cost_each":50,"quantity":8 ,"unit_sold":0,"last_updated":"2021-09-01"},

1000004 : {"name": "Chair","category":"furniture" ,"Cost_each":180,"quantity":15 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000005 : {"name": "Desk","category":"furniture" ,"Cost_each":250,"quantity":15 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000006 : {"name": "Bookshelf","category":"furniture" ,"Cost_each":500,"quantity":6 ,"unit_sold":0,"last_updated":"2021-09-01"},

1000007 : {"name": "Bata sandal","category":"footware" ,"Cost_each":800,"quantity":25 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000008 : {"name": "Adidas Sneakers","category":"footware" ,"Cost_each":1050,"quantity":15 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000009 : {"name": "Puma Shoes","category":"footware" ,"Cost_each":2000,"quantity":40 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000010 : {"name": "Nike Shoes","category":"footware" ,"Cost_each":2500,"quantity":30 ,"unit_sold":0,"last_updated":"2021-09-01"},

1000011 : {"name": "Jackets","category":"clothes" ,"Cost_each":1000,"quantity":10 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000012 : {"name": "Shirts","category":"clothes" ,"Cost_each":400,"quantity":12 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000013 : {"name": "Socks","category":"clothes" ,"Cost_each":50,"quantity":20 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000014 : {"name": "Sweatshirts","category":"clothes" ,"Cost_each":250,"quantity":9 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000015 : {"name": "Pants","category":"clothes" ,"Cost_each":500,"quantity":12 ,"unit_sold":0,"last_updated":"2021-09-01"},

1000016 : {"name": "keyboard","category":"Houseware" ,"Cost_each":20,"quantity":10 ,"unit_sold":0,"last_updated":"2021-09-01"},

1000017 : {"name": "Bose speaker","category":"speaker" ,"Cost_each":10000,"quantity":6 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000018 : {"name": "JBL speakers","category":"speaker" ,"Cost_each":4000,"quantity":10 ,"unit_sold":0,"last_updated":"2021-09-01"},

1000019 : {"name": "MI-TV 55 inches","category":"electronics" ,"Cost_each":40000,"quantity":3 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000020 : {"name": "Samsung-TV 65 inches","category":"electronics" ,"Cost_each":50000,"quantity":7 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000021 : {"name": "OnePlus TV 45 inches ","category":"electronics" ,"Cost_each":45000,"quantity":10 ,"unit_sold":0,"last_updated":"2021-09-01"},

1000022 : {"name": "Football","category":"sports" ,"Cost_each":840,"quantity":9 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000023 : {"name": "Basketball","category":"sports" ,"Cost_each":780,"quantity":18 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000024 : {"name": "Hockey Stick","category":"sports" ,"Cost_each":900,"quantity":15 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000025 : {"name": "Cricket bat","category":"sports" ,"sports":2000,"quantity":10 ,"unit_sold":0,"last_updated":"2021-09-01"},

1000026 : {"name": "Samsung M31","category":"Mobile" ,"Cost_each":14999,"quantity":25 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000027 : {"name": "One Plus Nord2","category":"Mobile" ,"Cost_each":24999,"quantity":25 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000028 : {"name": "iphone 12","category":"Mobile" ,"Cost_each":65000,"quantity":25 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000029 : {"name": "Realme GT","category":"Mobile" ,"Cost_each":20000,"quantity":25 ,"unit_sold":0,"last_updated":"2021-09-01"},
1000030 : {"name": "Jiophone","category":"Mobile" ,"Cost_each":1500,"quantity":25 ,"unit_sold":0,"last_updated":"2021-09-01"}
}


dump_data = json.dumps(record)
file = open("record.json",'w')
file.write(dump_data)
file.close()
print("items add to Inventory")



