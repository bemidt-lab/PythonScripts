devices = ["laptop", "tablet", "smartphone", "printer"]
print("Devices:" , devices)
print(len(devices))

assigned_devices = {"bemidt": "laptop", "sullivani": "tablet", "bankse": "smartphone"}
print("Assigned Devices:", assigned_devices)

devices.append("gateway")
assigned_devices["sullivani"] = "gateway"
print("Updated Devices:", devices)
print("Updated Assigned Devices:", assigned_devices)

print("IT Asset Count:", len(devices))
print("IT Asset Summary:")
for user, device in assigned_devices.items():
    print(user, "has", device)