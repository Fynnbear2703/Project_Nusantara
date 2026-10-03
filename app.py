import os
import datetime
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Project Nusantara | Socratic AI Companion",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced CSS Injection for SaaS Level Bright Academic Aesthetics
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    /* Global reset and background */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #F8FAFC !important;
        font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif !important;
        color: #0F172A !important;
    }

    /* Hide standard Streamlit header clutter */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    
    footer {
        visibility: hidden;
    }

    /* Header Bar Container */
    .brand-header {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 20px 28px;
        margin-bottom: 24px;
        box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.04);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .brand-title {
        font-size: 1.5rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.02em;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .brand-subtitle {
        font-size: 0.88rem;
        color: #64748B;
        margin-top: 2px;
        font-weight: 500;
    }

    /* Custom Navigation Tabs Styling */
    div[data-baseweb="tab-list"] {
        gap: 8px !important;
        background-color: #FFFFFF !important;
        padding: 8px !important;
        border-radius: 14px !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03) !important;
        margin-bottom: 24px !important;
    }

    button[data-baseweb="tab"] {
        border-radius: 10px !important;
        padding: 10px 24px !important;
        font-size: 0.92rem !important;
        font-weight: 600 !important;
        color: #64748B !important;
        background-color: transparent !important;
        border: none !important;
        transition: all 0.2s ease !important;
    }

    button[aria-selected="true"] {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
    }

    /* Cards and Containers */
    .nusantara-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.03);
    }

    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 6px;
    }

    /* Custom Badges */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.01em;
    }

    .badge-emerald {
        background-color: #ECFDF5;
        color: #047857;
        border: 1px solid #A7F3D0;
    }

    .badge-blue {
        background-color: #EFF6FF;
        color: #1D4ED8;
        border: 1px solid #BFDBFE;
    }

    .badge-amber {
        background-color: #FFFBEB;
        color: #B45309;
        border: 1px solid #FDE68A;
    }

    /* Socratic Prompt Banner */
    .socratic-box {
        background: linear-gradient(135deg, #EFF6FF 0%, #F0F9FF 100%);
        border: 1px solid #BFDBFE;
        border-left: 5px solid #2563EB;
        padding: 18px;
        border-radius: 12px;
        margin: 16px 0;
    }

    .socratic-title {
        font-size: 0.85rem;
        text-transform: uppercase;
        font-weight: 800;
        color: #1D4ED8;
        letter-spacing: 0.05em;
        margin-bottom: 6px;
    }

    .socratic-text {
        font-size: 0.95rem;
        color: #1E293B;
        font-weight: 600;
        line-height: 1.5;
    }

    /* Metric Visual Blocks */
    .metric-container {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 18px;
        text-align: left;
        box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }

    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0F172A;
    }

    .metric-label {
        font-size: 0.82rem;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
    }

    /* Timeline Styling */
    .timeline-node {
        border-left: 2px solid #E2E8F0;
        padding-left: 20px;
        margin-left: 10px;
        padding-bottom: 18px;
        position: relative;
    }

    .timeline-dot {
        position: absolute;
        left: -7px;
        top: 2px;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background-color: #2563EB;
        border: 2px solid #FFFFFF;
        box-shadow: 0 0 0 2px #BFDBFE;
    }

    /* Styled Input and Text Areas */
    .stTextArea textarea {
        border-radius: 12px !important;
        border: 1px solid #CBD5E1 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.95rem !important;
        padding: 14px !important;
        background-color: #FFFFFF !important;
    }

    .stTextArea textarea:focus {
        border-color: #2563EB !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
    }

    /* Buttons */
    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        padding: 10px 20px !important;
        border: 1px solid #CBD5E1 !important;
        transition: all 0.2s ease !important;
    }

    div.stButton > button[kind="primary"] {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
    }

    div.stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 16px rgba(15, 23, 42, 0.08) !important;
    }
