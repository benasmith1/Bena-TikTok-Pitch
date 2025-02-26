import streamlit as st
import base64


st.set_page_config(
    page_title = "Sentiment Analysis",
    page_icon = "🌉",
    layout = "wide"
)

# Sidebar navigation header
with st.sidebar:
    st.header("🔍 Navigate the App")
    st.write("Use the links above to explore:")
    st.markdown("""
    - **Sentiments About TikTok**: Explore sentiments about TikTok on the web.
    - **About Bena**: A bit about me!
    """)


# Code to size image with the text from ash2shukla https://discuss.streamlit.io/t/image-and-text-next-to-each-other/7627/18
st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
    }
    .logo-img {
        float:right;
        height: 55px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open("figures/TikTokLogoSmall.jpg", "rb").read()).decode()}">
        <h2 class="logo-text">&nbsp; Sentiments About TikTok</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(f"The bar graph below shows the distribution of sentiments of webpages mentioning TikTok. Click on a bar to view each link.")

with open('figures/SentimentsGraph.html', 'r', encoding='utf-8') as file:
    sentiment_graph_data = file.read()


st.components.v1.html(sentiment_graph_data, height=650, width=1500)


col1, col2, col3 = st.columns([1, 1, 1])  

with col1: 
    st.markdown(f"<h3> Popular phrases in positive webpages: </h3>", unsafe_allow_html=True)

    st.markdown(
    """
    - Users enjoy the diverse range of content on TikTok
    - The platform provides a space for creativity and self-expression
    - TikTok has a positive impact on mental health for many users
    - The algorithm helps users discover new and interesting content
    - TikTok allows users to connect with others and build a community
    - Many users appreciate the educational content available on TikTok
    - The platform promotes inclusivity and diversity
    - Users find TikTok to be a source of entertainment and inspiration
    - TikTok offers a platform for young people to share their voices and perspectives
    - The app provides a sense of belonging and support for many users
    """
    )

with col2: 
    st.markdown(f"<h3> Popular phrases in neutral webpages: </h3>", unsafe_allow_html=True)

    st.markdown(
    """
    - More diverse content creators on the platform
    - Improved algorithm to show a wider range of content
    - Enhance user feedback mechanisms for content moderation
    - Implement better privacy settings for user data
    - Increase transparency in content recommendations
    - Enhance user engagement through interactive features
    - Improve search functionality for easier content discovery
    - Enhance user interface for better user experience
    - Implement stricter guidelines for inappropriate content
    - Provide more educational content for users
    """
    )

with col3: 
    st.markdown(f"<h3> Popular phrases in negative webpages: </h3>", unsafe_allow_html=True)
    st.markdown("""
    - Lack of transparency in content moderation
    - Concerns about data privacy and security
    - Negative impact on mental health and self-esteem
    - Promotion of harmful challenges and trends
    - Spread of misinformation and fake news
    - Inadequate measures to protect younger users
    - Issues with algorithm favoritism and visibility
    - Lack of accountability for inappropriate content
    - Limited options for content control and filtering
    - Negative influence on societal values and behaviors
    """)

st.write("")

with st.expander("🥳 **Conclusion**"):
    st.write("""
    Most webpages express positive sentiments about TikTok and write about the wide range of available content and the community that TikTok provides. Users would like to see TikTok improve
    transparency in its content moderation and algorithm and to see more guardrails against inappropriate content. To examine these issues more carefully, we might send out surveys to get direct
    feedback about our product and run this analysis on those surveys. People might be more inclinded to include more detailed descriptions of potential feature fixes anonymously. 🔮
""")
    
st.write("")

with st.expander("🧮 **Procedure**"):
    st.write("""
    🔎 **1. Scrape the web for pages mentioning TikTok**: I used the googlesearch Python package to retreive URLs that appear in the Google Search: \"TikTok Opinions\"\
    The newspaper package was used to parse the text from these webpages
             
    😁 **2. Analyze Sentiments**: I used the vaderSentiment package to estimate the sentiment of each webpage
             
    📊 **3. Plot Sentiments**: The plot shown on this webpage uses the bokeh package
             
    📝 **4. Get popular phrases**: Using the OpenAI API, I submit a prompt with the parsed webpages and requested that the top phrases contributing to the positive/ neutral/negative\
            sentiments be returned
    """)

st.write("")

with st.expander("🦋 **Future Use Cases**"):
    st.write("""A similar algorithm to this application may be used to examine the impact of TikTok ads on public sentiment. If we are interested in how customers like a specific TikTok feature, we may also analyze public sentiment with this procedure.""")