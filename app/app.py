def calculate_discount(price, discount):
    discounted_price = price - (price * discount)
    return discounted_price

if __name__ == "__main__":
    price = 200
    discount = 0.15
    result = calculate_discount(price, discount)
    print(f"Prezzo originale:{price}")
    print(f"Sconto: {discount * 100}%")
    print(f"Prezzo scontato: {result}")