import streamlit as st
import plotly.graph_objects as go
import math

# Custom CSS for visual appeal
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 18px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .main {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    h1, h2 {
        color: #2c3e50;
        text-align: center;
    }
    .stMarkdown {
        font-size: 16px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Main app
st.title("UPSC Polity Notes Dashboard")

# Tile layout
st.header("Explore Topics")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("Municipalities"):
        st.session_state['page'] = "Municipalities"
    else:
        st.session_state.setdefault('page', None)

with col2:
    st.write("Coming Soon...")
with col3:
    st.write("Coming Soon...")

# Municipalities Page
if st.session_state['page'] == "Municipalities":
    st.header("Municipalities in India (74th CAA)")

    # Mind Map Data (radial layout)
    nodes = [
        {"id": "Municipalities", "label": "Municipalities", "radius": 0, "angle": 0, "color": "#2c3e50", "details": "Central topic: Urban governance under 74th CAA."},
        {"id": "Composition", "label": "Composition & Structure", "radius": 150, "angle": 0, "color": "#3498db", "details": """
            - Wards: Every municipal area divided into territorial constituencies termed wards.
            - Ward Members: Directly elected by electorate.
            - Municipal Body: 
              - Directly elected ward members.
              - Others (state law): 
                - (a) Experts in municipal admin.
                - (b) MPs/State Legislators.
                - (c) Ward Committee Chairs.
            - Chairperson: Chosen per state law.
            - Ward Committees (Art. 243S): 
              - For >3L population.
              - Chairperson: Ward member (single) or elected (multi-ward).
              - Functions: State-defined.
        """},
        {"id": "Types", "label": "Types of Municipal Bodies", "radius": 150, "angle": 45, "color": "#2ecc71", "details": """
            - Classified by: Population, density, revenue, employment, economic importance.
            - Types:
              - Municipal Corporation (large cities).
              - Municipal Council (towns).
              - Nagar Panchayat (transitional).
            - Others:
              - Cantonment Board: Elected + Nominated, CEO (IDS) + Military President.
              - Township Area Committee: Industrial towns.
              - Notified Area Committee: Fast-developing towns.
        """},
        {"id": "Powers", "label": "Powers & Authorities", "radius": 150, "angle": 90, "color": "#e67e22", "details": """
            - District Planning Committee (DPC) (Art. 243ZD):
              - Consolidates Panchayat + Municipality plans.
              - 4/5 elected, 1/5 nominated.
            - Municipal Corporation of Delhi (MCD):
              - Commissioner (IAS, executive).
              - Standing Committee (elected).
              - Nominated experts.
        """},
        {"id": "Context", "label": "Context & Figures", "radius": 150, "angle": 135, "color": "#9b59b6", "details": """
            - 2025: >40% urban; 2050: Urban nation.
            - Cities: 65% GDP.
            - Challenges: Planning, environment, waste.
            - ₹40T needed (NITI Aayog).
        """},
        {"id": "Challenges", "label": "Challenges", "radius": 150, "angle": 180, "color": "#e74c3c", "details": """
            1. Financial Paucity: 0.15% GDP.
            2. Corruption: Underpaid staff.
            3. State Control: Dissolution, budget approval.
            4. Limited Devolution: Twelfth Schedule.
            5. Unplanned Urbanization: Slums.
            6. Multiplicity: Overlap with parastatals.
            7. Bureaucratic Dominance.
            8. Substandard Personnel.
            9. Land Titling: >90% unclear, 1.3% GDP loss.
            10. Low CapEx.
            11. Low Participation.
            12. Ecological Challenges.
        """},
        {"id": "Recommendations", "label": "Recommendations", "radius": 150, "angle": 225, "color": "#f1c40f", "details": """
            - National Commission on Urbanization.
            - Transparency: Open data.
            - Direct Mayors + Commissioner consultation.
            - RWAs for participation.
            - 2nd ARC: Property tax reform, fines, bonds.
            - Property Tax Issues: Poor delegation, exemptions, corruption.
        """},
        {"id": "CaseStudies", "label": "Case Studies", "radius": 150, "angle": 270, "color": "#8e44ad", "details": """
            1. Ahmedabad: AJL (BRTS, PPP).
            2. Pune: Waste management (door-to-door, segregation).
            3. Surat: Tech infra, parks (post-1994 plague).
        """}
    ]

    # Convert polar coordinates to Cartesian for Plotly
    x_vals, y_vals, labels, colors, hovertexts = [], [], [], [], []
    for node in nodes:
        x = node["radius"] * math.cos(math.radians(node["angle"]))
        y = node["radius"] * math.sin(math.radians(node["angle"]))
        x_vals.append(x)
        y_vals.append(y)
        labels.append(node["label"])
        colors.append(node["color"])
        hovertexts.append(node["details"])

    # Edges
    edge_x, edge_y = [], []
    for i in range(1, len(nodes)):
        edge_x.extend([0, x_vals[i], None])
        edge_y.extend([0, y_vals[i], None])

    # Create the mind map
    fig = go.Figure()

    # Add edges
    fig.add_trace(go.Scatter(
        x=edge_x, y=edge_y,
        mode="lines",
        line=dict(color="gray", width=2),
        hoverinfo="none"
    ))

    # Add nodes
    fig.add_trace(go.Scatter(
        x=x_vals, y=y_vals,
        mode="markers+text",
        marker=dict(size=30, color=colors, line=dict(width=2, color="white")),
        text=labels,
        textposition="middle center",
        textfont=dict(size=14, color="white"),
        hovertext=hovertexts,
        hoverinfo="text",
        hoverlabel=dict(bgcolor="white", font_size=12)
    ))

    # Layout
    fig.update_layout(
        title="Interactive Mind Map: Municipalities",
        showlegend=False,
        plot_bgcolor="#ecf0f1",
        paper_bgcolor="#ecf0f1",
        height=700,
        width=700,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Display the mind map
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("*Hover over nodes for detailed notes. Use this visual aid to chunk and recall key concepts!*", unsafe_allow_html=True)

else:
    st.write("Click the 'Municipalities' tile to explore!")
