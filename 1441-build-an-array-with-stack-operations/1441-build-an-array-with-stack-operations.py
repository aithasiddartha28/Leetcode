class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        st=[]
        for i in range(1,n+1):
            if i in target:
                st.append("Push")
                if i==target[-1]:
                    break
            else:
                st.append("Push")
                st.append("Pop")
                
        return st