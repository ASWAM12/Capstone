def generate_email(services, client_name, sender_name="Ananya"):
    templates = {
        "strategy": """• Brand positioning and messaging
• Market differentiation
• Growth roadmap and planning""",
        "analytics": """• Data analysis and interpretation
• Dashboards and reporting
• Insight generation for decisions""",
        "training": """• Team training sessions
• Tool onboarding
• Process documentation""",
    }

    sections = []
    unknown = []
    for s in services:
        key = s.strip().lower()
        if key in templates:
            sections.append(templates[key])
        else:
            unknown.append(s.strip())

    if not sections:
        return "No valid services selected. Try: strategy, analytics, training."

    services_text = "\n\n".join(sections)

    email = f"""Subject: Services Support Inquiry

Hi {client_name},

Thank you for your interest in our services. Based on your selections, we can support you with:

{services_text}

If you share your goals and timeline, I’d be happy to recommend next steps.

Best regards,  
{sender_name}
"""
    if unknown:
        email += "\n\n(P.S. I didn’t recognize: " + ", ".join(unknown) + ")"
    return email


# --- multiple input in one line ---
client = input("Client name: ")
services_raw = input("Enter services (comma-separated): ")

services_list = services_raw.split(",")  # e.g. "strategy, analytics, training"
print("\n" + generate_email(services_list, client))
