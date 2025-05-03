class Solution:
    def maximumSwap(self, num: int) -> int:
        def solve(num_list, k, index):
            nonlocal max_num
            if k == 0 or index == len(num_list):
                return

            max_digit = max(num_list[index:])

            if num_list[index] != max_digit:
                for i in range(len(num_list) - 1, index - 1, -1):
                    if num_list[i] == max_digit:
                        num_list[index], num_list[i] = num_list[i], num_list[index]
                        curr_num = int(''.join(num_list))
                        max_num = max(max_num, curr_num)
                        solve(num_list, k - 1, index + 1)
                        num_list[index], num_list[i] = num_list[i], num_list[index]
            else:
                solve(num_list, k, index + 1)

        num_list = list(str(num))
        max_num = num
        solve(num_list, 1, 0)
        return max_num