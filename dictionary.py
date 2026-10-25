#dictionary 
server = {
    "ip": "192.168.1.10",
    "port": 22,
    "status": "running"
}

server["status"] = "stopped"
server["city"] = "New York"

del server["port"]
print(server)  # Output: {'ip': '192.168.1.10', 'port': 22, 'status': 'stopped', 'city': 'New York'}


a = (10, [20, 30], 40, 50)
print(a[1][1])
print(a[1])


print("update")