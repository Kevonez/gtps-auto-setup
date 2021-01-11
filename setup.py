import os
from time import sleep
os.system("cls")

def server_data_make():
    global ip, port
    #make server_data.php
    #send help pls i stackoverflowed just to make this
    print("Do you want to make server_data.php?\n")
    fuk = input("(y/n): ")
    if fuk == "y":
        os.system("cd C:/xampp/htdocs")
        os.system("mkdir growtopia")

        with open('server_data.php', 'w') as f:
            f.write(f"server|{ip}\n")
            f.write(f"port|{port}\n")
            f.write("type|1\n")
            f.write("#maint|maintenance server (to send maintenance message!)\n")
            f.write("beta_server|127.0.0.1\n")
            f.write("beta_port|17091\n")
            f.write("beta_type|1\n")
            f.write("meta|localhost\n")
            f.write("RTENDMARKERBS1001")
            print("Done!")
        os.system("copy server_data.php C:/xampp/htdocs/growtopia")
        print("If u check growtopia folder is not available or no server_data inside just make a growtopia folder\nand copy server_data there!")
        sleep(10)
    elif fuk == "n":
        print("Done setup thx for using tools!")
    else:
        exit()

def install_xampp():
    print("If you have installed xampp just write n or and error will occur")
    fart = input("Do you want install xampp(y/n): ")
    if fart == "y":
        print('installing xampp now!')
        os.system("""%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\powershell.exe -Command "Invoke-WebRequest https://downloadsapachefriends.global.ssl.fastly.net/7.4.11/xampp-windows-x64-7.4.11-0-VC15-installer.exe?from_af=true -OutFile xampp.exe""")
        os.system("start xampp.exe")
        server_data_make()
    elif fart == "n":
        print("Ok we will make server_data.php now!")
        os.system("cls")
        server_data_make()

def main():
    #global ip, port
    print("Please Wait...")

    sleep(1)
    os.system('cls')

    #setup firewall
    print("Doing firewall...")
    os.system("""netsh advfirewall firewall delete rule name="80" protocol=TCP localport=80""")
    os.system("""netsh advfirewall firewall delete rule name="80" protocol=TCP localport=80""")
    os.system(f"""netsh advfirewall firewall delete rule name="{port}" protocol=UDP localport={port}""")
    os.system(f"""netsh advfirewall firewall delete rule name="{port}" protocol=UDP localport={port}""")
    os.system("""netsh advfirewall firewall add rule name="80" dir=in action=allow protocol=TCP localport=80""")
    os.system("""netsh advfirewall firewall add rule name="80" dir=in action=allow protocol=TCP localport=80""")
    os.system(f"""netsh advfirewall firewall add rule name="{port}" dir=in action=allow protocol=UDP localport={port}""")
    os.system(f"""netsh advfirewall firewall add rule name="{port}" dir=in action=allow protocol=UDP localport={port}""")
    os.system('cls')

    print("Done setup port!")
    install_xampp()

ip = input("Your Vps Ip: ")
port = input("Your port (optional): ")
main()
