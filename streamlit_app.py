import streamlit as st
import base64
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
import io

# Set page configuration
st.set_page_config(
    page_title="Mikaël Pelletier Lachapelle - Interactive CV",
    page_icon=":briefcase:",
    layout="wide",
)

# Apply custom styles
def apply_custom_styles():
    custom_css = """
    <style>
    /* Header */
    .header h2 {
        color: #4B0082;
        font-size: 36px;
        font-weight: bold;
    }
    /* Subheaders */
    .subheader h3 {
        color: #4B0082;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    /* Normal Text */
    .normal-text {
        font-size: 16px;
    }
    /* Bullet Points */
    .bullet-point {
        font-size: 16px;
        margin-left: 20px;
    }
    /* Horizontal Line */
    hr {
        border: 1px solid #4B0082;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Header Section
def header():
    st.markdown('<div class="header"><h2>MIKAËL PELLETIER LACHAPELLE</h2></div>', unsafe_allow_html=True)
    st.markdown('*Bilingual (English and French)*')
    st.markdown("""
    53, Rue Grove  
    Danville, Quebec J0A 1A0  
    📞 819-740-6080  
    📧 [mikael.pelletier_lachapelle@telus.com](mailto:mikael.pelletier_lachapelle@telus.com)  
    """)
    st.markdown('<hr>', unsafe_allow_html=True)

# Professional Summary
def professional_summary():
    with st.expander("**Professional Summary**", expanded=True):
        st.write("""
            Versatile and analytically driven professional with over a decade of experience at TELUS, specializing in business analysis, operational efficiency, and customer experience. Adept at leveraging technical skills in Python and data analysis to streamline processes and drive strategic initiatives. Proven track record in managing high-stakes escalations, developing innovative tools, and leading cross-functional teams to achieve organizational goals.
        """)

# Key Skills
def key_skills():
    st.markdown('<div class="subheader"><h3>Key Skills</h3></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - **Business Analysis & Data Analysis**
        - **Python Programming & Automation**
        - **Project Management & Process Improvement**
        - **Customer Relationship Management (CRM)**
        - **Workforce Management & Operational Efficiency**
        - **Strategic Communication & Collaboration**
        """)
    with col2:
        st.markdown("""
        - **Problem-Solving & Root Cause Analysis**
        - **Business Intelligence Tools: DOMO**
        - **Salesforce Reporting**
        - **API Integration**
        - **Bilingual: English & French**
        - **Adaptable & Quick Learner**
        """)
    st.markdown('<hr>', unsafe_allow_html=True)

