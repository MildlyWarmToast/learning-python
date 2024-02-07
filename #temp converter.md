#while true loops the code back if failed
while True:
    tempunit=input('What temperature unit are you converting, C or F?').lower()
    #if converting F to C
    if tempunit == 'f':
        try:
            tempF=float(input('What is the temperature in F'))
            tempC=(tempF-32)*5/9
            print('Temperature in Celsius',tempC)
            break #exits loop if input is converted succefuly
        #if non numeric value given
        except ValueError:
            (print('Please enter a numeric value.'))
    #if converting C to F
    elif tempunit == 'c':
        try:
            tempC=float(input("What is the temperature in celcius"))
            tempF=(tempC*9/5)+32
            print('Temperature in Farenheit',tempF)
            break#exits loop if input is converted succefuly
        #if non numeric value given
        except ValueError:
            print('Please enter a numeric value.')
    #if temp unit given is not C or F
    else:
        print('Invalid temperature unit, please enter C for Celsius or F for Farenheit.')