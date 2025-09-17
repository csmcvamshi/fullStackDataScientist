import os;

from unicodedata import category;
from supabase import create_client, Client;
from dotenv import load_dotenv;
from datetime import date

load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")
sb:Client=create_client(url,key)

def add_book(id,name,author,cate,stock):
    payload={"book_id":id,"title":name,"author":author,"category":cate,"stock":stock}
    resp=sb.table("members").insert(payload).execute()
    return resp

if __name__ == "__main__":
    id=int(input("enter id "))
    name=input("enter book name  ")
    auth=input("enter the auth name ")
    cat=input("Enter the category ")
    stock=int(input("Enter the stock "))

    print(add_book(id,name,auth,cat,stock))
