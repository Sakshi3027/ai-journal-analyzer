# AI Daily Journal Analyzer

A GPT-4o powered AI tool that analyzes daily journal entries to detect mood, recurring themes, and personal insights.
The project includes both a Command Line Interface (CLI) and a Streamlit Web Application for interactive analysis.

This tool helps transform unstructured journal text into meaningful reflections, enabling users to better understand their emotional patterns, thoughts, and personal growth trends.

### Features

**Mood Detection**
Automatically identifies the emotional tone of a journal entry (e.g., happy, anxious, reflective, stressed).

**Theme Extraction**
Extracts major life themes such as work, relationships, productivity, self-growth, etc.

**Insight Generation**
Provides thoughtful AI-generated observations about patterns and experiences.

**Customizable Analysis Depth**
Choose between brief or detailed analysis depending on how deep you want the reflection.

**Input Validation & Error Handling**
Ensures reliable behavior for empty inputs or API errors.

**Streamlit Web Interface**
Simple and interactive UI for analyzing journal entries without using the terminal.

### Tech Stack

Python

OpenAI API (GPT-4o)

Streamlit

python-dotenv

### Project Structure
ai-journal-analyzer
│
├── journal_analyzer.py      # Core journal analysis logic
├── streamlit_app.py         # Streamlit web interface
├── .env                     # Environment variables (API key)
├── requirements.txt         # Project dependencies
└── README.md

### Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Sakshi3027/ai-journal-analyzer.git
cd ai-journal-analyzer

2️⃣ Create a Virtual Environment
python -m venv venv


**Activate the environment:**

**Mac/Linux**

source venv/bin/activate


**Windows**

venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt


or

pip install openai streamlit python-dotenv

4️⃣ Set Up Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

▶️ Running the Application
Run the Command Line Version
python journal_analyzer.py


You will be prompted to enter your journal entry and choose the analysis depth.

Run the Streamlit Web App
streamlit run streamlit_app.py


The application will open in your browser where you can paste your journal entry and view the analysis results.

### Example Output

Detected Mood

Reflective


### Key Themes

• Personal Growth
• Work Challenges
• Self Reflection


### Insights

You appear to be reflecting on recent challenges at work while also recognizing personal progress. This indicates a growth-oriented mindset despite temporary stress.

### Future Improvements

Sentiment score visualization

Weekly mood trend dashboard

Journal entry history tracking

Export analysis to PDF

Multi-language journal support

### Author

Sakshi Chavan
MS in Data Science - University of Massachusetts Dartmouth

GitHub: https://github.com/Sakshi3027
