# List of server hostnames in the data center
servers = ["web01", "db01", "auth01", "backup01"]

# Access and display specific servers
print("Primary web server:", servers[0])
print("Database server:", servers[1])

# Display the total number of servers
server_count = len(servers)
print("Total number of servers:", server_count)