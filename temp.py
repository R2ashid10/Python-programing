def convert(fahrenheit):
    return (5/9) * (fahrenheit - 32)

def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = convert(fahrenheit)
    print(f"Temperature in Celsius: {celsius:.2f}")
    
    if celsius > 20:
        print("IT'S HOT HERE")
    else:
        print("IT'S COLD HERE")


main()
