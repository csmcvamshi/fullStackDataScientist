import os;
from supabase import Client, create_client;
from unicodedata import category
from dotenv import load_dotenv
load_dotenv()

url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")
sb:Client=create_client(url,key)

def update_mem(cond,para,newVal):
    dic={para:newVal}
    response=sb.table("books").update(dic).eq("prod_id",cond).execute()
    return response
if __name__ =="__main__":
    id=int(input("enter the id to change "))
    col=input("enter the name of the col to change ")
    val=int(input("enter the new val "))

    print(update_mem(id,col,val))
