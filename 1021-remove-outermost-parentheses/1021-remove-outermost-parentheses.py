class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st=[]
        d=0
        for i in s:
            if i=="(" :
                if d>0:
                    st.append(i)
                d+=1
            elif  i==")":
                d-=1
                if d>0:
                   st.append(i)
        return "".join(st)
