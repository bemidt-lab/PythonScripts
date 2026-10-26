user_name = input("Enter username: ")
device_name = input("Enter device name: ")
temp_password = input("Enter temporary password: ")

print("Username:", user_name.strip())
print("Device ID start:", device_name[0:4])
print("Temporary password:", temp_password)
if len(temp_password) < 8:
    print("Warning: Your temporary password is less than 8 characters long. Please consider changing it to a stronger password.")