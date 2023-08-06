# TLS Port Scanner

This is a simple Python script that allows you to scan TLS-enabled ports on a target host. The script uses the `socket` and `ssl` libraries to establish TLS connections and retrieve information about the server's SSL/TLS capabilities and certificate.

## Prerequisites

- Python 3.x

## Usage

To use the TLS Port Scanner, run the script from the command line with the following arguments:

```
python tls_port_scanner.py ip [ports] [-s {0, 1, 2}]
```

### Arguments:

- `ip`: FDQN or IPv4 address of the target host.

- `ports` (optional): The ports you want to scan for TLS support. You can provide multiple port numbers separated by spaces. By default, the script will scan well-known TLS ports if this argument is not provided.

- `-s`, `--scan` (optional): Increase output verbosity. This argument takes an integer value: `0` for minimal output, `1` for intermediate output, and `2` for detailed output.

## Examples

1. Scan well-known TLS ports (default behavior):

```
python tls_port_scanner.py example.com
```

2. Scan specific ports:

```
python tls_port_scanner.py example.com 443 8443
```

3. Increase output verbosity:

```
python tls_port_scanner.py example.com -s 2
```

## Functionality

The script uses the provided target IP address (`ip`) and port numbers (`ports`) to attempt TLS connections. For each specified port, it checks if TLS is supported and retrieves information about the server's SSL/TLS capabilities and certificate.

If the specified port does not support TLS or if a connection error occurs, the script will display a message indicating that TLS is not supported on that particular port.

The `scan_ports()` function is responsible for checking the TLS support on the specified ports, and the `check_tls_port()` function retrieves detailed information about the SSL/TLS configuration for each supported port.

Please note that the TLS handshake timeout is set to `0.1` seconds (`timeout=0.1`). You can modify this value in the script if needed.

## Disclaimer

This script is intended for educational and testing purposes only. Unauthorized port scanning and testing on live systems without permission is illegal and unethical. Use this script responsibly and only on systems you own or have explicit permission to test.

**Use at your own risk! The author is not responsible for any misuse or damage caused by this script.**

## License

This script is released under the MIT License. Feel free to modify and distribute it according to the terms of the MIT License.
