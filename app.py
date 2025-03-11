import streamlit as st
import plotly.graph_objects as go

# Minimal CSS to ensure visibility
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    h1, h2 {
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# Main app
st.title("UPSC Polity Notes")

# Tile layout
st.subheader("Select a Topic")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Municipalities"):
        st.session_state['page'] = "Municipalities"
    else:
        st.session_state.setdefault('page', None)

with col2:
    st.write("Coming Soon")
with col3:
    st.write("Coming Soon")

# Municipalities Page
if st.session_state['page'] == "Municipalities":
    st.header("Municipalities in India")

    # Simplified Mind Map Data
    nodes = [
        {"label": "Municipalities", "x": 0, "y": 0, "color": "#007bff", "details": "Urban governance under 74th CAA."},
        {"label": "Composition", "x": 2, "y": 2, "color": "#28a745", "details": """
            - Wards: Divided into territorial constituencies.
            - Ward Members: Directly elected.
            - Municipal Body: Ward Members + Experts + MPs + Ward Committee Chairs.
            - Chairperson: State law decides mode.
            - Ward Committees (Art. 243S): For >3L population.
        """},
        {"label": "Types", "x": -2, "y": 2, "color": "#dc3545", "details": """
            - Municipal Corporation (large cities).
            - Municipal Council (towns).
            - Nagar Panchayat (transitional).
            - Others: Cantonment Board, Township, Notified Area.
        """},
        {"label": "Powers", "x": 2, "y": -2, "color": "#ffc107", "details": """
            - DPC (Art. 243ZD): 4/5 elected, integrates plans.
            - MCD: Commissioner (IAS) + Standing Committee.
        """},
        {"label": "Context", "x": -2, "y": -2, "color": "#17a2b8", "details": """
            - 2025: >40% urban.
            - Cities: 65% GDP.
            - ₹40T needed (NITI Aayog).
        """},
        {"label": "Challenges", "x": 0, "y": 3, "color": "#6f42c1", "details": """
            1. Financial: 0.15% GDP.
            2. Corruption.
            3. State Control.
            4. Limited Devolution.
            5. Unplanned Urbanization.
        """},
        {"label": "Recommendations", "x": 0, "y": -3, "color": "#fd7e14", "details": """
            - National Commission.
            - Transparency.
            - Direct Mayors.
            - RWAs.
            - 2nd ARC: Property tax reform.
        """},
        {"label": "Case Studies", "x": 3, "y": 0, "color": "#20c997", "details": """
            1. Ahmedabad: AJL (BRTS).
            2. Pune: Waste management.
            3. Surat: Tech infra.
        """}
    ]

    # Edges
    edge_x = [0, 2, None, 0, -2, None, 0, 2, None, 0, -2, None, 0, 0, None, 0, 0, None, 0, 3, None]
    edge_y = [0, 2, None, 0, 2, None, 0, -2, None, 0, -2, None, 0, 3, None, 0, -3, None, 0, 0, None]

    # Create the mind map
    fig = go.Figure()

    # Add edges
    fig.add_trace(go.Scatter(
        x=edge_x, y=edge_y,
        mode="lines",
        line=dict(color="#666666", width=2),
        hoverinfo="none"
    ))

    # Add nodes
    fig.add_trace(go.Scatter(
        x=[node["x"] for node in nodes],
        y=[node["y"] for node in nodes],
        mode="markers+text",
        marker=dict(size=30, color=[node["color"] for node in nodes], line=dict(width=2, color="white")),
        text=[node["label"] for node in nodes],
        textposition="middle center",
        textfont=dict(size=14, color="white"),
        hovertext=[node["details"] for node in nodes],
        hoverinfo="text",
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_color="black",
            bordercolor="gray",
            align="left",
            namelength=-1
        )
    ))

    # Layout
    fig.update_layout(
        title="Mind Map: Municipalities",
        showlegend=False,
        height=600,
        width=600,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    # Display
    st.plotly_chart(fig, use_container_width=True)
    st.write("Hover over nodes to see details.")

else:
    st.write("Click a topic to begin!")
