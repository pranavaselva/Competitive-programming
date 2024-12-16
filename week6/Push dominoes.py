class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        domino = list(dominoes)
        length = len(domino)
        array = [0]*length
        force = 0
        for i in range(0, length):
            if domino[i] == 'R':
                force = length
            elif domino[i] == 'L':
                force = 0
            else:
                force = max(force-1, 0)
            array[i] += force

        force = 0
        for i in range(length-1, -1, -1):
            if domino[i] == 'L':
                force = length
            elif domino[i] == 'R':
                force = 0
            else:
                force = max(force-1, 0)
            array[i] -= force

        result = []
        for i in array:
            if i > 0:
                result.append('R')
            elif i < 0:
                result.append('L')
            else:
                result.append('.')
        
        return ''.join(result)