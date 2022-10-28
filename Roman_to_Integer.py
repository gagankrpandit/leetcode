import re

class Solution:
    def romanToInt(self, s: str) -> int:
        dict_ = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        try:
            if re.split(r'IV|CM|IX|XL|XC|CD', s):
                split = re.split(r'IV|CM|IX|XL|XC|CD', s)
                int_ = 0
                for i in range(len(split)):
                    if len(split[i]) == 1:
                        int_ = int_ + dict_[split[i]]
                    elif len(split[i]) > 1:
                        split_2 = list(split[i])
                        for i in range(len(split_2)):
                            int_ = int_ + dict_[split_2[i]]

                match_ = re.findall(r'IV|CM|IX|XL|XC|CD', s)
                for i in range(len(match_)):
                    int_ = int_ + dict_[match_[i]]
                return int_
        except:
            split_ = list(s)
            int_ = 0
            for i in range(len(split_)):
                int_ = int_ + dict_[split_[i]]
            return int_