# Professional Experience
def professional_experience():
    st.markdown('<div class="subheader"><h3>Professional Experience</h3></div>', unsafe_allow_html=True)
    
    # Operations Manager - Executive Escalations
    with st.expander("**Operations Manager - Executive Escalations, Business Customer Experience | TELUS Communications Inc. | May 2022 - Present**", expanded=False):
        st.markdown("""
        - **Advocacy and Escalation Management:**
            - Advocated for TELUS' WLS Business customers to resolve pre and post-sales escalations to their satisfaction.
            - Managed a variety of escalations, including regulatory, legal, and media threats.
            - Acted as a Subject Matter Expert, coaching team members, providing support, and driving ownership.
        - **Root Cause Analysis and Reporting:**
            - Conducted high-level root cause analysis to identify and mitigate recurring issues.
            - Developed Python-based tools for data analysis and automation to streamline escalation tracking and reporting.
            - Maintained and enhanced the Escalation Volume Tracker with detailed breakdowns and visualizations.
        - **Process Improvement and Initiatives:**
            - Led initiatives to analyze and improve billing processes, contributing to the Bring It Back program and Return Exception initiatives.
            - Developed automated word cloud tools using Python to identify key themes and trends in escalations.
            - Analyzed the impact of credit policy changes on escalations, providing actionable insights for strategic decision-making.
        - **Business Analysis and Research:**
            - Conducted in-depth analysis of Bring It Back (BIB) return exceptions, collecting data from Tier 1 Escalations and executive teams.
            - Performed manual deep dive to identify common scenarios and root causes across numerous cases.
            - Provided detailed findings and recommendations based on comprehensive data collection and analysis.
            - Developed additional support materials including bilingual templates to enhance process efficiency.
        - **Data Analysis and Tool Development:**
            - Developed and implemented secure tools for analyzing sensitive business data.
            - Created visualization solutions for identifying patterns in escalation data.
            - Demonstrated adaptability in learning and applying new technologies based on business needs.
            - Showcased potential of secure, internal alternatives to third-party analysis tools.
        """)

    # Store Manager
    with st.expander("**Store Manager | TELUS Retail | September 2014 - May 2022**", expanded=False):
        st.markdown("""
        - **Team Leadership and Customer Satisfaction:**
            - Led store operations, ensuring exceptional customer satisfaction and team performance.
            - Conducted individual coaching sessions and team projects to enhance skills and productivity.
        - **Administrative and Operational Excellence:**
            - Performed administrative tasks including scheduling, analyzing sales statistics, and targeting improvement opportunities.
            - Developed tools and strategies to facilitate operations, reduce human error, and increase productivity.
        - **Key Projects and Initiatives:**
            - **Trade-In Shipping Inaccuracies Reduction:**
                - Developed a process to reduce trade-in shipping inaccuracies, leading to substantial revenue protection.
                - Improved packaging protocols by reusing materials, ensuring safe shipping at no additional cost.
            - **Sales Tracker Development:**
                - Collaborated to develop a Sales Tracker tool for managers to track individual sales across multiple store locations.
                - Provided detailed views for representative-level results and store-level metrics.
            - **Synerion Prime Initiatives:**
                - Participated in a TELUS development program to gain business analysis skills and knowledge.
                - Applied learned skills to improve operational workflows and compliance.
        - **OBDF Initiative Support:**
            - Supported the Outbound Direct Fulfillment (OBDF) initiative during COVID-19.
            - Managed onboarding and troubleshooting for sales teams across Quebec and the Atlantic provinces.
        """)

    # Sales Representative
    with st.expander("**Sales Representative | TELUS Retail | January 2013 - September 2014**", expanded=False):
        st.markdown("""
        - Achieved sales targets and provided exceptional customer service.
        - Identified customer needs and offered tailored solutions.
        - Offered support and training for customers on how to use their devices.
        """)

    # Self-Employed
    with st.expander("**ATV/Small Engine Repair and Sales | Self-Employed | 2018 - Present**", expanded=False):
        st.markdown("""
        - Purchased and sold ATVs and other small machinery.
        - Performed aesthetic work, painting, welding, and restorations.
        - Repaired and rebuilt components, engines, fuel/exhaust systems, and general bodywork.
        """)
    st.markdown('<hr>', unsafe_allow_html=True)

# Projects and Achievements
def projects_and_achievements():
    st.markdown('<div class="subheader"><h3>Projects and Achievements</h3></div>', unsafe_allow_html=True)
    
    with st.expander("**Escalation Analysis and Process Improvement**", expanded=False):
        st.markdown("""
        - Led comprehensive analysis of the temp check process, streamlining workflows and reducing manual effort.
        - Maintained and enhanced the Escalation Volume Tracker with detailed YOY breakdowns and visualizations.
        - Conducted thorough analysis of credit reduction impact on escalations, providing actionable insights to leadership.
        """)

    with st.expander("**Business Analysis and Research**", expanded=False):
        st.markdown("""
        - Conducted in-depth analysis of Bring It Back (BIB) return exceptions, collecting data from Tier 1 Escalations and executive teams.
        - Performed manual deep dive to identify common scenarios and root causes across numerous cases.
        - Provided detailed findings and recommendations based on comprehensive data collection and analysis.
        - Developed additional support materials including bilingual templates to enhance process efficiency.
        """)

    with st.expander("**Data Analysis and Tool Development**", expanded=False):
        st.markdown("""
        - Developed and implemented secure tools for analyzing sensitive business data.
        - Created visualization solutions for identifying patterns in escalation data.
        - Demonstrated adaptability in learning and applying new technologies based on business needs.
        - Showcased potential of secure, internal alternatives to third-party analysis tools.
        """)

    with st.expander("**Sales Tracker Development**", expanded=False):
        st.markdown("""
        - Developed a tool with a colleague to track individual sales for all representatives in stores.
        - Enabled managers to track multiple locations with full month tracking and detailed views.
        - Provided insights into various qualitative and quantitative sales metrics.
        """)

    with st.expander("**Leadership in OBDF Initiative**", expanded=False):
        st.markdown("""
        - Played a key role in supporting the Outbound Direct Fulfillment (OBDF) initiative during COVID-19.
        - Managed onboarding and troubleshooting for sales teams across regions.
        """)

    with st.expander("**Synerion Prime Initiatives**", expanded=False):
        st.markdown("""
        - Participated in a TELUS development program to gain business analysis skills and knowledge.
        - Applied learned skills to improve operational workflows and compliance.
        """)
    st.markdown('<hr>', unsafe_allow_html=True)

