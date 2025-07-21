# GenAI Assistant with and LangChain

This project is a simple web application that allows users to interact with a local open-source Large Language Model (LLM) powered by Ollama. The application is built using Streamlit and LangChain, providing an intuitive interface for generating intelligent responses to user queries.

## Features
- **Local LLM Integration**: Powered by Ollama's `gemma:2b` model.
- **Streamlit Interface**: A user-friendly web interface for asking questions and receiving responses.
- **Customizable Prompts**: Easily modify the assistant's behavior by changing the system prompt.

## Prerequisites
1. **Ollama Installation**: Ensure that Ollama is installed on your system. You can download it from [Ollama's official website](https://ollama.ai/).
2. **Python**: Python 3.8 or higher is required.
3. **Environment Variables**: Create a `.env` file in the project root with the following variables:
   - `LANGCHAIN_API_KEY`: Your LangChain API key (if required).
   - `LANGCHAIN_PROJECT`: (Optional) The name of your LangChain project.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Sri-Galaxy/Simple-LLM_APP_with_Ollama.git
   cd Simple-LLM_APP_with_Ollama
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the Streamlit application:
   ```bash
   streamlit run main.py
   ```
2. Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
3. Enter your question in the input box and get responses from the LLM.

## Notes
- Ensure that Ollama is running and properly configured on your system before starting the application.
- The `gemma:2b` model is used by default. You can modify this in the `build_chain` function in `main.py`.


## Acknowledgments
- [Ollama](https://ollama.ai/) for providing the LLM.
- [Streamlit](https://streamlit.io/) for the web application framework.
- [LangChain](https://www.langchain.com/) for the powerful chain-building tools.
