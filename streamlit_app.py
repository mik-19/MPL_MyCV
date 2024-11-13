# Import necessary libraries
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, ListFlowable, ListItem, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
import io

# ===========================
# Configuration & CV Data
# ===========================

# ---------------------------
# Header Information
# ---------------------------
header_info = {
    'name': "Mikaël Pelletier Lachapelle",
    'address': "53, Rue Grove, Danville, Quebec J0A 1A0",
    'phone': "819-740-6080",
    'email': "mikael.pelletier_lachapelle@telus.com",
    'languages': "Fluent in English and French"
}

# ---------------------------
# Professional Summary
# ---------------------------
professional_summary = {
    'concise': """
Versatile and analytically driven professional with over a decade of experience at TELUS, focusing on operational efficiency and customer experience. Proven track record in managing high-stakes escalations and improving operational processes through data-driven insights. Proficient in Microsoft Office Suite with advanced Excel skills. Self-taught in Python programming with focus on data analysis and insights generation. Bilingual in English and French, with a strong understanding of the wireless industry and a proactive mindset for continuous improvement.
""",
    'detailed': """
As a dedicated professional with over 10 years at TELUS, I have consistently demonstrated my ability to enhance operational efficiency and elevate customer experiences. My expertise lies in managing complex escalations, leading teams, and implementing process improvements that drive results. Through data analysis and interpretation, I leverage my skills to provide strategic insights and actionable solutions. My self-driven journey into Python programming has equipped me with the tools to perform advanced data analysis, enabling data-driven decision-making. My bilingual proficiency allows me to communicate effectively with a diverse range of clients and colleagues.

<b>Professional Experience Highlights:</b>
- Completing the <b>Business Analyst Development Program</b> at TELUS, enhancing my analytical and strategic planning skills
- Over a decade of progressive roles at TELUS, from Sales Representative to Operations Manager
- Proven ability to lead teams, manage high-stakes escalations, and drive operational efficiencies
"""
}

# ---------------------------
# Education and Qualifications
# ---------------------------
education = [
    {
        'degree': "Business Analyst Development Program",
        'institution': "TELUS",
        'date': "Completed September 2024",
        'description': "Developed skills in business analysis, data interpretation, and strategic planning."
    },
    {
        'degree': "Programme de Qualifications en Assurance de Personnes",
        'institution': "Services Financiers Primerica Ltée",
        'date': "2019",
        'description': "Gained knowledge in personal insurance qualifications and financial services."
    },
    {
        'degree': "Leadership Essentials",
        'institution': "The Ken Blanchard Companies",
        'date': "2018",
        'description': "Enhanced leadership skills and team management capabilities."
    },
    {
        'degree': "TELUS Leadership Development Program",
        'institution': "TELUS Retail",
        'date': "2014",
        'description': "Completed internal leadership training program."
    },
    {
        'degree': "Diplôme d'Aptitude aux Fonctions d’Animateur",
        'institution': "Projet Jeunesse de Richmond",
        'date': "2012",
        'description': "Qualified in youth animation and mentoring."
    },
    {
        'degree': "Special Care Counselling (Incomplete)",
        'institution': "Champlain Regional College",
        'date': "2012",
        'description': "Studied special care counselling."
    }
]

