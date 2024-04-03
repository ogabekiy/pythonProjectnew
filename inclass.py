# def base_to_binary(n:int):
#     result=""
#     while n!=0:
#         result += f"{n % 2}"
#         n //= 2
#     return result[::-1]
#
#
# a = input()
# s = ""
# for i in a:
#     if i.isdigit():
#         s+=i
#     else:
#         s+=" "
# l = s.split()
# ll=list()
# for i in l:
#     ll.append(int(i))
# ll.sort()
# lk = ll[::-1]
# res=""
# for i in lk:
#     res+=str(i)
#     res+=" "



# inp = input()
# result,tmp = "",""
# for i in range(len(inp)):
#     if inp.isdigit():
#         tmp +== inp[i]
#     else:
#         if tmp != '':
#             result += base_to_binary(tmp)


class Developer():
    def __init__(self,surname,position,salary):
        self.salary = salary
        self.position = position
        self.surname = surname



class SoftwareEngineer(Developer):
    def __init__(self,bonus,department):
        super(). __init__()
        self.department = department
        self.bonus = bonus




















