import serial
import argparse
import struct

def write_data(uart_device, filename, address):
    try:
        ser = serial.Serial(uart_device, baudrate=19200, timeout=1)

        with open(filename, 'rb') as input_file:
            while True:
                # Calculate the number of bytes needed to align the address
                alignment_bytes = address % 4
                if alignment_bytes != 0:
                    bytes_to_align = 4 - alignment_bytes
                    data = input_file.read(bytes_to_align)  # Read bytes to align the address
                    for byte in data:
                        command = f"xm {hex(address)} b {hex(address)} {hex(byte)} f\r\n"
                        ser.write(command.encode())

                        while True:
                            response = ser.readline().decode().strip()
                            if response == "Dry>":
                                break

                        address += 1

                # Now perform aligned writes or handle remaining bytes with byte write
                data = input_file.read(4)  # Read 4 bytes at a time
                if len(data) < 4:  # Less than 4 bytes read, use byte write for the remaining bytes
                    for byte in data:
                        command = f"xm {hex(address)} b {hex(address)} {hex(byte)} f\r\n"
                        ser.write(command.encode())

                        while True:
                            response = ser.readline().decode().strip()
                            if response == "Dry>":
                                break

                        address += 1
                else:  # Perform aligned write for 4-byte chunks
                    # Convert data to little-endian format
                    little_endian_data = struct.unpack('<I', data)[0]
                    command = f"xm {hex(address)} l {hex(address)} {hex(little_endian_data)} f\r\n"
                    ser.write(command.encode())

                    while True:
                        response = ser.readline().decode().strip()
                        if response == "Dry>":
                            break

                    address += len(data)

                if len(data) < 4:
                    break

        ser.close()
        print(f"Data from '{filename}' written to memory address successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Write data from a file to memory address')
    parser.add_argument('uart_device', type=str, help='UART device node')
    parser.add_argument('filename', type=str, help='Input file name')
    parser.add_argument('address', type=lambda x: int(x,0), help='Memory address')

    args = parser.parse_args()

    write_data(args.uart_device, args.filename, args.address)