# ---------------------------
# Professional Experience
# ---------------------------
professional_experience = [
    {
        'title': "Operations Manager - Executive Escalations",
        'company': "TELUS",
        'dates': "May 2022 - Present",
        'summary': "Manage executive-level escalations for TELUS WLS Business customers, ensuring swift and satisfactory resolutions.",
        'responsibilities': [
            "Advocate for TELUS' WLS Business customers to resolve escalations",
            "Manage regulatory, legal, and media threat escalations",
            "Conduct root cause analysis and provide strategic insights",
            "Assess, track, and monitor customer incidents to ensure timely resolution",
            "Demonstrate strong problem-solving and negotiation skills",
            "Prioritize work among competing demands to meet customer expectations",
            "Serve as a Subject Matter Expert, coaching team members and driving ownership"
        ],
        'additional_projects': [
            "Created Python tools to analyze escalation data and identify trends",
            "Maintained and enhanced the Escalation Volume Tracker with detailed breakdowns",
            "Conducted comprehensive analysis of credit reduction impacts on escalations",
            "Performed analysis of temp check process, leading to workflow improvements",
            "Gathered insights on return exception scenarios across multiple teams"
        ]
    },
    {
        'title': "Store Manager",
        'company': "TELUS",
        'dates': "September 2014 - May 2022",
        'summary': "Led store operations, ensuring exceptional customer satisfaction and team performance.",
        'responsibilities': [
            "Ensured customer satisfaction and achieved sales targets.",
            "Led team projects and performed administrative tasks including scheduling and sales analysis.",
            "Acted as Area Prime on various projects, enhancing operations and compliance.",
            "Developed tools and strategies for Workforce Management to facilitate operations.",
            "Implemented process improvements to reduce human error and increase productivity.",
            "Supported the Outbound Direct Fulfillment (OBDF) initiative during COVID-19.",
            "Provided guidance on best practices and CRM call list management."
        ]
    },
    {
        'title': "Sales Representative",
        'company': "TELUS",
        'dates': "January 2013 - September 2014",
        'summary': "Executed sales strategies to meet and exceed targets while providing excellent customer service.",
        'responsibilities': [
            "Executed sales strategies to meet and exceed targets.",
            "Provided comprehensive support and training to customers.",
            "Identified customer needs and offered tailored solutions.",
            "Built strong customer relationships leading to repeat business."
        ]
    }
]

# ---------------------------
# Skills and Personal Qualities
# ---------------------------
skills_and_qualities = [
    "Data Analysis & Interpretation",
    "Microsoft Office Suite (Advanced Excel)",
    "Python Programming (Self-taught)",
    "Business Intelligence: DOMO, Salesforce Reporting",
    "Project Management & Process Improvement",
    "Customer Relationship Management",
    "Strategic Communication & Collaboration",
    "Problem-Solving & Root Cause Analysis",
    "Leadership and Mentorship",
    "Adaptable and Resilient",
    "Proactive in Continuous Learning"
]

# ---------------------------
# Key Achievements and Projects
# ---------------------------
key_achievements_and_projects = {
    'concise': [
        "Developed a Sales Tracker tool improving sales performance monitoring.",
        "Improved Trade-In process, reducing inaccuracies and increasing revenue.",
        "Self-taught Python programming for data analysis and insights generation.",
        "Supported the OBDF initiative during COVID-19, enhancing remote operations.",
        "Created escalation analysis tools to identify trends and improve processes.",
        "Developed a website for spouse's business, enhancing online presence.",
        "Self-taught mechanics, enabling successful operation of own repair business."
    ],
    'detailed': [
        {
            'title': "Sales Tracker Development",
            'details': [
                "Collaborated to develop a comprehensive Sales Tracker tool.",
                "Enabled managers to monitor multiple store locations effectively.",
                "Provided detailed views for representative-level performance by day, week, and month.",
                "Implemented metrics tracking for both qualitative and quantitative indicators.",
                "Developed reports and dashboards in DOMO for rep, store, and area-level metrics."
            ]
        },
        {
            'title': "Trade-In Process Improvement",
            'details': [
                "Developed process documentation to reduce trade-in shipping inaccuracies.",
                "Implemented a zero-cost initiative leveraging existing teams.",
                "Improved tracking and accountability, decreasing lost revenue from inaccuracies.",
                "Enhanced packaging protocols using recycled materials at no additional cost."
            ]
        },
        {
            'title': "Self-Learning and Continuous Improvement",
            'details': [
                "Self-taught Python programming through prompt engineering and generative AI.",
                "Applied programming skills to data analysis and process automation.",
                "Developed a website for spouse's business, enhancing its online presence.",
                "Self-taught mechanics, operating a successful ATV and small engine repair business.",
                "Committed to lifelong learning, dedicating time daily to skill development."
            ]
        },
        {
            'title': "Escalation Analysis Tools",
            'details': [
                "Created Python tools to analyze escalation data and identify trends.",
                "Implemented text analysis features like word clouds and frequency analysis.",
                "Generated weekly insights reports highlighting common escalation drivers.",
                "Provided actionable insights leading to process improvements."
            ]
        },
        {
            'title': "Credit Reduction Impact Analysis",
            'details': [
                "Analyzed escalation data from January to October 2024 to assess impact of credit policy changes.",
                "Identified 1,063 credit-related escalations (35.9% of all cases).",
                "Categorized main drivers: Internal audit-related issues (58.3%), Sales offers (36.9%), Policy changes/BSR (4.8%).",
                "Discovered 21% of cases were repeat escalations.",
                "Provided actionable insights for strategic decision-making regarding credit policies.",
                "Developed comprehensive reports with visualizations to support findings."
            ]
        },
        {
            'title': "Temp Check Analysis",
            'details': [
                "Performed comprehensive business analysis for processes like 'temp check'.",
                "Led to streamlined workflows and substantial decrease in escalations.",
                "Implemented data-driven strategies to enhance operational efficiency."
            ]
        },
        {
            'title': "Return Exception Data Gathering",
            'details': [
                "Gathered various data points by reviewing cases from other managers and the tier one escalation team.",
                "Compiled insights to understand common scenarios in using the return exception process.",
                "Provided comprehensive insights for process improvement and better handling of return exceptions."
            ]
        }
    ]
}

