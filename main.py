def binarytodecimal():
    binary_num = input('Enter a binary number:')
    dec_num = int(binary_num, 2)
    return dec_num
def decimaltobinary():
    dec_num = int(input('Enter a decimal number:'))
    binary_num= bin(dec_num).replace('0b', '')
    return binary_num
num = int(input('Enter 1 for Binary to decimal conversion Enter 2 for Decimal to Binary conversion: \n'))
if num == 1:
      print('Decimal: ',num ,':', binarytodecimal())
elif num == 2:
      print('Binary:' , decimaltobinary())
else:
      print('Invalid choice')