# Gemini AI Applications

This repository contains two Streamlit applications that use Google's Gemini AI models:

1. **Text Q&A App**: Ask questions and get answers from Gemini
2. **Image Analysis App**: Upload images for Gemini to analyze

## Setup Instructions

### Requirements
- Python 3.10 or higher
- uv package manager

### Installation

1. **Clone the repository**
   ```
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Set up environment with uv**
   ```
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install packages**
   ```
   uv pip install streamlit python-dotenv google-generativeai pillow
   ```

4. **Create a .env file**
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
   Get your API key from [Google AI Studio](https://ai.google.dev/)

## Running the Apps

### Text Q&A Application
```
streamlit run main.py
```

### Image Analysis Application
```
streamlit run vision.py
```

## How to Use

### Text Q&A App
1. Type your question in the text box
2. Click "Submit"
3. View the response

### Image Analysis App
1. (Optional) Enter a text prompt
2. Upload an image
3. Click "Tell me about this image"
4. View the analysis

## Files in this Project

- `text_app.py`: Text Q&A application
- `vision_app.py`: Image analysis application
- `.env`: Stores your API key
- `requirements.txt`: List of required packages

---