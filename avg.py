# skew likh dena bas inse add
def input_time(prompt):
   tim = input(prompt)
   h, m = map(int, tim.split(':'))
   return h * 60 + m




def convt(min):
   return f"{min // 60:02d}:{min % 60:02d}"




n = int(input("Enter the number of nodes: "))


nodes = []
for i in range(n):
   t = input_time(f"Enter time for {i + 1} node :")
   nodes.append(t)


avg = (sum(nodes)) // n
print(f"Average time is :{convt(avg)}")


print("Time Difference :")
td = []
for i in range(n):
   print(f"node {i}: {avg - nodes[i]} mins")
   td.append(avg - nodes[i])


print("Sync: ")


for i in range(n):
   nodes[i] = nodes[i] + td[i]
   print(f"node {i}: {convt(nodes[i])}")


