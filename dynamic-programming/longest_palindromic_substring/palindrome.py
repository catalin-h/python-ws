import unittest

def max_palindrome(string: str) -> int:
    def palindrome(left: int, right: int):
        while left >= 0 and right < N and  string[left] == string[right]:
            left -= 1
            right += 1

        # rollback one unit
        left += 1
        right -= 1

        # slice format is [start: end: step] but actually is the subarray [start, end-1]
        return string[left:right+1]

    def max_string(lhs: str, rhs: str) -> str:
        if len(lhs) > len(rhs):
            return lhs
        return rhs

    ans = ''
    size = 0

    N = len(string)

    for center in range(N):
        # get odd palidrome
        ans = max_string(ans, palindrome(center, center))
        # get even palidrome
        ans = max_string(ans, palindrome(center, center + 1))

    return ans

def max_palindrome_manacher(s: str) -> str:
    def unpadded_size(s: str):
        if not s:
            return 0  
        if s[0] == '@':
            return (len(s) - 1) // 2
        return (len(s) + 1) // 2
    
    s = s.replace('','@')

    last_right = 0
    last_center = 0
    best = ''
    radius = [0] * len(s)

    for center in range(len(s)):
        if center <= last_right:
            rad = center - last_right
            mirror_center = last_right - rad

            # the mirror center radius may be 0 which means there is no
            # palindrome at current center other than self item
            radius[center] = min(radius[mirror_center], last_right - center)
        else:
            radius[center] = 1
        
        left = center - radius[center]
        right = center + radius[center]

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            radius[center] += 1

        left += 1
        right -= 1
        radius[center] -= 1

        p = s[left: right + 1]

        if unpadded_size(best) < unpadded_size(p):
            best = p

        # Note: best known palindrome is not related
        # to last palidrome center and right
        if last_right < right:
            last_right = right
            last_right = center

    return best.replace('@', '')

class TestPal(unittest.TestCase):
    def test(self):
        self.assertEqual(max_palindrome('12minim12'), 'minim')
        self.assertEqual(max_palindrome('12level'), 'level')
        self.assertEqual(max_palindrome('12abba'), 'abba')
        self.assertEqual(max_palindrome_manacher('12minim12'), 'minim')
        self.assertEqual(max_palindrome_manacher('12level'), 'level')
        self.assertEqual(max_palindrome_manacher('12abba'), 'abba')

if __name__ == "__main__":
    unittest.main()