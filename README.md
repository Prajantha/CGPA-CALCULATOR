# CGPA-CALCULATOR

This is a Python tool to calculate CGPA from student grade inputs.

---

## 💡 Features

- Accepts grade input for 9 subjects.
- Converts grades like O, A+, A, etc., into grade points.
- Each subject has a specific credit weight.
- Detects failure (RA) and stops CGPA calculation.
- Displays the calculated CGPA if all subjects are passed.

---

## 📘 Subjects & Credits

| Subject Code | Subject Name         | Credits |
|--------------|----------------------|---------|
| HS3152       | English              | 3       |
| MA3151       | Mathematics          | 4       |
| PH3151       | Physics              | 3       |
| CY3151       | Chemistry            | 3       |
| GE3151       | Python               | 3       |
| GE3152       | Tamil                | 1       |
| GE3171       | Python Lab           | 2       |
| BS3171       | Physics/Chem Lab     | 2       |
| GE3172       | English Lab          | 1       |

---

## 🧮 CGPA Formula

\[
\text{CGPA} = \frac{\sum(\text{Grade Point} \times \text{Credits})}{\sum(\text{Credits})}
\]

---

## 🚀 How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open a terminal or IDE and run:

```bash
python cgpa_calculator.py
