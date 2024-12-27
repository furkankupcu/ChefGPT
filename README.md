# Chef AI

Chef AI is an interactive application that offers culinary suggestions, critiques, and recipes based on user input. Users can choose between two AI personas:

1. **Turkish Chef**: An experienced and innovative Turkish chef who specializes in traditional Turkish cuisine, particularly baklava.
2. **Italian Chef**: A fun and energetic Italian chef who excels at making delicious pizza.

---

## Features
- **Dynamic Recipe Suggestions**: Get recipe ideas based on the ingredients you have.
- **Detailed Cooking Instructions**: Receive step-by-step guidance for making your favorite dishes.
- **Recipe Critique**: Submit recipes for constructive feedback and improvement suggestions.

---

## Technologies Used
- **Python 3.8+**
- **OpenAI API** for generating culinary suggestions and critiques.
- **Interactive CLI** for user-friendly interaction.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chef-ai.git
   cd chef-ai
   ```
2. Install required dependencies:
   ```bash
   pip install openai
   ```

3. Set up your OpenAI API key:
   - Obtain your API key from the [OpenAI website](https://openai.com/).
   - Add the following environment variable:
     ```bash
     export OPENAI_API_KEY='your-api-key-here'
     ```

---

## Usage

Run the main program:
```bash
python main.py
```

1. **Choose a Chef:**
   - Select between the Turkish Chef and Italian Chef.

2. **Select an Option:**
   - **Suggest a Recipe with Ingredients**: Provide available ingredients, and the AI will create a recipe for you.
   - **Get a Detailed Recipe**: Specify a dish, and the AI will provide step-by-step cooking instructions.
   - **Critique Recipes**: Input a recipe, and the AI will offer improvements.

3. **Exit**: Quit the application when done.

---

## Example

### Suggest a Recipe with Ingredients
```bash
Please enter the ingredients you want to use:
mushrooms, cheese, bread
``` 
**AI Response:**
- Suggested Dish: Mushroom and Cheese Bruschetta
- Preparation Steps:
  1. Slice the bread and toast until golden brown.
  2. Sauté the mushrooms with garlic and olive oil.
  3. Top the bread with sautéed mushrooms and grated cheese.
  4. Grill until the cheese is melted. Serve warm.

### Critique Recipes
```bash
Type in the recipes you would like to be criticized:
1. Mushroom Soup with Cream
2. Spaghetti Carbonara
``` 
**AI Response:**
- Recipe 1: Consider balancing the cream with chicken or vegetable stock for a lighter texture.
- Recipe 2: Ensure you temper the eggs correctly to avoid scrambling while mixing with hot pasta.

---

**Enjoy cooking with Chef AI!**


Muhammet Furkan Küpçü : GtCp6f 
