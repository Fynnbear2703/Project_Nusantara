import os
import datetime
import pandas as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Project Nusantara | Socratic AI & Academic Integrity",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Complete High-Contrast Light Mode CSS Injection
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    /* Global Background and Typography Reset */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"] {
        background-color: #F8FAFC !important;
        font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif !important;
        color: #0F172A !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    
    footer {
        visibility: hidden;
    }

    /* Force Dark Slate Text across all native HTML & Streamlit Markdown elements */
    p, span, div, label, h1, h2, h3, h4, h5, h6, strong, em, small, code {
        color: #0F172A !important;
    }

    /* Header Bar */
    .brand-header {
        background: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 16px;
        padding: 18px 28px;
        margin-bottom: 20px;
        box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.05);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .brand-title {
        font-size: 1.45rem;
        font-weight: 800;
        color: #0F172A !important;
        letter-spacing: -0.02em;
        margin: 0;
    }

    .brand-subtitle {
        font-size: 0.88rem;
        color: #334155 !important;
        margin-top: 2px;
        font-weight: 600;
    }

    /* Navigation Tabs */
    div[data-baseweb="tab-list"] {
        gap: 8px !important;
        background-color: #FFFFFF !important;
        padding: 6px !important;
        border-radius: 14px !important;
        border: 1px solid #CBD5E1 !important;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03) !important;
        margin-bottom: 22px !important;
    }

    button[data-baseweb="tab"] {
        border-radius: 10px !important;
        padding: 10px 24px !important;
        font-size: 0.90rem !important;
        font-weight: 700 !important;
        color: #334155 !important;
        background-color: transparent !important;
        border: none !important;
        transition: all 0.2s ease !important;
    }

    button[aria-selected="true"] {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
    }

    button[aria-selected="true"] p, button[aria-selected="true"] span {
        color: #FFFFFF !important;
    }

    /* Cards & Containers */
    .nusantara-card {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.04);
    }

    .card-title {
        font-size: 1.08rem;
        font-weight: 800;
        color: #0F172A !important;
        margin-bottom: 4px;
    }

    .card-caption {
        font-size: 0.84rem;
        color: #475569 !important;
        font-weight: 500;
        margin-bottom: 14px;
    }

    /* Custom Badges */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 800;
        margin-right: 6px;
    }

    .badge-emerald {
        background-color: #ECFDF5;
        color: #047857 !important;
        border: 1px solid #A7F3D0;
    }

    .badge-blue {
        background-color: #EFF6FF;
        color: #1D4ED8 !important;
        border: 1px solid #BFDBFE;
    }

    .badge-rose {
        background-color: #FFF1F2;
        color: #BE123C !important;
        border: 1px solid #FECDD3;
    }

    /* Socratic Guidance Banner */
    .socratic-box {
        background: linear-gradient(135deg, #EFF6FF 0%, #F0F9FF 100%);
        border: 1px solid #BFDBFE;
        border-left: 5px solid #2563EB;
        padding: 16px;
        border-radius: 12px;
        margin: 14px 0;
    }

    .socratic-title {
        font-size: 0.80rem;
        text-transform: uppercase;
        font-weight: 800;
        color: #1D4ED8 !important;
        letter-spacing: 0.05em;
        margin-bottom: 6px;
    }

    .socratic-text {
        font-size: 0.94rem;
        color: #0F172A !important;
        font-weight: 700;
        line-height: 1.5;
    }

    /* Metric Boxes */
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 14px;
        padding: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }

    .metric-val {
        font-size: 1.75rem;
        font-weight: 800;
        color: #0F172A !important;
    }

    .metric-lbl {
        font-size: 0.78rem;
        font-weight: 700;
        color: #475569 !important;
        text-transform: uppercase;
        margin-bottom: 4px;
    }

    /* Timeline Nodes */
    .timeline-node {
        border-left: 2px solid #CBD5E1;
        padding-left: 18px;
        margin-left: 8px;
        padding-bottom: 16px;
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

    /* Input & Selectbox Overrides for Universal Contrast */
    .stTextArea textarea, .stTextInput input, div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 10px !important;
        border: 1px solid #CBD5E1 !important;
        font-size: 0.92rem !important;
        font-weight: 500 !important;
    }

    /* Dropdown Menus (Baseweb Popovers) */
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"] {
        background-color: #FFFFFF !important;
    }

    div[data-baseweb="popover"] span, ul[role="listbox"] li {
        color: #0F172A !important;
        background-color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    /* Button Styling */
    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        padding: 8px 18px !important;
        border: 1px solid #CBD5E1 !important;
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        transition: all 0.2s ease !important;
    }

    div.stButton > button[kind="primary"] {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.22) !important;
    }

    div.stButton > button[kind="primary"] p, div.stButton > button[kind="primary"] span {
        color: #FFFFFF !important;
    }

    /* High-Contrast Streamlit Tables */
    div[data-testid="stTable"] table {
        color: #0F172A !important;
        background-color: #FFFFFF !important;
        border-collapse: collapse !important;
        border: 1px solid #CBD5E1 !important;
    }
    
    div[data-testid="stTable"] th {
        background-color: #F1F5F9 !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        border-bottom: 2px solid #CBD5E1 !important;
    }

    div[data-testid="stTable"] td {
        color: #0F172A !important;
        border-bottom: 1px solid #E2E8F0 !important;
        font-size: 0.88rem !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Environment & Gemini Setup
api_key = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))

