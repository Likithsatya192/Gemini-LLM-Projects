# Gemini AI Applications

This repository contains two Streamlit applications that leverage Google's Gemini AI models for text-based Q&A and image analysis.

## Applications Overview

1. **Text Q&A App**: Interact with Gemini AI by asking questions and receiving insightful answers.
2. **Image Analysis App**: Upload images to get detailed analysis and insights from Gemini AI.

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- `uv` package manager (for managing virtual environments and dependencies)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Set Up a Virtual Environment**
   Use `uv` to create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Required Packages**
   Install all necessary dependencies using `uv`:
   ```bash
   uv pip install streamlit python-dotenv google-generativeai pillow
   ```

4. **Configure API Key**
   Create a `.env` file in the project root and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
   Obtain your API key from [Google AI Studio](https://ai.google.dev/).

## Running the Applications

### Text Q&A Application
Run the text-based Q&A app with the following command:
```bash
streamlit run main.py
```

### Image Analysis Application
Run the image analysis app with this command:
```bash
streamlit run vision.py
```

## Usage Instructions

### Text Q&A App
1. Enter your question in the provided text box.
2. Click the "Submit" button.
3. View the AI-generated response below the input box.

### Image Analysis App
1. Optionally, enter a text prompt to guide the analysis.
2. Upload an image file using the upload button.
3. Click the "Tell me about this image" button.
4. View the AI's analysis and insights about the uploaded image.

## Project Files

- `main.py`: Script for the Text Q&A application.
- `vision.py`: Script for the Image Analysis application.
- `.env`: File to securely store your Gemini API key.
- `requirements.txt`: List of required Python packages.
- `pyproject.toml`: Configuration file for the `uv` package manager.
- `uv.lock`: Lock file for dependency management.

## Additional Notes
- Ensure your Python version is compatible (3.10 or higher).
- Use the `uv` package manager for seamless environment setup and dependency management.
- For any issues or questions, refer to the [Google AI Studio documentation](https://ai.google.dev/) or open an issue in this repository.