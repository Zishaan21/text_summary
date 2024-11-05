# Text Summarization App

This repository hosts a Streamlit-based **Text Summarization App** that uses LangChain and OpenAI's API to generate concise summaries from user-provided text. The app is designed to simplify text summarization with a clean user interface and easy-to-use API integration.

## Features

- **Streamlit Interface**: The app is built with Streamlit, providing a user-friendly interface for text input and API integration.
- **OpenAI Integration**: Uses OpenAI’s language model to perform the text summarization. Simply input your OpenAI API key to get started.
- **LangChain and Map-Reduce Chain**: Utilizes LangChain’s `load_summarize_chain` function, with a `map_reduce` chain type, for efficient summarization.
- **Text Splitting for Large Inputs**: Text is split into smaller chunks for better summarization accuracy, ideal for handling longer text inputs.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/text-summarization-app.git
   cd text-summarization-app
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

4. **Enter Text and API Key**:
   - Input your text for summarization in the text area.
   - Provide your OpenAI API key.
   - Click **Submit** to generate the summary.

## Requirements

- Python 3.x
- [Streamlit](https://streamlit.io)
- [OpenAI API Key](https://openai.com) (required for summarization)
- LangChain library

## Example

After entering text and your OpenAI API key, the app will provide a summarized output based on the content you've provided.

---

Feel free to fork or modify the app to fit your own needs! Contributions and suggestions are welcome.

