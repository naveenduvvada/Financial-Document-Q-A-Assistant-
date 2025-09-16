# 📊 Financial Document Q&A Assistant  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)  
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)  
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-green)  
![Status](https://img.shields.io/badge/Status-Prototype-yellow)  

A **Streamlit-based web application** that allows users to upload **financial documents (PDF & Excel)** and ask **natural language questions** about key financial metrics such as **revenue, expenses, profit, assets, liabilities, and cash flow**.  

![Demo Screenshot](<img width="1918" height="1018" alt="Screenshot 2025-09-16 115318" src="https://github.com/user-attachments/assets/51158a42-4bd8-4ca6-88de-b60db00353e7" />
)  

---

## 🚀 Features  
✅ Upload **PDF and Excel financial statements**  
✅ Extract **text, tables, and numerical data**  
✅ Ask financial questions in **plain English**  
✅ Hybrid **Rule-based + Ollama Local LLM** Q&A  
✅ Interactive **chat-style UI** (like ChatGPT)  
✅ Works **fully offline** with local deployment  

---

## 🛠️ Tech Stack  
- **Python** (pandas, pdfplumber, openpyxl)  
- **Streamlit** (frontend web UI)  
- **Ollama** (local small language model for Q&A)  
- **Requests** (API integration)  

---

## 📂 Project Structure  
```
financial-doc-qa/
│── app.py              # Streamlit main app
│── extract.py          # PDF & Excel extraction
│── qa.py               # Question-answering logic
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```

---

## ⚡ Setup & Installation  

### 1. Clone the repository  
```bash
git clone https://github.com/your-username/financial-doc-qa.git
cd financial-doc-qa
```

### 2. Create virtual environment & install dependencies  
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

### 3. Start Ollama locally  
Make sure Ollama is installed and running in the background. Example (using `llama2`):  
```bash
ollama run llama2
```

### 4. Run the app  
```bash
streamlit run app.py
```

---

## 📊 Example Usage  
Upload a **financial PDF or Excel** (e.g., `sample_financials.pdf`) and try asking:  
- *“What is the revenue?”*  
- *“Show me the net profit.”*  
- *“What are the total assets and liabilities?”*  

📄 Example sample file: [sample_financials.pdf](sandbox:/mnt/data/sample_financials.pdf)  

---

## 🖼️ Screenshots  

### Upload Document  
![Upload Screenshot](https://via.placeholder.com/800x300.png?text=Upload+Financial+Document)  

### Ask Questions  
![Chat Screenshot](https://via.placeholder.com/800x300.png?text=Ask+Questions+About+Revenue+Expenses+Profit)  

---

## 📤 Submission  
This repo contains:  
- `app.py` → Streamlit UI  
- `extract.py` → PDF/Excel processing  
- `qa.py` → Q&A with Ollama integration  
- `requirements.txt` → Python dependencies  
- `README.md` → Documentation  

---

✨ Developed as part of an **assignment project** to demonstrate document processing + natural language Q&A.  
