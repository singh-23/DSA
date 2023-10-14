class Solution:
    def longestPalin(self, s):  # aaaabbaa
        i = 1;  # 01234567
        ans = ''
        while i < len(s):
            tmp = ''
            if (s[i] == s[i - 1]):
                j = i;
                k = i - 1;
                while (j < len(s) and k >= 0):
                    if (s[j] == s[k]):
                        tmp = s[k] + tmp + s[j];
                        j = j + 1;
                        k = k - 1;
                    else:
                        break;

                if (len(tmp) > len(ans)):
                    ans = tmp;
            i += 1;

        i = 1;

        while i < len(s):
            tmp = ''
            if (i + 1 < len(s) and i - 1 >= 0 and (s[i + 1] == s[i - 1])):
                tmp = tmp + s[i];
                j = i + 1;
                k = i - 1;
                while (j < len(s) and k >= 0):
                    if (s[j] == s[k]):
                        tmp = s[k] + tmp + s[j];
                        j = j + 1;
                        k = k - 1;
                    else:
                        break;

                if (len(tmp) > len(ans)):
                    ans = tmp;
            i += 1;
        if (len(ans) == 0):
            return str(s[0])

        return ans;