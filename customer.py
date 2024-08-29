#1.Real-World Python Dictionary Applications
#Task 1: Restaurant Menu 
#Update You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
    }

# Add a new category called "Beverages" with at least two items.
dict1 = {"Beverages": {"Iced-tea": 5.99, "G-J": 6.50}}
restaurant_menu.update(dict1)
print(restaurant_menu)

#Update the price of "Steak" to 17.99.
restaurant_menu.update({"Main Course": {"Steak": 17.99, "Salmon": 13.99}})
print(restaurant_menu)

#Remove "Bruschetta" from "Starters". 
#2.Python Programming Challenges for Customer Service Data Handling
restaurant_menu.pop("Starters")
print(restaurant_menu)
#Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by 
#creating a system to track customer service tickets.
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

while True:
    print("The completed service tickets are:")
    print(service_tickets)
    print("This is a template for service tickets avalible")
    New_service_Template = {"Ticket003":{"Customer": "Name", "Issue":"Login problem", "Status": "open"}}
    print(New_service_Template)
    print("We will be adding a new service ticket to the group based on the template:")
    break

#Problem Statement: Develop a program that:
#Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
New_service_Template = {"Ticket00":{"Customer": "Name", "Issue": "issue" , "Status": "status"}}
#Implement functions to: Open a new service ticket.
print("We need to open a new service ticket for Name:Emma-James, ID:Ticket004, Issue:New device settup, Status:open")
print("Template")
print(New_service_Template)
def New_customer(): 
    name = input("Input the Customer name")
    Customer_ID = input("Input the Customer ID")
    Issue = input("Input the Customer Issue")
    Status = input("Input the Customer Status")
    x = {Customer_ID:{"Customer": name, "Issue": Issue , "Status": Status}}
    service_tickets.update(x)
    print(service_tickets)
New_customer()
#Update the status of an existing ticket.
def Status_update():
    Status = input("Input the Customer Status")
    f = {"Ticket004":{"Customer": "Emma-James", "Issue": "New device settup" , "Status": Status}}
    service_tickets.update(f)
    print(service_tickets)  

Status_update()
print(service_tickets)


