import os

#FCFS Algorithm
def fcfs():
    while True:
        try:
            num_processes = int(input("Enter the number of processes (0 to 10): "))
            if 0 <= num_processes <= 10:
                break
            else:
                print("Invalid input. Number of processes should be between 0 and 10.")
                continue
        except ValueError:
                print("Invalid input! Please enter a valid number for process number.")
    if num_processes == 0:
        print("No processes to calculate. Exiting program.")
    else:
        processes = {}

        for i in range(1, num_processes + 1):
            while True:
                try:
                    arrival_time = int(input(f"Enter arrival time for process {i} (0 to 15): "))
                    if 0 <= arrival_time <= 15:
                        break
                    else:
                        print("Invalid input! Please enter a number between 0 and 15.")
                except ValueError:
                    print("Invalid input! Please enter a valid number for arrival time.")

            while True:
                try:
                    burst_time = int(input(f"Enter burst time for process {i} (1 to 15): "))
                    if 1 <= burst_time <= 15:
                        break
                    else:
                        print("Invalid input! Please enter a number between 1 and 15.")
                except ValueError:
                    print("Invalid input! Please enter a valid number for burst time.")

            processes[f"P{i}"] = {
                'burst_time': burst_time,
                'arrival_time': arrival_time,
                'end_time': 0,
                'turnaround_time': 0,
                'waiting_time': 0
            }
        current_time = 0
        total_burst_time = 0
        total_turnaround_time = 0
        total_waiting_time = 0

        for process in sorted(processes, key=lambda x: processes[x]['arrival_time']):
            start_time = max(current_time, processes[process]['arrival_time'])
            end_time = start_time + processes[process]['burst_time']

            processes[process]['end_time'] = end_time
            processes[process]['turnaround_time'] = end_time - processes[process]['arrival_time']
            processes[process]['waiting_time'] = start_time - processes[process]['arrival_time']

            total_burst_time += processes[process]['burst_time']
            total_turnaround_time += processes[process]['turnaround_time']
            total_waiting_time += max(0, processes[process]['waiting_time'])

            current_time = end_time

        cpu_utilization = (total_burst_time / current_time) * 100
        num_processes = len(processes)
        avg_turnaround_time = total_turnaround_time / num_processes
        avg_waiting_time = total_waiting_time / num_processes

        label = f"{'-'*79}\n|{'Process':^15}|{'Arrival Time':^11}|{'Burst Time':^9}|{'End Time':^7}|{'Turnaround Time':^14}|{'Waiting Time':^11}|\n{'-'*79}\n"
        contents = f"\n{'-'*79}\n".join([f"|{process:^15}|{processes[process]['arrival_time']:^12}|{processes[process]['burst_time']:^10}|{processes[process]['end_time']:^8}|{processes[process]['turnaround_time']:^15}|{processes[process]['waiting_time']:^12}|" for process in sorted(processes, key=lambda x: processes[x]['arrival_time'])]) + f"\n{'-'*79}\n" 
        print(label + contents)

        P_NAMES = " "
        BAR = "|"
        START = ""

        timings = 0

        for process in sorted(processes, key=lambda x: processes[x]['arrival_time']):
            arrival_time = processes[process]['arrival_time']
            burst_timing = processes[process]['burst_time']
            end_time = processes[process]['end_time']

            this_BAR = ""
            this_name = str(process)
            this_time = str(timings)
            if arrival_time > timings:
                idle_timing = arrival_time - timings
                this_BAR += '+' * idle_timing

                timings += idle_timing
            this_BAR += '-' * burst_timing

            length = max(len(this_BAR) + 1, len(this_name) + 1, len(this_time) + 2)

            # BAR still has a "|" to add.
            if len(this_BAR) + 1 < length:
                left = (length - len(this_BAR) - 1)//2
                right = length - len(this_BAR) - 1 - left
                this_BAR = (" "*left) + this_BAR + (" "*right)
            this_BAR += "|"

            if len(this_name) < length:
                left = (length - len(this_name))//2
                right = length - len(this_name) - left
                this_name = (" "*left) + this_name + (" "*right)

            # Buffer only on the right.
            if len(this_time) < length:
                this_time += " " * (length - len(this_time))

            BAR += this_BAR
            P_NAMES += this_name
            START += this_time

            timings = end_time

        # Prepare the gantt
        GANTT = P_NAMES + "\n" + BAR + "\n" + START + str(timings) + "\n"
        print()
        print(GANTT)

        print("\nCPU Utilization:", "{:.2f}".format(cpu_utilization), "%")
        print("Average Turnaround Time:", "{:.2f}".format(avg_turnaround_time), "ms")
        print("Average Waiting Time:", "{:.2f}".format(avg_waiting_time), "ms")
