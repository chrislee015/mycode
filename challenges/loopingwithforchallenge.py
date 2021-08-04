farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


for animal in farms[0]["agriculture"]: 
    print(animal)

user_farm = input("choose a farm (NE Farm, W Farm, or SE Farm)")

for find in farms:
    if find["name"] == user_farm:
        print(find["agriculture"])

plants = ["bananas", "apples", "oranges","carrots","celery"]

for find in farms:
    if find["name"] == user_farm:
        for animal in find["agriculture"]:
            if animal != "bananas" and animal != "apples" and animal != "oranges" and animal != "carrots" and animal != "celery":
                print(animal)


