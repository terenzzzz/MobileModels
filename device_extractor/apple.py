import re

def extract_apple_models(file_path):
    # Define a regular expression pattern to extract model numbers
    pattern = r"\]([^`]*)\("

    # Open the file and read its contents
    with open(file_path, "r") as file:
        data = file.read()

    # Use the regular expression pattern to find all matches in the data
    matches = re.findall(pattern, data)

    # Initialize lists for each device type
    iphones = []
    ipads = []
    apple_watches = []
    ipods = []

    # Categorize the model numbers based on device type
    for model in matches:
        model = model.strip()
        if "iPhone" in model:
            iphones.append(model)
        elif "iPad" in model:
            ipads.append(model)
        elif "Apple Watch" in model:
            apple_watches.append(model)
        elif "iPod" in model:
            ipods.append(model)

    # Return the lists for each device type
    return iphones, ipads, apple_watches, ipods

# Example usage:
# iphones, ipads, apple_watches, ipods = extract_device_models("apple_all_en.md")

# print("iPhones:", iphones)
# print("iPads:", ipads)
# print("Apple Watches:", apple_watches)
# print("iPods:", ipods)