# ---------------------------
# Cover Letter
# ---------------------------
cover_letter = """
53, Rue Grove  
Danville, Quebec J0A 1A0  
819-740-6080  
mikael.pelletier_lachapelle@telus.com  

November 13, 2024

Dear Hiring Manager,

I am writing to express my enthusiastic interest in the **Business Analyst II - 44731** position within TELUS's Marketing team. With over a decade of experience at TELUS, specializing in operational efficiency and customer experience, I am confident in my ability to contribute effectively to your team and drive impactful results.

In my current role as **Operations Manager - Executive Escalations**, I have honed my skills in managing complex escalations, conducting root cause analysis, and implementing data-driven process improvements. My proactive approach and ability to collaborate with diverse stakeholders have been instrumental in achieving a 600% reduction in payroll inaccuracies and streamlining workflows to enhance operational efficiency.

The **Business Analyst II** role excites me as it aligns perfectly with my expertise in business analysis, data interpretation, and strategic planning. I am particularly drawn to the opportunity to support Channel Partners and Internal Stakeholders, driving operational efficiencies within Supply Operations. My proficiency in tools such as DOMO, Salesforce Reporting, and my self-taught Python programming skills enable me to process complex data, generate insightful reports, and implement effective solutions.

I am highly detail-oriented, organized, and possess exceptional analytical skills, which I have consistently applied to improve E2E processes and manage transactional reports. My experience in generating system reports, supporting step-by-step process documentation, and handling special requests has prepared me to excel in this role. Additionally, my ability to embrace and adapt to change in a continuous learning environment ensures that I stay ahead of industry trends and best practices.

I am particularly impressed by TELUS's commitment to innovation and excellence, and I am eager to leverage my skills in business analysis and strategic communication to contribute to the success of the Marketing team. My proven ability to work collaboratively in a lean, agile environment and my sense of urgency in driving issues to closure make me a strong fit for this position.

Thank you for considering my application. I look forward to the opportunity to discuss how my background, skills, and passions align with the goals of TELUS and how I can contribute to the continued success of your team.

Sincerely,  
Mikaël Pelletier Lachapelle
"""

# ===========================
# Streamlit App Configuration
# ===========================

# Set page configuration
st.set_page_config(
    page_title=f"{header_info['name']} - Professional CV",
    page_icon=":briefcase:",
    layout="wide",
)

