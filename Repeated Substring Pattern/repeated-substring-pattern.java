class Solution {
    public static boolean repeatedSubstringPattern(String s) {
        String str = s + s;
        String str1 = str.substring(1, str.length() - 1);
        return str1.contains(s);
    }
}