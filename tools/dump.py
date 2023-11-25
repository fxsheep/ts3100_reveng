import serial
import binascii
import argparse

def hexdump_to_raw(uart_device, filename, address, lines):
    try:
        ser = serial.Serial(uart_device, baudrate=19200, timeout=1)
        ser.write(f"xd {address} {lines}\r\n".encode())

        with open(filename, 'wb') as output_file:
            while True:
                line = ser.readline().decode().strip()
                if line.startswith("Dry>"):
                    break
                parts = line.split(':')
                if len(parts) == 2:
                    hex_data = parts[1][:48].replace(' ', '').replace('.', '')  # Extract the hex part, excluding ASCII
                    output_data = binascii.unhexlify(hex_data)
                    output_file.write(output_data)

        ser.close()
        print(f"Memory dump from address {address} with {lines} lines converted and written to {filename}")
    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dump memory from UART hexdump to a file')
    parser.add_argument('uart_device', type=str, help='UART device node')
    parser.add_argument('output_filename', type=str, help='Output file name')
    parser.add_argument('memory_address', type=str, help='Memory address')
    parser.add_argument('lines_to_dump', type=str, help='Number of lines to dump')

    args = parser.parse_args()

    hexdump_to_raw(args.uart_device, args.output_filename, args.memory_address, args.lines_to_dump)
