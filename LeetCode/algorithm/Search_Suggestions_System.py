class Node:
    
    def __init__(self):
        self.wordMap: dict[str, Node] = {}
        self.fullWord = ''

    def findWords(self, cnt: int) -> List[str]:
        answer = []
        for k, v in sorted(self.wordMap.items()):
            if v.fullWord:
                answer.append(v.fullWord)
            answer.extend(v.findWords(cnt - len(answer)))
            if len(answer) >= cnt:
                break
        return answer[:cnt]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Node()
        for p in products:
            node = root
            for c in p:
                if c in node.wordMap:
                    node = node.wordMap[c]
                else:
                    child = Node()
                    node.wordMap[c] = child
                    node = child
            node.fullWord = p

        answer = [[] for _ in range(len(searchWord))]
        node = root
        for i, c in enumerate(searchWord):
            if c not in node.wordMap:
                return answer
            node = node.wordMap[c]
            sugCnt = 0
            if node.fullWord:
                answer[i].append(node.fullWord)
                sugCnt += 1
            answer[i].extend(node.findWords(3 - sugCnt))

        return answer