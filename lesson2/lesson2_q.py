sci_book_price = 58
comic_price = 32
his_book_price = 24

total_sci = sci_book_price * int(input("How many sci-fi books do you have? "))
total_comic = comic_price * int(input("How many comic books do you have? "))
total_his = his_book_price * int(input("How many history books do you have? "))

his_promotion = (total_his / his_book_price) // 3

# total_sci / sci_book_price = amount of sci-fi books purchased
if total_sci / sci_book_price >= 3:
    total_sci = (total_sci * 0.9)

# $20 off if total purchase price is over $300
final_price = total_sci + total_comic + ((total_his / his_book_price) - his_promotion) * 24
if final_price > 300:
    final_price -= 20

print(f"Hi! Your final price is {final_price}, you earned {his_promotion} history books.")