# 4. Session State Initialization
if "student_database" not in st.session_state:
    st.session_state.student_database = {
        "Gryffyn Teh": {
            "nim": "5025211001",
            "dept": "Computer Science",
            "milestone": "Bab 3 Metodologi",
            "draft_version": "v3.2",
            "effort_hours": 42.5,
            "socratic_count": 38,
            "authenticity_score": "99% High",
            "status": "On Track",
            "risk_level": "Low",
            "content": (
                "BAB 3 METODOLOGI PENELITIAN\n\n"
                "3.1 Metode Pengumpulan Data\n"
                "Penelitian ini menggunakan pendekatan kuantitatif eksperimental dengan menyebarkan "
                "kuesioner terstruktur kepada 50 responden mahasiswa di Jawa Timur. Pengambilan sampel "
                "dilakukan menggunakan teknik Stratified Random Sampling untuk mengukur efektivitas "
                "interaksi Socratic AI pada platform Learning Management System (LMS).\n\n"
                "3.2 Populasi dan Sampel\n"
                "Populasi dalam penelitian ini mencakup seluruh mahasiswa aktif program studi teknik. "
                "Rujukan penentuan ukuran sampel mengacu pada formula Slovin dengan marjin eror 5% "
                "serta ditunjang oleh studi terdahulu Sukarna et al. (2023) mengenai efisiensi pembelajaran digital.\n\n"
                "3.3 Teknik Analisis Data\n"
                "Pengujian hipotesis menggunakan Regresi Linear Berganda dan Partial Least Squares (PLS-SEM) "
                "untuk mengevaluasi hubungan antara frekuensi refleksi Socratic dan tingkat pemahaman konsep."
            ),
            "citations": [
                {"citation": "Sukarna et al. (2023)", "index": "SINTA 2", "status": "Verified", "doi": "10.1234/sinta.v2i1.45"},
                {"citation": "Pratama & Rahmawati (2022)", "index": "Scopus Q2", "status": "Verified", "doi": "10.1016/j.compedu.2022.10"}
            ]
        },
        "Budi Santoso": {
            "nim": "5025211000",
            "dept": "Information Systems",
            "milestone": "Bab 3 Metodologi",
            "draft_version": "v2.1",
            "effort_hours": 34.0,
            "socratic_count": 24,
            "authenticity_score": "95% High",
            "status": "On Track",
            "risk_level": "Low",
            "content": (
                "BAB 3 METODOLOGI PENELITIAN\n\n"
                "3.1 Desain Penelitian\n"
                "Penelitian ini menerapkan metode Design Science Research Methodology (DSRM) "
                "untuk merancang arsitektur integrasi Socratic Chatbot pada sistem akademik perguruan tinggi."
            ),
            "citations": [
                {"citation": "Hevner et al. (2004)", "index": "Scopus Q1", "status": "Verified", "doi": "10.2307/25148625"}
            ]
        },
        "Siti Nurhaliza": {
            "nim": "5025211002",
            "dept": "Software Engineering",
            "milestone": "Bab 2 Tinjauan Pustaka",
            "draft_version": "v1.0",
            "effort_hours": 14.2,
            "socratic_count": 8,
            "authenticity_score": "78% Moderate",
            "status": "Needs Nudge",
            "risk_level": "Medium (Idle 8 days)",
            "content": (
                "BAB 2 TINJAUAN PUSTAKA\n\n"
                "2.1 Large Language Models dalam Pendidikan\n"
                "Penggunaan AI generatif telah berkembang pesat dalam dunia pendidikan tinggi..."
            ),
            "citations": [
                {"citation": "Zhao et al. (2023)", "index": "Unverified", "status": "Pending Check", "doi": "Pending"}
            ]
        }
    }

