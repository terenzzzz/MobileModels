import re

def extract_google_models(file_path):
    # Define a regular expression pattern to extract model numbers
    pattern = r"\*\*([^`]+)\(`"

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
        if "Tablet" in model:
            pad.append(model)
        elif "Watch" in model:
            watch.append(model)
        elif "Pixel" in model:
            phone.append(model)

    # Return the lists for each device type
    return phone,pad,watch

# Example usage:
# phone,pad,watch = extract_google_models("./source/google.md")

# print("Phone:", phone)
# print()
# print("Pad:", pad)
# print()
# print("watch:", watch)