# Education and Qualifications
def education_and_qualifications():
    st.markdown('<div class="subheader"><h3>Education and Qualifications</h3></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - **Business Analyst Development Program**, TELUS | September 2024
        - **Leadership Essentials**, The Ken Blanchard Companies | 2018
        - **TELUS Leadership Development Program**, TELUS Retail | 2014
        """)
    with col2:
        st.markdown("""
        - **Diplôme d'Aptitude aux Fonctions d’Animateur**, Projet Jeunesse de Richmond | 2012
        - **Special Care Counselling (Incomplete)**, Champlain Regional College | 2012
        """)
    st.markdown('<hr>', unsafe_allow_html=True)

# Personal Qualities and Interests
def personal_qualities_and_interests():
    st.markdown('<div class="subheader"><h3>Personal Qualities and Interests</h3></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - **Analytical and Detail-Oriented**
        - **Creative Problem Solver**
        - **Passionate and Devoted**
        - **Excellent Communicator**
        - **Adaptable and Resilient**
        - **Lifelong Learner**
        """)
    with col2:
        st.markdown("""
        - **Family Activities**
        - **Strategy Games (Near-professional level in Rocket League)**
        - **ATV Mechanics**
        - **Python Programming**
        - **DIY Home Improvement**
        - **Continuous Learning**
        """)
    st.markdown('<hr>', unsafe_allow_html=True)

