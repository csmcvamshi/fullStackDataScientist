import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def delete_book(book_id: int):
    response = sb.table("books").delete().eq("book_id", book_id).execute()
    return response

if __name__ == "__main__":
    book_id = int(input("Enter the book_id to delete: "))
    result = delete_book(book_id)
    print(result)
