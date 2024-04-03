head = [1,2,6,3,4,5,6]
val = 6

s = list()
i = 0
while i != len(head):
    if head[i] != val:
        s.append(head[i])
    i += 1

print(s)
# s = list()
#         i = 0
#         while i != len(head):
#             if head[i] != val:
#                 s.append(head[i])
#             i += 1
#         return s