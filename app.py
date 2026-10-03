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

# Custom Styling for SaaS Aesthetic
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
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

    /* Top Brand Navigation Header */
    .brand-header {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 16px 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.03);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .brand-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.02em;
        margin: 0;
    }

    .brand-subtitle {
        font-size: 0.85rem;
        color: #64748B;
        margin-top: 2px;
        font-weight: 500;
    }

    /* Navigation Tabs */
    div[data-baseweb="tab-list"] {
        gap: 8px !important;
        background-color: #FFFFFF !important;
        padding: 6px !important;
        border-radius: 14px !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.02) !important;
        margin-bottom: 20px !important;
    }

    button[data-baseweb="tab"] {
        border-radius: 10px !important;
        padding: 10px 22px !important;
        font-size: 0.90rem !important;
        font-weight: 600 !important;
        color: #64748B !important;
        background-color: transparent !important;
        border: none !important;
        transition: all 0.2s ease !important;
    }

    button[aria-selected="true"] {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.22) !important;
    }

    /* Cards and Dashboard Containers */
    .nusantara-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.03);
    }

    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 14px;
    }

    .card-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0F172A;
    }

    /* Custom Badges */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 700;
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
        font-size: 0.82rem;
        text-transform: uppercase;
        font-weight: 800;
        color: #1D4ED8;
        letter-spacing: 0.05em;
        margin-bottom: 6px;
    }

    .socratic-text {
        font-size: 0.94rem;
        color: #1E293B;
        font-weight: 600;
        line-height: 1.5;
    }

    /* Metric Boxes */
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }

    .metric-val {
        font-size: 1.7rem;
        font-weight: 800;
        color: #0F172A;
    }

    .metric-lbl {
        font-size: 0.80rem;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        margin-bottom: 4px;
    }

    /* Timeline Nodes */
    .timeline-node {
        border-left: 2px solid #E2E8F0;
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

    /* Inputs and Buttons */
    .stTextArea textarea {
        border-radius: 12px !important;
        border: 1px solid #CBD5E1 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.92rem !important;
        padding: 12px !important;
    }

    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        padding: 8px 18px !important;
        border: 1px solid #CBD5E1 !important;
        transition: all 0.2s ease !important;
    }

    div.stButton > button[kind="primary"] {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# API Key Retrieval
api_key = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))

# Session State Initialization
if "effort_log" not in st.session_state:
    st.session_state.effort_log = [
        {"time": "Today at 09:15", "action": "Answered Socratic Prompt on Slovin sample formula rationale", "category": "socratic"},
        {"time": "Yesterday at 14:30", "action": "Added verified SINTA citation (Sukarna et al., 2023)", "category": "citation"},
        {"time": "2 days ago", "action": "Uploaded Chapter 3 Methodology initial draft", "category": "draft"},
        {"time": "3 days ago", "action": "Completed Chapter 2 Literature Review milestone", "category": "milestone"}
    ]

if "last_socratic_prompt" not in st.session_state:
    st.session_state.last_socratic_prompt = (
        "Bagaimana ukuran sampel 50 responden ini secara spesifik dapat mendukung validitas "
        "analisis statistik kuantitatif Anda di Bab 3?"
    )

if "advisor_feedback_list" not in st.session_state:
    st.session_state.advisor_feedback_list = [
        "Dr. Aris Setiawan: Please clarify the sampling technique criteria in Section 3.2 before Friday."
    ]

# Socratic Coaching Function
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

