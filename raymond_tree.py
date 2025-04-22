class Process:
   def __init__(self, pid):
       self.pid = pid
       self.par = None
       self.has_token = False
       self.queue = []
       self.in_cs = False


   def request_cs(self):
       print(f"\n[Process {self.pid}] Requesting critical section...")
       if not self.has_token:
           print(f"[Process {self.pid}] Forwarding request to parent {self.par.pid}")
           self.par.receive_request(self)
       else:
           print(f"[Process {self.pid}] Already has token.")
           self.enter_cs()


   def receive_request(self, requester):
       if requester not in self.queue:
           self.queue.append(requester)
           print(f"[Process {self.pid}] Received request from {requester.pid}. Queue: {[p.pid for p in self.queue]}")


       if not self.has_token:
           print(f"[Process {self.pid}] Forwarding request to parent {self.par.pid}")
           self.par.receive_request(self)
       elif not self.in_cs:
           self.send_token()


   def send_token(self):
       if self.queue:
           next_process = self.queue.pop(0)
           print(f"[Process {self.pid}] Sending token to {next_process.pid}")
           self.has_token = False


           next_process.receive_token()
           next_process.enter_cs()
       else :
           self.par=self


   def receive_token(self):
       self.has_token = True
       print(f"[Process {self.pid}] Received token.")


   def enter_cs(self):
       self.in_cs = True
       print(f"[Process {self.pid}] Entering Critical Section.")
       input("Press Enter to exit CS...")
       self.exit_cs()


   def exit_cs(self):
       self.in_cs = False
       print(f"[Process {self.pid}] Exiting Critical Section.")
       self.send_token()


# Setup Tree
P0 = Process(0)
P1 = Process(1)
P2 = Process(2)
P3 = Process(3)
P4 = Process(4)


n=5


# Set parents to match the tree
P1.par = P0
P2.par = P0
P3.par = P2
P4.par = P2
P0.par = P0  # Root points to itself


# Initial token holder
P0.has_token = True


# Store for easy access
processes = [P0, P1, P2, P3, P4]


# Simulation loop
while True:
   print("\n[Raymond Tree] Choose a process to request CS (0-4) or type 'exit':")
   for p in processes:
       print(f"P{p.pid} -> Parent: P{p.par.pid}, Has Token: {p.has_token}")


   inp = input("Enter PID: ").strip()
   if inp.lower() == 'exit':
       break


   try:
       pid = int(inp)
       if 0 <= pid < len(processes):
           processes[pid].request_cs()
       else:
           print("Invalid PID.")
   except ValueError:
       print("Enter a valid number.")


#
# n = int(input("Enter number of processes: "))
# processes = [Process(i) for i in range(n)]
# for i in range(n):
#     while True:
#         try:
#             par_id = int(input(f"Enter parent PID for P{i} (enter {i} if root): "))
#             if 0 <= par_id < n:
#                 processes[i].par = processes[par_id]
#                 break
#             else:
#                 print("Invalid PID. Try again.")
#         except ValueError:
#             print("Please enter a valid number.")
# token_holder = int(input(f"Enter PID of initial token holder (0 to {n-1}): "))
# processes[token_holder].has_token = True

