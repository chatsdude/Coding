 st = []
        d = {"(": ")"}
        ct = 0
        for char in S:
            # Opening parenthesis: Add it to the stack
            if char in d:
                st.append(char)
            else:
                # Closing parenthesis: Pop opening parenthesis from stack if stack has elements
                # Else, if the stack is empty we need to add a closing parenthesis here to make it valid so increment ct
                if st:
                    st.pop()
                else:
                    ct += 1
        
        # Return the number of closing parenthesis needed + number of opening parenthesis that couldn't be closed
        return ct + len(st)
