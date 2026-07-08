from collections import deque

def run_queue_demo():
    # 1. Create an empty queue
    ticket_line = deque()
    
    # 2. ENQUEUE: People joining the back of the line
    ticket_line.append("Rahul")
    ticket_line.append("Soumya")
    ticket_line.append("Amit")
    
    print("Initial Line (Front to Back):", list(ticket_line))
    # Output: ['Rahul', 'Soumya', 'Amit']
    
    # 3. DEQUEUE: Serving the person at the front of the line
    # popleft() removes and returns the absolute first element
    served_person = ticket_line.popleft()
    print("Served:", served_person)
    
    print("Line after serving one person:", list(ticket_line))
    # Output: ['Soumya', 'Amit']

# Run the machine
run_queue_demo()
