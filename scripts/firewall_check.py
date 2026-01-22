print("\nChecking Ip on FW1")
block_list = ["1.1.1.1", "8.8.4.4", "192.168.5.5"]
#Asking user to enter ip 
ip_address:str = input("\nEnter IP Address: ").strip()

if ip_address in block_list:
    print("Connection to Blocked_IP")
else:
    print("Safe Connection")

