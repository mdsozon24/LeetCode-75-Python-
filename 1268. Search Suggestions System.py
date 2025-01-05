class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        for i in range(1,len(searchWord)+1):
            crr = []
            for j in range(len(products)):
                if searchWord[:i] == products[j][:i]:
                    crr.append(products[j])
                if len(crr)>=3:
                    break
            ans.append(crr)
        return ans