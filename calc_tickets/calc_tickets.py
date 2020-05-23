#!/usr/bin/env python3
# How many remaining tickets

ticket_price = 12
service_charge = 2
tickets_remaining = 100

def calculate_price(a):
    return (a * ticket_price) + service_charge

def buy_tickets():
    global tickets_remaining
    num_tickets = input(f"How many tickets would you like, {name}?  ")
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError(f"There are only {tickets_remaining} tickets left")
    except ValueError as err:
        print(f"Something went wrong. {err}" )
    else:
        price = calculate_price(num_tickets)
        tickets_remaining = tickets_remaining - num_tickets
        print(f"Final price will be : ${price}")

def buy_more():
    return input(f"Would you like buy more tickets, {name}: Y/N").lower().startswith("y")

while tickets_remaining >= 1:
    print("There are {} tickets remaining at this moment.".format(tickets_remaining))
    name = input("What is your name ? ")
    buy_tickets()
    if tickets_remaining == 0:
        print("There is no tickets available")
        break
    if not buy_more():
        break
    