# Safe Schema Initializer for Effort Logs to Prevent KeyError
if "effort_log" not in st.session_state or not isinstance(st.session_state.effort_log, list):
    st.session_state.effort_log = [
        {"time": "Today at 09:15", "student": "Gryffyn Teh", "action": "Answered Socratic Prompt on Stratified Random Sampling rationale", "tag": "Socratic Reflection"},
        {"time": "Yesterday at 14:30", "student": "Gryffyn Teh", "action": "Validated SINTA 2 citation: Sukarna et al. (2023)", "tag": "Citation Audit"},
        {"time": "2 days ago", "student": "Budi Santoso", "action": "Submitted Chapter 3 Methodology Draft v2.1", "tag": "Milestone Submit"},
        {"time": "3 days ago", "student": "Gryffyn Teh", "action": "Completed 45 min focused drafting session in Canvas Editor", "tag": "Writing Session"}
    ]

if "last_socratic_prompt" not in st.session_state:
    st.session_state.last_socratic_prompt = (
        "Bagaimana pemeliharaan marjin eror 5% pada formula Slovin secara khusus dapat menjamin "
        "keterwakilan data populasi mahasiswa dalam analisis statistik Bab 3 Anda?"
    )

if "advisor_feedback_feed" not in st.session_state:
    st.session_state.advisor_feedback_feed = [
        {"author": "Dr. Aris Setiawan (NIP: 19780312...)", "time": "Yesterday at 16:20", "text": "Penjelasan Stratified Random Sampling pada Bab 3.1 sudah tajam. Pastikan instrumen kuesioner diselipkan pada Lampiran A."},
        {"author": "Dr. Aris Setiawan (NIP: 19780312...)", "time": "3 days ago", "text": "Mohon perjelas kriteria inklusi populasi pada Bagian 3.2 sebelum bimbingan hari Jumat."}
    ]

# 5. Gemini Socratic API Function
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

