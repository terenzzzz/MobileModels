import re

def extract_xiaomi_models(file_path):
    # Define a regular expression pattern to extract model numbers
    pattern = r"\]\s*([^()]+)"

    # Open the file and read its contents
    with open(file_path, "r") as file:
        data = file.read()

    # Use the regular expression pattern to find all matches in the data
    matches = re.findall(pattern, data)

    # Initialize lists for each device type
    phone = []
    pad = []
    watch = []

    # Categorize the model numbers based on device type

    for model in matches:
        model = model.strip()
        if "Pad" in model:
            pad.append(model)
        elif "Watch" in model:
            watch.append(model)
        else:
            phone.append(model)

    # Return the lists for each device type
    return phone,pad,watch

# Example usage:
# phone, pad, watch = extract_xiaomi_models("./source/xiaomi_en.md")

# print("Phone:", phone)
# print()
# print("Pad:", pad)
# print()
# print("watch:", watch)
