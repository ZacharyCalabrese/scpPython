import os
from paramiko import SSHClient
import paramiko
from jbardin.scp import SCPClient, SCPException

def _get_ssh_instance(connection_string, port):
    ssh_info = {
        'hostname': os.environ.get('SCPPY_HOSTNAME', connection_string[connection_string.find('@')+1:]),
        'port': int(os.environ.get('SCPPY_PORT', port)),
        'username': os.environ.get('SCPPY_USERNAME', connection_string[:connection_string.find('@')]),
        }
    
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh.load_system_host_keys()
    ssh.connect(**ssh_info)

    return ssh

def send_file(source_path_and_file, destination, connection_string, port):
    ssh = _get_ssh_instance(connection_string, port)
    scp = SCPClient(ssh.get_transport())

    try:
        scp.put(source_path_and_file, destination)
    except SCPException as e:
        print "Error trasnferring file: %s" % e

    scp.close()

def get_file(source_path_and_file, connection_string, port, destination_path = ''):
    ssh = _get_ssh_instance(connection_string, port)
    scp = SCPClient(ssh.get_transport())

    try:
        scp.get(source_path_and_file, destination_path)
    except SCPException as e:
        print "Error transferring file: %s" % e

    scp.close()