#SJF Algorithm
def sjf():
    while True:
        try:
            num_processes = int(input("Enter the number of processes (0 to 10): "))
            if 0 <= num_processes <= 10:
                break
            else:
                print("Invalid input. Number of processes should be between 0 and 10.")
                continue
        except ValueError:
                print("Invalid input! Please enter a valid number for arrival time.")
    if num_processes == 0:
        print("No processes to calculate. Exiting program.")
    else:
        processes = []

        for i in range(1, num_processes + 1):
            while True:
                try:
                    arrival_time = int(input(f"Enter arrival time for process {i} (0 to 15): "))
                    if 0 <= arrival_time <= 15:
                        break
                    else:
                        print("Invalid input! Please enter a number between 0 and 15.")
                except ValueError:
                    print("Invalid input! Please enter a valid number for arrival time.")
            while True:
                try:
                    burst_time = int(input(f"Enter burst time for process {i} (1 to 15): "))
                    if 1 <= burst_time <= 15:
                        break
                    else:
                        print("Invalid input! Please enter a number between 1 and 15.")
                except ValueError:
                    print("Invalid input! Please enter a valid number for burst time.")

            processes.append({
                'process_id': i,
                'burst_time': burst_time,
                'arrival_time': arrival_time,
                'end_time': 0,
                'turnaround_time': 0,
                'waiting_time': 0
            })
        current_time = 0

        sorted_processes_by_arrival = sorted(processes, key=lambda x: x['arrival_time'])

        first_process = sorted_processes_by_arrival[0]
        first_process['end_time'] = first_process['arrival_time'] + first_process['burst_time']
        current_time = first_process['end_time']
        first_process['turnaround_time'] = first_process['end_time'] - first_process['arrival_time']
        turnaround_time = first_process['turnaround_time']
        first_process['waiting_time'] = abs(turnaround_time - first_process['burst_time'])

        total_burst_time = first_process['burst_time']
        total_turnaround_time = first_process['turnaround_time']
        total_waiting_time = first_process['waiting_time']

        sorted_remaining_processes = sorted(sorted_processes_by_arrival[1:], key=lambda x: x['burst_time'])

        for process in sorted_remaining_processes:
            end_time = current_time + process['burst_time']

            process['end_time'] = end_time
            process['turnaround_time'] = end_time - process['arrival_time']
            turnaround_time = process['turnaround_time']
            process['waiting_time'] = abs(turnaround_time - process['burst_time'])

            total_burst_time += process['burst_time']
            total_turnaround_time += turnaround_time
            total_waiting_time += process['waiting_time']

            current_time = end_time

        processes = [first_process] + sorted_remaining_processes

        cpu_utilization = (total_burst_time / current_time) * 100
        avg_turnaround_time = total_turnaround_time / len(processes)
        avg_waiting_time = total_waiting_time / len(processes)

        label = f"{'-'*79}\n|{'Process':^15}|{'Arrival Time':^11}|{'Burst Time':^9}|{'End Time':^7}|{'Turnaround Time':^14}|{'Waiting Time':^11}|\n{'-'*79}\n"
        contents = f"\n{'-'*79}\n".join([f"|{process['process_id']:^15}|{process['arrival_time']:^12}|{process['burst_time']:^10}|{process['end_time']:^8}|{process['turnaround_time']:^15}|{process['waiting_time']:^12}|" for process in sorted(processes, key=lambda x: x['arrival_time'])]) + f"\n{'-'*79}\n" 
        print(label + contents)

        P_NAMES = " "
        BAR = "|"
        START = ""

        timings = 0

        remaining_processes = sorted(processes, key=lambda x: x['arrival_time'])

        while remaining_processes:
            current_process = remaining_processes[0]

            arrival_time = current_process['arrival_time']
            burst_timing = current_process['burst_time']

            this_BAR = ""
            this_name = f"P{current_process['process_id']}"
            
            if arrival_time > timings:
                idle_timing = arrival_time - timings
                this_BAR += '+' * idle_timing
                timings += 0

            this_BAR += '-' * burst_timing

            remaining_processes = remaining_processes[1:]

            remaining_processes = sorted(remaining_processes, key=lambda x: x['burst_time'])

            end_time = current_process['end_time']
            this_time = str(timings)
            timings = end_time
            
            length = max(len(this_BAR) + 1, len(this_name) + 1, len(this_time) + 2)

            if len(this_BAR) + 1 < length:
                left = (length - len(this_BAR) - 1) // 2
                right = length - len(this_BAR) - 1 - left
                this_BAR = (" " * left) + this_BAR + (" " * right)
            this_BAR += "|"

            if len(this_name) < length:
                left = (length - len(this_name)) // 2
                right = length - len(this_name) - left
                this_name = (" " * left) + this_name + (" " * right)

            if len(this_time) < length:
                this_time += " " * (length - len(this_time))

            BAR += this_BAR
            P_NAMES += this_name
            START += this_time

        GANTT_CHART = P_NAMES + "\n" + BAR + "\n" + START + str(timings) + "\n"
        print()
        print(GANTT_CHART)

        print("\nCPU Utilization:", "{:.2f}".format(cpu_utilization), "%")
        print("Average Turnaround Time:", "{:.2f}".format(avg_turnaround_time), "ms")
        print("Average Waiting Time:", "{:.2f}".format(avg_waiting_time), "ms")
