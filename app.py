import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

st.set_page_config(page_title="Nykaa Sentiment Analyzer", page_icon="💄")

st.title("💄 Nykaa Reviews - Sentiment Analyzer")
st.write("Beauty products ke reviews ka mood detect karo!")

reviews_input = st.text_area(
    "Yahan Nykaa reviews paste karo (har line ek review):",
    placeholder="Ex:\nI love this lipstick, best glow\nWorst product ever\nNice packaging but average",
    height=150
)

if st.button("Analyze Now"):
    if reviews_input.strip() == "":
        st.warning("Pehle reviews paste karo!")
    else:
        reviews = [r.strip() for r in reviews_input.split("\n") if r.strip()!=""]
        
        results = []
        for rev in reviews:
            blob = TextBlob(rev)
            polarity = blob.sentiment.polarity
            if polarity > 0.1:
                sentiment = "Positive 😍"
            elif polarity < -0.1:
                sentiment = "Negative 😡"
            else:
                sentiment = "Neutral 😐"
            results.append({"Review": rev, "Score": polarity, "Sentiment": sentiment})
        
        df = pd.DataFrame(results)
        
        total = len(df)
        positive = len(df[df["Sentiment"].str.contains("Positive")])
        negative = len(df[df["Sentiment"].str.contains("Negative")])
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Reviews", total)
        col2.metric("Positive", positive)
        col3.metric("Negative", negative)
        
        st.dataframe(df, use_container_width=True)
        
        # Chart
        counts = df["Sentiment"].value_counts()
        fig, ax = plt.subplots()
        ax.bar(counts.index, counts.values, color=["green","red","gray"])
        st.pyplot(fig)
        
        if positive > total/2:
            st.success("✅ Verdict: Customers LOVE this product!")
        elif negative > total/2:
            st.error("❌ Verdict: Customers HATE this product!")
        else:
            st.info("🤔 Verdict: Mixed Reviews")
