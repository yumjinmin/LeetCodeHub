class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 단어 문자가 아닌 모든 문자 공백으로 치환
        words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
        
        # counts = collections.Counter(words)
        # return counts.most_common(1)[0][0]

        counts = collections.defaultdict(int) # 존재하지 않는 키일 때 자동으로 기본값 (int) 설정
        for word in words:
            counts[word] += 1
        return max(counts, key=counts.get) # defualtdict인 counts의 value를 기준으로 최대값 구함