#!/bin/sh

# Server online-status check with reporting to telegram
# https://RundesBalli.com
# https://GitHub.com/RundesBalli
# https://gist.github.com/RundesBalli/4bdcf555c78c17a7b917de31cd7b4df0

# Server variables
server="http://cottonwear.ddns.net"
port=80

# Telegram variables
botToken="1737882228:AAGbziTC3YsUPnGuFzuF-f3bJE_URsw3EuY"
chatId="739619208"

# Use netcat to check if a daemon on $server:$port is running.
# If not, send telegram message.
if ! nc -w 2 -z $server $port > /dev/null 2>&1
then
    curl \
    -X POST \
    -s \
    --data "chat_id=${chatId}" \
    --data "disable_web_page_preview=true" \
    --data "text=Server ${server}:${port} down!%0A$(date +"%a, %d. %B %Y, %H:%M:%S")" \
    --connect-timeout 30 \
    --max-time 45 \
    "https://api.telegram.org/bot${botToken}/sendMessage" \
    > /dev/null
fi