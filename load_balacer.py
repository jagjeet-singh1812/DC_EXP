import random

# --- Round Robin Load Balancer ---
class RR:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server


# --- Least Connections Load Balancer ---
class LC:
    def __init__(self, connections):
        self.connections = connections

    def get(self):
        server = min(self.connections, key=self.connections.get)
        self.connections[server] += 1
        return server

    def release(self, server):
        if self.connections[server] > 0:
            self.connections[server] -= 1


# --- Least Time Load Balancer ---
class LT:
    def __init__(self, times):
        self.times = times

    def get(self):
        server = min(self.times, key=self.times.get)
        self.times[server] += random.uniform(0.05, 0.2)
        return server


# --- Hash Based Load Balancer ---
def hash_lb(client_id, servers):
    return servers[hash(client_id) % len(servers)]


# --- Main Simulation ---
def main():
    print("Load Balancing Algorithms:")
    print("1: Round Robin (RR)")
    print("2: Least Connections (LC)")
    print("3: Least Time (LT)")
    print("4: Hash Based")
    
    choice = input("Choose algorithm (1-4): ")
    n = int(input("Number of servers: "))
    servers = [input(f"Server {i+1} name: ") for i in range(n)]

    if choice == '1':  # Round Robin
        r = int(input("Number of requests: "))
        obj = RR(servers)
        print("\n--- Round Robin Allocation ---")
        for i in range(r):
            print(f"Request {i+1} → {obj.get()}")

    elif choice == '2':  # Least Connections
        conn = {s: int(input(f"Initial connections on {s}: ")) for s in servers}
        r = int(input("Number of incoming requests: "))
        obj = LC(conn)
        print("\n--- Least Connections Allocation ---")
        for i in range(r):
            s = obj.get()
            print(f"Request {i+1} → {s}")
            if random.random() > 0.5:
                obj.release(s)
                print(f"[Release] One connection from {s} closed.")

    elif choice == '3':  # Least Time
        times = {s: float(input(f"Response time of {s} (in sec): ")) for s in servers}
        r = int(input("Number of requests: "))
        obj = LT(times)
        print("\n--- Least Time Allocation ---")
        for i in range(r):
            print(f"Request {i+1} → {obj.get()}")

    elif choice == '4':  # Hash-Based
        r = int(input("Number of client requests: "))
        client_ids = [input(f"Client ID {i+1}: ") for i in range(r)]
        print("\n--- Hash-Based Allocation ---")
        for cid in client_ids:
            print(f"Client {cid} → {hash_lb(cid, servers)}")

    else:
        print("❌ Invalid choice!")


# Run the simulation
if __name__ == "__main__":
    main()