# PDF Generation Function
def generate_pdf():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='CustomHeading1',
        fontSize=18,
        leading=22,
        spaceAfter=15,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#4B0082")
    ))
    styles.add(ParagraphStyle(
        name='CustomHeading2',
        fontSize=14,
        leading=18,
        spaceAfter=10,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#4B0082")
    ))
    styles.add(ParagraphStyle(
        name='CustomNormal',
        fontSize=10,
        leading=12,
        spaceAfter=8,
        alignment=TA_LEFT
    ))
    styles.add(ParagraphStyle(
        name='CustomBullet',
        leftIndent=15,
        bulletIndent=10,
        spaceBefore=3,
        spaceAfter=3,
        fontSize=10,
        leading=12
    ))

    elements = []

    # Header
    elements.append(Paragraph("MIKAËL PELLETIER LACHAPELLE", styles['CustomHeading1']))
    elements.append(Paragraph("Operations Manager - Executive Escalations", styles['CustomNormal']))
    elements.append(Paragraph("Danville, Quebec | 819-740-6080 | mikael.pelletier_lachapelle@telus.com", styles['CustomNormal']))
    elements.append(Spacer(1, 12))

    # Professional Summary
    elements.append(Paragraph("Professional Summary", styles['CustomHeading2']))
    elements.append(Paragraph(
        "Versatile and analytically driven professional with over a decade of experience at TELUS, specializing in business analysis, operational efficiency, and customer experience. Adept at leveraging technical skills in Python and data analysis to streamline processes and drive strategic initiatives.",
        styles['CustomNormal']
    ))

    # Key Skills
    elements.append(Paragraph("Key Skills", styles['CustomHeading2']))

    # Organize skills into two columns
    skills = [
        "Business Analysis & Data Analysis",
        "Python Programming & Automation",
        "Project Management & Process Improvement",
        "Customer Relationship Management (CRM)",
        "Workforce Management & Operational Efficiency",
        "Strategic Communication & Collaboration",
        "Problem-Solving & Root Cause Analysis",
        "Business Intelligence Tools: DOMO",
        "Salesforce Reporting",
        "API Integration",
        "Bilingual: English & French",
        "Adaptable & Quick Learner"
    ]

    skills_data = [
        [Paragraph(skills[i], styles['CustomNormal']), Paragraph(skills[i+1], styles['CustomNormal'])]
        for i in range(0, len(skills), 2)
        if i+1 < len(skills)
    ]

    if len(skills) % 2 != 0:
        skills_data.append([Paragraph(skills[-1], styles['CustomNormal']), Paragraph('', styles['CustomNormal'])])

    skills_table = Table(skills_data, colWidths=[250, 250])
    elements.append(skills_table)
    elements.append(Spacer(1, 12))

    # Professional Experience
    elements.append(Paragraph("Professional Experience", styles['CustomHeading2']))

    # Operations Manager
    elements.append(Paragraph("Operations Manager - Executive Escalations, Business Customer Experience | TELUS Communications Inc. | May 2022 - Present", styles['CustomNormal']))

    opm_bullets = [
        Paragraph("Advocacy and Escalation Management:", styles['CustomNormal']),
        ListFlowable(
            [
                ListItem(Paragraph("Advocated for TELUS' WLS Business customers to resolve pre and post-sales escalations to their satisfaction.", styles['CustomNormal'])),
                ListItem(Paragraph("Managed a variety of escalations, including regulatory, legal, and media threats.", styles['CustomNormal'])),
                ListItem(Paragraph("Acted as a Subject Matter Expert, coaching team members, providing support, and driving ownership.", styles['CustomNormal']))
            ],
            bulletType='bullet',
            leftIndent=20
        ),
        Paragraph("Root Cause Analysis and Reporting:", styles['CustomNormal']),
        ListFlowable(
            [
                ListItem(Paragraph("Conducted high-level root cause analysis to identify and mitigate recurring issues.", styles['CustomNormal'])),
                ListItem(Paragraph("Developed Python-based tools for data analysis and automation to streamline escalation tracking and reporting.", styles['CustomNormal'])),
                ListItem(Paragraph("Maintained and enhanced the Escalation Volume Tracker with detailed breakdowns and visualizations.", styles['CustomNormal']))
            ],
            bulletType='bullet',
            leftIndent=20
        ),
        Paragraph("Process Improvement and Initiatives:", styles['CustomNormal']),
        ListFlowable(
            [
                ListItem(Paragraph("Led initiatives to analyze and improve billing processes.", styles['CustomNormal'])),
                ListItem(Paragraph("Developed automated word cloud tools using Python.", styles['CustomNormal'])),
                ListItem(Paragraph("Analyzed the impact of credit policy changes on escalations.", styles['CustomNormal']))
            ],
            bulletType='bullet',
            leftIndent=20
        ),
        Paragraph("Business Analysis and Research:", styles['CustomNormal']),
        ListFlowable(
            [
                ListItem(Paragraph("Conducted in-depth analysis of Bring It Back (BIB) return exceptions.", styles['CustomNormal'])),
                ListItem(Paragraph("Identified common scenarios and root causes.", styles['CustomNormal'])),
                ListItem(Paragraph("Provided detailed findings and recommendations.", styles['CustomNormal'])),
                ListItem(Paragraph("Developed bilingual templates to enhance process efficiency.", styles['CustomNormal']))
            ],
            bulletType='bullet',
            leftIndent=20
        ),
    ]
    elements.extend(opm_bullets)
    elements.append(Spacer(1, 12))

    # Store Manager
    elements.append(Paragraph("Store Manager | TELUS Retail | September 2014 - May 2022", styles['CustomNormal']))

    sm_bullets = [
        Paragraph("Team Leadership and Customer Satisfaction:", styles['CustomNormal']),
        ListFlowable(
            [
                ListItem(Paragraph("Led store operations, ensuring exceptional customer satisfaction.", styles['CustomNormal'])),
                ListItem(Paragraph("Conducted coaching sessions to enhance team productivity.", styles['CustomNormal']))
            ],
            bulletType='bullet',
            leftIndent=20
        ),
        Paragraph("Administrative and Operational Excellence:", styles['CustomNormal']),
        ListFlowable(
            [
                ListItem(Paragraph("Managed scheduling and analyzed sales statistics.", styles['CustomNormal'])),
                ListItem(Paragraph("Developed tools to reduce human error and increase productivity.", styles['CustomNormal']))
            ],
            bulletType='bullet',
            leftIndent=20
        ),
        Paragraph("Key Projects and Initiatives:", styles['CustomNormal']),
        ListFlowable(
            [
                ListItem(Paragraph("Trade-In Shipping Inaccuracies Reduction:", styles['CustomNormal'])),
                ListFlowable(
                    [
                        ListItem(Paragraph("Developed a process to reduce trade-in shipping inaccuracies.", styles['CustomNormal'])),
                        ListItem(Paragraph("Improved packaging protocols using recycled materials.", styles['CustomNormal']))
                    ],
                    bulletType='bullet',
                    leftIndent=40
                ),
                ListItem(Paragraph("Sales Tracker Development:", styles['CustomNormal'])),
                ListFlowable(
                    [
                        ListItem(Paragraph("Collaborated to develop a Sales Tracker tool.", styles['CustomNormal'])),
                        ListItem(Paragraph("Provided detailed views for sales metrics.", styles['CustomNormal']))
                    ],
                    bulletType='bullet',
                    leftIndent=40
                ),
                ListItem(Paragraph("Synerion Prime Initiatives:", styles['CustomNormal'])),
                ListFlowable(
                    [
                        ListItem(Paragraph("Participated in a TELUS development program.", styles['CustomNormal'])),
                        ListItem(Paragraph("Applied skills to improve operational workflows.", styles['CustomNormal']))
                    ],
                    bulletType='bullet',
                    leftIndent=40
                ),
            ],
            bulletType='bullet',
            leftIndent=20
        ),
    ]
    elements.extend(sm_bullets)
    elements.append(Spacer(1, 12))

    # Education and Qualifications
    elements.append(Paragraph("Education and Qualifications", styles['CustomHeading2']))
    edu_qual = [
        ["**Business Analyst Development Program**, TELUS", "September 2024"],
        ["**Leadership Essentials**, The Ken Blanchard Companies", "2018"],
        ["**TELUS Leadership Development Program**, TELUS Retail", "2014"],
        ["**Diplôme d'Aptitude aux Fonctions d’Animateur**, Projet Jeunesse de Richmond", "2012"],
    ]
    table = Table(edu_qual, colWidths=[330, 170])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0E0E0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Personal Qualities and Interests
    elements.append(Paragraph("Personal Qualities and Interests", styles['CustomHeading2']))
    pq_i = [
        [Paragraph("**Personal Qualities**", styles['CustomNormal']), Paragraph("**Interests and Hobbies**", styles['CustomNormal'])],
        [Paragraph("Analytical and Detail-Oriented", styles['CustomNormal']), Paragraph("Family Activities", styles['CustomNormal'])],
        [Paragraph("Creative Problem Solver", styles['CustomNormal']), Paragraph("Strategy Games", styles['CustomNormal'])],
        [Paragraph("Passionate and Devoted", styles['CustomNormal']), Paragraph("ATV Mechanics", styles['CustomNormal'])],
        [Paragraph("Excellent Communicator", styles['CustomNormal']), Paragraph("Python Programming", styles['CustomNormal'])],
        [Paragraph("Adaptable and Resilient", styles['CustomNormal']), Paragraph("DIY Home Improvement", styles['CustomNormal'])],
        [Paragraph("Lifelong Learner", styles['CustomNormal']), Paragraph("Continuous Learning", styles['CustomNormal'])],
    ]
    table_pq = Table(pq_i, colWidths=[250, 250])
    table_pq.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0E0E0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elements.append(table_pq)
    elements.append(Spacer(1, 12))

    # Build PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

