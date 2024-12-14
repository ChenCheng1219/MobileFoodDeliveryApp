import pyautogui
import time
import subprocess
# Launch the app (example: python main.py)
subprocess.Popen(["python", "main.py"])
time.sleep(3) # wait for GUI to appear
# Find the "Register" button by coordinates (adjust coordinates as needed)
time.sleep(1)
# Type email
pyautogui.typewrite("testuser@example.com")
pyautogui.press("tab")
# Type password
pyautogui.typewrite("ValidPass123")
pyautogui.press("tab")
# Confirm password
pyautogui.typewrite("ValidPass123")
pyautogui.press("enter")
# Wait for confirmation
time.sleep(2)
# Take a screenshot to verify success message
pyautogui.screenshot("registration_result.png")
# Manually check the screenshot or use OCR for verification
