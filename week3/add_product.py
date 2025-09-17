import os
from unicodedata import category;
from supabase import create_client, Client;
from dotenv import load_dotenv;
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")
sb:Client = create_client(url,key)

def add_product(prod_id,name,price,stock,category):
    payload = {"prod_id":prod_id,"name":name,"price":price,"stock":stock,"category":category}
    resp=sb.table("products").insert(payload).execute()
    return resp.data

if __name__== "__main__":
    id=int(input("enter id "))
    name=input("enter the name ")
    price=int(input("enter price "))
    stock=int(input("enter the stock "))
    category=input("enter the catrgory ")

    created=add_product(id,name,price,stock,category)
    print("inserted ",created)
