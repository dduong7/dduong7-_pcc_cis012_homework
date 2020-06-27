

if __name__ == '__main__':
    hours = float(input('How many hours did you work?'))
    rate = float(input('How much is your rate per hour?'))
    #To calculate the gross hours you multiple hours x rate
    gross_pay = hours*rate

    print(f'The gross pay is ${gross_pay}')