import os
import pdfplumber
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# ---------- CONFIG ----------
RESUME_FOLDER = "resumes"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
# ----------------------------

# Load model
print("[INFO] Loading embedding model...")
model = SentenceTransformer(EMBEDDING_MODEL)

# Extract text from PDF
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return " ".join(page.extract_text() or "" for page in pdf.pages)

# Get job description from user
print("\nPaste your job description below (press Enter twice to finish):")
lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)
job_text = " ".join(lines)

# Encode job description
job_embedding = model.encode(job_text, convert_to_tensor=False)

# Read resumes
resume_texts = []
resume_names = []
print("\n[INFO] Reading resumes...")
for filename in os.listdir(RESUME_FOLDER):
    if filename.lower().endswith(".pdf"):
        path = os.path.join(RESUME_FOLDER, filename)
        text = extract_text_from_pdf(path)
        resume_texts.append(text)
        resume_names.append(filename)

if not resume_texts:
    print("[ERROR] No PDF resumes found in 'resumes' folder.")
    exit()

# Encode resumes
print("[INFO] Encoding resumes...")
resume_embeddings = model.encode(resume_texts, convert_to_tensor=False)

# Create FAISS index
embedding_dim = resume_embeddings.shape[1]
index = faiss.IndexFlatIP(embedding_dim)  # Inner product for cosine similarity

# Normalize for cosine similarity
faiss.normalize_L2(resume_embeddings)
faiss.normalize_L2(job_embedding.reshape(1, -1))

# Add to index
index.add(resume_embeddings)

# Search
print("[INFO] Scoring resumes...")
scores, ids = index.search(job_embedding.reshape(1, -1), len(resume_names))

# Show results
print("\n=== ATS Match Results ===")
for rank, (idx, score) in enumerate(zip(ids[0], scores[0]), start=1):
    print(f"{rank}. {resume_names[idx]} — Match Score: {score*100:.2f}%")
