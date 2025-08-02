# 🌐 Web Ping CLI Tool

A Python-based CLI tool to check website uptime, status codes, and response latency using `requests` and `argparse`.

## 🚀 Features

- Ping websites continuously using intervals
- Print response times and error messages
- Graceful handling of timeouts, HTTP errors, and connection failures

## 🧪 Example Usage

```bash
# Basic one-time ping
python web_ping.py -u openai.com

# Ping every 5 seconds for 15 seconds
python web_ping.py -u openai.com -t 15 -i 5
