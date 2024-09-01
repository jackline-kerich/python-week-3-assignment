def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    # Prompt user for input
    try:
        original_price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)

    # Print result
    print(f"The final price after applying the discount is: ${final_price:.2f}")

if __name__ == "__main__":
    main()