# Apply custom styles
def apply_custom_styles():
    custom_css = """
    <style>
    /* General Styling */
    body {
        font-family: 'Arial', sans-serif;
        color: #333333;
    }
    
    /* Navigation Styling */
    .css-1544g2n {  /* This targets Streamlit's sidebar */
        background-color: #4B286D;
        padding: 1rem;
        width: 100% !important;
    }
    
    .css-1544g2n .stRadio {
        color: white !important;
    }
    
    /* Radio button text color */
    .stRadio label {
        color: white !important;
    }
    
    /* Selected radio button color */
    .stRadio input:checked + label {
        color: #ffffff !important;
        font-weight: bold;
    }
    
    /* Header */
    .header-title {
        color: #4B286D;
        font-size: 24px;
        font-weight: bold;
        text-align: left;
    }
    
    .header-details {
        text-align: right;
        margin-bottom: 10px;
        font-size: 12px;
    }
    
    /* Section Headers with full purple bar */
    .section-header {
        background-color: #4B286D;
        color: white;
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
        padding: 5px 10px;
        width: 100%;
    }
    
    /* Professional Experience Layout */
    .experience-container {
        display: flex;
        gap: 20px;
    }
    
    .experience-column {
        flex: 1;
        padding: 10px;
    }
    
    /* Subsection Headers */
    .subsection-header {
        color: #4B286D;
        font-size: 16px;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    
    /* Bullet Points */
    ul {
        list-style-type: disc;
        margin-left: 20px;
    }
    
    /* Two Column */
    .two-column {
        display: flex;
        flex-wrap: wrap;
    }
    .two-column > div {
        width: 50%;
    }
    
    /* Line Separator */
    hr {
        border: 0;
        height: 1px;
        background: #4B286D;
        margin: 20px 0;
    }
    
    /* Expandable Sections */
    .streamlit-expanderHeader {
        color: #4B286D;
        font-weight: bold;
        background-color: #F7F7F7;
    }
    
    /* Cover Letter Styling */
    .cover-letter {
        white-space: pre-wrap;
        line-height: 1.6;
        padding: 20px;
        background-color: #F7F7F7;
        border-radius: 4px;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# ===========================
# Streamlit App Functions
# ===========================

def header_section(left_aligned=True):
    # Single column, all left-aligned
    st.markdown(f"""
        <div style='text-align: left;'>
            <div class='header-title'>{header_info['name']}</div>
            <div class='header-details' style='text-align: left;'>
                {header_info['address']}<br>
                {header_info['phone']}<br>
                {header_info['email']}<br>
                {header_info['languages']}
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

