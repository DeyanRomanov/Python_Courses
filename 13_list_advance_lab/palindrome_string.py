words = input().split()
searched_polindrome = input()

polindrome = [word for word in words if word == word[::-1]]

print(polindrome)

print(f'Found palindrome {polindrome.count(searched_polindrome)} times')
