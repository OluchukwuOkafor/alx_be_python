# main_temp_conversion.py
from temp_conversion_tool import convert_to_celsius, convert_to_fahrenheit

def main():
    try:
        # Ask user for temperature
        temp = float(input("Enter the temperature to convert: "))
        # Ask user for unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Determine which conversion to perform
        if unit == "C":
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted}°F")
        elif unit == "F":
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}°C")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
