import streamlit as st
import plotly.graph_objects as go

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
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .main {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #2c3e50;
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

    # Mind Map Data (from your notes)
    nodes = [
        {"id": "Municipalities", "label": "Municipalities in India", "x": 0, "y": 0, "z": 0, "color": "#2c3e50", "details": "Central topic covering urban governance under 74th CAA."},
        {"id": "Composition", "label": "Composition & Structure", "x": 1, "y": 1, "z": 1, "color": "#3498db", "details": """
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
        {"id": "Types", "label": "Types of Municipal Bodies", "x": -1, "y": 1, "z": 1, "color": "#2ecc71", "details": """
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
        {"id": "Powers", "label": "Powers & Authorities", "x": 1, "y": -1, "z": 1, "color": "#e67e22", "details": """
            - District Planning Committee (DPC) (Art. 243ZD):
              - Consolidates Panchayat + Municipality plans.
              - 4/5 elected, 1/5 nominated.
            - Municipal Corporation of Delhi (MCD):
              - Commissioner (IAS, executive).
              - Standing Committee (elected).
              - Nominated experts.
        """},
        {"id": "Context", "label": "Context & Figures", "x": -1, "y": -1, "z": 1, "color": "#9b59b6", "details": """
            - 2025: >40% urban; 2050: Urban nation.
            - Cities: 65% GDP.
            - Challenges: Planning, environment, waste.
            - ₹40T needed (NITI Aayog).
        """},
        {"id": "Challenges", "label": "Challenges", "x": 1, "y": 0, "z": -1, "color": "#e74c3c", "details": """
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
        {"id": "Recommendations", "label": "Recommendations", "x": -1, "y": 0, "z": -1, "color": "#f1c40f", "details": """
            - National Commission on Urbanization.
            - Transparency: Open data.
            - Direct Mayors + Commissioner consultation.
            - RWAs for participation.
            - 2nd ARC: Property tax reform, fines, bonds.
            - Property Tax Issues: Poor delegation, exemptions, corruption.
        """},
        {"id": "CaseStudies", "label": "Case Studies", "x": 0, "y": 1, "z": -1, "color": "#8e44ad", "details": """
            1. Ahmedabad: AJL (BRTS, PPP).
            2. Pune: Waste management (door-to-door, segregation).
            3. Surat: Tech infra, parks (post-1994 plague).
        """}
    ]

    # Edges for the mind map
    edges = [
        ("Municipalities", "Composition"), ("Municipalities", "Types"), ("Municipalities", "Powers"),
        ("Municipalities", "Context"), ("Municipalities", "Challenges"), ("Municipalities", "Recommendations"),
        ("Municipalities", "CaseStudies")
    ]

    # Create 3D Mind Map with Plotly
    fig = go.Figure()

    # Add nodes
    for node in nodes:
        fig.add_trace(go.Scatter3d(
            x=[node["x"]], y=[node["y"]], z=[node["z"]],
            mode="markers+text",
            marker=dict(size=20, color=node["color"]),
            text=[node["label"]],
            hovertext=[node["details"]],
            hoverinfo="text",
            textposition="middle center"
        ))

    # Add edges
    for edge in edges:
        x0, y0, z0 = next(n["x"] for n in nodes if n["id"] == edge[0]), next(n["y"] for n in nodes if n["id"] == edge[0]), next(n["z"] for n in nodes if n["id"] == edge[0])
        x1, y1, z1 = next(n["x"] for n in nodes if n["id"] == edge[1]), next(n["y"] for n in nodes if n["id"] == edge[1]), next(n["z"] for n in nodes if n["id"] == edge[1])
        fig.add_trace(go.Scatter3d(
            x=[x0, x1], y=[y0, y1], z=[z0, z1],
            mode="lines",
            line=dict(color="gray", width=2),
            hoverinfo="none"
        ))

    # Layout for 3D effect
    fig.update_layout(
        title="Interactive 3D Mind Map: Municipalities",
        scene=dict(
            xaxis=dict(showgrid=True, zeroline=True, title=""),
            yaxis=dict(showgrid=True, zeroline=True, title=""),
            zaxis=dict(showgrid=True, zeroline=True, title=""),
            bgcolor="#ecf0f1"
        ),
        showlegend=False,
        height=600,
        margin=dict(l=0, r=0, t=50, b=0)
    )

    # Display the mind map
    st.plotly_chart(fig, use_container_width=True)
    st.write("*Hover over nodes to see detailed notes from your class!*")

else:
    st.write("Click the 'Municipalities' tile to explore!")
