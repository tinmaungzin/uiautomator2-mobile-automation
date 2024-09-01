# UI Automation with uiautomator2

This project demonstrates how to use the `uiautomator2` library for automating interactions with a mobile application. The script connects to a device, navigates through tabs in the Facebook app, and checks for a specific UI element.

## Prerequisites

- Python 3.x
- `uiautomator2` library
- An Android device or emulator with the Facebook app installed

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/tinmaungzin/uiautomator2-mobile-automation.git
    cd uiautomator2-mobile-automation
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```


## Usage

1. **Connect to the Device:**

    Make sure your Android device is connected via USB or that your emulator is running.

2. **Run the Main Script:**

    Execute the main script to start the automation process:

    ```bash
    python app.py
    ```


3. **Script Behavior:**

    - **Launches the Facebook app** using its package name (`com.facebook.katana`).
    - **Navigates through specific tabs** in the app (Notifications, Menu, Home).
    - **Checks for a specific UI element** with the description "What's on your mind? Make a post on Facebook".
    - **Stops the Facebook app** after completing the checks.

## Hierarchy Inspection

If you do not have a GUI inspector installed, you can use the `generate_hierarchy.py` script to inspect the UI hierarchy of your application. This script provides a textual representation of the UI components, which can be useful for identifying the elements you need to interact with.

### Running `generate_hierarchy.py`

1. **Execute the Script:**

    ```bash
    python generate_hierarchy.py
    ```

2. **Script Behavior:**

    - **Connects to the device** using `uiautomator2`.
    - **Generates and prints the UI hierarchy** of the currently active application.
    - **Helps identify UI element attributes** and structure for further automation tasks.

## Code Overview

- **Device Connection:** Uses `uiautomator2` to connect to the device.
- **App Interaction:** Starts and stops the Facebook app.
- **Navigation:** Uses `navigate_to_tab` function to click on different tabs.
- **Element Check:** Finds and prints information about a specific UI element.
- **Hierarchy Inspection:** Provides a textual representation of the UI hierarchy using `generate_hierarchy.py`.

## Troubleshooting

- **Device Connection Issues:** Ensure the device is properly connected and USB debugging is enabled.
- **App Not Found:** Verify the package name of the Facebook app is correct.
- **Element Not Found:** UI elements might change; adjust the `description` as needed.
- **Hierarchy Inspection:** If the hierarchy output is not as expected, ensure that the target application is in the foreground and accessible.