# 6. Global Header
st.markdown("""
<div class="brand-header">
    <div>
        <div class="brand-title">🎓 Project Nusantara</div>
        <div class="brand-subtitle">Socratic Academic Writing & Process Integrity Portal</div>
    </div>
    <div>
        <span class="badge badge-emerald">Institut Teknologi Sepuluh Nopember</span>
        <span class="badge badge-blue">Socratic AI Engine Active</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 7. Main Navigation Tabs
tab_student, tab_advisor, tab_faculty = st.tabs([
    "📝 Student Workspace & Extension", 
    "👨‍🏫 Advisor / Lecturer Review Dashboard", 
    "📊 Faculty & Department Analytics"
])

# ==========================================
# TAB 1: STUDENT WORKSPACE
# ==========================================
with tab_student:
    col_editor, col_sidebar = st.columns([0.64, 0.36], gap="large")
    
    with col_editor:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div>
                <div class="card-title">📄 Canvas Docs Editor: Thesis_Chapter3_GryffynTeh.docx</div>
                <div class="card-caption">Target Chapter: Bab 3 Metodologi Penelitian | Word Count: 520 words</div>
            </div>
            <div>
                <span class="badge badge-emerald">Live Chrome Extension Sync</span>
                <span class="badge badge-blue">Version 3.2</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        t1, t2, t3, t4, t5 = st.columns([1, 1, 1.2, 1.2, 2.6])
        with t1: st.button("<b>B</b>", use_container_width=True)
        with t2: st.button("<i>I</i>", use_container_width=True)
        with t3: st.button("🔗 Cite (SINTA)", use_container_width=True)
        with t4: st.button("📐 Formatting", use_container_width=True)
        with t5: st.caption("Auto-saved to Campus Cloud at 10:25 PM")
        
        active_student_data = st.session_state.student_database["Gryffyn Teh"]
        
        sample_draft = st.text_area(
            label="Thesis Text Area",
            value=active_student_data["content"],
            height=320,
            label_visibility="collapsed"
        )
        
        b1, b2, b3 = st.columns([2, 1.5, 1.5])
        with b1:
            if st.button("🔍 Run Diagnostic Socratic Check", use_container_width=True, type="primary"):
                with st.spinner("Socratic AI analyzing methodology logic..."):
                    prompt_result = generate_socratic_coaching(sample_draft)
                    st.session_state.last_socratic_prompt = prompt_result
                    st.rerun()
        with b2:
            st.button("⚡ Audit Citations", use_container_width=True)
        with b3:
            st.button("💾 Submit to LMS", use_container_width=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">💬 Advisor Notes & Guidance Feed</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-caption">Direct qualitative directives from your supervising lecturer</div>', unsafe_allow_html=True)
        
        for feed_item in st.session_state.advisor_feedback_feed:
            st.markdown(f"""
            <div style="background-color: #F8FAFC; border: 1px solid #CBD5E1; border-left: 4px solid #2563EB; padding: 12px 16px; border-radius: 8px; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <strong style="font-size: 0.88rem; color: #0F172A;">{feed_item['author']}</strong>
                    <span style="font-size: 0.78rem; color: #475569;">{feed_item['time']}</span>
                </div>
                <div style="font-size: 0.90rem; color: #0F172A; font-weight: 500;">{feed_item['text']}</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

    with col_sidebar:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">💡 Socratic AI Companion</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-caption">Diagnostic inquiry layer (Will NOT auto-write or generate content)</div>', unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="socratic-box">
            <div class="socratic-title">Active Socratic Diagnostic Nudge</div>
            <div class="socratic-text">{st.session_state.last_socratic_prompt}</div>
        </div>
        """, unsafe_allow_html=True)
        
        reflection_input = st.text_area(
            "Your Reflective Defense Answer:", 
            placeholder="Ex: Formula Slovin dengan e=5% dipilih karena keterbatasan populasi terjangkau...", 
            height=120
        )
        
        if st.button("Log Answer to Effort Audit Trail", use_container_width=True):
            if reflection_input.strip():
                timestamp = datetime.datetime.now().strftime("%H:%M")
                st.session_state.effort_log.insert(0, {
                    "time": f"Today at {timestamp}",
                    "student": "Gryffyn Teh",
                    "action": f"Answered Socratic Nudge: '{reflection_input[:38]}...'",
                    "tag": "Socratic Reflection"
                })
                st.session_state.student_database["Gryffyn Teh"]["socratic_count"] += 1
                st.success("Reflective defense successfully registered in Effort Audit!")
                st.rerun()
            else:
                st.warning("Please type your reflective answer prior to logging.")
        
        st.markdown("<hr style='margin: 18px 0; border-color: #CBD5E1;'>", unsafe_allow_html=True)
        st.markdown("#### 📑 Integrity & Citation Index")
        st.markdown("- **SINTA 2 Citation:** <span class='badge badge-emerald'>Sukarna et al. (2023) Verified</span>", unsafe_allow_html=True)
        st.markdown("- **Scopus Q2 Citation:** <span class='badge badge-emerald'>Pratama & Rahmawati (2022) Verified</span>", unsafe_allow_html=True)
        st.markdown("- **Formatting Rule:** <span class='badge badge-blue'>96% Campus Compliant</span>", unsafe_allow_html=True)
        st.markdown("- **Human Effort Authenticity:** <span class='badge badge-emerald'>99% Genuine</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TAB 2: ADVISOR / LECTURER REVIEW DASHBOARD
# ==========================================
with tab_advisor:
    st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
    f1, f2, f3, f4 = st.columns([1.8, 1.2, 1.2, 1.2])
    with f1:
        selected_student_name = st.selectbox(
            "Select Student Thesis Review:",
            options=list(st.session_state.student_database.keys())
        )
    student_info = st.session_state.student_database[selected_student_name]
    
    with f2:
        st.markdown(f"**NIM / Dept:**  \n{student_info['nim']} | {student_info['dept']}")
    with f3:
        st.markdown(f"**Milestone / Draft:**  \n{student_info['milestone']} ({student_info['draft_version']})")
    with f4:
        if student_info['status'] == "On Track":
            st.markdown("**Status Flag:**  \n<span class='badge badge-emerald'>On Track</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"**Status Flag:**  \n<span class='badge badge-rose'>{student_info['status']}</span>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col_left, col_right = st.columns([0.56, 0.44], gap="large")

    with col_left:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">📄 Manuscript Viewer: {selected_student_name}</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-caption">Pre-screened manuscript with inline citation verification</div>', unsafe_allow_html=True)
        
        st.text_area(
            "Manuscript Content Viewer",
            value=student_info["content"],
            height=280,
            disabled=True,
            label_visibility="collapsed"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🔬 Citation & Index Verification Engine</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-caption">Cross-checked against national SINTA database and Scopus index</div>', unsafe_allow_html=True)
        
        cit_df = pd.DataFrame(student_info["citations"])
        st.table(cit_df)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🛡️ Process Integrity & Effort Audit</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-caption">Verifiable chronological proof of student effort and reflection</div>', unsafe_allow_html=True)
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f'<div class="metric-card"><div class="metric-lbl">Logged Hours</div><div class="metric-val">{student_info["effort_hours"]}h</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="metric-card"><div class="metric-lbl">Reflections</div><div class="metric-val">{student_info["socratic_count"]}</div></div>', unsafe_allow_html=True)
        with m3:
            st.markdown(f'<div class="metric-card"><div class="metric-lbl">Authenticity</div><div class="metric-val">{student_info["authenticity_score"].split()[0]}</div></div>', unsafe_allow_html=True)
            
        st.markdown("<hr style='margin: 14px 0; border-color: #CBD5E1;'>", unsafe_allow_html=True)
        st.markdown("#### Chronological Activity Stream")
        
        # Safe KeyError Prevention using .get()
        student_logs = [log for log in st.session_state.effort_log if log.get("student", "Gryffyn Teh") == selected_student_name]
        
        if student_logs:
            for log in student_logs:
                st.markdown(f"""
                <div class="timeline-node">
                    <div class="timeline-dot"></div>
                    <div style="font-size: 0.76rem; color: #475569; font-weight: 700;">{log.get('time', 'Recently')} • <span style="color: #2563EB;">{log.get('tag', 'General')}</span></div>
                    <div style="font-size: 0.88rem; color: #0F172A; font-weight: 600; margin-top: 2px;">{log.get('action', 'Activity recorded')}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info(f"No specific log activity recorded for {selected_student_name} yet.")
            
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">✍️ Evaluation & Decision Engine</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-caption">Grade milestone criteria and push structured directives to student</div>', unsafe_allow_html=True)
        
        r1, r2 = st.columns(2)
        with r1:
            score_methodology = st.slider("Methodological Rigor", 0, 100, 88)
            score_citations = st.slider("Literature & Citations", 0, 100, 92)
        with r2:
            score_socratic = st.slider("Socratic Defense Quality", 0, 100, 95)
            score_formatting = st.slider("Campus Guidelines Compliance", 0, 100, 90)

        st.markdown("**Quick Preset Feedback Directives:**")
        qp1, qp2, qp3 = st.columns(3)
        preset_text = ""
        with qp1:
            if st.button("Clarify Sampling", use_container_width=True):
                preset_text = "Please expand the theoretical justification for the sampling size in Section 3.2."
        with qp2:
            if st.button("Add SINTA Refs", use_container_width=True):
                preset_text = "Incorporate at least 2 more recent SINTA-indexed journal references in Chapter 3."
        with qp3:
            if st.button("Approve Milestone", use_container_width=True):
                preset_text = "Methodology chapter looks solid and process integrity verified. Approved for seminar presentation."

        advisor_comment = st.text_input("Custom Advisor Directive:", value=preset_text, placeholder="Type qualitative guidance here...")
        
        btn_c1, btn_c2 = st.columns(2)
        with btn_c1:
            if st.button("✅ Approve Milestone & Issue Grade", use_container_width=True, type="primary"):
                st.session_state.student_database[selected_student_name]["status"] = "Approved"
                st.success(f"Milestone approved for {selected_student_name}! Grade recorded.")
                st.rerun()
        with btn_c2:
            if st.button("🔄 Push Feedback Nudge", use_container_width=True):
                if advisor_comment.strip():
                    st.session_state.advisor_feedback_feed.insert(0, {
                        "author": "Dr. Aris Setiawan (NIP: 19780312...)",
                        "time": "Just now",
                        "text": advisor_comment
                    })
                    st.success("Feedback directive pushed directly to student extension sidebar!")
                    st.rerun()
                else:
                    st.warning("Please select or enter a directive message first.")
                    
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# TAB 3: FACULTY & DEPARTMENT ANALYTICS
# ==========================================
with tab_faculty:
    st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">🏛️ Executive Campus Analytics & Accreditation Portal</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-caption">Department-wide oversight for thesis completion speed, lecturer workload, and BAN-PT process integrity compliance</div>', unsafe_allow_html=True)
    
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown('<div class="metric-card"><div class="metric-lbl">Active Student Cohort</div><div class="metric-val">1,240</div><span class="badge badge-emerald">98% On Track</span></div>', unsafe_allow_html=True)
    with k2:
        st.markdown('<div class="metric-card"><div class="metric-lbl">Avg Completion Velocity</div><div class="metric-val">3.2 wks/ch</div><span class="badge badge-blue">0.8 wks Faster</span></div>', unsafe_allow_html=True)
    with k3:
        st.markdown('<div class="metric-card"><div class="metric-lbl">Lecturer Turnaround</div><div class="metric-val">1.8 days</div><span class="badge badge-emerald">-35% Guidance Time</span></div>', unsafe_allow_html=True)
    with k4:
        st.markdown('<div class="metric-card"><div class="metric-lbl">BAN-PT Integrity Rating</div><div class="metric-val">98.4/100</div><span class="badge badge-emerald">A Grade Certified</span></div>', unsafe_allow_html=True)
        
    st.markdown("<hr style='margin: 20px 0; border-color: #CBD5E1;'>", unsafe_allow_html=True)
    
    st.markdown("#### Department Thesis Progress & Risk Matrix")
    
    cohort_list = []
    for name, sdata in st.session_state.student_database.items():
        cohort_list.append({
            "Student Name": name,
            "NIM": sdata["nim"],
            "Department": sdata["dept"],
            "Milestone": sdata["milestone"],
            "Draft Ver": sdata["draft_version"],
            "Logged Effort": f"{sdata['effort_hours']} hrs",
            "Socratic Defenses": sdata["socratic_count"],
            "Authenticity": sdata["authenticity_score"],
            "Risk Level": sdata["risk_level"],
            "Status": sdata["status"]
        })
        
    cohort_df = pd.DataFrame(cohort_list)
    st.table(cohort_df)
    
    st.markdown("<hr style='margin: 20px 0; border-color: #CBD5E1;'>", unsafe_allow_html=True)
    
    st.markdown("#### Supervising Lecturer Workload Balancing Matrix")
    
    lecturer_data = [
        {"Lecturer Name": "Dr. Aris Setiawan", "Department": "Computer Science", "Assigned Students": 8, "Pending Reviews": 2, "Avg Turnaround": "1.2 days", "Burnout Index": "Normal"},
        {"Lecturer Name": "Prof. Rina Triana", "Department": "Information Systems", "Assigned Students": 12, "Pending Reviews": 5, "Avg Turnaround": "2.4 days", "Burnout Index": "Moderate"},
        {"Lecturer Name": "Dr. Hendra Wijaya", "Department": "Software Engineering", "Assigned Students": 6, "Pending Reviews": 0, "Avg Turnaround": "0.9 days", "Burnout Index": "Optimal"},
    ]
    st.table(pd.DataFrame(lecturer_data))
    
    st.markdown("<br>", unsafe_allow_html=True)
    exp1, exp2 = st.columns([2, 1])
    with exp1:
        if st.button("📥 Export BAN-PT Process Integrity Compliance Report (PDF/CSV)", use_container_width=True, type="primary"):
            st.info("Generating certified process audit package containing all Socratic dialogue logs and citation verification records...")
    with exp2:
        st.button("⚙️ Configure Socratic Policy Bounds", use_container_width=True)
        
    st.markdown('</div>', unsafe_allow_html=True)
