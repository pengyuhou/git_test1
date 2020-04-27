class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if A==C or B==D :
            return (G - E) * (H - F)
        if G==E or H==F:
            return (C - A) * (D - B)
        if E>A and F>B and G<C and H<D:
            return (C - A) * (D - B)
        if E<A and F<B and G>C and H>D:
            return (G - E) * (H - F)
        if E <= C and F <= D and H >= D:
            return (C - A) * (D - B) + (G - E) * (H - F) - (D - F) * (C - E)
        elif E <= C and H >= B and F <= B:
            return (C - A) * (D - B) + (G - E) * (H - F) - (C - E) * (H - B)
        elif G >= A and H >= B and F <= B:
            return (C - A) * (D - B) + (G - E) * (H - F) - (G - A) * (H - B)
        elif G >= A and F <= D and H >= D:
            return (C - A) * (D - B) + (G - E) * (H - F) - (G - A) * (D - F)
        else:
            return (C - A) * (D - B) + (G - E) * (H - F)


print(Solution().computeArea(-2, -2, 2, 2, -1, -1,1, 1))
