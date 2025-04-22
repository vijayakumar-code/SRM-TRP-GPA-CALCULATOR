#!/usr/bin/env python3
"""
Enhanced HTTP Server with additional configuration options and documentation
while maintaining the original simple file serving functionality.
"""

import http.server
import socketserver
import argparse
import socket
from datetime import datetime

# Default configuration values
DEFAULT_PORT = 8000
DEFAULT_BIND_ADDRESS = ""
DEFAULT_PROTOCOL = "HTTP/1.0"

class EnhancedHTTPServer(socketserver.TCPServer):
    """Extended TCPServer with additional settings"""
    allow_reuse_address = True
    request_queue_size = 10
    
    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)
        self.start_time = datetime.now()

def get_local_ip():
    """Utility function to get the server's local IP address"""
    try:
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        return local_ip
    except:
        return "127.0.0.1"

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Simple HTTP Server with enhanced options",
        epilog="Serves files from the current directory"
    )
    parser.add_argument(
        "-p", "--port",
        type=int,
        default=DEFAULT_PORT,
        help=f"Port to serve on (default: {DEFAULT_PORT})"
    )
    parser.add_argument(
        "-b", "--bind",
        default=DEFAULT_BIND_ADDRESS,
        help="Bind address (default: all interfaces)"
    )
    return parser.parse_args()

def print_server_info(port, bind_address):
    """Display server startup information"""
    print("\n" + "=" * 60)
    print(f"Python HTTP Server started at {datetime.now()}")
    print("=" * 60)
    print(f"Server running on:")
    print(f"- http://localhost:{port}")
    if bind_address == "":
        local_ip = get_local_ip()
        print(f"- http://{local_ip}:{port}")
    else:
        print(f"- http://{bind_address}:{port}")
    print("\nServing files from current directory")
    print("=" * 60 + "\n")
    print("Press Ctrl+C to stop the server\n")

def main():
    """Main server execution function"""
    args = parse_arguments()
    
    # Configure the request handler
    Handler = http.server.SimpleHTTPRequestHandler
    Handler.protocol_version = DEFAULT_PROTOCOL
    
    # Create server instance
    server_address = (args.bind, args.port)
    
    print_server_info(args.port, args.bind)
    
    try:
        with EnhancedHTTPServer(server_address, Handler) as httpd:
            print(f"[STATUS] Ready to handle requests on port {args.port}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer is shutting down gracefully...")
    except Exception as e:
        print(f"\nError occurred: {e}")
    finally:
        print("Server has stopped")

if __name__ == "__main__":
    main()
