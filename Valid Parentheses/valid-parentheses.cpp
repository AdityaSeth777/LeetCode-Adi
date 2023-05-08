class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(auto i:s)
        {
            // if element is open parantheses, push it in stack
            if(i=='(' or i=='{' or i=='[')
            st.push(i);
            else
            {
                // checking if top element is opening parantheses
                // of same kind as closing parantheses
                if(st.empty() or (st.top()=='(' and i!=')') or (st.top()=='{' and i!='}') or (st.top()=='[' and i!=']')) return false;
                st.pop();
            }
        }
        // If the stack is not empty,that is there is an opening 
        // parentheses without a corresponding closing parentheses and we can return False, else return true.
        return st.empty();
    }
};