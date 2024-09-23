"""Temperature conversion program."""

def celsius_to_fahrenheit(celsius):
    """Converting celsius to fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converting fahrenheit to celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    celsius = float(input("Enter Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius is {fahrenheit:.2f} Fahrenheit")

    fahrenheit = float(input("Enter Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit is {celsius:.2f} Celsius")

main()
