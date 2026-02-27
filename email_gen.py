import textwrap


def generate_email(services, client_name, sender_name="Angela Neal"):
    templates = {
        "Strategy": textwrap.dedent("""\
**Strategy** - We partner with clients to define a clear, actionable path forward.
By understanding your goals, budget, and operational bandwidth, we develop data-driven strategies
that align marketing, technology, and design into a cohesive roadmap. From forecasting and 
projections to performance reporting, our strategic planning ensures every initiative moves your 
organization closer to its long-term vision. Training and workshops are available to help teams 
confidently execute and sustain strategic initiatives."""),
        "Marketing": textwrap.dedent("""\
**Marketing** - We craft purposeful marketing strategies that connect brands to the right 
audiences with clarity and consistency. From brand positioning and messaging to organic, 
paid, and social campaigns, we recommend and execute the platforms and tactics best suited 
to your goals. Our approach ensures every campaign works toward a unified objective. We 
also provide hands-on training and workshops to empower teams to maintain strong, consistent 
brand presence."""),
        "Technology": textwrap.dedent("""\
**Technology** - We design and implement technology solutions that simplify processes and 
make data work for you. From building forms and databases to automating workflows and 
aligning key data points, we create systems that are efficient, scalable, and 
user-friendly — even for non-technical teams. Our training programs and workshops ensure 
clients feel confident using and managing their technology solutions long after implementation."""),
        "Design": textwrap.dedent("""\
**Design** - We develop thoughtful, research-driven creative that strengthens brand identity and visual 
impact. From logos and corporate identity systems to publications, motion graphics, and digital assets, 
our design work blends strategy with the psychology of color and visual storytelling. Using 
industry-leading tools, we create distinctive brands that resonate. Training and workshops are also 
offered to help teams understand and consistently apply brand standards."""),
    }

    also_templates = {
        "Strategy": "**With Strategy** - We help organizations define clear goals and actionable roadmaps, with workshops and training to support team execution.",
        "Marketing": "**With Marketing** - We create cohesive brand messaging and campaign strategies, supported by training and workshops to empower your team.",
        "Technology": "**With Technology** - We provide solutions to streamline processes, organize data, and automate workflows, with training to ensure your team can make the most of them.",
        "Design": "**With Design** - We craft unique visual identities and branded assets, with workshops to help your team consistently apply your brand standards.",
    }

    sections = []
    unknown = []

    for s in services:
        key = s.strip()
        if key in templates:
            sections.append(templates[key])
        else:
            unknown.append(s.strip())

    if not sections:
        return "No valid services selected. Try: Strategy, Marketing, Technology, Design."

    services_text = "\n\n".join(sections)

    # Find unselected services (this MUST be inside the function)
    unselected = [s for s in templates.keys() if s not in services]

    also_available = ""
    if unselected:
        also_blurbs = "\n\n".join(
            f"{also_templates[s]}" for s in unselected
        )
        also_available = f"\n\n---\n\n**Also Available:**\n\n{also_blurbs}"

    email = f"""Subject: Services Support Inquiry

Hi {client_name},

Thank you for your interest in our services. Based on your selections, we have provided further information on them below: 

{services_text}{also_available}

If you share your goals and timeline, I’d be happy to recommend next steps.

Best regards,  

{sender_name}
"""

    if unknown:
        email += "\n\n(P.S. I didn’t recognize: " + ", ".join(unknown) + ")"

    return email


# Optional: export the service keys so UI stays in sync
SERVICE_OPTIONS = ["Strategy", "Marketing", "Technology", "Design"]