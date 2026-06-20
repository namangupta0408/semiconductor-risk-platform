import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Semiconductor Supply Chain Intelligence",
    layout="wide"
)

st.title("Semiconductor Supply Chain Intelligence Platform")

conn = sqlite3.connect(
    "data/semiconductor_risk.db"
)

articles = pd.read_sql(
    "SELECT COUNT(*) AS count FROM articles",
    conn
).iloc[0]["count"]

events = pd.read_sql(
    "SELECT COUNT(*) AS count FROM events",
    conn
).iloc[0]["count"]

critical = pd.read_sql(
"""
SELECT COUNT(*) AS count

FROM risk_scores

WHERE risk_level='Critical'
""",
conn
).iloc[0]["count"]

avg = pd.read_sql(
"""
SELECT ROUND(AVG(risk_score),2) AS avg

FROM risk_scores
""",
conn
).iloc[0]["avg"]

c1,c2,c3,c4 = st.columns(4)

c1.metric(
"Articles",
articles
)

c2.metric(
"Events",
events
)

c3.metric(
"Critical Risks",
critical
)

c4.metric(
"Average Risk",
avg
)

st.divider()

st.header("Latest Events")

events_df = pd.read_sql("""

SELECT

company,

country,

event_type,

severity,

summary

FROM events

ORDER BY id DESC

LIMIT 20

""",conn)

st.dataframe(
events_df,
use_container_width=True
)

st.divider()

left,right = st.columns(2)

with left:

    st.header("Company Risk")

    company = pd.read_csv(
        "data/company_risk.csv"
    )

    st.dataframe(
        company,
        use_container_width=True
    )

with right:

    st.header("Country Risk")

    country = pd.read_csv(
        "data/country_risk.csv"
    )

    st.dataframe(
        country,
        use_container_width=True
    )

st.divider()

st.header("Risk Distribution")

risk = pd.read_sql("""

SELECT

risk_level,

COUNT(*) total

FROM risk_scores

GROUP BY risk_level

""",conn)

st.bar_chart(
risk.set_index(
"risk_level"
)
)

st.divider()

st.header("Executive AI Brief")

with open(
"data/executive_summary.txt"
) as f:

    st.write(
        f.read()
    )

conn.close()