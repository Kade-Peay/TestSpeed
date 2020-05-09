import speedtest
import time

start = time.time()
test = speedtest.Speedtest()

download = test.download()
print(f"Download Speed: {download}", flush=True)


upload = test.upload()
print(f"Upload Speed: {upload}", flush=True)

end = time.time()
print("Done in " + str(end - start) + " seconds")