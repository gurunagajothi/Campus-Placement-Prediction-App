# Campus Placement Prediction App

This is a **Streamlit-based web app** to predict whether a student will get placed in campus recruitment drives based on academic scores and employability test scores.

---

## 🔹 Features

* Upload your dataset (CSV) or use the sample dataset.
* Preview dataset.
* Correlation heatmap of features.
* Logistic Regression model to predict placement.
* Shows accuracy, classification report, and confusion matrix.
* Predict placement for new students by entering feature values.

---

## 🔹 Dataset

The app uses a dataset with the following columns:

| Column                   | Description                                  |
| ------------------------ | -------------------------------------------- |
| SSC Percentage           | Secondary school score                       |
| HSC Percentage           | Higher secondary school score                |
| Degree Percentage        | Undergraduate degree score                   |
| MBA Percentage           | MBA score (if applicable)                    |
| Employability Test Score | Score from employability test                |
| Placed                   | Target variable (0 = Not Placed, 1 = Placed) |

Sample dataset is provided as **campus_placement.csv**.

---

## 🔹 Requirements

Install Python packages:

```
pip install -r requirements.txt
```

Required packages:

* streamlit
* pandas
* scikit-learn
* matplotlib
* seaborn

---

## 🔹 How to Run Locally

1. Clone or download the repository.
2. Open terminal and navigate to the project folder.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

5. The app will open in your default browser. If not, open the link shown in the terminal (usually `http://localhost:8501`).

---

## 🔹 Usage

1. Upload your CSV dataset or use the sample dataset.
2. Preview the data and see the correlation heatmap.
3. View model accuracy, classification report, and confusion matrix.
4. Enter new student details in the input fields and click **Predict** to see placement prediction.

---

## 🔹 Deployment

You can deploy this app on **Streamlit Community Cloud**:

1. Push the project to your GitHub repository.
2. Login to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub and select this repository.
4. Click **Deploy**.
5. Share the live app URL.

---

## 🔹 Example

![Example Screenshot](https://raw.githubusercontent.com/your-username/repo-name/main/screenshot.png)

---

## 🔹 License

This project is open-source under the MIT License.
