n = int(input().strip()) # stri odstraní mezery, taby a tak před i za

if n % 2 == 1 or n in range(5,21):
    print('Weird')
else:
    print('Not Weird')