import os
import pandas as pd
from resume_parser import extract_text
from summarizer import summarize_text
from matcher import match_summary_to_job
from notifier import simulate_notification
from utils import save_results

results_data = []

def main():
    resume_folder = "resumes"
    job_path = "job_description.txt"

    # Load job description once
    with open(job_path, "r") as f:
        job_description = f.read()

    # Loop through all resumes
    for filename in os.listdir(resume_folder):
        if filename.endswith(".pdf") or filename.endswith(".docx"):
            file_path = os.path.join(resume_folder, filename)
            print(f"\n🔍 Processing {filename}...")

            try:
                resume_text = extract_text(file_path)
                summary = summarize_text(resume_text)
                match_status, score = match_summary_to_job(summary, job_description)

                # Save result
                output_filename = os.path.splitext(filename)[0]
                save_results(summary, match_status, score, output_filename)

                # Prepare result for notification and CSV
                result = {
                    "filename======": filename,
                    "match_status======": match_status,
                    "score======": score,
                    "summary======": summary
                }

                results_data.append(result)
                simulate_notification(result)

            except Exception as e:
                print(f"❌ Failed to process {filename}: {e}")

    # Save all results to a CSV
    df = pd.DataFrame(results_data)
    os.makedirs("output", exist_ok=True)
    df.to_csv("output/all_results.csv", index=False)
    print("\n✅ All results saved to: output/all_results.csv")

if __name__ == "__main__":
    main()
