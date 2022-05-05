""" 05-02-2022  Leetcode 844. Backspace String Compare"""

s = "#"
t = "#a#c"

s_list = list(s)
t_list = list(t)

i = 0
while s_list and i < len(s_list):
    if s_list[0] == "#":
        s_list = s_list[1:]
        continue
    if s_list[i] == "#":
        s_list = s_list[: i - 1] + (s_list[i + 1 :] if i < len(s_list) - 1 else [])
        i -= 2
    i += 1

i = 0
while t_list and i < len(t_list):
    if t_list[0] == "#":
        t_list = t_list[1:]
        continue
    if t_list[i] == "#":
        t_list = t_list[: i - 1] + (t_list[i + 1 :] if i < len(t_list) - 1 else [])
        i -= 2
    i += 1
print(s_list == t_list)
# return s_list == t_list
