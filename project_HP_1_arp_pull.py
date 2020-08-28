from nornir import init_nornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

command_to_run = input("Enter Command: ")


nr = init_nornir.InitNornir()

result = nr.run(
    task=netmiko_send_command,
    command_string=command_to_run
)

print_result(result) 

