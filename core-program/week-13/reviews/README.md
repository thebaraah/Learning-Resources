# Review Spam Classifier

An exercise for classifying and removing spam reviews from a product review database using an LLM.

## Database

The database is a SQLite file (`reviews.db`) containing a single table:

### `reviews`

| Column    | Type    | Description                              |
| --------- | ------- | ---------------------------------------- |
| `id`      | INTEGER | Primary key                              |
| `author`  | TEXT    | Name or username of the reviewer         |
| `product` | TEXT    | Product name the review is about         |
| `rating`  | INTEGER | Rating from 1 to 5                       |
| `text`    | TEXT    | The review content                       |
| `is_spam` | INTEGER | Ground truth: `1` = spam, `0` = not spam |

The database contains **60 reviews** across 5 products. **15 of them are spam.**

### Products in the database

- ProChef Blender X500
- CloudWalk Running Shoes
- LuminaDesk LED Lamp
- TrueSound Wireless Earbuds
- QuickBrew Coffee Maker


## Exercise

### Goal

Write a Node.js script that:

1. Reads all reviews from the database
2. Sends each review to an LLM and asks it to classify the review as spam or not spam
3. Compares the LLM's classification to the `is_spam` column
4. Prints the results: how many reviews were correctly classified, how many were missed

### Requirements

- Use an LLM API (e.g. Ollama running locally, or an external API) to classify each review
- Do **not** send the `is_spam` column to the LLM — that is your ground truth for evaluation only

### Tips

- Think about what information to include in your prompt. Does the LLM need the author name? The rating? Or just the review text?
- Think about how to structure the LLM's response so you can parse it reliably
- Try different prompts and see how they affect accuracy
