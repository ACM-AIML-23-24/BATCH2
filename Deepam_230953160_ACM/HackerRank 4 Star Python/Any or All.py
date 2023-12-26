def palindrome(n):
    n_list = list(str(n))
    return (str.join('', n_list) == str.join('', reversed(n_list)))

input()
numbers = list(map(int, input().split()))

is_palindrome = [palindrome(x) for x in numbers]
is_positive = [x >= 0 for x in numbers]

print(all(is_positive) and any(is_palindrome))