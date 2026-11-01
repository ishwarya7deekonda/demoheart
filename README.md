# Heart Disease Prediction App

A small Streamlit demo that uses a saved Random Forest model to classify sample heart-related measurements.

## Project files

- `front.py` — the Streamlit app
- `heart.py` — trains the model using `heart.csv`
- `heart.csv` — the training dataset
- `heart_model.pkl` — the saved model used by the app

The model uses these input columns: `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, and `thalach`. It predicts the dataset's `target` class.

## Run the app

Install Python, then install the required packages:

```bash
python -m pip install streamlit pandas scikit-learn
```

Start the app from the repository folder:

```bash
streamlit run front.py
```

To train a new model from `heart.csv`, run:

```bash
python heart.py
```

This replaces `heart_model.pkl`. The saved model may require a compatible scikit-learn version to load.

## Dataset and limitations

The dataset's source and reuse terms were not provided with this project. Confirm its provenance and license before redistributing or using it beyond this demo.

This project is for educational demonstration only. Its output is a dataset class prediction, not a medical assessment. Do not use it for diagnosis, treatment, or health decisions.
