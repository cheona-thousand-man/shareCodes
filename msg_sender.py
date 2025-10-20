import socket
import argparse
import time

def main():
    parser = argparse.ArgumentParser(description='UDP 송신 프로그램')
    parser.add_argument('--dest_ip', type=str, default='192.168.20.110', help='수신자 IP 주소')
    parser.add_argument('--dest_port', type=int, default=7000, help='수신자 UDP 포트')
    parser.add_argument('--msg_count', type=int, default=10, help='보낼 메시지 수')
    parser.add_argument('--interval', type=float, default=1.0, help='메시지 송신 간격(초)')

    args = parser.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i in range(args.msg_count):
        message = f"Message {i+1}"
        sock.sendto(message.encode(), (args.dest_ip, args.dest_port))
        print(f"Sent: {message} to {args.dest_ip}:{args.dest_port}")
        time.sleep(args.interval)

    sock.close()

if __name__ == '__main__':
    main()
