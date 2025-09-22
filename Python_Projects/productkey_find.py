import subprocess
import ctypes

def get_product_key():
    key = subprocess.getoutput("wmic path softwarelicensingservice get OA3xOriginalProductKey").strip()
    if not key or "OA3xOriginalProductKey" in key:
        key = subprocess.getoutput(
            "powershell -command \"(Get-CimInstance -query 'select * from SoftwareLicensingService').OA3xOriginalProductKey\""
        ).strip()
    return key if key else "No OEM Product Key found"

if __name__ == "__main__":
    product_key = get_product_key()
    ctypes.windll.user32.MessageBoxW(0, f"OEM Product Key:\n{product_key}", "Windows Key Info", 1)
