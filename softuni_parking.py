number_of_commands = int(input())
parking = {}

for _ in range(number_of_commands):
    command = input().split()

    if command[0] == 'register':
        name = command[1]
        plate = command[2]
        if plate not in parking.values():
            parking[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f'ERROR: already registered with plate number {plate}')

    if command[0] == 'unregister':
        name = command[1]
        if name not in parking.keys():
            print(f'ERROR: user {name} not found')
        else:
            parking.__delitem__(name)
            print(f'{name} unregistered successfully')

for username, license_plate in parking.items():
    print(f'{username} => {license_plate}')

