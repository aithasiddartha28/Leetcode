class Solution:
    def processStr(self, s: str) -> str:
        st=[]
        for i in s:
            if i.isalpha():
                st.append(i)
            elif i=="*":
                if st:
                    st.pop()
            elif i=="#":
                st.extend(st)
            elif i=="%":
                st.reverse()
        return "".join(st)