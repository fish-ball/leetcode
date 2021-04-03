class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum([(k+1)*((v-1)//(k+1)+1) for k, v in Counter(answers).items()])
