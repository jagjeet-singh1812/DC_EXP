n = int(input("Enter the number of the sites :"))


request_set = {}
for i in range(1, n + 1):
   lst = []
   for j in range(1, n + 1):
       if i != j:
           lst.append(j)
   request_set[i] = lst


for i, k in request_set.items():
   print(f"{i}:{k}")


required_client = int(input("Enter the number of the sites who want to enter the CS:"))


required_sites = []


for i in range(required_client):
   t, id = map(int, input("Enter t and id for site:").split())
   required_sites.append((t, id))


required_sites.sort()


print(" -----------Request Phase---------------")


for i, id in required_sites:
   for j in request_set[id]:
       print(f"Request Send from {id} to {j}")


pending_task = []
for t, id in required_sites:
   pending_task.append(id)


for t, id in required_sites:
   for i in request_set[id]:
       if i not in pending_task:
           print(f"Reply from {i} to {id}")
       else:
           for peer_timestamp, peer_id in required_sites:
               if peer_id == i and peer_timestamp > t:
                   print(f"Site {i} sends REPLY to Site {id}")
   print(f"\nSite {id} enters the Critical Section")
   x = input("Enter anything to exit CS....")
   print(f"Site {id} exits the Critical Section\n")
   pending_task.remove(id)

