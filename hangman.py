import random

words = ['artichoke', 'asparagus', 'aubergene', 'avocado', 'beet',
          'broccoli', 'broccolini', 'cabbage', 'carrot',
            'cauliflower', 'celery', 'chard', 'corn', 'cucumber', 'daikon', 'eggplant', 'garlic',
            'collards', 'jicama', 'kale', 'kohlrabi', 'leek', 'arugula', 'lettuce', 'mushroom',
            'okra', 'onion', 'parsnip', 'peas', 'pepper', 'potato', 'pumpkin', 'radish', 'rhubarb',
            'rutabaga', 'shallot', 'spinach', 'squash', 'tomatillo', 'tomato', 'turnip', 'zucchini']


word = random.choice(words)

if __name__ == '__main__':
    print('Hangman! HINT: Vegetable')

    for i in word:
        print('_', end=" ")
    print()