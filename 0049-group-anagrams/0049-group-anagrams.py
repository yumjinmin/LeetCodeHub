class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list) # 존재하지 않는 키 삽입 시 에러나지 않도록 함

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            # key: ''.join(sorted(word))
            # value: word
        return list(anagrams.values())