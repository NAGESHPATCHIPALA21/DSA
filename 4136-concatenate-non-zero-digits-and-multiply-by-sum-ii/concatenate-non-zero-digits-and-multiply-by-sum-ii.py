class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:


        prefix = [0]
        sprefix = [0]
        size = [0]
        sm = 0
        num = 0
        st = 0
        for i in range(len(s)):
            if s[i] != "0":
                st += 1
                sm += int(s[i])
                sm = sm % (10 ** 9 + 7)
                # print(num, (10), st)
                num *= (10 )
                # print(num)
                num += int(s[i])
                # print(num)
            prefix.append(sm)
            size.append(st)
            num %= (10 ** 9 + 7)
            sprefix.append(num)
        
        # print(prefix)
        # print(sprefix)
        # print(size)

        ans = []
        for i, j in queries:
            
            sm = prefix[j + 1] - prefix[i]
            tmp = size[j + 1] - size[i]
            # print(tmp, sprefix[i])
            tm = sprefix[j + 1] - (sprefix[i] * pow(10, tmp, (10 ** 9 + 7))) 
            # print(tm, sprefix[j + 1], (sprefix[i] * 10 ** tmp))
            ans.append(tm * sm % (10 ** 9 + 7))

        return (ans)





































        # tree = [""] * (len(s) * 4)

        # def build(node, l, r):

        #     if l == r:
        #         if l < len(s):
        #             if s[l] != "0":
        #                 # print(l, node)
        #                 tree[node] = [s[l]]
        #                 return [s[l]]
        #             else:
        #                 tree[node] = [""]
        #                 return [""]
        #         else:
        #             tree[node] = [""]
        #             return [""]

        #     mid = (l + r) // 2

        #     left = build(node * 2, l, mid)
        #     right = build(node * 2 + 1, mid + 1, r)

        #     tree[node] = left + right

        #     return tree[node]

        # (build(1, 0, len(s)))

        # # print(tree)        


        # def search(node, l, r, l1, r1):

        #     if l == l1 and r == r1:
        #         return tree[node]
             
        #     mid = (l + r) // 2

        #     left = []
        #     if l1 <= mid:
        #         left = search(node * 2, l, mid, max(l, l1), min(mid, r1))
            
        #     # print(left)
            

        #     right = []
        #     if r1 >= mid + 1:
        #         # print(mid + 1, r, l1, r1)
        #         right = search(node * 2 + 1, mid + 1, r, max(mid + 1, l1), min(r1, r))

        #     # if left:
        #     #     left = "".join(left)
        #     #     left = int(left)
        #     #     left = left % (10 ** 9 + 7)
            
        #     # if right:
        #     #     right = "".join(right)
        #     #     right = int(right)
        #     #     right = right % (10 ** 9 + 7)

        #     # group = str(left) + str(right)

        #     group = left + right

        #     return group
    
        # ans = []
        # for i, j in queries:
        #     arr = (search(1, 0, len(s), i, j))
        #     # print(arr)
        #     nw = "".join(arr)
        #     num = 0
        #     if nw:
        #         num = int(nw)
        #     # print(num)
        #     sm = 0
        #     for i in arr:
        #         if not i: continue
        #         sm += int(i)
        #     ans.append(((sm * num) % (10 ** 9 + 7)))

        # # print( * sum(arr))

        # return ans