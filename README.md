
# Local ATS (Applicant Tracking System) with Python & FAISS

This project is a **local** Applicant Tracking System that:
- Parses multiple PDF resumes.
- Lets you paste a job description.
- Scores resumes against the job description using **semantic similarity**.
- Runs **completely offline** with a local embedding model (`model.safetensors`).

---

## Features
- **Offline**: No cloud AI calls — works fully on your machine.
- **Fast**: Uses `all-MiniLM-L6-v2` or any local `sentence-transformers` model.
- **Scalable**: Can search thousands of resumes using FAISS.
- **Easy to Use**: Just drop your resumes in a folder and run.

---

## Requirements
- Python 3.8 or higher
- A local embedding model in `model/` (must include:
  `model.safetensors`, `config.json`, `tokenizer.json`, `tokenizer_config.json`)

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Pepperjack-svg/ATS.git
cd ATS
````

2. **Create a virtual environment**

```bash
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install --upgrade pip
pip install pdfplumber sentence-transformers faiss-cpu
```

---

## Usage

1. Place resumes in the `resumes/` folder.
2. Make sure your local embedding model is in the `model/` folder.
3. Run:

```bash
python app.py
```

4. Paste your job description when prompted (press **Enter twice** to finish).
5. Get a ranked list of matching resumes.

---

## Example Output

```
[INFO] Loading embedding model from model ...
Paste your job description below (press Enter twice to finish):
Looking for a Python developer with experience in Django and REST APIs.

[INFO] Reading resumes...
[INFO] Encoding resumes...
[INFO] Scoring resumes...

=== ATS Match Results ===
1. resume.pdf — Match Score: 89.42%
```

---

## Notes

* If you only have `model.safetensors`, download the rest of the model files from Hugging Face.
* To keep your repo small, add `venv/` and `model/` to `.gitignore`.

---

