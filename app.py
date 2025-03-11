import streamlit as st
import plotly.graph_objects as go
import math

# Custom CSS with modern UX/UI
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #eceff1, #b0bec5);
        font-family: 'Roboto', sans-serif;
        color: #263238;
    }
    .stButton>button {
        background: linear-gradient(90deg, #0288d1, #03a9f4);
        color: white;
        border-radius: 12px;
        padding: 15px 30px;
        font-size: 18px;
        font-weight: 500;
        border: none;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0277bd, #039be5);
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        transform: translateY(-2px);
    }
    .main {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    h1 {
        color: #01579b;
        font-size: 40px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
    }
    h2 {
        color: #0288d1;
        font-size: 28px;
        font-weight: 600;
        text-align: center;
    }
    .card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .stMarkdown {
        font-size: 16px;
        line-height: 1.7;
        color: #37474f;
    }
    </style>
""", unsafe_allow_html=True)

# Main app
st.title("UPSC Polity Notes")

# Tile layout with cards
st.markdown("### Explore Topics", unsafe_allow_html=True)
cols = st.columns(3)

with cols[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    if st.button("Municipalities"):
        st.session_state['page'] = "Municipalities"
    else:
        st.session_state.setdefault('page', None)
    st.markdown('</div>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div class="card"><p style="text-align:center; color:#78909c;">Coming Soon</p></div>', unsafe_allow_html=True)
with cols[2]:
    st.markdown('<div class="card"><p style="text-align:center; color:#78909c;">Coming Soon</p></div>', unsafe_allow_html=True)

# Municipalities Page
if st.session_state['page'] == "Municipalities":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.header("Municipalities in India")

    # Mind Map Data
    nodes = [
        {"id": "Municipalities", "label": "Municipalities", "radius": 0, "angle": 0, "color": "#01579b", "details": "Urban governance under 74th CAA."},
        {"id": "Composition", "label": "Composition & Structure", "radius": 200, "angle": 0, "color": "#0288d1", "details": """
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
        {"id": "Types", "label": "Types of Municipal Bodies", "radius": 200, "angle": 45, "color": "#4caf50", "details": """
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
        {"id": "Powers", "label": "Powers & Authorities", "radius": 200, "angle": 90, "color": "#f57c00", "details": """
            - District Planning Committee (DPC) (Art. 243ZD):
              - Consolidates Panchayat + Municipality plans.
              - 4/5 elected, 1/5 nominated.
            - Municipal Corporation of Delhi (MCD):
              - Commissioner (IAS, executive).
              - Standing Committee (elected).
              - Nominated experts.
        """},
        {"id": "Context", "label": "Context & Figures", "radius": 200, "angle": 135, "color": "#8e24aa", "details": """
            - 2025: >40% urban; 2050: Urban nation.
            - Cities: 65% GDP.
            - Challenges: Planning, environment, waste.
            - ₹40T needed (NITI Aayog).
        """},
        {"id": "Challenges", "label": "Challenges", "radius": 200, "angle": 180, "color": "#d32f2f", "details": """
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
        {"id": "Recommendations", "label": "Recommendations", "radius": 200, "angle": 225, "color": "#fbc02d", "details": """
            - National Commission on Urbanization.
            - Transparency: Open data.
            - Direct Mayors + Commissioner consultation.
            - RWAs for participation.
            - 2nd ARC: Property tax reform, fines, bonds.
            - Property Tax Issues: Poor delegation, exemptions, corruption.
        """},
        {"id": "CaseStudies", "label": "Case Studies", "radius": 200, "angle": 270, "color": "#7b1fa2", "details": """
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
        hovertexts.append(f"<b>{node['label']}</b><br><br>{node['details']}")

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
        line=dict(color="#90a4ae", width=2, dash="dot"),
        hoverinfo="none"
    ))

    # Add nodes
    fig.add_trace(go.Scatter(
        x=x_vals, y=y_vals,
        mode="markers+text",
        marker=dict(size=45, color=colors, line=dict(width=3, color="white")),
        text=labels,
        textposition="middle center",
        textfont=dict(size=16, color="white", family="Roboto"),
        hovertext=hovertexts,
        hoverinfo="text",
        hoverlabel=dict(
            bgcolor="rgba(255, 255, 255, 0.95)",
            font_size=14,
            font_family="Roboto",
            font_color="#263238",
            bordercolor="#b0bec5",
            align="left",
            padding=dict(l=15, r=15, t=10, b=10),
            namelength=-1
        )
    ))

    # Layout
    fig.update_layout(
        title=dict(text="Mind Map: Municipalities", font=dict(size=26, color="#01579b"), x=0.5),
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=800,
        width=800,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        margin=dict(l=50, r=50, t=80, b=50)
    )

    # Display the mind map in a collapsible section
    with st.expander("Explore the Mind Map", expanded=True):
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("*Hover over nodes for detailed insights. Click and drag to explore!*", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="main"><p style="text-align:center; font-size:18px;">Select a topic above to dive in!</p></div>', unsafe_allow_html=True)
