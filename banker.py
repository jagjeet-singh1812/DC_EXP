class Process:
    def __init__(self, pid, alloc, max_):  
        self.id = pid
        self.alloc = alloc
        self.max = max_
        self.need = [max_[i] - alloc[i] for i in range(len(max_))]
        self.done = False




# class Process:
#     def __init__(self,pid,alloc,max):
#         self.pid=pid
#         self.alloc=alloc
#         self.max=max
#         self.need=[max[i]-alloc[i] for i in range(len(max))]
#         self.done =False
       
def issafe(avail,need):
    for i in range(len(need)):
        if need[i]>avail[i]:
            return False
    return True


def is_safe(avail, need):
    for i in range(len(need)):
        if need[i] > avail[i]:
            return False
    return True


def bankers(avail, procs):
    seq = []
    count = 0
    print("\n--- Starting Banker's Algorithm Simulation ---\n")
    while count < len(procs):
        ran = False
        for p in procs:
            if not p.done:
                print(f"Checking P{p.id}: Need = {p.need}, Available = {avail}")
                if is_safe(avail, p.need):
                    print(f"--> P{p.id} can run. Allocated: {p.alloc}")
                    for i in range(len(avail)):
                        avail[i] += p.alloc[i]
                    p.done = True
                    seq.append(f'P{p.id}')
                    count += 1
                    print(f"--> P{p.id} finished. Resources released: {p.alloc}")
                    print(f"--> New Available = {avail}\n")
                    ran = True
                    break
                else:
                    print(f"--> P{p.id} cannot run now.\n")
        if not ran:
            print("No further process can safely execute. System is not in a safe state.\n")
            break
    if count == len(procs):
        print("System is in a safe state.")
        print("Safe Sequence:", ' → '.join(seq))
    else:
        print("System is not in a safe state.")


n = 3
res = [10, 5, 7]
procs = [
    Process(0, [0, 1, 0], [7, 5, 3]),
    Process(1, [2, 0, 0], [3, 2, 2]),
    Process(2, [3, 0, 2], [9, 0, 2]),
    Process(3, [2, 1, 1], [2, 2, 2]),
    Process(4, [0, 0, 2], [4, 3, 3])
]
avail = [0] * n
for i in range(n):
    total = sum(p.alloc[i] for p in procs)
    avail[i] = res[i] - total


bankers(avail, procs)
