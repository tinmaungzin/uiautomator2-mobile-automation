import uiautomator2 as u2
import time

device = u2.connect()   

package_name = 'com.facebook.katana'
device.app_start(package_name)

time.sleep(10)

def navigate_to_tab(tab_desc):
    tab = device(description=tab_desc)
    if tab.exists:
        tab.click()
        time.sleep(3)  
    else:
        print(f"Tab '{tab_desc}' not found")

navigate_to_tab("Notifications, tab 5 of 6")
navigate_to_tab("Menu, tab 6 of 6")
navigate_to_tab("Home, tab 1 of 6")
time.sleep(5)


try:
    element = device(description="What's on your mind? Make a post on Facebook")
    if element.exists:
        print("Element found")
        print("Element info:", element.info['contentDescription'])   
    else:
        print("Element not found")
except Exception as e:
    print(f"An error occurred: {e}")

device.app_stop(package_name)
