import pandas as pd
import re

# ============================================================
# 1. LOAD DATASET
# ============================================================

file_path = "data/Resume.csv"

df = pd.read_csv(file_path)

# Fill missing resume text
df["Resume_str"] = df["Resume_str"].fillna("")


# ============================================================
# 2. RESUME CLEANING
# ============================================================

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()


df["Cleaned_Resume"] = df["Resume_str"].apply(clean_text)

print("Dataset Shape:", df.shape)

print("\nCategories:")
print(df["Category"].value_counts())

print("\nSample Cleaned Resume:")
print(df["Cleaned_Resume"].iloc[0][:500])

print("\nMissing Values:")
print(
    df[["Resume_str", "Cleaned_Resume", "Category"]]
    .isnull()
    .sum()
)


# ============================================================
# 3. SKILL EXTRACTION
# ============================================================

skills = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "data analysis",
    "data science",
    "tensorflow",
    "pytorch",
    "scikit learn",
    "pandas",
    "numpy",
    "excel",
    "communication",
    "leadership",
    "project management",
    "marketing",
    "customer service",
    "recruitment",
    "human resources",
    "accounting",
    "sales",
    "autocad",
    "javascript",
    "html",
    "css",
    "react",
    "database",
    "cloud computing"
]


def extract_skills(text):
    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return found_skills


df["Extracted_Skills"] = df["Cleaned_Resume"].apply(
    extract_skills
)

print("\nSample Extracted Skills:")
print(
    df[["Category", "Extracted_Skills"]]
    .head(10)
    .to_string(index=False)
)


# ============================================================
# 4. TARGET JOB REQUIREMENTS
# ============================================================

required_skills = [
    "python",
    "sql",
    "machine learning",
    "data analysis",
    "data science",
    "pandas",
    "numpy",
    "scikit learn"
]

print("\nTarget Job: Data Scientist")
print("Required Skills:")
print(required_skills)


# ============================================================
# 5. SKILL MATCHING
# ============================================================

def calculate_match_score(extracted_skills):
    matched_skills = set(extracted_skills).intersection(
        required_skills
    )

    score = (
        len(matched_skills) / len(required_skills)
    ) * 100

    return round(score, 2)


df["Match_Score"] = df["Extracted_Skills"].apply(
    calculate_match_score
)

print("\nSample Skill Match Scores:")
print(
    df[
        ["Category", "Extracted_Skills", "Match_Score"]
    ]
    .head(10)
    .to_string(index=False)
)


# ============================================================
# 6. CANDIDATE RANKING
# ============================================================

ranked_candidates = df.sort_values(
    by="Match_Score",
    ascending=False
).reset_index(drop=True)


# Create anonymous candidate IDs
ranked_candidates["Candidate_ID"] = [
    f"Candidate_{i:03d}"
    for i in range(1, len(ranked_candidates) + 1)
]


print("\nTop 10 Candidates:")
print(
    ranked_candidates[
        [
            "Candidate_ID",
            "Category",
            "Match_Score",
            "Extracted_Skills"
        ]
    ]
    .head(10)
    .to_string(index=False)
)


# ============================================================
# 7. SKILL GAP IDENTIFICATION
# ============================================================

def find_skill_gaps(extracted_skills):
    matched_skills = set(extracted_skills).intersection(
        required_skills
    )

    missing_skills = (
        set(required_skills) - matched_skills
    )

    return sorted(missing_skills)


ranked_candidates["Skill_Gaps"] = ranked_candidates[
    "Extracted_Skills"
].apply(find_skill_gaps)


print("\nTop 10 Candidates with Skill Gaps:")
print(
    ranked_candidates[
        [
            "Candidate_ID",
            "Match_Score",
            "Skill_Gaps"
        ]
    ]
    .head(10)
    .to_string(index=False)
)

# ============================================================
# 8. CANDIDATE RANKING VISUALISATION
# ============================================================

import matplotlib.pyplot as plt

top_candidates = ranked_candidates.head(10)

plt.figure(figsize=(10, 6))

plt.bar(
    top_candidates["Candidate_ID"],
    top_candidates["Match_Score"]
)

plt.xlabel("Candidate")
plt.ylabel("Skill Match Score (%)")
plt.title("Top 10 Candidates by Skill Match Score")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("candidate_ranking.png", dpi=300)
plt.show()

