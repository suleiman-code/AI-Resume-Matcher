# import json
# import os

# def save_results(summary, match, score):
#     os.makedirs("output", exist_ok=True)
#     with open("output/summary.txt", "w") as f:
#         f.write(summary)
#     with open("output/result.json", "w") as f:
#         json.dump({
#             "summary": summary,
#             "match_status": match,
#             "score": score
#         }, f, indent=4)

import json
import os

def save_results(summary, match, score, filename="result"):
    os.makedirs("output", exist_ok=True)
    with open(f"output/{filename}_summary.txt", "w") as f:
        f.write(summary)
    with open(f"output/{filename}_result.json", "w") as f:
        json.dump({
            "summary": summary,
            "match_status": match,
            "score": score
        }, f, indent=4)
