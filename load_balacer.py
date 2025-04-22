import random

# --- Round Robin ---
class RR:
    def __init__(self, svrs): 
        self.svrs, self.i = svrs, 0
    def get(self):
        s = self.svrs[self.i]
        self.i = (self.i + 1) % len(self.svrs)
        return s

# --- Least Connections ---
class LC:
    def __init__(self, conns): 
        self.c = conns

    def get(self):
        s = min(self.c, key=self.c.get)
        self.c[s] += 1
        return s
    def release(self, s):
        if self.c[s] > 0: self.c[s] -= 1

# --- Least Time ---
class LT:
    def __init__(self, times): self.t = times
    def get(self):
        s = min(self.t, key=self.t.get)
        self.t[s] += random.uniform(0.05, 0.2)
        return s

# --- Hash Based ---
def hash_lb(cid, svrs): return svrs[hash(cid) % len(svrs)]

# --- Main ---
def main():
    print("1: RR\n2: LC\n3: LT\n4: Hash")
    ch = input("Choose (1-4): ")
    n = int(input("No. of servers: "))
    svrs = [input(f"Server {i+1}: ") for i in range(n)]

    if ch == '1':
        r = int(input("Requests: "))
        obj = RR(svrs)
        print("\n-- RR --")
        for i in range(r): print(f"Req {i+1} → {obj.get()}")

    elif ch == '2':
        conn = {s: int(input(f"Connections for {s}: ")) for s in svrs}
        r = int(input("Requests: "))
        obj = LC(conn)
        print("\n-- LC --")
        for i in range(r):
            s = obj.get()
            print(f"Req {i+1} → {s}")
            if random.random() > 0.5: obj.release(s)

    elif ch == '3':
        t = {s: float(input(f"Time for {s}: ")) for s in svrs}
        r = int(input("Requests: "))
        obj = LT(t)
        print("\n-- LT --")
        for i in range(r): print(f"Req {i+1} → {obj.get()}")

    elif ch == '4':
        r = int(input("Client requests: "))
        cids = [input(f"Client ID {i+1}: ") for i in range(r)]
        print("\n-- Hash --")
        for cid in cids: print(f"{cid} → {hash_lb(cid, svrs)}")

    else: print("Invalid choice!")

main()