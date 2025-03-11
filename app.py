import streamlit as st

# Main app
st.title("UPSC Polity Notes Dashboard")

# Sidebar for navigation
st.sidebar.header("Topics")
st.sidebar.write("Select a topic below to explore detailed notes.")

# Tile layout for topics
st.header("Explore Topics")
col1, col2, col3 = st.columns(3)

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

    # Mind Map Section
    with st.expander("Mind Map - Overview", expanded=True):
        st.subheader("Mind Map: Municipalities")
        st.markdown("""
        ### Central Node: **Municipalities in India**
        - **1. Composition and Structure** (Blue)
          - Wards: Territorial units, elected Ward Members.
          - Municipal Body: Ward Members + Experts + MPs + Ward Committee Chairs.
          - Ward Committees (Art. 243S): >3L population, state-defined.
        - **2. Types** (Green)
          - Corporation, Council, Nagar Panchayat.
          - Others: Cantonment Board, Township, Notified Area.
        - **3. Powers** (Orange)
          - DPC (Art. 243ZD): 4/5 elected, integrates plans.
          - MCD: Commissioner (IAS) + Standing Committee.
        - **4. Challenges** (Red)
          - Financial (0.15% GDP), Corruption, State Control, Unplanned Urbanization.
        - **5. Recommendations** (Yellow)
          - Direct Mayors, Property Tax Reform, Citizen Involvement.
        - **6. Case Studies** (Purple)
          - Ahmedabad (AJL), Pune (Waste), Surat (Tech).
        """)
        st.write("*Note*: Visualize with colors: Blue, Green, Orange, Red, Yellow, Purple.")

    # Detailed Notes
    st.subheader("Detailed Notes")
    st.write("#### Composition and Structure")
    st.markdown("""
    - **Wards**: Divided into territorial constituencies.
    - **Ward Members**: Directly elected.
    - **Municipal Body**:
      - Ward Members + Experts (municipal admin) + MPs/State Legislators + Ward Committee Chairs.
      - Chairperson: State law decides mode.
    - **Ward Committees** (Art. 243S):
      - For >3L population.
      - Chairperson: Ward member (single) or elected (multi-ward).
    """)
    st.write("#### Types of Municipal Bodies")
    st.markdown("""
    - Corporation (large cities), Council (towns), Nagar Panchayat (transitional).
    - **Others**:
      - Cantonment Board: Elected + Nominated, CEO + Military President.
      - Township Area Committee: Industrial towns.
      - Notified Area Committee: Fast-developing towns.
    """)
    st.write("#### Powers and Authorities")
    st.markdown("""
    - **DPC** (Art. 243ZD): 4/5 elected, 1/5 nominated, integrates plans.
    - **MCD**: Commissioner (IAS) + Standing Committee + Nominated experts.
    """)
    st.write("#### Context and Figures")
    st.markdown("""
    - 2025: >40% urban; 2050: Urban nation.
    - Cities: 65% GDP.
    - ₹40T needed for infra (NITI Aayog).
    """)
    st.write("#### Challenges")
    st.markdown("""
    1. Financial: 0.15% GDP.
    2. Corruption: Weak admin.
    3. State Control: Budget approval, dissolution.
    4. Limited Devolution: Twelfth Schedule.
    5. Unplanned Urbanization: Slums.
    6. Multiplicity: Overlap with parastatals.
    7. Bureaucratic Dominance.
    8. Substandard Personnel.
    9. Land Titling: >90% unclear.
    10. Low CapEx.
    11. Low Participation.
    12. Ecological Issues.
    """)
    st.write("#### Recommendations")
    st.markdown("""
    - National Commission on Urbanization.
    - Transparency: Open data.
    - Direct Mayors + Commissioner consultation.
    - RWAs for participation.
    - 2nd ARC: Property tax reform, fines, bonds.
    """)
    st.write("#### Case Studies")
    st.markdown("""
    1. Ahmedabad: AJL (BRTS).
    2. Pune: Waste management.
    3. Surat: Tech infra.
    """)

else:
    st.write("Click a topic tile above to view detailed notes!")
