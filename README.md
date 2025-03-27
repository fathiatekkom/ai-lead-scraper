# AI Lead Scraper by Fathia Alfajr

A lightweight Streamlit app built to help you:
- Scrape **emails**, **socials**, and **summaries** from websites
- Customize what to extract using **web scraping or AI prompts**
- Upload CSVs and export clean results in seconds!

---

## 🚀 Features

- 🔗 **Manual input** or **CSV upload** of website links  
- ✉️ Extracts emails and social links automatically  
- 🧠 AI-generated summary of each website  
- 🧩 Add your own custom fields:
  - **Web scraping** using CSS selectors or a keyword
  - **AI assistant** that answers the questions with one-two sentences explanation
  - Automatically marks leads as “Qualified” when emails are found
- 🧹 Intuitive checkbox delete (like Gmail)  
- 📦 Download results to CSV  

---

## 🎥 Demo Video

[![Watch the demo](https://img.youtube.com/vi/JSVns08Ctz0/0.jpg)](https://youtu.be/JSVns08Ctz0)

This short demo shows how the tool extracts emails, social links, and generates AI summaries to qualify leads.

---

## 🖥️ How It Works

1. **Manual Input**  
   Go to `Manual Website Input` → type website URLs and run scraping.

2. **CSV Upload**  
   Upload a `.csv` file with a `Website` column via the `CSV Upload` page.

3. **Add Custom Columns**  
   Use the `Settings` page to add:
   - Web scraping fields using CSS selectors (e.g. `meta[name='author']`)
   - AI assistance fields using prompts (e.g. "Does this company offer a virtual assistant?")

4. **View & Download**  
   Check results on the same page. Select rows to delete or export to CSV.

---

## 📂 File Structure
```csv
ai-lead-scraper/
├── pages/
│   ├── manual_input.py      # Manual website input and scraping UI
│   ├── csv_input.py         # Upload websites via CSV
│   └── settings.py          # Add custom columns with Web/AI assistance modes
├── utils/
│   ├── processor.py         # Core scraping + AI column logic
│   ├── scraping.py          # Email, social, and about section scraping (these are the default columns)
│   └── ai_helpers.py        # Together.ai-based assistance
├── .env                     # Storing the API key
└── requirements.txt         # Python dependencies
```

---

## 📄 Example CSV Format
```csv
Website
https://tokopedia.com
https://www.ibm.com/id-id
https://ui.ac.id
```
---

## 🔧 Setup Instructions

```bash
git clone https://github.com/fathiatekkom/ai-lead-scraper.git
cd ai-lead-scraper

pip install -r requirements.txt

# Add your Together.ai key
echo "TOGETHER_API_KEY=your-key-here" > .env

# Run the app
streamlit run pages/manual_input.py

🗝️ Don't have a Together.ai key yet?  
> Go to [https://www.together.ai](https://www.together.ai) → Sign up → Go to your dashboard → Copy your API key.

```

## 🧠 AI Model

- Model: `mistralai/Mixtral-8x7B-Instruct-v0.1`  
- Provider: [Together.ai](https://together.ai/)  
- Use: Generating summary & answering prompt-based questions

## 🤝 Credits

Made by **Fathia Alfajr**  
Built in just **5 hours** ⏱️ using Python, Pandas, Streamlit, BeautifulSoup Web Scraper, and Together.AI API.
