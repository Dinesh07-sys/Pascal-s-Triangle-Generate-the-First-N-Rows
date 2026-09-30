class Solution:
    def generateFromList(self, input_values: list[int]) -> list[list[int]]:
        return self.generate(input_values[0])
    def generate(self, numRows: int) -> list[list[int]]:
        triangle: list[list[int]] = []
        for row in range(numRows):
            current: list[int] = [1] * (row + 1)
            for col in range(1, row):
                current[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
            triangle.append(current)
        return triangle
def main() -> None:
    numRows: int = 8
    sol: Solution = Solution()
    print(sol.generate(numRows))
if __name__ == "__main__":
    main()