from openai import OpenAI

#client = OpenAI()
model = "gpt-3.5-turbo"

messages = [
     {
          "role": "system",
          "content": "An young Italian chef who loves making Pizza."
     }
]

def suggest_recipe_with_ingredients():
    ingredients = input("Please enter the ingredients you want to use:\n")
    messages.append(
        {
            "role": "user",
            "content": f"Suggest a detailed recipe that I can make with {ingredients}."
        }
    )

def suggest_detailed_recipe():
    dish = input("Please type the name of the dish you want a recipe for:\n")
    messages.append(
        {
            "role": "user",
            "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}."
        }
    )

def critique_recipes():
    recipes = input("Type in the recipes you would like to be criticized:\n")
    messages.append(
        {
            "role": "user",
            "content": f"Critique {recipes} recipes."
        }
    )

while True:
    
    print("1. Suggest a recipe with ingredients")
    print("2. Suggest a detailed recipe for a dish")
    print("3. Critique recipes")
    print("4. Exit")
        
    choice = input("Please enter a choice number: ")
        
    if choice == "1":
        suggest_recipe_with_ingredients()
    elif choice == "2":
        suggest_detailed_recipe()
    elif choice == "3":
        critique_recipes()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("You entered an invalid choice, please try again.")

    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )