### **Exercise 4: Receipt Generator (Challenging)**

# Create a mini shopping cart:

# - Ask for 3 items (name and price each)
# - Calculate subtotal, 10% discount, 5% tax, final total
# - Print a formatted receipt


def generate_receipt(arr):
    subtotal = 0
    discount = 10
    tax = 5

    for item in arr:
        subtotal += int(item[1])
        final_amount_with_tax_and_discount = (
            int(item[1]) - (discount / 100) * int(item[1]) + (tax / 100) * int(item[1])
        )
        item[1] = final_amount_with_tax_and_discount

    print(arr)


arr = []
for i in range(3):
    name = input(f"Enter the name of item {i + 1}: ")
    price = input(f"Enter the price of item {i + 1}: ")
    arr.append([name, price])

generate_receipt(arr)
