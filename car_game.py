# Exercise
# My Solution
user = input("")
if user.upper() == 'HELP':
    print("""
    start - to start the car
    stop - to stop the car
    quit - to exit
    """)
    while user.upper() == 'HELP':
        if user.upper() == "START":
            print("Car started... Ready to go!")
        elif user.upper() == "STOP":
            print("Car stopped.")
        elif user.upper() == "QUIT":
            break
else:
    print("I don't understand that...")


# Mosh's Solution
command = ''
started = False
while True:
    command = input('> ').lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that...")
