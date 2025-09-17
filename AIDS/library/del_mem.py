import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def delete_member(mem_id: int):
    response = sb.table("members").delete().eq("member_id", mem_id).execute()
    return response

if __name__ == "__main__":
    member_id = int(input("Enter the member_id to delete: "))
    result = delete_member(member_id)
    print(result)
