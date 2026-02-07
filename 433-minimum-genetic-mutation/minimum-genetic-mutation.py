class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        visited = set()
        queue = collections.deque([(startGene, 0)])

        possible_chars = "ACGT"

        while queue:
            curr, steps = queue.popleft()

            if curr == endGene:
                return steps
            

            for i in range(len(curr)):
                original_char = curr[i]

                for char in possible_chars:
                    if original_char == char: continue

                    mutation = curr[:i] + char + curr[i+1:]

                    if mutation in bank and mutation not in visited:
                        visited.add(mutation)
                        queue.append((mutation, steps+1))

        return -1


