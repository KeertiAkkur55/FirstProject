def show_events():
    events = {
        1: "Movie: Inception",
        2: "Concert: Coldplay",
        3: "Play: Hamlet"
    }

    print("\nAvailable Events:")
    for key, value in events.items():
        print(f"{key}. {value}")

    return events


def book_ticket(events):
    try:
        choice = int(input("\nEnter the event number you want to book: "))
        if choice in events:
            name = input("Enter your name: ")
            tickets = int(input("Number of tickets: "))
            print("\n✅ Booking Confirmed!")
            print(f"Name: {name}")
            print(f"Event: {events[choice]}")
            print(f"Tickets: {tickets}")
        else:
            print("❌ Invalid event selection.")
    except ValueError:
        print("❌ Please enter valid input.")


def main():
    print("🎟️ Welcome to the Online Ticket Booking System")
    events = show_events()
    book_ticket(events)


if __name__ == "__main__":
    main()

