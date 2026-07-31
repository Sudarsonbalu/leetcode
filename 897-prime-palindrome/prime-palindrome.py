class Solution(object):
    def primePalindrome(self, n):
        def is_prime(num):
            if num < 2: 
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        if 8 <= n <= 11:
            return 11
        while True:
            s = str(n)
            if len(s) % 2 == 0:
                n = 10 ** len(s)
                continue
            if s == s[::-1]:
                if is_prime(n):
                    return n
            n += 1