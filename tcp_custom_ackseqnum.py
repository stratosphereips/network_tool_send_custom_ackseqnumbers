import argparse
from scapy.all import IP, TCP, send

def send_tcp_ack_packets(source_ip, destination_ip, sport, dport, seq_increment, ack_increment):
    initial_seq=1
    initial_ack=1
    # Define the IP layer
    ip = IP(src=source_ip, dst=destination_ip)

    # List to store sequence and acknowledgment numbers
    seq_nums = [initial_seq + i * seq_increment for i in range(3)]
    ack_nums = [initial_ack + i * ack_increment for i in range(3)]

    # Send three TCP ACK packets with specified sequence and acknowledgment numbers
    for seq_num, ack_num in zip(seq_nums, ack_nums):
        tcp = TCP(sport=sport, dport=dport, flags="A", seq=seq_num, ack=ack_num)

        # Create the packet
        packet = ip / tcp

        # Send the packet
        send(packet)
        print(f"Sent packet with SEQ={seq_num} and ACK={ack_num}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send TCP ACK packets with specified sequence and acknowledgment numbers.")
    parser.add_argument("--src_ip", type=str, default="172.10.0.10", help="Source IP address (default: 172.10.0.10)")
    parser.add_argument("--dst_ip", type=str, default="172.10.0.20", help="Destination IP address (default: 172.10.0.20)")
    parser.add_argument("--sport", type=int, default=12345, help="Source port (default: 12345)")
    parser.add_argument("--dport", type=int, default=80, help="Destination port (default: 80)")
    parser.add_argument("--seq_increment", type=int, default=1073741824, help="Sequence number increment (default: 1073741824)")
    parser.add_argument("--ack_increment", type=int, default=1073741824, help="Acknowledgment number increment (default: 1073741824)")


    args = parser.parse_args()

    # Send the TCP ACK packets
    send_tcp_ack_packets(args.src_ip, args.dst_ip, args.sport, args.dport, args.seq_increment, args.ack_increment)
