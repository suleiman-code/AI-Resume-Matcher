from sentence_transformers import SentenceTransformer, util

def match_summary_to_job(summary, job_description):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    summary_embed = model.encode(summary, convert_to_tensor=True)
    job_embed = model.encode(job_description, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(summary_embed, job_embed).item()
    match = "Match" if similarity > 0.6 else "No Match"
    return match, round(similarity, 2)