def home_page():
    header_section(left_aligned=True)
    
    # Cover Letter Section
    st.markdown("<div class='section-header'>Cover Letter</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='cover-letter'>{cover_letter}</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Education and Qualifications
    st.markdown("<div class='section-header'>Education and Qualifications</div>", unsafe_allow_html=True)
    for edu in education:
        st.markdown(f"**{edu['degree']}**, {edu['institution']} ({edu['date']})")
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Professional Experience in two columns
    st.markdown("<div class='section-header'>Professional Experience</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        exp = professional_experience[0]  # First experience
        st.markdown(f"**{exp['title']}**")
        st.markdown(f"{exp['company']} ({exp['dates']})")
        st.markdown(f"{exp['summary']}")
    
    with col2:
        for exp in professional_experience[1:]:  # Remaining experiences
            st.markdown(f"**{exp['title']}**")
            st.markdown(f"{exp['company']} ({exp['dates']})")
            st.markdown(f"{exp['summary']}")
    
    # Professional Summary
    st.markdown("<div class='section-header'>Professional Summary</div>", unsafe_allow_html=True)
    st.markdown(professional_summary['concise'], unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Skills and Personal Qualities
    st.markdown("<div class='section-header'>Skills and Personal Qualities</div>", unsafe_allow_html=True)
    # Two-column layout for Skills and Personal Qualities
    cols = st.columns(2)
    half = len(skills_and_qualities) // 2 + len(skills_and_qualities) % 2
    col1 = skills_and_qualities[:half]
    col2 = skills_and_qualities[half:]
    with cols[0]:
        for skill in col1:
            st.markdown(f"- {skill}")
    with cols[1]:
        for skill in col2:
            st.markdown(f"- {skill}")
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Key Achievements and Projects (single column)
    st.markdown("<div class='section-header'>Key Achievements and Projects</div>", unsafe_allow_html=True)
    for achievement in key_achievements_and_projects['concise']:
        st.markdown(f"• {achievement}")
    st.markdown("<hr>", unsafe_allow_html=True)

def professional_summary_page():
    header_section(left_aligned=False)
    st.markdown("<div class='section-header'>Professional Summary</div>", unsafe_allow_html=True)
    st.markdown(professional_summary['detailed'], unsafe_allow_html=True)
    
    st.markdown("<div class='section-header'>Professional Experience Details</div>", unsafe_allow_html=True)
    for exp in professional_experience:
        with st.expander(f"{exp['title']} at {exp['company']} ({exp['dates']})"):
            st.markdown(f"**Overview:** {exp['summary']}")
            st.markdown("**Key Responsibilities:**")
            for resp in exp['responsibilities']:
                st.markdown(f"- {resp}")

def projects_and_achievements_page():
    header_section(left_aligned=False)
    st.markdown("<div class='section-header'>Key Achievements and Projects</div>", unsafe_allow_html=True)
    for project in key_achievements_and_projects['detailed']:
        with st.expander(project['title']):
            for detail in project['details']:
                st.markdown(f"- {detail}")
    
    st.markdown("<div class='section-header'>Self-Learning and Continuous Improvement</div>", unsafe_allow_html=True)
    st.markdown("Committed to lifelong learning, dedicating time daily to skill development in areas such as:")
    st.markdown("- Python programming and data analysis")
    st.markdown("- Mechanics and small engine repair")
    st.markdown("- Website development and digital marketing")

def download_cv():
    pdf = generate_cv_pdf()
    st.sidebar.download_button(
        label="Download CV as PDF",
        data=pdf,
        file_name="Mikael_Pelletier_Lachapelle_CV.pdf",
        mime="application/pdf",
    )

def download_cover_letter():
    pdf = generate_cover_letter_pdf()
    st.sidebar.download_button(
        label="Download Cover Letter as PDF",
        data=pdf,
        file_name="Mikael_Pelletier_Lachapelle_Cover_Letter.pdf",
        mime="application/pdf",
    )

# ===========================
# PDF Generation Functions
# ===========================

def generate_cv_pdf():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=24,  # Reduced from 36
        leftMargin=24,   # Reduced from 36
        topMargin=24,    # Reduced from 36
        bottomMargin=24  # Reduced from 36
    )
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles with TELUS branding
    banner_style = ParagraphStyle(
        'Banner',
        parent=styles['Heading1'],
        fontSize=16,  # Reduced from 20
        textColor=colors.HexColor("#4B286D"),
        spaceAfter=20,  # Reduced from 30
        spaceBefore=0,
        alignment=TA_LEFT
    )
    
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=8,  # Reduced by 10% from 9
        textColor=colors.HexColor("#2A2C2E"),
        spaceAfter=4,
        alignment=TA_LEFT,
        leading=12
    )
    
    section_header = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor("#4B286D"),
        spaceBefore=12,
        spaceAfter=6,
        alignment=TA_LEFT
    )
    
    body_text = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontSize=9,  # Reduced by 10% from 10
        textColor=colors.HexColor("#2A2C2E"),
        spaceAfter=6,
        alignment=TA_LEFT,
        leading=12
    )
    
    bullet_text = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor("#2A2C2E"),
        spaceAfter=1,    # Reduced from 3
        leftIndent=8,    # Reduced from 12
        bulletIndent=4,  # Reduced from 6
        alignment=TA_LEFT,
        leading=11       # Reduced from 12
    )
    
    subsection_header = ParagraphStyle(
        'SubsectionHeader',
        parent=styles['Normal'],
        fontSize=11,  # Reduced by 10% from 12
        textColor=colors.HexColor("#4B286D"),
        spaceBefore=6,
        spaceAfter=4,
        alignment=TA_LEFT
    )
    
    elements = []
    
    # Page 1: Name, Contact, Professional Summary, Professional Experience
    # Name and Contact all left-aligned in single column
    elements.append(Paragraph(f"<b>{header_info['name']}</b>", banner_style))
    elements.append(Paragraph(
        f"{header_info['address']}<br/>"
        f"{header_info['phone']}<br/>"
        f"{header_info['email']}<br/>"
        f"{header_info['languages']}", contact_style
    ))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#4B286D")))
    elements.append(Spacer(1, 12))
    
    # Professional Summary
    elements.append(Paragraph("Professional Summary", section_header))
    
    # Split the detailed professional summary into paragraphs and bullets
    prof_summary = professional_summary['detailed'].split('\n\n')
    for para in prof_summary:
        if para.strip().startswith("<b>Education and Professional Experience Highlights:</b>"):
            # Add subsection header
            elements.append(Paragraph("Education and Professional Experience Highlights:", subsection_header))
            # Extract bullet points from the paragraph
            bullets = para.strip().split('- ')[1:]
            bullet_items = [ListItem(Paragraph(f"{bullet}", bullet_text)) for bullet in bullets]
            elements.append(ListFlowable(bullet_items, bulletType='bullet'))
        else:
            # Regular paragraph
            elements.append(Paragraph(para.strip(), body_text))
        elements.append(Spacer(1, 6))
    
    # Professional Experience (Moved to Page 1)
    elements.append(Paragraph("Professional Experience", section_header))
    for exp in professional_experience:
        # Filter out the specific bullet points we want to remove
        filtered_responsibilities = [
            resp for resp in exp['responsibilities'] 
            if not any(excluded in resp for excluded in [
                "Analyze credit reduction impacts",
                "Conduct temp check analysis",
                "Gather and compile data insights"
            ])
        ]
        
        exp_title = f"<b>{exp['title']}</b>, {exp['company']} ({exp['dates']})"
        elements.append(Paragraph(exp_title, subsection_header))
        elements.append(Paragraph(exp['summary'], body_text))
        bullet_points = [ListItem(Paragraph(resp, bullet_text)) for resp in filtered_responsibilities]
        elements.append(ListFlowable(bullet_points, bulletType='bullet'))
        elements.append(Spacer(1, 4))  # Reduced spacing after bullet points from 6

    # Move Education and other sections to page 2
    elements.append(PageBreak())
    
    # Page 2: Education and Qualifications, Skills and Personal Qualities, Key Achievements and Projects
    elements.append(Paragraph("Education and Qualifications", section_header))
    for edu in education:
        edu_text = f"<b>{edu['degree']}</b>, {edu['institution']} ({edu['date']})"
        elements.append(Paragraph(edu_text, body_text))
    elements.append(Spacer(1, 12))
    
    # Skills and Personal Qualities
    elements.append(Paragraph("Skills and Personal Qualities", section_header))
    skill_data = []
    half = len(skills_and_qualities) // 2 + len(skills_and_qualities) % 2
    col1 = skills_and_qualities[:half]
    col2 = skills_and_qualities[half:]
    for i in range(half):
        row = []
        if i < len(col1):
            row.append(Paragraph(f"• {col1[i]}", body_text))
        else:
            row.append(Paragraph("", body_text))
        if i < len(col2):
            row.append(Paragraph(f"• {col2[i]}", body_text))
        else:
            row.append(Paragraph("", body_text))
        skill_data.append(row)
    skill_table = Table(skill_data, colWidths=[250, 250])
    skill_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    elements.append(skill_table)
    elements.append(Spacer(1, 12))
    
    # Key Achievements and Projects (modified for single column)
    elements.append(Paragraph("Key Achievements and Projects", section_header))
    for achievement in key_achievements_and_projects['concise']:
        elements.append(Paragraph(f"• {achievement}", body_text))
    elements.append(Spacer(1, 12))
    
    # Line Separator at the bottom
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#4B286D")))
    elements.append(Spacer(1, 12))
    
    # Build PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

