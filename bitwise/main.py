# Operator bitwise

# OR (|)
print('\n==========OR==========')
a = 9
b = 10
c = a | b
print('Nilai', a, 'binary :', format(a, '08b'))
print('Nilai', b, 'binary :', format(b, '08b'))
print('----------------------------(|)')
print('Nilai', c, 'binary :', format(c, '08b'))

# AND (&)
print('\n===========AND==========')
c = a & b
print('Nilai', a, 'binary :', format(a, '08b'))
print('Nilai', b, 'binary :', format(b, '08b'))
print('----------------------------(&)')
print('Nilai', c, 'binary :', format(c, '08b'))

# XOR (^)
print('\n==========XOR==========')
c = a ^ b
print('Nilai', a, 'binary :', format(a, '08b'))
print('Nilai', b, 'binary :', format(b, '08b'))
print('----------------------------(^)')
print('Nilai', c, 'binary :', format(c, '08b'))

# NOT (~)
print('\n==========NOT==========')
c = ~a
print('----------------------------(~)')
print('Nilai', c, 'binary :', format(c & 0xFF, '08b'))

# Shifting

# Shifting right
print('\n===========>>==========')
c = a >> 1
print('Nilai', a, 'binary :', format(a, '08b'))
print('----------------------------(>>)')
print('Nilai', c, 'binary :', format(c, '08b'))


# Shifting left
print('\n===========<<==========')
c = a << 1
print('Nilai', a, 'binary :', format(a, '08b'))
print('----------------------------(<<)')
print('Nilai', c, 'binary :', format(c, '08b'))