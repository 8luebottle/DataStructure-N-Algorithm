# Use two lists : arabic & roman (pair with index)

def intToRoman(num):
    arabic   = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman    = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']   
    romanized= ''

    for idx in range(0, len(arabic)):
        while num >= arabic[idx]:
            num       -= arabic[idx]
            romanized += roman[idx]
    return romanized
