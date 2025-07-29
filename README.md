# Blog Generator using Llama 2

A Streamlit web application that generates customized blog posts using Meta’s Llama 2 large language model, integrated via Ollama and LangChain.

---

## 🚀 Features

- Generate blog posts by specifying topic, target audience, and desired length.
- Powered by the Llama 2 (7B) model running locally via Ollama.
- Simple, clean user interface built with Streamlit.
- Customizable prompts managed with LangChain.

---

## 💻 Tech Stack

- Python 3.10+
- Streamlit (UI Framework)
- LangChain & langchain-community 
- Ollama (Local Llama 2 model runtime)

---

## 🔧 How to Run Locally

1. **Clone the repository:**
```bash
git clone https://github.com/BasutkarSony/Blog-Generator-using-Llama2.git
cd Blog-Generator-using-Llama2


2. **Install Ollama:**

- Download and install from [https://ollama.com/download](https://ollama.com/download)
- Verify with:

  ```
  ollama --version
  ```

3. **Create and activate virtual environment:**

On Windows:
```
python -m venv .venv
venv\Scripts\activate
```


On macOS/Linux:
```
python -m venv .venv
source venv/bin/activate
```

4. **Install required dependencies:**

```
pip install -r requirements.txt
```

5. **Download the Llama 2 model (7B) using Ollama:**

```
ollama pull llama2:7b
``` 

6. **Run the Streamlit app:**
```
streamlit run app.py
```
## 📝 Usage

- Enter your blog topic.
- Select your target audience from predefined options.
- Choose the number of words (up to 500).
- Click **Generate Blog** to receive a tailored blog post.

---

## 🚀 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-blog-generator-app.streamlit.app/)


---

## 📸 Screenshot

![App Screenshot](screenshot.png)  
*Sample user interface of the Blog Generator app.*

---
## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Happy blogging with AI! 🤖*