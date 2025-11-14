# Tutorial: From Jupyter to Interactive Dashboard with Streamlit

**Objective:** To teach how to transform a static data analysis (such as a Jupyter Notebook) into an interactive web application that anyone can use, without needing knowledge of HTML/CSS/JavaScript.

**Practical Example:** Use a municipal spending dataset to create a dashboard where the user can filter by municipality and see spending over time.

---

### 1. Concept: Why a Dashboard?

* **The Problem:** A Jupyter Notebook is great for *analysts*, but terrible for the *public*. Nobody will download your notebook, install Jupyter, and run your cells.

* **The Solution:** A web dashboard allows the end user to **interact** with the data (filtering, selecting) and see the results (graphs) in real time, directly in the browser.

**The Tool (Streamlit):** It's a Python library that transforms Python scripts into web applications. You write pure Python; Streamlit magically draws the buttons, menus, and graphics.

### 2. Installation and Execution

For this tutorial, you will need the following libraries:

```bash
pip install streamlit pandas plotly
```
