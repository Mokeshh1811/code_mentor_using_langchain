# Code Mentor 🧑‍🏫🧑‍💻

Code Mentor is a Streamlit-based application designed to help programmers analyze and improve their code snippets using the power of Google's Gemini AI (LangChain Google Generative AI). This tool provides strengths, identifies weaknesses, and suggests improvements for code written in various programming languages.

## Features

- **Code Analysis**: Get insights into the strengths and weaknesses of your code.
- **Code Improvement Suggestions**: Receive AI-generated recommendations to enhance your code quality.
- **Multi-Language Support**: Works with popular programming languages including Python, JavaScript, Java, C++, Ruby, Go, Swift, and C#.
- **User-Friendly Interface**: Simple and intuitive interface using Streamlit.

## How It Works

1. Select a programming language from the sidebar.
2. Paste your code snippet into the provided text area.
3. Click the "Submit" button.
4. View the analysis, including strengths, weaknesses, and suggestions for improvement.

## Requirements

- Python 3.8 or later
- Streamlit
- LangChain
- Google Generative AI API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/code-mentor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd code-mentor
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your Google Generative AI API key:
   Replace the placeholder in `application.py` with your API key:
   ```python
   api_key = "your-google-api-key"
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run application.py
   ```
2. Open the app in your browser and start analyzing your code.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any questions or suggestions, feel free to reach out at mokesh1811@example.com.
