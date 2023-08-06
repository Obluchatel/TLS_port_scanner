import socket
import ssl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ip", type=str,
                    help="FDQN or IPv4 address of target host")
parser.add_argument("ports", type=int, nargs='*',
                    help="Port you want to scan. Option 0 - scan all ports, "
                         "option 1 - scan specific ports. Default option 1")
parser.add_argument("-s", "--scan", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")

args = parser.parse_args()
target = args.ip
list_of_ports = args.ports

context = ssl.create_default_context()


def scan_ports(list_of_ports):
    for port_number in list_of_ports:
        print(f"Checking port {port_number}")
        try:
            with socket.create_connection((target, port_number), timeout=0.1) as sock:
                with context.wrap_socket(sock, server_hostname=target) as ssock:
                    print(f"{ssock.version()} connection established  with port {port_number}")
        except ConnectionError:
            print(f'TLS is not supported for port {port_number} on {target}')


def check_tls_port(hostname):
    for port_number in list_of_ports:
        try:
            with socket.create_connection((hostname, port_number), timeout=0.1) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    for i in ssock.shared_ciphers():
                        print(f"Server support {i}")
                    print(f"Server chose {ssock.cipher()}")
                    cert_info = ssock.getpeercert()
                    for i in cert_info.keys():
                        print(f"{i}: {cert_info[i]}")
        except ConnectionError:
            print(f'TLS is not supported for port {port_number} on {hostname}')


if args.scan and args.scan == 0:
    scan_ports(range(0, 65536))
elif args.scan and args.scan == 1:
    scan_ports([443, 8443])
elif args.scan and args.scan == 2:
    check_tls_port(target)
else:
    scan_ports(args.ports)
