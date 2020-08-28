from nornir import init_nornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


nr = init_nornir.InitNornir()

result = nr.run(
    task=netmiko_send_command,
    command_string='wr m'
)

print_result(result) 
