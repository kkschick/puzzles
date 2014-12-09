def largest_palindrome():
    for i in range(999, 0, -1):
        for j in range(i, i - 2, -1):
            product = i * j
            product_str = str(product)
            if product_str == product_str[::-1]:
                return product

def main():
    print largest_palindrome()

if __name__ == '__main__':
    main()