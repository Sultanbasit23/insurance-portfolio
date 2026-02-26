import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time
import os
import streamlit.components.v1 as components
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Insurance Portfolio", layout="wide")
st.markdown("""
<style>
.block-container {
    padding-left: 0rem;
    padding-right: 0rem;
    padding-top: 2rem;
    max-width: 100%;
}

.main > div {
    padding-left: 3rem;
    padding-right: 3rem;
}

section {
    margin-bottom: 4rem;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# LOAD CSS
# ----------------------------
def load_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("design.css")

# SIDEBAR NAVIGATION
st.sidebar.markdown("""
<div class="sidebar-logo">
    <div class="logo-badge">BSM</div>
    <div class="logo-sub">Basit Sultan Mohammed</div>
</div>
""", unsafe_allow_html=True)
page = st.sidebar.radio(
    "Navigate",
    ["Resume Portfolio", "Insurance Intelligence Lab"]
)

# ==========================================================
# ===================== RESUME SECTION =====================
# ==========================================================
if page == "Resume Portfolio":

    # ===== SECTION NAVIGATION =====
    st.markdown("""
    <div class="section-nav">
        <a href="#about">About</a>
        <a href="#education">Education</a>
        <a href="#experience">Experience</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#case-studies">Case Studies</a>
        <a href="#contact">Contact</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<script>
const links = document.querySelectorAll(".section-nav a");

links.forEach(link => {
    link.addEventListener("click", function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            target.scrollIntoView({ behavior: "smooth" });
        }
    });
});
</script>
""", unsafe_allow_html=True)
    # TITLE
    st.markdown('<div id="about" class="section-title">About Me</div>', unsafe_allow_html=True)

    # CENTERED BIGGER QUOTE
    st.markdown("""
    <div style="
        padding:22px;
        border-radius:14px;
        background: linear-gradient(90deg,#1e293b,#0f172a);
        border-left:5px solid #3b82f6;
        font-style:italic;
        font-size:20px;
        text-align:center;
        margin-bottom:40px;">
        "Lose money for the firm, and I will be understanding.
        Lose a shred of reputation for the firm, and I will be ruthless."
    </div>
    """, unsafe_allow_html=True)

    # TIGHTER SIDE BY SIDE LAYOUT
    col1, col2 = st.columns([1, 2.20], gap="small")

    with col1:
        try:
            st.image("assets/profile.jpg", width=380)
        except:
            st.warning("Profile image not found.")

    with col2:
        st.markdown("## Basit Sultan Mohammed")
        st.markdown("### Insurance & Data Analyst")

        st.markdown("---")

        st.markdown("**Date of Birth:** 23 December 2003")
        st.markdown("**Location:** Chennai, India")
        st.markdown("**Email:** basitsultanmohammed@gmail.com")
        st.markdown("**Phone:** +91 7305797531")

    # CENTERED DOWNLOAD BUTTON
    st.markdown("<br>", unsafe_allow_html=True)

    colA, colB, colC = st.columns([1,2,1])
    with colB:
        try:
            with open("basitsultanresume.pdf", "rb") as file:
                st.download_button(
                    label="Download Resume",
                    data=file,
                    file_name="Basit_Sultan_Mohammed_Resume.pdf",
                    use_container_width=True
                )
        except:
            st.info("Resume file not found.")

    # ================= EDUCATION =================
    st.markdown('<div id="education" class="section-title">Education</div>', unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([1, 2.5, 1])

    with col_center:
        st.markdown("""
        <div class="edu-card">

        <h3>Bachelor of Technology (B.Tech) – Computer Science & Engineering</h3>
        <p class="edu-sub">SRM Institute of Science and Technology, India | 2021 – 2025</p>

        <p><b>Leadership & Roles:</b></p>
        <ul>
        <li>Student Coordinator – Association of Computer Science Engineers</li>
        <li>Core Member – White Hat Hackers Club</li>
        <li>Official Videographer – Rotaract Club</li>
        <li>Professional Cricket Player – University Team</li>
        </ul>

        <div class="cgpa-container">
        <div class="cgpa-label">CGPA: 8.5 / 10</div>
        <div class="cgpa-bar">
        <div class="cgpa-fill" style="width:85%;"></div>
        </div>
        </div>

        <div class="badge-container">
        <span class="badge">Machine Learning</span>
        <span class="badge">Data Analytics</span>
        <span class="badge">Risk Management</span>
        <span class="badge">Insurance Systems</span>
        </div>

        <div class="academic-highlight">
        Gold Medalist – Science Olympiad | Represented school at World Robot Olympiad
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="edu-card" style="margin-top:30px;">

        <h3>Diploma in Risk Management</h3>
        <p class="edu-sub">Alison | CPD Certified  | India 2026</p>

        <p><b>Score:</b> 90%</p>

        <div class="badge-container">
        <span class="badge">Insurance for Risk</span>
        <span class="badge">Insurance Operations</span>
        <span class="badge">Risk Assessment</span>
        <span class="badge">Property and Global Risk</span>
        <span class="badge">Life Insurance</span>
        <span class="badge">Social Insurance</span>
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="edu-card" style="margin-top:30px;">

        <h3>Advanced Personal Coursework – Finance & Insurance</h3>

        <p><b>Yale University</b></p>
        <ul>
        <li>ECON 252 – Insurance: The Archetypal Risk Management Institution</li>
        <li>Opportunities & Vulnerabilities in Insurance Systems</li>
        </ul>

        <p><b>Gresham College</b></p>
        <ul>
        <li>The London Insurance Market</li>
        <li>The Origins of London Marine Insurance</li>
        <li>Financial Insurance Against Macro Risks (Currency Instability & Global Terrorism)</li>
        </ul>

        <p><b>Massachusetts Institute of Technology (MIT)</b></p>
        <ul>
        <li>MIT 15.401 – Finance Theory</li>
        <li>MIT 18.S096 – Mathematics with Applications in Finance</li>
        </ul>

        </div>
        """, unsafe_allow_html=True)

        # ---------------- EXPERIENCE ----------------
        st.markdown('<div id="experience" class="section-title">Experience</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="experience-card">

        <h3>Swiss Re & Clifford Chance</h3>

        <p class="exp-role">Insurance, Risk & Resilience Internship</p>

        <span class="exp-badge">Applied Learning</span>
        <span class="exp-badge">Data Analysis</span>
        <span class="exp-badge">Risk Management</span>
        <span class="exp-badge">Resource Management</span>
        <span class="exp-badge">Contact Analysis</span>

        <ul class="exp-list">
        <li>Completed a simulation involving insurance and reinsurance policies for the SwissRe team</li>
        <li>Wrote a professional email to communicate a new global office policy to all employees</li>
        <li>Prepared a legal risk map to demonstrate risks to client and ways to mitigate them</li>
        <li><strong>Impact:</strong> Researched insurance documentation, parties, and terms required to prepare resources for a client meeting</li>
        </ul>

        </div>


        <div class="experience-card">

        <h3>Yuva</h3>
        <p class="exp-role">Insurance Analyst Intern</p>
        <span class="exp-badge">Insurer Risk Assessment</span>
        <span class="exp-badge">Mitigation Strategies</span>
        <span class="exp-badge">Policy Evaluation</span>
        <span class="exp-badge">Customer Claims Analysis</span>

        <ul class="exp-list">
        <li>Conducted end to end insurance data analysis to uncover trends, risk drivers, and strategic business insights</li>
        <li>Developed a structured risk scoring model and designed mitigation strategies to manage portfolio exposure</li>
        <li>Evaluated insurance policies using a mult dimensinal framework and delivered data backed improvement recommendaions</li>
        <li><strong>Impact:</strong> Stimulated claims analysis and applied forecasting techniques to predict industry trends and support strategic decision making</li>
        </ul>

        </div>


        <div class="experience-card">

        <h3>Chartered Insurance Institute (CII)</h3>
        <p class="exp-role">Insurance Work Experience Program</p>
        <span class="exp-badge">General Insurance</span>
        <span class="exp-badge">Insurance Underwriting</span>
        <span class="exp-badge">Insurance Broking</span>
        <span class="exp-badge">Employability Skills</span>

        <ul class="exp-list">
        <li>Studied underwriting lifecycle, policy issuance, and claims management processes.</li>
        <li>Analyzed risk categorization and pricing strategies.</li>
        <li>Explored regulatory compliance frameworks in insurance markets.</li>
        <li><strong>Impact:</strong> Strengthened foundational understanding of underwriting & insurance governance.</li>
        </ul>

        </div>


        <div class="experience-card">

        <h3>Allianz</h3>
        <p class="exp-role">Insurance Industry Experience</p>
        <span class="exp-badge">Underwriting, Claims & Data</span>
        <span class="exp-badge">Engineering, Pricing & Finance</span>
        <span class="exp-badge">Project & Change Management</span>

        <ul class="exp-list">
        <li>Examined enterprise risk management strategies used in multinational insurance operations.</li>
        <li>Studied portfolio diversification and capital allocation principles.</li>
        <li>Reviewed risk mitigation techniques across insurance products.</li>
        <li><strong>Impact:</strong> Gained exposure to real-world corporate insurance decision-making models.</li>
        </ul>

        </div>


        <div class="experience-card">

        <h3>AXA XL</h3>
        <p class="exp-role">Insurance Market Experience</p>
        <span class="exp-badge">Claims</span>
        <span class="exp-badge">Underwriting</span>
        <span class="exp-badge">Sustainability and Energy Transition</span>

        <ul class="exp-list">
        <li>Explored specialty insurance markets and commercial risk policies.</li>
        <li>Reviewed catastrophe risk and exposure modeling frameworks.</li>
        <li>Analyzed pricing strategies in complex insurance portfolios.</li>
        <li><strong>Impact:</strong> Built strong understanding of specialty & commercial insurance structures.</li>
        </ul>

        </div>


        <div class="experience-card">

        <h3>AIG</h3>
        <p class="exp-role">Actuarial Analyst Job Simulation</p>
        <span class="exp-badge">Data Interpretation</span>
        <span class="exp-badge">Pricing Analysis</span>
        <span class="exp-badge">Report Writing</span>
        <span class="exp-badge">Technical Writing</span>
                    
        <ul class="exp-list">
        <li>Completed simulation involving Marine Liability insurance pricing and risk assessment for the Specialty Lines Actuarial team at AIG</li>
        <li>Analyzed and interpreted a dataset of 100 Marine Liability insurance claims, identifying key trends and anomalies using statistical methods and data visualization techniques</li>
        <li>Applied actuarial principles to evaluate risks and calculated premiums using experience-based rating, resulting in detailed pricing assessments and recommendations</li>
        <li><strong>Impact:</strong> Developed comprehensive reports that included assumptions, methodologies, and commentary on risks and uncertainites, demonstrating strong technical writing and critical thinking skills</li>
        </ul>

        </div>


        <div class="experience-card">

        <h3>AIG</h3>
        <p class="exp-role">Underwriting & Claims Simulation</p>
        <span class="exp-badge">Proposal Writing</span>
        <span class="exp-badge">Logical Reasoning</span>
        <span class="exp-badge">Presentation Skills</span>
        <span class="exp-badge">Policy Analysis</span>
        <span class="exp-badge">Process Mapping</span>
                    
        <ul class="exp-list">
        <li>Completed a simulation involving underwriting policies for AIG's healthcare team</li>
        <li>Utilized both quantitative and qualitative methods for risk assessment in a healthcare contect</li>
        <li>Created Policy summaries and presentations to effectively convey product strengths to clients</li>
        <li><strong>Impact:</strong> Developed structured underwriting & claims evaluation approach.</li>
        </ul>

        </div>


        <div class="experience-card">

        <h3>London Insurance Life</h3>
        <p class="exp-role">Claims Adjuster & Claims Operations Simulation</p>
        <span class="exp-badge">Claims Analysis</span>
        <span class="exp-badge">Process Managament</span>
        <span class="exp-badge">Systems Analysis</span>

        <ul class="exp-list">
        <li>Completed a simulation where i worked as a London Market Claims Adjuster</li>
        <li>Reviewed a First Notice of Loss to identify areas where further information was required</li>
        <li>Prepared for a client relationship meeting, analysing a Claims Report to idenify key patterns in the data</li>
        <li><strong>Impact:</strong> Analysed a data set relating to the performance of a claims department and suggested process improvements</li>
        </ul>

        </div>

        """, unsafe_allow_html=True)

    # ---------------- SKILLS ----------------
    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Core Insurance Skills</div>', unsafe_allow_html=True)


    # ---------- DONUT FUNCTION ----------
    def animated_donut(title, value):
        st.markdown(f'<div class="donut-title">{title}</div>', unsafe_allow_html=True)

        fig = go.Figure()
        fig.add_trace(go.Pie(
            values=[value, 100-value],
            hole=0.75,
            marker_colors=["#3b82f6", "#1e293b"],
            textinfo='none'
        ))

        fig.update_layout(
            showlegend=False,
            margin=dict(t=10, b=0, l=0, r=0),
            height=230,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            annotations=[dict(
                text=f"<b>{value}%</b>",
                x=0.5, y=0.5,
                showarrow=False,
                font_size=22,
                font_color="white"
            )]
        )

        st.plotly_chart(fig, use_container_width=True)


    # ---------- SKILL BAR FUNCTION ----------
    def skill_bar(label, value):
        st.markdown(f"""
        <div class="skill-item">
            <div class="skill-header">
                <span>{label}</span>
                <span>{value}%</span>
            </div>
            <div class="skill-bar">
                <div class="skill-fill" style="width:{value}%"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)


    # ---------- LAYOUT ----------
    col1, col2 = st.columns(2)

    with col1:

        animated_donut("Core Claim Skills", 88)
        skill_bar("Policy Interpretation", 90)
        skill_bar("Claim Admissibility", 85)
        skill_bar("Fraud Detection", 80)
        skill_bar("Regulatory Compliance", 88)

        animated_donut("Operations & Policy Servicing Skills", 84)
        skill_bar("Proposal Processing", 85)
        skill_bar("Policy Issuance & Endorsements", 82)
        skill_bar("Documentation Management", 80)
        skill_bar("Process Improvement", 86)

    with col2:

        animated_donut("Risk Management & Corporate Insurance Skills", 86)
        skill_bar("Risk Identification", 88)
        skill_bar("Insurance Program Design", 85)
        skill_bar("Loss Prevention", 83)
        skill_bar("Contract Risk Analysis", 87)

        animated_donut("Insurance Analytics & Product Skills", 82)
        skill_bar("Excel", 90)
        skill_bar("Power BI / Tableau", 80)
        skill_bar("Claims & Premium Analysis", 85)
        skill_bar("Fraud Analytics", 78)


# ---------------- CASE STUDIES ----------------
    st.markdown('<div id="case-studies" class="section-title">Insurance Case Studies</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    def case_card(title, desc, tags, link):
            tags_html = "".join([f'<span class="case-tag">{tag}</span>' for tag in tags])

            return f"""
            <div class="case-card fade-in">
                <div class="case-title">{title}</div>
                <div class="case-desc">{desc}</div>
                {tags_html}
                <br><br>
                <a href="{link}" target="_blank" class="case-button">
                View Case Study (PDF)
                </a>
            </div>
            """

    with col1:
            st.markdown(case_card(
                "Analytics-Driven Claims Automation",
                "Built an analytics-led claims triage framework to reduce manual adjudication and improve severity-based prioritization using fraud indicators and risk scoring.",
                ["Claims Analytics", "Automation", "Operational Efficiency"],
                "https://raw.githubusercontent.com/Sultanbasit23/insurance-case-studies/main/analytics-driven-claims-automation.pdf"
            ), unsafe_allow_html=True)

            st.markdown(case_card(
                "Insurance Capital Optimization",
                "Developed a capital allocation strategy using risk-adjusted performance metrics to optimize solvency positioning and enhance portfolio capital efficiency.",
                ["Capital Management", "Solvency Analysis", "Risk Allocation"],
                "https://raw.githubusercontent.com/Sultanbasit23/insurance-case-studies/main/insurance-capital-optimization.pdf"
            ), unsafe_allow_html=True)

            st.markdown(case_card(
                "Integrated Claims Decisioning",
                "Designed a structured claims decisioning model integrating underwriting inputs, fraud signals, and severity thresholds to enhance adjudication accuracy.",
                ["Decision Framework", "Fraud Signals", "Claims Governance"],
                "https://raw.githubusercontent.com/Sultanbasit23/insurance-case-studies/main/integrated-claims-decisioning.pdf"
            ), unsafe_allow_html=True)

    with col2:
            st.markdown(case_card(
                "Life Insurance Needs Analysis",
                "Built a structured financial protection model evaluating income replacement ratios, dependents, and long-term liabilities for optimal coverage design.",
                ["Life Insurance", "Financial Planning", "Protection Strategy"],
                "https://raw.githubusercontent.com/Sultanbasit23/insurance-case-studies/main/life-insurance-needs-analysis.pdf"
            ), unsafe_allow_html=True)

            st.markdown(case_card(
                "Motor Claims Digital Transformation",
                "Proposed a digital transformation roadmap leveraging automation, workflow optimization, and analytics dashboards to improve claims turnaround.",
                ["Digital Strategy", "Motor Insurance", "Process Optimization"],
                "https://raw.githubusercontent.com/Sultanbasit23/insurance-case-studies/main/motor-claims-digital-transformation.pdf"
            ), unsafe_allow_html=True)

            st.markdown(case_card(
                "Personal Income Protection Strategy",
                "Evaluated disability and income protection frameworks to design risk-adjusted coverage solutions aligned with income volatility profiles.",
                ["Income Protection", "Risk Assessment", "Policy Structuring"],
                "https://raw.githubusercontent.com/Sultanbasit23/insurance-case-studies/main/personal-income-protection.pdf"
            ), unsafe_allow_html=True)

    # ---------------- PROJECTS ----------------
    st.markdown('<div id="projects" class="section-title">Projects</div>', unsafe_allow_html=True)

    proj_col1, proj_col2 = st.columns(2)

    def render_project(title, desc, tech_tags, status=None, live_link=None, git_link=None):
        with st.container(border=True):
            header = f"**{title}**"
            if status:
                header += f"  \n_Status: {status}_"
            st.markdown(header)

            st.write(desc)

            st.write("**Tech Stack:**")
            st.write(", ".join(tech_tags))

            button_col1, button_col2 = st.columns(2)

            if live_link:
                with button_col1:
                    st.link_button("Live Demo", live_link)

            if git_link:
                with button_col2:
                    st.link_button("GitHub", git_link)

    # ===== LEFT COLUMN =====
    with proj_col1:
        render_project(
            title="Insurance AI Platform",
            desc="A deployed Streamlit application integrating multiple insurance AI modules to assist underwriting, claims decisioning, and policy recommendations.",
            tech_tags=["Streamlit", "Python", "ML", "APIs", "Frontend"],
            status="Live",
            live_link="https://insurance-ai-platform-7drqdp3qmjdatdjv9vl4fq.streamlit.app/",
            git_link="https://github.com/Sultanbasit23/Insurance-AI-platform"
        )

        render_project(
            title="Car Insurance Claim Prediction AI",
            desc="End-to-end ML model predicting probability of car insurance claims with SHAP explainability and interactive Streamlit deployment.",
            tech_tags=["Python", "scikit-learn", "SHAP", "Streamlit"],
            status="Live",
            live_link="https://car-insurance-claim-utosybsqhkwxtkgbqycenv.streamlit.app/",
            git_link="https://github.com/Sultanbasit23/car-insurance-claim"
        )

        render_project(
            title="AI Life Insurance Agent",
            desc="Intelligent AI agent analyzing customer financial profile to recommend optimized life insurance structures.",
            tech_tags=["AI Agent", "LLM", "NLP"],
            status="In Development"
        )

    # ===== RIGHT COLUMN =====
    with proj_col2:
        render_project(
            title="AI Real Estate Agent",
            desc="AI-driven system assisting property investment decisions and valuation analytics.",
            tech_tags=["AI Agent", "Predictive Modeling"],
            status="In Development"
        )

        render_project(
            title="AI Crypto Quant Agent",
            desc="Algorithmic AI trading agent leveraging market signals and reinforcement learning.",
            tech_tags=["AI Agent", "Quant", "Reinforcement Learning"],
            status="In Development"
        )

        render_project(
            title="AI Hedge Fund Agent",
            desc="Autonomous AI framework for multi-asset allocation and strategic portfolio optimization.",
            tech_tags=["AI Agent", "Multi-Asset Strategy"],
            status="In Development"
        )

    # ================== CONTACT ============================

    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

    st.markdown("<div class='contact-title'>Connect With Me</div>", unsafe_allow_html=True)
    st.markdown("<div class='contact-subtitle'>Far far away, behind the word mountains, far from the countries Narnia and Hogwarts</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='contact-card'>
            <div class='contact-icon'>📱</div>
            <h4>Phone</h4>
            <a href='tel:+917305797531'>+91 73057 97531</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='contact-card'>
            <div class='contact-icon'>📧</div>
            <h4>Email</h4>
            <a href='mailto:basitsultanmohammed@gmail.com'>basitsultanmohammed@gmail.com</a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='contact-card'>
            <div class='contact-icon'>💼</div>
            <h4>LinkedIn</h4>
            <a href='https://www.linkedin.com/in/basitsultan/' target='_blank'>https://www.linkedin.com/in/basitsultan/</a>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class='contact-card'>
            <div class='contact-icon'>💻</div>
            <h4>GitHub</h4>
            <a href='https://github.com/Sultanbasit23' target='_blank'>https://github.com/Sultanbasit23</a>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class='contact-card'>
            <div class='contact-icon'>🌐</div>
            <h4>Website</h4>
            <a href='https://basitsultan.streamlit.app/' target='_blank'>https://basitsultan.streamlit.app/</a>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div class='contact-card'>
            <div class='contact-icon'>🐦</div>
            <h4>Twitter</h4>
            <a href='https://x.com/IAmSultanBasit' target='_blank'>https://x.com/IAmSultanBasit</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align:center; margin-top:60px;'>
        <a href='mailto:basitsultanmohammed@gmail.com' 
        style='padding:16px 40px;
                background: linear-gradient(90deg,#3b82f6,#6366f1);
                color:white;
                border-radius:50px;
                text-decoration:none;
                font-weight:600;
                box-shadow: 0 15px 30px rgba(59,130,246,0.3);
                transition:0.3s;'>
            Let’s Work Together 🚀
        </a>
    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# ================== ANALYTICS PLAYGROUND ==================
# ==========================================================
if page == "Insurance Intelligence Lab":

    st.markdown("""
    <div style='text-align:center; margin-bottom:50px;'>
        <h1>Insurance Intelligence Lab</h1>
        <p style='color:#94a3b8; font-size:18px;'>
        AI-Powered Risk & Fraud Analytics Sandbox
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ======================
    # Generate Synthetic Data (Cached)
    # ======================
    @st.cache_data
    def generate_data():
        np.random.seed(42)
        df = pd.DataFrame({
            "Age": np.random.randint(18, 75, 300),
            "Premium": np.random.randint(5000, 50000, 300),
            "Claim Amount": np.random.randint(0, 60000, 300),
            "Previous Claims": np.random.randint(0, 5, 300)
        })

        df["Fraud"] = np.where(
            (df["Claim Amount"] > 40000) & (df["Previous Claims"] > 2),
            1, 0
        )
        return df

    data = generate_data()

    # ======================
    # KPIs
    # ======================
    fraud_rate = round(data["Fraud"].mean() * 100, 2)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Policies Evaluated", f"{len(data)}+")
    col2.metric("Fraud Cases", f"{data['Fraud'].sum()}+")
    col3.metric("Fraud Rate", f"{fraud_rate}%")
    col4.metric("Avg Claim Amount", f"₹{int(data['Claim Amount'].mean())}")

    st.markdown("---")

    # ======================
    # Claims Distribution Chart
    # ======================
    st.subheader("Claim Amount Distribution")

    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=data["Claim Amount"],
        marker=dict(color="#3b82f6")
    ))

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ======================
    # Train ML Model (Cached)
    # ======================
    @st.cache_resource
    def train_model(df):
        X = df[["Age", "Premium", "Previous Claims"]]
        y = df["Fraud"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LogisticRegression()
        model.fit(X_train, y_train)

        return model, X_test, y_test

    model, X_test, y_test = train_model(data)

    accuracy = accuracy_score(y_test, model.predict(X_test))

    st.subheader("Underwriting Risk Intelligence Engine")
    st.progress(int(accuracy * 100))
    st.caption(f"Model Accuracy: {round(accuracy * 100, 2)}%")

    # ======================
    # Confusion Matrix
    # ======================
    preds = model.predict(X_test)

    cm = pd.crosstab(
        y_test,
        preds,
        rownames=["Actual"],
        colnames=["Predicted"]
    )

    st.subheader("Confusion Matrix")
    st.dataframe(cm, use_container_width=True)

    # ======================
    # Feature Importance
    # ======================
    st.subheader("Model Feature Importance")

    importance = pd.DataFrame({
        "Feature": ["Age", "Premium", "Previous Claims"],
        "Coefficient": model.coef_[0]
    }).sort_values(by="Coefficient", key=abs, ascending=False)

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=importance["Coefficient"],
        y=importance["Feature"],
        orientation="h",
        marker=dict(color="#6366f1")
    ))

    fig2.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # ======================
    # Interactive Risk Simulator
    # ======================
    st.subheader("Live Risk Simulator")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Client Age", 18, 75, 30)
        premium = st.slider("Premium Amount", 5000, 50000, 15000)

    with col2:
        prev_claims = st.slider("Previous Claims", 0, 5, 1)

    input_data = np.array([[age, premium, prev_claims]])
    risk = model.predict_proba(input_data)[0][1]

    st.markdown("### Fraud Risk Probability")

    st.progress(int(risk * 100))

    if risk > 0.6:
        st.error(f"High Fraud Risk: {round(risk * 100, 2)}%")
    elif risk > 0.3:
        st.warning(f"Moderate Fraud Risk: {round(risk * 100, 2)}%")
    else:
        st.success(f"Low Fraud Risk: {round(risk * 100, 2)}%")