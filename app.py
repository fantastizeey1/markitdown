import streamlit as st
from markitdown import MarkItDown

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MarkItDown",
    page_icon="🥪",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Google Fonts (injected as <link> to avoid Streamlit base-path URI error) ───
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>

/* ── Root tokens ── */
:root {
    --sand:    #F5F0E8;
    --ink:     #1A1714;
    --muted:   #6B6560;
    --accent:  #D4541E;
    --accent2: #2A5C45;
    --border:  #DDD8CE;
    --surface: #FDFAF5;
    --radius:  12px;
}

/* ── Global resets ── */
html, body, [class*="css"] {
    font-family: 'Instrument Sans', sans-serif;
    background-color: var(--sand) !important;
    color: var(--ink);
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    max-width: 680px !important;
    padding: 3rem 2rem 4rem !important;
}

/* ── Hero header ── */
.hero {
    text-align: center;
    margin-bottom: 2.5rem;
}
.hero-badge {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--accent2);
    background: #E8F2ED;
    border: 1px solid #B8D9C8;
    border-radius: 100px;
    padding: 4px 14px;
    margin-bottom: 1rem;
}
.hero h1 {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2.4rem, 6vw, 3.6rem);
    font-weight: 400;
    line-height: 1.1;
    color: var(--ink);
    margin: 0 0 0.6rem;
    letter-spacing: -0.02em;
}
.hero h1 em {
    font-style: italic;
    color: var(--accent);
}
.hero p {
    font-size: 1rem;
    color: var(--muted);
    margin: 0;
    max-width: 400px;
    margin-inline: auto;
    line-height: 1.6;
}

/* ── Supported formats pill row ── */
.formats {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    justify-content: center;
    margin: 1.5rem 0 2.5rem;
}
.fmt-pill {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    color: var(--muted);
    background: white;
    border: 1px solid var(--border);
    border-radius: 100px;
    padding: 3px 10px;
    letter-spacing: 0.04em;
}

/* ── Divider ── */
.divider {
    height: 1px;
    background: var(--border);
    margin: 2rem 0;
}

/* ── File uploader override ── */
[data-testid="stFileUploader"] {
    background: var(--surface) !important;
    border: 2px dashed var(--border) !important;
    border-radius: var(--radius) !important;
    transition: border-color 0.2s;
}
[data-testid="stFileUploader"]:hover {
    border-color: var(--accent) !important;
}
[data-testid="stFileUploader"] label {
    font-family: 'Instrument Sans', sans-serif !important;
    font-size: 0.95rem !important;
    color: var(--muted) !important;
}
[data-testid="stFileUploaderDropzone"] {
    background: transparent !important;
    padding: 2rem !important;
}

/* ── Alerts / status ── */
[data-testid="stAlert"] {
    border-radius: var(--radius) !important;
    border-left-width: 3px !important;
    font-size: 0.9rem !important;
}

/* ── Textarea override ── */
.stTextArea textarea {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.82rem !important;
    line-height: 1.65 !important;
    background: white !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    color: var(--ink) !important;
    resize: vertical !important;
}
.stTextArea textarea:focus {
    border-color: var(--accent2) !important;
    box-shadow: 0 0 0 3px rgba(42, 92, 69, 0.12) !important;
}

/* ── Section label ── */
.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 6px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
}

/* ── Stats bar ── */
.stats-row {
    display: flex;
    gap: 1px;
    background: var(--border);
    border-radius: var(--radius);
    overflow: hidden;
    margin-bottom: 1rem;
}
.stat-cell {
    flex: 1;
    background: var(--surface);
    padding: 0.8rem 1rem;
    text-align: center;
}
.stat-cell .val {
    font-family: 'DM Serif Display', serif;
    font-size: 1.4rem;
    color: var(--ink);
    display: block;
    line-height: 1;
}
.stat-cell .lbl {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--muted);
    display: block;
    margin-top: 2px;
}

/* ── Download button ── */
.stDownloadButton button {
    background: var(--accent) !important;
    color: white !important;
    border: none !important;
    border-radius: var(--radius) !important;
    font-family: 'Instrument Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    padding: 0.6rem 1.4rem !important;
    transition: background 0.15s, transform 0.1s !important;
    width: 100% !important;
}
.stDownloadButton button:hover {
    background: #B8431A !important;
    transform: translateY(-1px) !important;
}
.stDownloadButton button:active {
    transform: translateY(0) !important;
}

/* ── Footer ── */
.app-footer {
    text-align: center;
    margin-top: 3rem;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 0.06em;
}
</style>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ Free converter</div>
    <h1>Any file,<br><em>pure Markdown.</em></h1>
    <p>Drop a document below. Get clean, portable Markdown back — instantly.</p>
</div>

<div class="formats">
    <span class="fmt-pill">.pdf</span>
    <span class="fmt-pill">.docx</span>
    <span class="fmt-pill">.pptx</span>
    <span class="fmt-pill">.xlsx</span>
    <span class="fmt-pill">.html</span>
    <span class="fmt-pill">.txt</span>
    <span class="fmt-pill">.csv</span>
    <span class="fmt-pill">.json</span>
    <span class="fmt-pill">.png</span>
    <span class="fmt-pill">.jpg</span>
    <span class="fmt-pill">.jpeg</span>
    <span class="fmt-pill">.webp</span>
    <span class="fmt-pill">.gif</span>
</div>
""", unsafe_allow_html=True)

# ── Upload ─────────────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "Drop your file here, or click to browse",
    type=["pdf", "docx", "pptx", "xlsx", "html", "txt", "csv", "json",
          "png", "jpg", "jpeg", "webp", "gif"],
    label_visibility="visible",
)

# ── Conversion ────────────────────────────────────────────────────────────────
if uploaded_file is not None:
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    with st.spinner("Converting…"):
        try:
            md = MarkItDown()
            result = md.convert_stream(uploaded_file)
            markdown_text = result.text_content

            # Compute quick stats
            word_count  = len(markdown_text.split())
            char_count  = len(markdown_text)
            line_count  = markdown_text.count("\n") + 1

            # Stats bar
            st.markdown(f"""
            <div class="stats-row">
                <div class="stat-cell">
                    <span class="val">{word_count:,}</span>
                    <span class="lbl">words</span>
                </div>
                <div class="stat-cell">
                    <span class="val">{char_count:,}</span>
                    <span class="lbl">characters</span>
                </div>
                <div class="stat-cell">
                    <span class="val">{line_count:,}</span>
                    <span class="lbl">lines</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Output label
            st.markdown(
                '<p class="section-label">Markdown output</p>',
                unsafe_allow_html=True,
            )

            # Result textarea
            st.text_area(
                label="output",
                value=markdown_text,
                height=420,
                label_visibility="collapsed",
            )

            # Download
            base_name = uploaded_file.name.rsplit(".", 1)[0]
            st.download_button(
                label=f"⬇ Download  {base_name}.md",
                data=markdown_text,
                file_name=f"{base_name}.md",
                mime="text/markdown",
            )

        except Exception as e:
            st.error(f"Conversion failed: {e}")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="app-footer">Powered by MarkItDown &mdash; no data stored</div>',
    unsafe_allow_html=True,
)