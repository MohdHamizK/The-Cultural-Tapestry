import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="Cultural Tapestry", layout="wide")

# Sidebar Navigation
st.sidebar.title("Explore India's Heritage")
page = st.sidebar.selectbox("Choose a Section", [
    "Home",
    "Art Explorer",
    "Cultural Hotspots",
    "Tourism Trends",
    "Untouched Regions",
    "Responsible Travel Tips"
])

# Load data
@st.cache_data
def load_data():
    return {
        "art": pd.read_csv("data/art_forms.csv"),
        "sites": pd.read_csv("data/cultural_sites.csv"),
        "trends": pd.read_csv("data/seasonal_trends.csv"),
        "untouched": pd.read_csv("data/untouched_regions.csv")
    }

data = load_data()

# Home Page
if page == "Home":
    st.title("🎨 Cultural Tapestry: Exploring India’s Heritage Through Data")
    st.markdown("""
    Welcome to *Cultural Tapestry*, a data-driven exploration of India's rich cultural heritage.
    
    - Discover traditional art forms
    - Explore UNESCO and cultural hotspots
    - Analyze tourism trends
    - Highlight untouched regions
    - Promote responsible tourism
    
    Use the sidebar to navigate through different sections.
    """)

# Art Explorer Page
elif page == "Art Explorer":
    st.title("🖌️ Traditional Indian Art Forms Gallery")

    # Filter by state
    state_filter = st.selectbox("🎨 Filter by State", ["All"] + sorted(data["art"]["state"].str.title().unique().tolist()))

    if state_filter == "All":
        filtered_art = data["art"]
    else:
        filtered_art = data["art"][data["art"]["state"] == state_filter]

    # Display as cards
    st.markdown("""
    <style>
    .card {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        margin: 10px;
        text-align: center;
        transition: transform 0.2s ease-in-out;
    }
    .card:hover {
        transform: scale(1.03);
    }
    .card img {
        max-width: 100%;
        height: auto;
        border-radius: 8px;
    }
    .card h4 {
        font-size: 18px;
        margin: 10px 0 5px;
    }
    .card p {
        font-size: 14px;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

    cols = st.columns(3)  # 3 cards per row
    if not filtered_art.empty:
        for i, row in enumerate(filtered_art.iterrows()):
            _, art = row
            with cols[i % 3]:
                # Try loading and displaying the image using st.image()
                image_url = art['image_url']
                if image_url:
                    try:
                        st.image(image_url, caption=art['art_name'], use_container_width=True)
                    except:
                        st.write(f"Error loading image from: {image_url}")
                
                st.markdown(f"""
                <div class="card">
                    <h4>{art['art_name']}</h4>
                    <p><strong>State:</strong> {art['state'].title()}</p>
                    <p><small>{art['description'][:120]}...</small></p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.write("No art forms found for the selected state.")


# Cultural Hotspots Page
elif page == "Cultural Hotspots":
    st.title("🏛️ UNESCO & Cultural Sites Across India")
    df = data["sites"]

    # Map Visualization
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"{row['site_name']} ({row['state']})<br>Visitors: {row['visitors_2023']}",
            icon=folium.Icon(icon="building", prefix='fa')
        ).add_to(m)

    st_folium(m, width=700, height=500)

    # Top Sites Chart
    top_sites = df.sort_values(by="visitors_2023", ascending=False).head(10)
    fig = px.bar(top_sites, x="site_name", y="visitors_2023", color="state", title="Top 10 Visited Cultural Sites")
    st.plotly_chart(fig)

# Tourism Trends Page
elif page == "Tourism Trends":
    st.title("📈 Seasonal Tourism Trends by State")
    df = data["trends"]
    state_filter = st.selectbox("Select State", ["All"] + sorted(df["state"].str.title().unique().tolist()))

    if state_filter != "All":
        df = df[df["state"] == state_filter]

    fig = px.line(df, x="month", y="total_visitors", color="state", title="Tourist Trends Over Time")
    st.plotly_chart(fig)

# Untouched Regions Page
elif page == "Untouched Regions":
    st.title("🔍 Hidden Cultural Gems of India")
    df = data["untouched"]

    # Map Visualization
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=f"{row['region_name']} ({row['state']})<br>Reason: {row['reason']}"
        ).add_to(m)

    st_folium(m, width=700, height=500)

    st.dataframe(df)

# Responsible Travel Tips Page
elif page == "Responsible Travel Tips":
    st.title("🌿 Promoting Responsible Tourism")
    st.markdown("""
    - Respect local customs and traditions
    - Support local artisans and businesses
    - Avoid littering; carry eco-friendly items
    - Choose homestays over large resorts
    - Educate yourself about the culture before visiting
    """)