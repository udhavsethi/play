docker build -t ping:v1 .

# Ensure the firewalld service has been started with:
# sudo systemctl start firewalld.service

# You can verify the service is running with:
# systemctl status firewalld.service

docker run -p 4040:4040 ping
