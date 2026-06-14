import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from load_db_data import load_db_data
from kpi import show_kpis
from charts import show_charts
from manager_ai.db_manager_assistant import ask_db_manager

st.set_page_config(
    page_title="Acko Dashboard",
    layout="wide"
)

st.title(
    "📊 Acko Insurance Management Dashboard"
)



quotations, claims, chat_logs = load_db_data()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Quotations",
        len(quotations)
    )

with col2:
    st.metric(
        "Total Claims",
        len(claims)
    )

with col3:
    st.metric(
        "Chatbot Conversations",
        len(chat_logs)
    )

    import plotly.express as px

st.subheader("📈 PostgreSQL Analytics")

if not quotations.empty:

    fig1 = px.bar(
        quotations,
        x="vehicle_type",
        y="predicted_premium",
        title="Premium Quotation by Insurance Type"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

if not claims.empty:

    fig2 = px.pie(
        claims,
        names="status",
        title="Claim Status Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.subheader("🚨 Manual Review Queue")

review_claims = claims[
    claims["status"] == "review"
]

if review_claims.empty:

    st.success(
        "No claims currently flagged for manual review."
    )

else:

    st.dataframe(
        review_claims[
            [
                "vehicle_type",
                "damage_type",
                "damage_severity",
                "predicted_amount",
                "approval_probability",
                "created_at"
            ]
        ]
    )

    st.divider()

st.subheader("🤖 Manager AI Assistant")

if "manager_answer" not in st.session_state:
    st.session_state.manager_answer = ""

manager_question = st.text_input(
    "Ask a business question",
    placeholder="Example: How many quotations?",
    key="manager_question"
)

if st.button("Ask Manager Assistant"):

    if manager_question.strip() == "":

        st.warning("Please enter a question.")

    else:

        st.session_state.manager_answer = ask_db_manager(
            manager_question
        )

if st.session_state.manager_answer != "":

    st.success(
        st.session_state.manager_answer
    )