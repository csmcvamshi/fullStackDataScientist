import os;

from unicodedata import category;
from supabase import create_client, Client;
from dotenv import load_dotenv;
from datetime import date

load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")
sb:Client=create_client(url,key)

def add_member(mem_id,name,email):
    payload={"mem_id":mem_id,"name":name,"email":email}
    resp=sb.table("members").insert(payload).execute()
    return resp

if __name__ == "__main__":
    id=int(input("enter id "))
    name=input("enter name ")
    email=input("enter the email ")

    print(add_member(id,name,email))
