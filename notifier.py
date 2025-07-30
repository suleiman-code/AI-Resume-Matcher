def simulate_notification(result):
    print("🔔 Simulated Notification:")
    print(f"Summary: {result['summary'][:100]}...")
    print(f"Match Status: {result['match_status']}")
    print(f"Score: {result['score']}")

    if result['match_status'] == "Match":
        print("✅ Candidate is a good fit. Message sent to HR via WhatsApp/Email (simulated).")
    else:
        print("❌ Candidate doesn't match well. No alert sent (simulated).")
