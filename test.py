def binary(num):
    if num < 2:
        return f'{num % 2}'
    return f'{num % 2}{binary(num // 2)}'

print(binary(6))