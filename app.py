import collections
import joblib
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import os
from utils import *

st.title('Skin Disease Classifier')
st.subheader('Choose from the Options')
st.write('')
st.write('')

data = collections.defaultdict()
for label, options in dic.items():
    options = ['-'] + options
    choice = st.selectbox(label, options)
    data[label] = choice
    st.write()

if st.checkbox('Done'):
    pass
else:
    st.stop()

if '-' in data.values():
    st.warning('Please select all option. You seem to skip some!')
    st.stop()

model = joblib.load(os.path.join(path_models, "model_random_forest.joblib"))
enc = joblib.load(os.path.join(path_models,'encoder.joblib'))

# data in proper sequence
x = [data[label] for label in columns]
# single batch
X = [x]
X = enc.transform(X)
pred_disease = model.predict(X)[0]
pred_proba = model.predict_proba(X)[0]
st.subheader(f'The predicted disease is -> {pred_disease}.')


# removing 0 probs, testing
non_zero = [i for i, n in enumerate(pred_proba) if n > 0]
pred_proba = pred_proba[non_zero]

# proba chart
fig, ax = plt.subplots()
idxs = np.arange(len(non_zero))
ax.barh(idxs, pred_proba, align='center')
ax.set_yticks(idxs)
ax.set_yticklabels(diseases[non_zero])
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
ax.set_title('Disease Probabilities')
st.pyplot(fig)

