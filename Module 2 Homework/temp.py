

if __name__ == '__main__':
    #Converts from Celsius to Fahrenheit
    Celsius = float(input('What degree is it in Celsius?'))
    Fahrenheit = round(Celsius / 5 * 9 + 32, 2)
    print(f'The degree in Fahrenheit is {Fahrenheit}')