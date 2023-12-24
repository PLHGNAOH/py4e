def is_palindrome(num):
    # Hàm kiểm tra số đối xứng
    return str(num) == str(num)[::-1]

def is_perfect_square(num):
    # Hàm kiểm tra số chính phương
    return num > 0 and (int(num ** 0.5))**2 == num

def is_prime(num):
    # Hàm kiểm tra số nguyên tố
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_and_sum_special_numbers(a, b):
    palindrome_count = 0
    palindrome_sum = 0
    square_count = 0
    square_sum = 0
    prime_count = 0
    prime_sum = 0

    for num in range(a, b + 1):
        if is_palindrome(num):
            palindrome_count += 1
            palindrome_sum += num
        if is_perfect_square(num):
            square_count += 1
            square_sum += num
        if is_prime(num):
            prime_count += 1
            prime_sum += num

    print(f"Số đối xứng trong đoạn [{a}, {b}]: {palindrome_count}")
    print(f"Tổng các số đối xứng trong đoạn [{a}, {b}]: {palindrome_sum}")
    print(f"Số chính phương trong đoạn [{a}, {b}]: {square_count}")
    print(f"Tổng các số chính phương trong đoạn [{a}, {b}]: {square_sum}")
    print(f"Số nguyên tố trong đoạn [{a}, {b}]: {prime_count}")
    print(f"Tổng các số nguyên tố trong đoạn [{a}, {b}]: {prime_sum}")

# Nhập vào 2 số nguyên dương a và b (với điều kiện b > a)
a = int(input("Nhập số nguyên dương a: "))
b = int(input(f"Nhập số nguyên dương b (lớn hơn {a}): "))

# Kiểm tra và thực hiện đếm, tính tổng các số đặc biệt trong đoạn [a, b]
count_and_sum_special_numbers(a, b)
