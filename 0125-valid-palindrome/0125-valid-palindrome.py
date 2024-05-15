
# 풀이2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        
        for char in s:
            if char.isalnum(): # isalnum(): 영문자, 숫자 여부 판별
                strs.append(char.lower())

        # 판별
        while len(strs) > 1: # strs 문자가 1개 이하로 남을 때까지 반복
            if strs.popleft() != strs.pop():
                return False
        return True

'''
# 풀이1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # isalnum(): 영문자, 숫자 여부 판별
                strs.append(char.lower())

        # 판별
        while len(strs) > 1: # strs 문자가 1개 이하로 남을 때까지 반복
            if strs.pop(0) != strs.pop():
                return False
        return True
'''   