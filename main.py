import speedtest
import time

start = time.time()
test = speedtest.Speedtest()
download = test.download()
upload = test.upload()
end = time.time()

print(f"Download Speed: {download} Upload Speed : {upload}")
print("Done in " + str(end - start) + " seconds")