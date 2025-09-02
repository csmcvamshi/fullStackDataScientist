books = eval(input("enter the books "))
new = input("enter the book to add ")
rem = input("enter book to remove ")

books.append(new)
books.remove(rem)

print(books)