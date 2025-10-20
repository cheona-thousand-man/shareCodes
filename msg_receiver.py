import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description='UDP 수신 프로그램')
    parser.add_argument('--bind_ip', type=str, default='0.0.0.0', help='수신할 IP 주소')
    parser.add_argument('--bind_port', type=int, default=7000, help='수신할 UDP 포트')
    parser.add_argument('--timeout', type=float, default=1.0, help='recv 타임아웃(초)')
    args = parser.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((args.bind_ip, args.bind_port))
    sock.settimeout(args.timeout)  # 블로킹 recvfrom을 주기적으로 깨워 Ctrl+C를 빠르게 반영 [web:35][web:26]

    print(f"Listening on {args.bind_ip}:{args.bind_port}... (Press Ctrl+C to exit)")

    try:
        while True:
            try:
                data, addr = sock.recvfrom(1024)
                print(f"Received from {addr}: {data.decode()}")
            except socket.timeout:
                # 주기적으로 깨워 종료 신호를 빨리 반영
                continue
    except KeyboardInterrupt:
        print("\nStopping receiver...")
    finally:
        sock.close()
        print("Socket closed. Bye.")

if __name__ == '__main__':
    main()