# Document Upload and Preview
def document_upload():
    st.markdown('<div class="subheader"><h3>Document Upload and Preview</h3></div>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader("Upload Documents (e.g., Certificates, Recommendations)", accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_details = {
                "filename": uploaded_file.name,
                "filetype": uploaded_file.type,
                "filesize": uploaded_file.size
            }
            st.markdown(f"### {file_details['filename']}")
            if uploaded_file.type.startswith("image/"):
                st.image(uploaded_file)
            elif uploaded_file.type == "application/pdf":
                # Display PDF
                base64_pdf = base64.b64encode(uploaded_file.read()).decode('utf-8')
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
            else:
                st.write("Preview not available for this file type.")
    else:
        st.write("")
    st.markdown('<hr>', unsafe_allow_html=True)

# Download CV
def download_cv():
    st.markdown('<div class="subheader"><h3>Download CV as PDF</h3></div>', unsafe_allow_html=True)
    pdf = generate_pdf()
    st.download_button(
        label="📄 Download CV as PDF",
        data=pdf,
        file_name="Mikael_Pelletier_Lachapelle_CV.pdf",
        mime="application/pdf",
    )
    st.markdown('<hr>', unsafe_allow_html=True)

# Main Function to Render All Sections
def main():
    apply_custom_styles()
    header()
    professional_summary()
    key_skills()
    professional_experience()
    projects_and_achievements()
    education_and_qualifications()
    personal_qualities_and_interests()
    document_upload()
    download_cv()

if __name__ == "__main__":
    main()
