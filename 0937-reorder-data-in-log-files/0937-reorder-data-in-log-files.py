class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit(): # log.splict()[1]: 식별자 다음에 오는 word
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        # 식별자 제외한 문자열을 키로 하여 정렬한 후
        # 동일한 경우 식별자로 정렬함

        return letters + digits