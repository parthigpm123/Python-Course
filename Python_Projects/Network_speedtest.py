from tkinter import *
import speedtest

def test_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    ping_result = st.results.ping

    download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
    ping_label.config(text=f"Ping: {ping_result} ms")

# Main window
sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="blue")

# Button to start test
start_button = Button(sp, text="Start Speed Test", command=test_speed, font=("Arial", 14), bg="white")
start_button.pack(pady=20)

# Labels to display results
download_label = Label(sp, text="Download Speed: ", font=("Arial", 12), bg="blue", fg="white")
download_label.pack(pady=10)

upload_label = Label(sp, text="Upload Speed: ", font=("Arial", 12), bg="blue", fg="white")
upload_label.pack(pady=10)

ping_label = Label(sp, text="Ping: ", font=("Arial", 12), bg="blue", fg="white")
ping_label.pack(pady=10)

sp.mainloop()
