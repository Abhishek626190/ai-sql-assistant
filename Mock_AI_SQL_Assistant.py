import streamlit as st

# -----------------------------
# 1. Sample HR Data (Mock DB)
# -----------------------------
data = [
    ("ID","Name","Salary","Department"),
    (1, "John", 6000, "IT"),
    (2, "Alice", 4000, "HR"),
    (3, "Bob", 7000, "Finance"),
    (4, "Emma", 3000, "HR"),
    (5, "David", 8000, "IT"),
]

# -----------------------------
# 2. Simple AI Logic (Mock AI)
# -----------------------------
def generate_answer(question, data):
    question = question.lower()  # make case-insensitive

    # --------- Salary Queries ---------
    if "salary" in question:
        if "greater" in question:
            # Extract the number if mentioned
            import re
            match = re.search(r'\d+', question)
            threshold = int(match.group()) if match else 5000
            result = [f"{row[1]} - {row[2]}" for row in data if row[2] > threshold]
            return f"Employees with salary > {threshold}:\n" + "\n".join(result) if result else "No matching employees."
        else:
            result = [f"{row[1]} - {row[2]}" for row in data]
            return "Employees with salary:\n" + "\n".join(result) if result else "No matching employees."

    # --------- Department Specific Queries ---------
    departments = list(set([row[3] for row in data]))
    for dept in departments:
        if dept.lower() in question:
            result = [row[1] for row in data if row[3].lower() == dept.lower()]
            return f"{dept} Employees:\n" + "\n".join(result) if result else f"No employees in {dept}."

    # --------- All Departments ---------
    if "department" in question:
        return "Departments:\n" + ", ".join(departments)

    # --------- All Employees ---------
    if "employee" in question:
        return "All Employees:\n" + "\n".join([row[1] for row in data])

    # --------- Fallback ---------
    return "Sorry, I can answer basic SQL-like questions about employees, salaries, and departments."
# -----------------------------
# 3. Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI SQL Assistant", layout="centered")

st.title("🤖 AI SQL Assistant")
st.write("Ask questions about employees, salary, or departments.")
st.markdown("""
**Examples of questions you can ask:**  
- Show all employees  
- Show all employees with salary  
- Show employees with salary greater than 5000  
- List departments  
- Show IT employees
""")

# User input
user_question = st.text_input("Enter your question:")

if st.button("Ask AI"):
    if not user_question.strip():
        st.warning("Please enter a question.")
    else:
        answer = generate_answer(user_question, data)
        st.subheader("AI Response:")
        st.write(answer)

# -----------------------------
# 4. Show Data Table
# -----------------------------
with st.expander("📊 View Employee Data"):
    st.table(data)