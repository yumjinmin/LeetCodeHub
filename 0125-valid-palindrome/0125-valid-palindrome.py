# 풀이3 정규표현식 + 슬라이싱
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1] # 슬라이싱

'''
# 풀이2 데크 자료형을 이용한 최적화
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        # strs: Deque = deque()는 strs를 deque 타입의 빈 데크로 초기화
        # Deque는 양쪽 끝에서의 빠른 추가와 삭제를 지원하는 자료구조
        
        for char in s:
            if char.isalnum(): # isalnum(): 영문자, 숫자 여부 판별
                strs.append(char.lower())
				
        # 판별
        while len(strs) > 1: # strs 문자가 1개 이하로 남을 때까지 반복
            if strs.popleft() != strs.pop():
            # 데크: 양방향 연결 리스트로 구현되어 있어 포인터만 조정하면 되므로
            # popleft()의 시간 복잡도는 O(1)
                return False
        return True

# 풀이1 리스트로 변환
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # isalnum(): 영문자, 숫자 여부 판별
                strs.append(char.lower())

        # 판별
        while len(strs) > 1: # strs 문자가 1개 이하로 남을 때까지 반복
            if strs.pop(0) != strs.pop():
            # 리스트: 첫 번째 요소를 제거하려면 모든 요소를 이동시켜야 하므로
            # pop(0)의 시간 복잡도는 O(n)
                return False
        return True
'''