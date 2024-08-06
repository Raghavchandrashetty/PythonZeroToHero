class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 0
        d = {}
        pntr = 0
        incrementFlag = True
        while i < len(s):
            # print("&&&&&       i value : ", i)
            # print("Pointer before assignment ", pntr)

            if pntr in d:
                d[pntr].append(s[i])
            else:
                d[pntr] = [s[i]]

            if pntr == numRows - 1:
                incrementFlag = False
            if pntr == 0:
                incrementFlag = True
            i += 1

            if incrementFlag:
                pntr += 1
            else:
                pntr -= 1

            # print("Pointer after assignment ", pntr)
            result = ''
            for key in sorted(d.keys()):
                result += ''.join(d[key])

        return result

convert("PAYPALISHIRING", 3 )