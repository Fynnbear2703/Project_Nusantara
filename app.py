import os
import datetime
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Project Nusantara | AI Thesis Companion",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for Bright Academic Design System
st.markdown("""
<style>
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Inter', system-ui, sans-serif;
    }
    .app-header {
        background-color: #FFFFFF;
        padding: 18px 28px;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 24px;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .app-title {
        color: #0F172A;
        font-size: 1.4rem;
        font-weight: 700;
        margin: 0;
    }
    .app-subtitle {
        color: #64748B;
        font-size: 0.9rem;
        margin: 0;
    }
    .nusantara-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }
    .badge-emerald {
        background-color: #D1FAE5;
        color: #065F46;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .badge-blue {
        background-color: #DBEAFE;
        color: #1E40AF;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .socratic-card {
        background-color: #EFF6FF;
        border-left: 4px solid #2563EB;
        padding: 16px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 16px;
    }
    .timeline-item {
        border-left: 2px solid #CBD5E1;
        padding-left: 16px;
        margin-left: 8px;
        padding-bottom: 14px;
        position: relative;
    }
    .timeline-dot {
        position: absolute;
        left: -6px;
        top: 2px;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: #2563EB;
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
        {"time": "3 hours ago", "action": "Answered Socratic Prompt on Data Limitations"}
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
            "💡 [Socratic Guidance Simulation]\n"
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

# Top Navigation Header
st.markdown("""
<div class="app-header">
    <div>
        <div class="app-title">🎓 Project Nusantara Platform</div>
        <div class="app-subtitle">Socratic Academic Writing & Process Integrity System</div>
    </div>
    <div>
        <span class="badge-emerald">Campus Portal: Active</span>
        <span class="badge-blue">API Connected</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Navigation Tabs
tab_student, tab_advisor, tab_faculty = st.tabs([
    "📝 Student Workspace & Socratic Sidebar", 
    "👨‍🏫 Advisor Review & Effort Monitor", 
    "📊 Faculty Analytics Portal"
])

# Tab 1: Student Workspace
with tab_student:
    st.caption("Simulated Google Docs / Canvas writing editor with active Socratic sidebar")
    col_editor, col_sidebar = st.columns([0.68, 0.32], gap="medium")
    
    with col_editor:
        st.subheader("Document Title: Chapter_3_Methodology_Budi.docx")
        sample_draft = st.text_area(
            label="Active Thesis Canvas",
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
            height=420
        )
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔍 Run Socratic Diagnostic Check", use_container_width=True, type="primary"):
                with st.spinner("Analyzing methodology logic..."):
                    prompt_result = generate_socratic_coaching(sample_draft)
                    st.session_state.last_socratic_prompt = prompt_result
                    st.rerun()
        with c2:
            st.button("💾 Save & Sync to Canvas LMS", use_container_width=True)

    with col_sidebar:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown("### 💡 Socratic AI Companion")
        st.caption("Guided reflection layer (No auto-generated text)")
        st.markdown(f'<div class="socratic-card"><b>Active Diagnostic Question:</b><br><br>{st.session_state.last_socratic_prompt}</div>', unsafe_allow_html=True)
        reflection_input = st.text_area("Your Reflective Defense:", placeholder="Ex: Sample size of 50 was calculated using Slovin formula...")
        
        if st.button("Log Reflection to Thesis Audit", use_container_width=True):
            if reflection_input.strip():
                timestamp = datetime.datetime.now().strftime("%H:%M")
                st.session_state.effort_log.insert(0, {
                    "time": f"Today at {timestamp}",
                    "action": f"Answered Socratic Prompt: '{reflection_input[:40]}...'"
                })
                st.success("Reflection recorded in Effort Audit Log!")
                st.rerun()
            else:
                st.warning("Please type a reflection response before logging.")
        
        st.markdown("---")
        st.markdown("#### 📑 Verification Status")
        st.markdown("- **SINTA Citation Check:** <span class="badge-emerald">Verified (Sukarna et al., 2023)</span>", unsafe_allow_html=True)
        st.markdown("- **Formatting Compliance:** <span class="badge-blue">94% Compliant</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Tab 2: Advisor Review Workspace
with tab_advisor:
    st.caption("Advisor workspace to inspect authentic student effort and provide qualitative feedback")
    col_draft_view, col_effort_monitor = st.columns([0.62, 0.38], gap="medium")
    
    with col_draft_view:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown("### Submitted Chapter Draft: Budi Santoso (NIM: 5025211000)")
        st.markdown("**Chapter 3: Methodology** | *Last updated 2 hours ago*")
        st.markdown("---")
        st.markdown("""
        **BAB 3 METODOLOGI PENELITIAN**
        
        **3.1 Metode Pengumpulan Data**  
        Penelitian ini menggunakan pendekatan kuantitatif dengan menyebarkan kuesioner kepada 50 responden mahasiswa di Jawa Timur. Pengambilan sampel dilakukan menggunakan teknik random sampling.  
        
        <div style="background-color: #D1FAE5; padding: 8px; border-radius: 6px; border-left: 3px solid #059669; margin: 8px 0;">
            <b>✓ Pre-screened Citation:</b> Sukarna et al. (2023) verified against national SINTA database.
        </div>
        
        **3.2 Populasi dan Sampel**  
        Populasi dalam penelitian ini adalah seluruh mahasiswa aktif. Rujukan utama mengacu pada penelitian Sukarna et al. (2023) mengenai efisiensi pembelajaran digital.
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("### Advisor Qualitative Decision")
        advisor_notes = st.text_input("Qualitative Remarks for Student:", placeholder="Focus on expanding sample justification in Section 3.2...")
        ac1, ac2 = st.columns(2)
        with ac1:
            st.button("✅ Approve Chapter Milestone", use_container_width=True, type="primary")
        with ac2:
            st.button("🔄 Request Revision with Nudge", use_container_width=True)

    with col_effort_monitor:
        st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
        st.markdown("### 🛡️ Interactive Effort Audit Log")
        st.caption("Chronological proof of human reflection and revision history")
        st.metric("Estimated Genuine Human Effort", "34.5 Hours", delta="+4.2 hrs this week")
        st.metric("Socratic Prompts Completed", f"{len(st.session_state.effort_log)} Interactions", delta="High Engagement")
        st.markdown("---")
        st.markdown("#### Activity Timeline")
        for item in st.session_state.effort_log:
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <small style="color: #64748B;">{item['time']}</small><br>
                <strong>{item['action']}</strong>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Tab 3: Faculty Analytics Portal
with tab_faculty:
    st.caption("Department executive oversight for thesis velocity and accreditation standards")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Active Thesis Writers", "1,240", delta="98% On Track")
    with m2:
        st.metric("Avg Milestone Velocity", "3.2 Weeks", delta="-0.8 wks faster")
    with m3:
        st.metric("Advisor Burnout Index", "Low", delta="-35% marking time")
    with m4:
        st.metric("Integrity Audit Score", "96/100", delta="Accreditation Ready")
    
    st.markdown("---")
    st.markdown('<div class="nusantara-card">', unsafe_allow_html=True)
    st.markdown("### Department Thesis Progress & Integrity Overview")
    dept_data = [
        {"Student": "Gryffyn Teh", "Department": "Computer Science", "Milestone": "Chapter 3 Methodology", "Effort Hours": "42 hrs", "Socratic Responses": 38, "Status": "On Track"},
        {"Student": "Budi Santoso", "Department": "Information Systems", "Milestone": "Chapter 3 Methodology", "Effort Hours": "34 hrs", "Socratic Responses": 24, "Status": "On Track"},
        {"Student": "Siti Nurhaliza", "Department": "Software Engineering", "Milestone": "Chapter 2 Lit Review", "Effort Hours": "18 hrs", "Socratic Responses": 12, "Status": "Needs Nudge"},
        {"Student": "Ahmad Rizki", "Department": "Computer Science", "Milestone": "Chapter 4 Results", "Effort Hours": "56 hrs", "Socratic Responses": 45, "Status": "Approved"},
    ]
    st.table(dept_data)
    if st.button("📥 Export Verified Accreditation Audit Log (PDF/CSV)"):
        st.info("Generating official audit report certified for national university accreditation...")
    st.markdown('</div>', unsafe_allow_html=True)
