import streamlit as st
import pandas as pd

st.set_page_config(page_title="Nykaa Sentiment", page_icon="💄")
st.title("💄 Nykaa Reviews - Sentiment Analyzer")
st.write("Beauty products ke reviews ka mood check karo - For Nykaa Job")

reviews_input = st.text_area("Yahan Nykaa reviews paste karo (ek line = ek review)",
                             placeholder="Example:\nThis cream is best, love it\nWorst product, gave me acne\nNice glow after use")

if st.button("Analyze Now"):
    if reviews_input.strip() == "":
        st.warning("Pehle reviews paste kar")
    else:
        positive_words = ["good", "best", "love", "awesome", "nice", "great", "soft", "glow", "amazing", "perfect"]
        negative_words = ["bad", "worst", "acne", "pimple", "hair fall", "itching", "damage", "waste", "bakwas"]

        pos = 0
        neg = 0
        neutral = 0

        lines = [l for l in reviews_input.split("\n") if l.strip() != ""]

        for line in lines:
            line_low = line.lower()
            is_pos = any(w in line_low for w in positive_words)
            is_neg = any(w in line_low for w in negative_words)

            if is_pos and not is_neg:
                pos += 1
            elif is_neg and not is_pos:
                neg += 1
            else:
                neutral += 1

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Reviews", len(lines))
        col2.metric("Positive 😍", pos)
        col3.metric("Negative 😡", neg)

        chart_data = pd.DataFrame({"Count": [pos, neg, neutral]}, index=["Positive", "Negative", "Neutral"])
        st.bar_chart(chart_data)

        if pos > neg:
            st.success(f"Overall: Customers LOVE this product! {pos} positive reviews ✅")
        elif neg > pos:
            st.error(f"Overall: Customers have complaints! {neg} negative reviews ⚠️")
        else:
            st.info("Overall: Mixed reviews")

st.divider()
st.caption("Project 2 - Made for Beauty-Tech Portfolio")