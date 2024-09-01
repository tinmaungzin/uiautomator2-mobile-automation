import uiautomator2 as u2
import time

# Connect to the Android device
# Replace 'device_ip' with your device's IP or leave it as 'device' for USB connection
device = u2.connect()

# Launch the Facebook app
# Ensure you have the correct package name for Facebook
package_name = 'com.facebook.katana'
device.app_start(package_name)

# Allow time for the app to launch
time.sleep(10)

# Define the scrolling action
def scroll_down():
    device(scrollable=True).scroll(steps=10)  # Scroll down with a specified number of steps

# Perform multiple scrolls to cover more content
for _ in range(3):  # Adjust the range for more or fewer scrolls
    scroll_down()
    time.sleep(2)  # Allow time for the UI to stabilize after each scroll

# Dump the current UI hierarchy as a string
xml_content = device.dump_hierarchy()

# Save the hierarchy XML to a file for inspection
with open("hierarchy.xml", "w") as f:
    f.write(xml_content)

print("UI hierarchy saved to hierarchy.xml")

# Close the app (optional)
device.app_stop(package_name)
