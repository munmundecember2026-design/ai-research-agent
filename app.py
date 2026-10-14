import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="AI Research Agent", page_icon="🔬", layout="wide")

st.title("🔬 AI Research Agent")
st.subheader("Your Personal Research Assistant")
st.write("Ask a question to search the web and explore sources.")

question = st.text_area(
    "What do you want to research?",
    placeholder="Example: How is AI changing education?"
)

num_results = st.slider("Number of sources", 3, 10, 5)

if st.button("Start Research", type="primary"):
    if not question.strip():
        st.warning("Please enter a research question.")
    else:
        try:
            with st.spinner("Searching the web..."):
                with DDGS() as ddgs:
                    results = list(
                        ddgs.text(question, max_results=num_results)
                    )

            if results:
                st.subheader("🌐 Web Research Sources")
                for i, result in enumerate(results, start=1):
                    title = result.get("title", "Untitled")
                    url = result.get("href", "")
                    body = result.get("body", "")

                    with st.expander(f"{i}. {title}"):
                        st.write(body)
                        if url:
                            st.markdown(f"[Open source]({url})")
            else:
                st.info("No results found. Try another question.")

        except Exception as e:
            st.error(f"Web search failed: {e}")
