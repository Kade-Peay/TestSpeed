# to install speedtest it is 'pip install speedtest-cli'
import speedtest
import time

print('Starting test please wait...\n')

start = time.time()
test = speedtest.Speedtest()

download = test.download()
print(f"Download Speed: {int(download / 1000000)} mbps", flush=True)

upload = test.upload()
print(f"Upload Speed: {int(upload / 1000000)} mbps", flush=True)

end = time.time()
print("Done in " + str(end - start) + " seconds")