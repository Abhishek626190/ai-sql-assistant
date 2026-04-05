import streamlit as st

# -----------------------------
# 1. Sample HR Data (Mock DB)
# -----------------------------
data = [
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
    question = question.lower()

    if "salary" in question:
        result = [f"{row[1]} - {row[2]}" for row in data if row[2] > 5000]
        return "Employees with salary > 5000:\n" + "\n".join(result) if result else "No matching employees."

    elif "department" in question:
        departments = list(set([row[3] for row in data]))
        return "Departments:\n" + ", ".join(departments)

    elif "employee" in question:
        return "All Employees:\n" + "\n".join([row[1] for row in data])

    elif "it" in question:
        result = [row[1] for row in data if row[3].lower() == "it"]
        return "IT Employees:\n" + "\n".join(result)

    else:
        return "Sorry, I can answer basic HR questions like employees, salary, and departments."

# -----------------------------
# 3. Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI HR Assistant", layout="centered")

st.title("🤖 AI HR Assistant")
st.write("Ask questions about employees, salary, or departments.")

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