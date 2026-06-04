import streamlit as st
from markitdown import MarkItDown

st.set_page_config(page_title="MarkItDown Web Interface", layout="centered")
st.title("🥪 The Free MarkItDown Sandwich App")
st.write("Drop any file below to instantly convert it to Markdown!")

# File uploader widget
uploaded_file = st.file_uploader(
    "Choose a file", 
    type=["pdf", "docx", "pptx", "xlsx", "html", "txt", "csv", "json"]
)

if uploaded_file is not None:
    st.info("Converting your document...")
    
    try:
        # Initialize MarkItDown
        md = MarkItDown()
        
        # Read the file directly from memory as a stream
        # (This is much safer for a web app than converting local paths!)
        result = md.convert_stream(uploaded_file)
        
        st.success("Done! Here is your Markdown:")
        
        # Display the output inside a neat text container
        st.text_area("Markdown Output", value=result.text_content, height=400)
        
        # Add a download button for convenience
        st.download_button(
            label="Download .md File",
            data=result.text_content,
            file_name=f"{uploaded_file.name.split('.')[0]}.md",
            mime="text/markdown"
        )
        
    except Exception as e:
        st.error(f"Oops! Something went wrong: {e}")