def check_scam(text):
    scam_keywords = [
        "registration fee",
        "security deposit",
        "pay before joining",
        "urgent joining",
        "no interview required",
        "processing fee"
    ]

    text_lower = text.lower()

    found_keywords = []

    for word in scam_keywords:
        if word in text_lower:
            found_keywords.append(word)

    score = (len(found_keywords) / len(scam_keywords)) * 100

    if score >= 50:
        level = "HIGH"
        message = "⚠️ HIGH SCAM RISK"
    elif score >= 20:
        level = "MEDIUM"
        message = "⚠️ MEDIUM RISK"
    else:
        level = "LOW"
        message = "✅ LOW RISK (Likely Genuine)"

    return message, score, found_keywords, level