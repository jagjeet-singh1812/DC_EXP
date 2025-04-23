#this is not actual gda but sir ko yahi chaiye 





#aur maam ko yeh chaiye 
# Function to convert time in HH:MM format to total minutes
def to_min(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

# Function to calculate skew (difference from agreed time)
def calc_skew(curr, agreed):
    return curr - agreed

# Function to adjust time based on skew
def sync_clock(avg, curr):
    abs_avg = abs(avg)
    if avg > 0:
        return curr - abs_avg, "Decrease"  # Decrease clock
    elif avg < 0:
        return curr + abs_avg, "Increase"  # Increase clock
    else:
        return curr, "No change"

# Input for agreed time and number of machines
agreed_time = to_min(input("Enter Agreed Upon Time (HH:MM): "))
n = int(input("Enter number of machines: "))
time_lst = input(f"Enter current time of {n} machines (space-separated HH:MM): ").split()

# Process the current times for each machine
curr_times = {}
for i in range(n):
    curr_times[i+1] = to_min(time_lst[i])

print(f"\nAgreed Upon Time (in minutes): {agreed_time}")

# Initial skew calculation for each machine
initial_skews = []
for i in range(1, n+1):
    skew = calc_skew(curr_times[i], agreed_time)
    initial_skews.append(skew)
    print(f"Machine {i}: Initial Time = {curr_times[i]} minutes, Skew = {skew} minutes")

# Simulate the passing of 5 minutes (add 5 minutes to each machine's time)
for i in range(1, n+1):
    curr_times[i] += 5

# Final skew calculation for each machine after 5 minutes
final_skews = []
for i in range(1, n+1):
    skew = calc_skew(curr_times[i], agreed_time)
    final_skews.append(skew)
    print(f"Machine {i}: Final Time after 5 minutes = {curr_times[i]} minutes, Skew = {skew} minutes")

# Calculate the average skew for each machine and sync the time
for i in range(1, n+1):
    # Calculate average skew for this machine (initial skew and final skew)
    avg_skew = (initial_skews[i-1] + final_skews[i-1]) / 2
    print(f"\nMachine {i}: Average Skew = {avg_skew} minutes")

    # Sync the machine's clock based on its average skew
    new_time, action = sync_clock(avg_skew, curr_times[i])
    print(f"Machine {i}: Current Time = {curr_times[i]} minutes, After Sync: {new_time} minutes, Action: {action}")aa