# Header Area
st.markdown("""
<div class="brand-header">
    <div>
        <div class="brand-title">🎓 Project Nusantara</div>
        <div class="brand-subtitle">Socratic Academic Writing & Process Integrity System</div>
    </div>
    <div>
        <span class="badge badge-emerald">Institut Teknologi Sepuluh Nopember</span>
        <span class="badge badge-blue">Socratic AI Engine Live</span>
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
    col_editor, col_sidebar = st.columns([0.64, 0.36], gap="large")
    
    with col_editor:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-header">
            <div>
                <div class="card-title">📄 Google Docs Workspace: Thesis_Chapter3_v4.docx</div>
                <small style="color: #64748B;">Target Chapter: Bab 3 Metodologi Penelitian | Word Count: 485 words</small>
            </div>
            <span class="badge badge-emerald">Live Extension Connected</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Toolbar Mockup
        t1, t2, t3, t4, t5 = st.columns([1, 1, 1, 1, 2])
        with t1: st.button("<b>B</b>", use_container_width=True)
        with t2: st.button("<i>I</i>", use_container_width=True)
        with t3: st.button("🔗 Citation", use_container_width=True)
        with t4: st.button("📐 Format", use_container_width=True)
        with t5: st.caption("Last auto save: 1 minute ago")
        
        sample_draft = st.text_area(
            label="Thesis Document Canvas",
            value=(
                "BAB 3 METODOLOGI PENELITIAN\n\n"
                "3.1 Metode Pengumpulan Data\n"
                "Penelitian ini menggunakan pendekatan kuantitatif dengan menyebarkan kuesioner "
                "kepada 50 responden mahasiswa di Jawa Timur. Pengambilan sampel dilakukan "
                "menggunakan teknik random sampling untuk mengukur tingkat adopsi teknologi LMS.\n\n"
                "3.2 Populasi dan Sampel\n"
                "Populasi dalam penelitian ini adalah seluruh mahasiswa aktif. Rujukan utama "
                "mengacu pada penelitian Sukarna et al. (2023) mengenai efisiensi pembelajaran digital.\n\n"
                "3.3 Teknik Analisis Data\n"
                "Data yang diperoleh disajikan melalui metode regresi linear berganda untuk menguji "
                "hipotesis efektivitas pendampingan Socratic AI."
            ),
            height=340,
            label_visibility="collapsed"
        )
        
        b1, b2, b3 = st.columns([2, 1.5, 1.5])
        with b1:
            if st.button("🔍 Run Socratic Diagnostic Check", use_container_width=True, type="primary"):
                with st.spinner("Socratic engine analyzing methodology logic..."):
                    prompt_result = generate_socratic_coaching(sample_draft)
                    st.session_state.last_socratic_prompt = prompt_result
                    st.rerun()
        with b2:
            st.button("⚡ Verify Citations", use_container_width=True)
        with b3:
            st.button("💾 Sync to Canvas LMS", use_container_width=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Advisor Notes Box inside Editor
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">💬 Advisor Notes Feed</div>', unsafe_allow_html=True)
        for note in st.session_state.advisor_feedback_list:
            st.markdown(f"<div style='background-color: #F8FAFC; padding: 12px; border-radius: 8px; border-left: 3px solid #2563EB; font-size: 0.90rem;'>{note}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_sidebar:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">💡 Nusantara Smart Sidebar</div>', unsafe_allow_html=True)
        st.caption("Active diagnostic coach (No text generation allowed)")
        
        st.markdown(f"""
        <div class="socratic-box">
            <div class="socratic-title">Socratic Diagnostic Nudge</div>
            <div class="socratic-text">{st.session_state.last_socratic_prompt}</div>
        </div>
        """, unsafe_allow_html=True)
        
        reflection_input = st.text_area("Your Reflective Defense Answer:", placeholder="Ex: Sample size of 50 was calculated using Slovin formula with 5 percent margin of error...", height=110)
        
        if st.button("Log Reflection to Effort Audit", use_container_width=True):
            if reflection_input.strip():
                timestamp = datetime.datetime.now().strftime("%H:%M")
                st.session_state.effort_log.insert(0, {
                    "time": f"Today at {timestamp}",
                    "action": f"Answered Socratic Prompt: '{reflection_input[:35]}...'",
                    "category": "socratic"
                })
                st.success("Reflection recorded in effort audit log!")
                st.rerun()
            else:
                st.warning("Please type your explanation before submitting.")
        
        st.markdown("<hr style='margin: 16px 0; border-color: #E2E8F0;'>", unsafe_allow_html=True)
        st.markdown("#### 📑 Integrity Checklist")
        st.markdown("- **SINTA Citation:** <span class='badge badge-emerald'>Verified (Sukarna et al., 2023)</span>", unsafe_allow_html=True)
        st.markdown("- **Formatting Check:** <span class='badge badge-blue'>94% Compliant</span>", unsafe_allow_html=True)
        st.markdown("- **Human Effort Index:** <span class='badge badge-emerald'>High Authenticity</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# TAB 2: ADVISOR REVIEW
with tab_advisor:
    st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
    
    # Active Student Switcher
    sc1, sc2, sc3 = st.columns([1.5, 1.5, 1])
    with sc1:
        selected_student = st.selectbox("Select Student Thesis Review:", ["Budi Santoso (NIM: 5025211000)", "Gryffyn Teh (NIM: 5025211001)", "Sarah Chen (NIM: 5025211002)"])
    with sc2:
        st.markdown("<br><span class='badge badge-blue'>Current Milestone: Bab 3 Metodologi</span> <span class='badge badge-emerald'>Pre-screened</span>", unsafe_allow_html=True)
    with sc3:
        st.caption("Review Speed: Fast")
    st.markdown('</div>', unsafe_allow_html=True)
    
    col_draft_view, col_effort_monitor = st.columns([0.58, 0.42], gap="large")
    
    with col_draft_view:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="card-title">Submitted Manuscript Draft: {selected_student}</div>', unsafe_allow_html=True)
        st.markdown("<hr style='margin: 14px 0; border-color: #E2E8F0;'>", unsafe_allow_html=True)
        
        st.markdown("""
        **BAB 3 METODOLOGI PENELITIAN**
        
        **3.1 Metode Pengumpulan Data**  
        Penelitian ini menggunakan pendekatan kuantitatif dengan menyebarkan kuesioner kepada 50 responden mahasiswa di Jawa Timur. Pengambilan sampel dilakukan menggunakan teknik random sampling.  
        
        <div style="background-color: #ECFDF5; padding: 10px; border-radius: 8px; border-left: 4px solid #059669; margin: 12px 0;">
            <b>✓ Verified Reference:</b> Sukarna et al. (2023) confirmed against SINTA national journal index.
        </div>
        
        **3.2 Populasi dan Sampel**  
        Populasi dalam penelitian ini adalah seluruh mahasiswa aktif. Rujukan utama mengacu pada penelitian Sukarna et al. (2023) mengenai efisiensi pembelajaran digital.
        
        <div style="background-color: #EFF6FF; padding: 10px; border-radius: 8px; border-left: 4px solid #2563EB; margin: 12px 0;">
            <b>💡 Socratic Dialogue Interaction:</b> Student defended sample size choice using Slovin formula calculation on October 3.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Advisor Feedback & Decision Panel</div>', unsafe_allow_html=True)
        new_note = st.text_input("Qualitative Remarks for Student:", placeholder="Ex: Expand sample justification in Section 3.2...")
        
        ac1, ac2 = st.columns(2)
        with ac1:
            if st.button("✅ Approve Chapter Milestone", use_container_width=True, type="primary"):
                st.success("Milestone approved and logged to academic record!")
        with ac2:
            if st.button("🔄 Send Qualitative Revision Nudge", use_container_width=True):
                if new_note.strip():
                    st.session_state.advisor_feedback_list.insert(0, f"Dr. Aris Setiawan: {new_note}")
                    st.success("Feedback pushed to student extension sidebar!")
                    st.rerun()
                else:
                    st.warning("Please type a note first.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_effort_monitor:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🛡️ Process Integrity & Effort Audit Log</div>', unsafe_allow_html=True)
        st.caption("Verifiable proof of student reflection and writing journey")
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="metric-card"><div class="metric-lbl">Total Effort</div><div class="metric-val">34.5h</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="metric-card"><div class="metric-lbl">Reflections</div><div class="metric-val">{len(st.session_state.effort_log)}</div></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric-card"><div class="metric-lbl">Authenticity</div><div class="metric-val">98%</div></div>', unsafe_allow_html=True)
            
        st.markdown("<hr style='margin: 16px 0; border-color: #E2E8F0;'>", unsafe_allow_html=True)
        st.markdown("#### Chronological Audit Trail")
        
        for item in st.session_state.effort_log:
            st.markdown(f"""
            <div class="timeline-node">
                <div class="timeline-dot"></div>
                <div style="font-size: 0.76rem; color: #64748B; font-weight: 600;">{item['time']}</div>
                <div style="font-size: 0.88rem; color: #0F172A; font-weight: 600; margin-top: 2px;">{item['action']}</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

# TAB 3: FACULTY ANALYTICS
with tab_faculty:
    st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Executive Campus Analytics Portal</div>', unsafe_allow_html=True)
    st.caption("Department level oversight for thesis completion velocity, advisor workload, and accreditation audits")
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-card"><div class="metric-lbl">Active Student Writers</div><div class="metric-val">1,240</div><span class="badge badge-emerald">98% Active</span></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><div class="metric-lbl">Avg Chapter Velocity</div><div class="metric-val">3.2 wks</div><span class="badge badge-blue">0.8 wks faster</span></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card"><div class="metric-lbl">Advisor Marking Time</div><div class="metric-val">-35%</div><span class="badge badge-emerald">Burnout Reduced</span></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-card"><div class="metric-lbl">Accreditation Score</div><div class="metric-val">96/100</div><span class="badge badge-emerald">Certified</span></div>', unsafe_allow_html=True)
        
    st.markdown("<hr style='margin: 20px 0; border-color: #E2E8F0;'>", unsafe_allow_html=True)
    
    st.markdown("#### Department Thesis Cohort Overview")
    
    dept_data = [
        {"Student Name": "Gryffyn Teh", "Department": "Computer Science", "Current Milestone": "Bab 3 Metodologi", "Logged Effort": "42 hrs", "Socratic Responses": 38, "Status": "On Track"},
        {"Student Name": "Budi Santoso", "Department": "Information Systems", "Milestone": "Bab 3 Metodologi", "Logged Effort": "34 hrs", "Socratic Responses": 24, "Status": "On Track"},
        {"Student Name": "Siti Nurhaliza", "Department": "Software Engineering", "Milestone": "Bab 2 Tinjauan Pustaka", "Logged Effort": "18 hrs", "Socratic Responses": 12, "Status": "Needs Nudge"},
        {"Student Name": "Ahmad Rizki", "Department": "Computer Science", "Milestone": "Bab 4 Hasil & Pembahasan", "Logged Effort": "56 hrs", "Socratic Responses": 45, "Status": "Approved"},
    ]
    st.table(dept_data)
    
    c1, c2 = st.columns([2, 1])
    with c1:
        if st.button("📥 Export Verified Process Integrity Audit Log (PDF/CSV)", use_container_width=True, type="primary"):
            st.info("Generating official audit report certified for national university accreditation...")
    with c2:
        st.button("⚙️ Configure Campus Socratic Policy", use_container_width=True)
        
    st.markdown('</div>', unsafe_allow_html=True)