#SRTF Algorithm
def srtf():
    while True:
        try:
            num_processes = int(input("Enter the number of processes (0 to 10): "))
            if 0 <= num_processes <= 10:
                break
            else:
                print("Invalid input. Number of processes should be between 0 and 10.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    if num_processes == 0:
        print("No processes to calculate. Exiting program.")
    else:
        processes = []

        for i in range(1, num_processes + 1):
            while True:
                try:
                    arrival_time = int(input(f"Enter arrival time for process {i} (0 to 15): "))
                    if 0 <= arrival_time <= 15:
                        break
                    else:
                        print("Invalid input! Please enter a number between 0 and 15.")
                except ValueError:
                    print("Invalid input! Please enter a valid number for arrival time.")
            while True:
                try:
                    burst_time = int(input(f"Enter burst time for process {i} (1 to 15): "))
                    if 1 <= burst_time <= 15:
                        break
                    else:
                        print("Invalid input! Please enter a number between 1 and 15.")
                except ValueError:
                    print("Invalid input! Please enter a valid number for burst time.")

            processes.append({
                'process_id': i,
                'burst_time': burst_time,
                'arrival_time': arrival_time,
                'end_time': 0,
                'turnaround_time': 0,
                'waiting_time': 0
            })

        current_time = 0
        total_burst_time = 0
        total_turnaround_time = 0
        total_waiting_time = 0

        remaining_processes = sorted(processes, key=lambda x: x['arrival_time'])
        sorted_remaining_processes = [] 

        while remaining_processes or sorted_remaining_processes:
            if not sorted_remaining_processes:
                current_process = remaining_processes.pop(0)
            else:
                current_process = sorted_remaining_processes.pop(0)

            if current_time < current_process['arrival_time']:
                current_time = current_process['arrival_time']

            end_time = current_time + current_process['burst_time']

            current_process['end_time'] = end_time
            current_process['turnaround_time'] = end_time - current_process['arrival_time']
            turnaround_time = current_process['turnaround_time']
            current_process['waiting_time'] = abs(turnaround_time - current_process['burst_time'])

            total_burst_time += current_process['burst_time']
            total_turnaround_time += turnaround_time
            total_waiting_time += current_process['waiting_time']

            current_time = end_time

            while remaining_processes and remaining_processes[0]['arrival_time'] <= current_time:
                sorted_remaining_processes.append(remaining_processes.pop(0))

            sorted_remaining_processes = sorted(sorted_remaining_processes, key=lambda x: x['burst_time'])

        cpu_utilization = (total_burst_time / current_time) * 100
        avg_turnaround_time = total_turnaround_time / len(processes)
        avg_waiting_time = total_waiting_time / len(processes)

        label = f"{'-'*79}\n|{'Process':^15}|{'Arrival Time':^11}|{'Burst Time':^9}|{'End Time':^7}|{'Turnaround Time':^14}|{'Waiting Time':^11}|\n{'-'*79}\n"
        contents = f"\n{'-'*79}\n".join([f"|{process['process_id']:^15}|{process['arrival_time']:^12}|{process['burst_time']:^10}|{process['end_time']:^8}|{process['turnaround_time']:^15}|{process['waiting_time']:^12}|" for process in sorted(processes, key=lambda x: x['arrival_time'])]) + f"\n{'-'*79}\n" 
        print(label + contents)

        P_NAME = " "
        BAR = "|"
        START = "0"
        timings = 0

        remaining_processes = sorted(processes, key=lambda x: x['arrival_time'])
        current_process = None

        while remaining_processes:
            eligible_processes = [process for process in remaining_processes if process['arrival_time'] <= timings]
            this_BAR = ""

            if not eligible_processes:
                timings += 1
                P_NAME += ''
                BAR += '+'
                continue

            if str(timings) not in START:
                last_start_value = int(START.split()[-1]) if START.strip() else 0
                space_difference = timings - last_start_value
                P_NAME +=  " " * space_difference
                BAR += "|" + "" * space_difference
                START += " " * space_difference + str(timings)

            shortest_remaining_time_process = min(eligible_processes, key=lambda x: x['burst_time'])

            arrival_time = shortest_remaining_time_process['arrival_time']
            burst_timing = min(shortest_remaining_time_process['burst_time'],
                                next((p['arrival_time'] for p in remaining_processes if p['arrival_time'] > timings),
                                    float('inf')) - timings)

            this_name = f"P{shortest_remaining_time_process['process_id']}"

            if arrival_time > timings:
                idle_timing = arrival_time - timings
                this_BAR += '+' * idle_timing
                this_name += " " * idle_timing
                timings += idle_timing

            this_BAR += '-' * burst_timing
            shortest_remaining_time_process['burst_time'] -= burst_timing
            timings += burst_timing
            time = shortest_remaining_time_process['end_time'] - shortest_remaining_time_process['burst_time']
            length = max(len(this_BAR) + 1, len(this_name), len(str(time)) + 1)
            last_start_value = int(START.split()[-1]) if START.strip() else 0
            space_difference = time - last_start_value
            if int(time) > 10 : 
                space_difference -= 1
            START += " " * space_difference + str(time)
            if len(this_BAR) + 1 < length:
                left = (length - len(this_BAR) - 1) // 2
                right = length - len(this_BAR) - 1 - left
                this_BAR = (" " * left) + this_BAR + (" " * right)
            this_BAR += "|"
            if len(this_name) < length:
                left = (length - len(this_name)) // 2
                right = length - len(this_name) - left
                this_name = (" " * left) + this_name + (" " * right)
            if  len(str(time)) < length:
                START += "" * (length -  len(str(time)))
            BAR += this_BAR
            P_NAME += this_name
            if shortest_remaining_time_process['burst_time'] == 0:
                remaining_processes.remove(shortest_remaining_time_process)
        GANTT = P_NAME + "\n" + BAR + "\n" + START + "\n"
        print()
        print(GANTT)

        print("\nCPU Utilization:", round(cpu_utilization, 2), "%")
        print("Average Turnaround Time:", round(avg_turnaround_time, 2), "ms")
        print("Average Waiting Time:", round(avg_waiting_time, 2), "ms")
#RR Algorithm
def rr():
    while True:
        processes = {}
        while True:
            try:
                num_processes = int(input("Enter the number of processes (0 to 10): "))
                if 0 <= num_processes <= 10:
                    break
                else:
                    print("Invalid input. Number of processes should be between 0 and 10.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        if num_processes == 0:
            print("No processes to calculate. Exiting program.")
        else:
            for i in range(1, num_processes + 1):
                while True:
                    try:
                        arrival_time = int(input(f"Enter arrival time for process {i} (0 to 15): "))
                        if 0 <= arrival_time <= 15:
                            break
                        else:
                            print("Invalid input! Please enter a number between 0 and 15.")
                    except ValueError:
                        print("Invalid input! Please enter a valid number for arrival time.")
                while True:
                    try:
                        burst_time = int(input(f"Enter burst time for process {i} (1 to 15): "))
                        if 1 <= burst_time <= 15:
                            break
                        else:
                            print("Invalid input! Please enter a number between 1 and 15.")
                    except ValueError:
                        print("Invalid input! Please enter a valid number for burst time.")
                processes[i] = {"arrival": arrival_time, "burst": burst_time}
            while True:
                try:
                    quantum = int(input("Enter Quantum (3 to 6): "))
                    if not (3 <= quantum <= 6):
                        print("Invalid input! Please enter a number between 3 and 6.")
                        continue
                except ValueError:
                    print(f"Invalid input for quantum! Please enter valid numbers.")
                    continue
                break
            p_names = ""
            line = "| "
            start = "0"
        
            processes = dict(sorted(processes.items(), key=lambda data: data[1]['arrival']))
            remaining_time = {dt: processes[dt]['burst'] for dt in processes}
            
            current_time = 0
            quantum_time = 0
            queue = []
            t_times = {}
            recent = None
            end_times = {}
            w_times = {}
            total_idle = 0
            idle_times = {}
        
            while remaining_time:
                available_process = {dt: remaining_time[dt] for dt in remaining_time if processes[dt]['arrival'] <= current_time}
                if recent is None:
                    queue = list(available_process.keys())
                elif sorted(list(available_process.keys())) == sorted(queue):
                    queue = queue
                else:
                    for key in available_process.keys():
                        if key not in queue:
                            queue.append(key)
            
                if not available_process:
                    next_arrival = min(((dt, processes[dt]['arrival']) for dt in remaining_time), key=lambda pair: pair[1])
                    list(next_arrival)
                    idle = next_arrival[1] - current_time
                    idle_times[next_arrival[0]] = idle
                    total_idle += idle
                    p_names += '  ' * idle
                    line += '+ ' * (idle - 1) + '| '
                    start += '   ' * (idle - len(str(current_time))) + str(next_arrival[1])
                    current_time = min(processes[dt]['arrival'] for dt in remaining_time)
                    continue
    
                if quantum_time == quantum:
                    queue.pop(0)
                    queue.append(recent)
                    quantum_time = 0
                next_process = queue[0]
                end_time = current_time + 1
                end_times[next_process] = end_time
                remaining_time[next_process] -= 1
                recent = next_process
                quantum_time += 1
        
                if next_process not in idle_times:
                    idle_times[next_process] = 0
                if quantum_time == quantum or remaining_time[next_process] == 0:
                    p_names += f'P{next_process} '.center(quantum * 2) if quantum > 1 else f'P{next_process}'.center((quantum * 2) - 1)
                    line += "- " * (quantum - 1) + "ￛ "
                    start += "  " * (quantum)
                    start = start[:-(len(str(end_time)))] + str(end_time)

                if remaining_time[next_process] == 0:
                    queue.pop(0)
                    quantum_time = 0
                    t_times[next_process] = end_times[next_process] - processes[next_process]['arrival']
                    w_times[next_process] = t_times[next_process] - processes[next_process]['burst']
                    del remaining_time[next_process]
                current_time += 1
            data = {dt: {'arrival': processes[dt]['arrival'], 'burst': processes[dt]['burst'], 'end': end_times[dt], 'turnaround': t_times[dt], 'waiting': w_times[dt], 'idle': idle_times[dt]} for dt in processes}
            label = f"{'-'*79}\n|{'Process':^15}|{'Arrival Time':^11}|{'Burst Time':^9}|{'End Time':^7}|{'Turnaround Time':^14}|{'Waiting Time':^11}|\n{'-'*79}\n"
            contents = f"\n{'-'*79}\n".join([f"|{data[0]:^15}|{data[1]['arrival']:^12}|{data[1]['burst']:^10}|{data[1]['end']:^8}|{data[1]['turnaround']:^15}|{data[1]['waiting']:^12}|" for data in dict(sorted(data.items(), key= lambda data: data[0])).items()]) + f"\n{'-'*79}\n"

            cpu_util = ((current_time - total_idle) / current_time) * 100
            awt = sum([data[1]['waiting'] for data in data.items()]) / len(data)
            att = sum([data[1]['turnaround'] for data in data.items()]) / len(data)
            averages = f"\nCPU Utilization: {cpu_util:.2f}%\nAvg. Turnaround Time: {att:.2f} ms\nAvg. Waiting Time: {awt:.2f} ms\n"

            table = '\n' + label + contents + '\n'
            rr = '\n' + p_names + '\n' + line + '\n' + start + '\n'
            print(table, rr, averages)
        break

def main():
    os.system('cls')
    while True:
        print("Choose the OS scheduling algorithm:")
        print("1. FCFS")
        print("2. SJF")
        print("3. SRTF")
        print("4. RR")
        print("5. Exit")

        choice = input("Enter the number corresponding to your choice: ")

        if choice == '1':
            print(f"\nFirst Come First Serve Algorithm")
            fcfs()
        elif choice == '2':
            print(f"\nShort Job First Algorithm")
            sjf()
        elif choice == '3':
            print(f"\nShortest Remaining Time First Algorithm")
            srtf()
        elif choice == '4':
            print(f"\nRound Robin Algorithm")
            rr()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            continue

        try_again = input("Do you want to try again? (yes/no): ").lower()
        if try_again == 'yes':
            os.system('cls')
        elif try_again == 'no':
            print("Exiting the program. Goodbye!")
            break
        elif try_again not in ['yes', 'no']:
            while True:
                print("Invalid input! Type 'yes' or 'no' and try again.")
                try_again = input("Do you want to try again? (yes/no): ").lower()
                if try_again in ['yes', 'no']:
                    break

if __name__ == "__main__":
    main()