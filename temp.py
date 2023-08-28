def temp():
    temperature_in_celsius = input('What is the temperature in Celsius? ')

    temperature_in_fahrenheit: float = (float(temperature_in_celsius) * 1.8) + 32

    print(f'{temperature_in_celsius} degree celsius is equivalent to {temperature_in_fahrenheit} degrees fahrenheit.')

