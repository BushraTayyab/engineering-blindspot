import streamlit as st

from analyzer.repo_loader import clone_repository
from analyzer.impact_analyzer import analyze_impact
from analyzer.report_analyzer import generate_report
from analyzer.ai_analyzer import generate_insight


st.set_page_config(
    page_title="Engineering Blindspot",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Engineering Blindspot")
st.subheader("Find what your code change might break before you merge.")

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/username/repository.git"
)

if st.button("Analyze Repository", type="primary"):

    try:
        if not repo_url:
            st.warning("Please enter a GitHub repository URL.")
            st.stop()

        with st.spinner("Cloning and analyzing repository..."):

            repo_path = clone_repository(repo_url)

            impact = analyze_impact(repo_path)
            report = generate_report(impact)
            insight = generate_insight(report)

        st.success("Analysis complete")

        st.divider()

        st.header("Commit")

        st.write(
            impact["commit"]["message"]
        )

        st.caption(
            impact["commit"]["hash"]
        )

        for item in report["reports"]:

            st.divider()

            risk = item["risk"]

            if risk == "HIGH":
                st.error(f"🔴 {risk} IMPACT")
            elif risk == "MEDIUM":
                st.warning(f"🟡 {risk} IMPACT")
            else:
                st.success(f"🟢 {risk} IMPACT")

            st.subheader(item["file"])

            with st.expander("🔍 What changed?"):

                diff = item.get("diff", "")

                if diff:
                    st.code(diff, language="diff")
                else:
                    st.warning("No code diff available for this file.")

            col1, col2 = st.columns(2)

            with col1:

                st.write("### Functions")
                st.write(item["functions"])

                st.write("### Production Dependents")
                st.write(item["dependents"])

            with col2:

                st.write("### Related Tests")
                st.write(item["related_tests"])

                st.write("### Risk Signals")

                for signal in item["risk_signals"]:
                    st.write(f"• {signal}")

        st.divider()

        st.header("🧠 Blindspot Analysis")

        st.write(insight)

    except Exception as e:
        st.error(f"Analysis failed: {e}")