import streamlit as st
import plotly.graph_objects as go
import math

# Custom CSS for visual appeal
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #e0eafc, #cfdef3);
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(90deg, #4CAF50, #66BB6A);
        color: white;
        border-radius: 15px;
        padding: 15px 30px;
        font-size: 20px;
        font-weight: bold;
        border: none;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        background: linear-gradient(90deg, #45a049, #5cb85c);
    }
    .main {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        margin: 20px;
    }
    h1 {
        color: #1a3c34;
        font-size: 36px;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    h2 {
        color: #2c3e50;
        font-size: 28px;
        text-align: center;
    }
    .stMarkdown {
        font-size: 16px;
        line-height: 1.8;
        color: #34495e;
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

    # Mind Map Data (radial layout with better colors)
    nodes = [
        {"id": "Municipalities", "label": "Municipalities", "radius": 0, "angle": 0, "color": "#34495e", "details": "Central topic: Urban governance under 74th CAA."},
        {"id": "Composition", "label": "Composition & Structure", "radius": 200, "angle": 0, "color": "#2980b9", "details": """
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
        {"id": "Types", "label": "Types of Municipal Bodies", "radius": 200, "angle": 45, "color": "#27ae60", "details": """
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
        {"id": "Powers", "label": "Powers & Authorities", "radius": 200, "angle": 90, "color": "#d35400", "details": """
            - District Planning Committee (DPC) (Art. 243ZD):
              - Consolidates Panchayat + Municipality plans.
              - 4/5 elected, 1/5 nominated.
            - Municipal Corporation of Delhi (MCD):
              - Commissioner (IAS, executive).
              - Standing Committee (elected).
              - Nominated experts.
        """},
        {"id": "Context", "label": "Context & Figures", "radius": 200, "angle": 135, "color": "#8e44ad", "details": """
            - 2025: >40% urban; 2050: Urban nation.
            - Cities: 65% GDP.
            - Challenges: Planning, environment, waste.
            - ₹40T needed (NITI Aayog).
        """},
        {"id": "Challenges", "label": "Challenges", "radius": 200, "angle": 180, "color": "#c0392b", "details": """
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
        {"id": "Recommendations", "label": "Recommendations", "radius": 200, "angle": 225, "color": "#f39c12", "details": """
            - National Commission on Urbanization.
            - Transparency: Open data.
            - Direct Mayors + Commissioner consultation.
            - RWAs for participation.
            - 2nd ARC: Property tax reform, fines, bonds.
            - Property Tax Issues: Poor delegation, exemptions, corruption.
        """},
        {"id": "CaseStudies", "label": "Case Studies", "radius": 200, "angle": 270, "color": "#9b59b6", "details": """
            1. Ahmedabad: AJL (BRTS, PPP).
            2. Pune: Waste management (door-to-door, segregation).
            3. Surat: Tech infra, parks (post-1994 plague).
        """}
    ]

    # Convert polar coordinates to Cartesian
    x_vals, y_vals, labels, colors, hovertexts = [], [], [], [], []
    for node in nodes:
        x = node["radius"] * math.cos(math.radians(node["angle"]))
        y = node["radius"] * math.sin(math.radians(node["angle"]))
        x_vals.append(x)
        y_vals.append(y)
        labels.append(node["label"])
        colors.append(node["color"])
        hovertexts.append(f"<b>{node['label']}</b><br>{node['details']}")

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
        line=dict(color="#bdc3c7", width=3, dash="dash"),
        hoverinfo="none"
    ))

    # Add nodes
    fig.add_trace(go.Scatter(
        x=x_vals, y=y_vals,
        mode="markers+text",
        marker=dict(size=40, color=colors, line=dict(width=2, color="#ecf0f1")),
        text=labels,
        textposition="middle center",
        textfont=dict(size=16, color="black", family="Segoe UI"),
        hovertext=hovertexts,
        hoverinfo="text",
        hoverlabel=dict(
            bgcolor="rgba(255, 255, 255, 0.9)",
            font_size=14,
            font_family="Segoe UI",
            bordercolor="#34495e",
            align="left",
            namelength=-1  # Show full text without truncation
        )
    ))

    # Layout
    fig.update_layout(
        title=dict(text="Interactive Mind Map: Municipalities", font_size=24, x=0.5),
        showlegend=False,
        plot_bgcolor="#ecf0f1",
        paper_bgcolor="#ecf0f1",
        height=800,
        width=800,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        margin=dict(l=60, r=60, t=80, b=60)
    )

    # Display the mind map
    with st.container():
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("*Hover over nodes to see detailed notes in a styled box. Use this for quick recall and revision!*", unsafe_allow_html=True)

else:
    st.write("Click the 'Municipalities' tile to explore!")
