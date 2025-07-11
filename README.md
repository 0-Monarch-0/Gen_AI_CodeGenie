# 🧠 CodeGenie: AI-Powered Code Generator

CodeGenie is an AI-based web application that allows users to convert natural language prompts into fully functional code snippets using state-of-the-art language models. Built using **Streamlit** and **Hugging Face Transformers**, CodeGenie supports multiple programming languages including **Python, Java, C, and C++**.

---

## 🚀 Features

- 🌐 **Web Interface**: A simple and intuitive UI built with Streamlit.
- ✨ **Natural Prompt Input**: Type what you want to build, and let the AI generate code.
- 🧠 **Model Powered**: Uses Hugging Face’s `Salesforce/codegen-350M-multi` model for multilingual code generation.
- 🔧 **Multiple Language Support**: Supports Python, Java, C, and C++.
- 💡 **Sidebar Guide**: Built-in usage guide with supported languages and example prompts.
- 🛑 **Graceful Shutdown**: In-app shutdown of the Streamlit server.
- 📊 **Execution Time Tracker**: Know how long it took to generate your code.

---

## 📸 Screenshots

<p align="center">
  <img src="https://github.com/0-Monarch-0/Gen_AI_CodeGenie/blob/main/demo.PNG?raw=true" alt="Main Interface" width="700"/>
</p>

---

## 🎥 Demo Video

Watch the working demo of CodeGenie in action here:  
🔗 [CodeGenie Demo Video](https://drive.google.com/file/d/1LrnzihiA0I025dSwsyOQ6CIVgjCOsmuI/view?usp=sharing)

---

## 📄 Project Report

The detailed project report includes problem statement, objectives, tools and technologies, project architecture, code structure, features, limitations, and contributions.

📥 [View the Full Report](https://github.com/0-Monarch-0/Gen_AI_CodeGenie/blob/main/CodeGenie_Project_Report.docx)

---

## 🧪 Try it on Google Colab

You can try the complete working of this project in Colab here:  
🔗 [Open in Google Colab](https://colab.research.google.com/drive/1P9hAR1CEldBwnsWNMCdcL4-JafJROh9Z?usp=sharing)

---

## 🛠 Tech Stack

| Tool                        | Purpose                                  |
|-----------------------------|------------------------------------------|
| `Python`                   | Backend logic                            |
| `Streamlit`                | Frontend and UI                          |
| `transformers`             | Model loading and inference              |
| `Salesforce/codegen-350M-multi` | Pre-trained code generation model |
| `LocalTunnel`              | To expose the app to the public web      |

---

## 📂 Project Structure

Gen_AI_CodeGenie/
├── app.py # Streamlit frontend
├── CodeModel.py # Code generation logic
├── logs.txt # Server logs
├── README.md # Project documentation
