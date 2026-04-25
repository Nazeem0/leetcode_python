import speedtest

speed_test = speedtest.Speedtest()
download = speed_test.download()
upload = speed_test.upload()
print(f"download speed: {download/1_000_000:.2f} Mbps")
print(f"upload speed: {upload/1_000_000:.2f} Mbps")
# download speed: 41.52 Mbps
# upload speed: 35.96 Mbps
# output 