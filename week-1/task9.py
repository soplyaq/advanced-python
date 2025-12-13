
ticket = input("Enter ticket number (6 digits): ")

if len(ticket) != 6 or not ticket.isdigit():
    print("Invalid ticket number")
else:
    first_sum = sum(map(int, ticket[:3]))
    second_sum = sum(map(int, ticket[3:]))
    
    if first_sum == second_sum:
        print("YES")
    else:
        print("NO")