def generate_cover_letter_pdf():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles with reduced font sizes (15% reduction)
    cover_header_style = ParagraphStyle(
        'CoverHeader',
        parent=styles['Normal'],
        fontSize=9,  # Reduced from 11
        textColor=colors.HexColor("#2A2C2E"),
        spaceAfter=12,
        alignment=TA_LEFT,
        leading=12,  # Reduced from 14
        fontName='Helvetica-Bold'
    )
    
    date_style = ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontSize=9,  # Reduced from 11
        textColor=colors.HexColor("#2A2C2E"),
        spaceBefore=12,
        spaceAfter=12,
        alignment=TA_LEFT,
        leading=12  # Reduced from 14
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=9,  # Reduced from 11
        textColor=colors.HexColor("#2A2C2E"),
        spaceBefore=12,
        spaceAfter=12,
        alignment=TA_LEFT,
        leading=12  # Reduced from 14
    )
    
    signature_style = ParagraphStyle(
        'Signature',
        parent=styles['Normal'],
        fontSize=9,  # Reduced from 11
        textColor=colors.HexColor("#2A2C2E"),
        spaceBefore=24,  # Reduced from 36
        spaceAfter=12,
        alignment=TA_LEFT,
        leading=12  # Reduced from 14
    )
    
    elements = []
    
    # Header block
    elements.append(Paragraph(
        f"{header_info['address']}<br/>"
        f"{header_info['phone']}<br/>"
        f"{header_info['email']}",
        cover_header_style
    ))
    
    # Date
    elements.append(Paragraph("November 13, 2024", date_style))
    
    # Salutation
    elements.append(Paragraph("Dear Hiring Manager,", body_style))
    
    # Break the body into paragraphs for better spacing
    paragraphs = [
        "I am writing to express my enthusiastic interest in the **Business Analyst II - 44731** position within TELUS's Marketing team. With over a decade of experience at TELUS, specializing in operational efficiency and customer experience, I am confident in my ability to contribute effectively to your team and drive impactful results.",
        
        "In my current role as **Operations Manager - Executive Escalations**, I have honed my skills in managing complex escalations, conducting root cause analysis, and implementing data-driven process improvements. My proactive approach and ability to collaborate with diverse stakeholders have been instrumental in achieving a 600% reduction in payroll inaccuracies and streamlining workflows to enhance operational efficiency.",
        
        "The **Business Analyst II** role excites me as it aligns perfectly with my expertise in business analysis, data interpretation, and strategic planning. I am particularly drawn to the opportunity to support Channel Partners and Internal Stakeholders, driving operational efficiencies within Supply Operations. My proficiency in tools such as DOMO, Salesforce Reporting, and my self-taught Python programming skills enable me to process complex data, generate insightful reports, and implement effective solutions.",
        
        "I am highly detail-oriented, organized, and possess exceptional analytical skills, which I have consistently applied to improve E2E processes and manage transactional reports. My experience in generating system reports, supporting step-by-step process documentation, and handling special requests has prepared me to excel in this role. Additionally, my ability to embrace and adapt to change in a continuous learning environment ensures that I stay ahead of industry trends and best practices.",
        
        "I am particularly impressed by TELUS's commitment to innovation and excellence, and I am eager to leverage my skills in business analysis and strategic communication to contribute to the success of the Marketing team. My proven ability to work collaboratively in a lean, agile environment and my sense of urgency in driving issues to closure make me a strong fit for this position."
    ]
    
    for paragraph in paragraphs:
        elements.append(Paragraph(paragraph, body_style))
    
    # Closing
    elements.append(Paragraph("Thank you for considering my application. I look forward to the opportunity to discuss how my background, skills, and passions align with the goals of TELUS and how I can contribute to the continued success of your team.", body_style))
    
    elements.append(Paragraph("Sincerely,", signature_style))
    elements.append(Paragraph(header_info['name'], signature_style))
    
    # Build PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

# ===========================
# Main Application Logic
# ===========================

def main():
    apply_custom_styles()
    
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    menu = ["Home", "Professional Summary", "Projects and Achievements"]
    choice = st.sidebar.radio("Go to", menu)
    
    # Download CV button always available
    download_cv()
    
    # Download Cover Letter button on Home page
    if choice == "Home":
        download_cover_letter()
    
    # Page Rendering
    if choice == "Home":
        home_page()
    elif choice == "Professional Summary":
        professional_summary_page()
    elif choice == "Projects and Achievements":
        projects_and_achievements_page()

if __name__ == "__main__":
    main()
