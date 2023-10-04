# Write a Python program to combine values in python list of dictionaries

def main():
    list_of_dict = [
        {"name": "John", "age": 20},
        {"name": "Mary", "age": 30},
        {"name": "Peter", "age": 40},
        {"name": "Lisa", "age": 50},
        {"name": "Sarah", "age": 60},
        {"name": "Nancy", "age": 70},
        {"name": "Karen", "age": 80},
        {"name": "Rachel", "age": 90},
        {"name": "Jennifer", "age": 100},
    ]
    print(list_of_dict)
    for i in list_of_dict:
        print(i["name"], i["age"])
        if i["name"] == "John":
            print(i["age"])

main()