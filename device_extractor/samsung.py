import re

def extract_samsung_models(file_path):
    # Define a regular expression pattern to extract model numbers
    pattern = r"\*\*(.*?)\(`"

    # Open the file and read its contents
    with open(file_path, "r") as file:
        data = file.read()
        # print(data)

    # Use the regular expression pattern to find all matches in the data
    matches = re.findall(pattern, data)

    # Initialize lists for each device type
    phone = []
    pad = []
    watch = []

    # Categorize the model numbers based on device type

    for model in matches:
        model = model.strip()
        if "Tab" in model:
            pad.append(model)
        elif "Watch" in model:
            watch.append(model)
        else:
            phone.append(model)



    # 创建一个新列表来保留原始顺序
    new_phone = []
    new_pad = []
    new_watch = []
    # 用集合来检查元素是否重复
    seen = set()

    for model in phone:
        if model not in seen:
            new_phone.append(model)
            seen.add(model)
    
    for model in pad:
        if model not in seen:
            new_pad.append(model)
            seen.add(model)

    for model in watch:
        if model not in seen:
            new_watch.append(model)
            seen.add(model)


    new_phone = [model for model in new_phone if not re.search(r'[\u4e00-\u9fff]', model)]
    new_pad = [model for model in new_pad if not re.search(r'[\u4e00-\u9fff]', model)]
    new_watch = [model for model in new_watch if not re.search(r'[\u4e00-\u9fff]', model)]

    # Return the lists for each device type
    return new_phone,new_pad,new_watch

# Example usage:
# new_phone,new_pad,new_watch = extract_samsung_models("./source/samsung_cn.md")

# print("Phone:", new_phone)
# print()
# print("Pad:", new_pad)
# print()
# print("watch:", new_watch)
