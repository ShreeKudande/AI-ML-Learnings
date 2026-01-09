#Q.Write a recursive function to calculate the sum of first n natural numbers.

# def sum(n):
#     if n == 1:
#         return 1
#     return sum(n-1) + n

# n = int(input("Enter the number : "))

# print(sum(n))
 
def sum_recursive(n):
    # ARRIVAL: A person enters the waiting room
    print(f"Person {n} enters the room and waits...")

    # THE BASE CASE: The only person who knows their answer immediately
    if n == 1:
        print("Person 1 says: 'I am the base case, I return 1!'")
        return 1

    # THE WAITING: Person n waits for the result of Person (n-1)
    # This is the "return sum(n-1) + n" part broken down:
    result_from_next_person = sum_recursive(n - 1)
    
    total = result_from_next_person + n
    
    # DEPARTURE: Person n finally gets their answer and leaves
    print(f"Person {n} received {result_from_next_person} from the room. Adding {n}...")
    print(f"Person {n} is leaving the room with a total of: {total}")
    
    return total

# Execution
num = 4
print(f"--- Starting Sum of first {num} numbers ---")
final_answer = sum_recursive(num)
print(f"--- Final Answer: {final_answer} ---")
