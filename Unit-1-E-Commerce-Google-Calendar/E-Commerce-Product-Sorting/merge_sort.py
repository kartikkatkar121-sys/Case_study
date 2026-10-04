class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ₹{self.price}"


def merge_sort(products):
    if len(products) <= 1:
        return products
    mid = len(products) // 2
    return merge(merge_sort(products[:mid]), merge_sort(products[mid:]))


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].price <= right[j].price:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    products = [
        Product("Laptop", 55000),
        Product("Headphones", 2500),
        Product("Mobile", 30000),
        Product("Keyboard", 1800),
        Product("Monitor", 12000),
    ]
    print("Original Products:")
    for p in products:
        print(p)

    print("\nProducts Sorted by Price:")
    for p in merge_sort(products):
        print(p)