</style>
""", unsafe_allow_html=True)

# Fetch API Key from Streamlit Secrets or Environment
api_key = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))

# Session State Initialization
if "effort_log" not in st.session_state:
    st.session_state.effort_log = [
        {"time": "3 days ago", "action": "Initial Chapter Structure Drafted"},
        {"time": "1 day ago", "action": "Verified SINTA Citations Added (Sukarna et al., 2023)"},
        {"time": "3 hours ago", "action": "Answered Socratic Prompt on Sample Justification"}
    ]

if "last_socratic_prompt" not in st.session_state:
    st.session_state.last_socratic_prompt = (
        "Bagaimana ukuran sampel 50 responden ini secara spesifik dapat mendukung validitas "
        "analisis statistik kuantitatif Anda di Bab 3?"
    )

# Function to trigger Socratic feedback
def generate_socratic_coaching(draft_text: str) -> str:
    if not api_key:
        return (
            "💡 [Socratic Guidance Engine]\n"
            "Bagaimana Anda dapat menjelaskan landasan teori yang memjustifikasi pemilihan "
            "metode pengambilan sampel ini dalam konteks penelitian Anda?"
        )
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        system_instruction = (
            "You are the Socratic AI Coach for Project Nusantara, an Indonesian higher education thesis companion. "
            "Your task is NEVER to rewrite or generate thesis paragraphs for the student. "
            "Instead, analyze the provided thesis draft and generate 1 to 2 diagnostic, thought-provoking Socratic questions "
            "in academic Indonesian."
        )
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Thesis Draft Segment:\n{draft_text}",
            config={"system_instruction": system_instruction, "temperature": 0.4}
        )
        return response.text
    except Exception as e:
        return f"Socratic Engine Active: Mohon jelaskan alasan mendasar pemilihan instrumen pengumpulan data ini. (Note: {str(e)})"

# Top Header Bar
st.markdown("""
<div class="brand-header">
    <div>
        <div class="brand-title">🎓 Project Nusantara</div>
        <div class="brand-subtitle">Socratic Academic Writing & Process Integrity System</div>
    </div>
    <div>
        <span class="badge badge-emerald">Campus Portal: Connected</span>
        <span class="badge badge-blue">Gemini Engine Live</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Navigation Tabs
tab_student, tab_advisor, tab_faculty = st.tabs([
    "📝 Student Workspace & Extension Sidebar", 
    "👨‍🏫 Advisor Review & Effort Audit", 
    "📊 Campus Analytics Portal"
])

# TAB 1: STUDENT WORKSPACE
with tab_student:
    col_editor, col_sidebar = st.columns([0.65, 0.35], gap="large")
    
    with col_editor:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">📄 Canvas Editor: Chapter_3_Methodology_Budi.docx</div>', unsafe_allow_html=True)
        st.caption("Simulated Google Docs drafting environment with active extension integration")
        
        sample_draft = st.text_area(
            label="Thesis Document Area",
            value=(
                "BAB 3 METODOLOGI PENELITIAN\n\n"
                "3.1 Metode Pengumpulan Data\n"
                "Penelitian ini menggunakan pendekatan kuantitatif dengan menyebarkan kuesioner "
                "kepada 50 responden mahasiswa di Jawa Timur. Pengambilan sampel dilakukan "
                "menggunakan teknik random sampling untuk mengukur tingkat adopsi teknologi LMS.\n\n"
                "3.2 Populasi dan Sampel\n"
                "Populasi dalam penelitian ini adalah seluruh mahasiswa aktif. Rujukan utama "
                "mengacu pada penelitian Sukarna et al. (2023) mengenai efisiensi pembelajaran digital."
            ),
            height=380,
            label_visibility="collapsed"
        )
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔍 Run Socratic Diagnostic Check", use_container_width=True, type="primary"):
                with st.spinner("Analyzing methodology logic..."):
                    prompt_result = generate_socratic_coaching(sample_draft)
                    st.session_state.last_socratic_prompt = prompt_result
                    st.rerun()
        with c2:
            st.button("💾 Save & Sync to Campus LMS", use_container_width=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

    with col_sidebar:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">💡 Nusantara Smart Sidebar</div>', unsafe_allow_html=True)
        st.caption("Socratic coaching layer (Diagnostic inquiry only)")
        
        st.markdown(f"""
        <div class="socratic-box">
            <div class="socratic-title">Active Diagnostic Nudge</div>
            <div class="socratic-text">{st.session_state.last_socratic_prompt}</div>
        </div>
        """, unsafe_allow_html=True)
        
        reflection_input = st.text_area("Your Reflective Defense:", placeholder="Ex: Sample size of 50 was calculated using Slovin formula...", height=110)
        
        if st.button("Log Reflection to Thesis Audit", use_container_width=True):
            if reflection_input.strip():
                timestamp = datetime.datetime.now().strftime("%H:%M")
                st.session_state.effort_log.insert(0, {
                    "time": f"Today at {timestamp}",
                    "action": f"Answered Socratic Prompt: '{reflection_input[:38]}...'"
                })
                st.success("Reflection recorded in Effort Audit Log!")
                st.rerun()
            else:
                st.warning("Please type a defense before logging.")
        
        st.markdown("<hr style='margin: 18px 0; border-color: #E2E8F0;'>", unsafe_allow_html=True)
        st.markdown("#### 📑 Verification Status")
        st.markdown("- **SINTA Citations:** <span class='badge badge-emerald'>Verified (Sukarna et al., 2023)</span>", unsafe_allow_html=True)
        st.markdown("- **Formatting Rule:** <span class='badge badge-blue'>94% Compliant</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# TAB 2: ADVISOR REVIEW
with tab_advisor:
    col_draft_view, col_effort_monitor = st.columns([0.60, 0.40], gap="large")
    
    with col_draft_view:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Submitted Chapter Draft: Budi Santoso (NIM: 5025211000)</div>', unsafe_allow_html=True)
        st.markdown("<span class='badge badge-blue'>Chapter 3: Methodology</span> <span class='badge badge-emerald'>Pre-screened</span>", unsafe_allow_html=True)
        st.markdown("<hr style='margin: 16px 0; border-color: #E2E8F0;'>", unsafe_allow_html=True)
        
        st.markdown("""
        **BAB 3 METODOLOGI PENELITIAN**
        
        **3.1 Metode Pengumpulan Data**  
        Penelitian ini menggunakan pendekatan kuantitatif dengan menyebarkan kuesioner kepada 50 responden mahasiswa di Jawa Timur. Pengambilan sampel dilakukan menggunakan teknik random sampling.  
        
        <div style="background-color: #ECFDF5; padding: 10px; border-radius: 8px; border-left: 4px solid #059669; margin: 12px 0;">
            <b>✓ Pre-screened Citation:</b> Sukarna et al. (2023) verified against national SINTA academic index.
        </div>
        
        **3.2 Populasi dan Sampel**  
        Populasi dalam penelitian ini adalah seluruh mahasiswa aktif. Rujukan utama mengacu pada penelitian Sukarna et al. (2023) mengenai efisiensi pembelajaran digital.
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Advisor Action & Feedback</div>', unsafe_allow_html=True)
        advisor_notes = st.text_input("Qualitative Remarks:", placeholder="Ex: Expand sample size justification in Section 3.2...")
        ac1, ac2 = st.columns(2)
        with ac1:
            st.button("✅ Approve Milestone", use_container_width=True, type="primary")
        with ac2:
            st.button("🔄 Request Revision", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_effort_monitor:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🛡️ Effort Audit Log</div>', unsafe_allow_html=True)
        st.caption("Chronological proof of student reflection and writing process")
        
        m1, m2 = st.columns(2)
        with m1:
            st.markdown('<div class="metric-container"><div class="metric-label">Genuine Effort</div><div class="metric-value">34.5h</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="metric-container"><div class="metric-label">Reflections</div><div class="metric-value">{len(st.session_state.effort_log)}</div></div>', unsafe_allow_html=True)
            
        st.markdown("<hr style='margin: 18px 0; border-color: #E2E8F0;'>", unsafe_allow_html=True)
        st.markdown("#### Activity Timeline")
        
        for item in st.session_state.effort_log:
            st.markdown(f"""
            <div class="timeline-node">
                <div class="timeline-dot"></div>
                <div style="font-size: 0.78rem; color: #64748B; font-weight: 600;">{item['time']}</div>
                <div style="font-size: 0.90rem; color: #0F172A; font-weight: 600; margin-top: 2px;">{item['action']}</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

# TAB 3: FACULTY ANALYTICS
with tab_faculty:
    st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Executive Department Dashboard</div>', unsafe_allow_html=True)
    st.caption("Institutional oversight for thesis completion speed and academic integrity standards")
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-container"><div class="metric-label">Active Writers</div><div class="metric-value">1,240</div><span class="badge badge-emerald">98% On Track</span></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-container"><div class="metric-label">Avg Chapter Speed</div><div class="metric-value">3.2 wks</div><span class="badge badge-blue">-0.8 wks faster</span></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-container"><div class="metric-label">Advisor Workload</div><div class="metric-value">Balanced</div><span class="badge badge-emerald">-35% review time</span></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-container"><div class="metric-label">Integrity Health</div><div class="metric-value">96/100</div><span class="badge badge-emerald">Accredited</span></div>', unsafe_allow_html=True)
        
    st.markdown("<hr style='margin: 20px 0; border-color: #E2E8F0;'>", unsafe_allow_html=True)
    
    st.markdown("#### Department Cohort Status")
    dept_data = [
        {"Student": "Gryffyn Teh", "Department": "Computer Science", "Milestone": "Chapter 3 Methodology", "Effort Hours": "42 hrs", "Socratic Responses": 38, "Status": "On Track"},
        {"Student": "Budi Santoso", "Department": "Information Systems", "Milestone": "Chapter 3 Methodology", "Effort Hours": "34 hrs", "Socratic Responses": 24, "Status": "On Track"},
        {"Student": "Siti Nurhaliza", "Department": "Software Engineering", "Milestone": "Chapter 2 Lit Review", "Effort Hours": "18 hrs", "Socratic Responses": 12, "Status": "Needs Nudge"},
        {"Student": "Ahmad Rizki", "Department": "Computer Science", "Milestone": "Chapter 4 Results", "Effort Hours": "56 hrs", "Socratic Responses": 45, "Status": "Approved"},
    ]
    st.table(dept_data)
    
    if st.button("📥 Export Accreditation Process Audit Report (PDF/CSV)"):
        st.info("Generating certified audit report for university accreditation board...")
        
    st.markdown('</div>', unsafe_allow_html=True)
