# RogueShield: AI-Powered Threat Detection & Forecasting

RogueShield is an AI-powered threat detection and attack forecasting system built using TensorFlow, Streamlit, and SHAP. It classifies network intrusions in real-time, forecasts future attack patterns, and maps results to the MITRE ATT&CK framework — making it a powerful tool for cybersecurity automation and intelligence.

---

## Features

-  Multiclass intrusion detection using deep learning
-  Future attack forecasting with RNN/LSTM
-  Model explainability via SHAP
-  MITRE ATT&CK tactic & technique mapping
-  Real-time dashboard built with Streamlit

---

##  Tech Stack

- **Machine Learning**: TensorFlow, Scikit-learn
- **Explainability**: SHAP
- **Frontend**: Streamlit
- **Backend**: Flask (optional REST API)
- **Data**: [NSL-KDD Dataset](https://www.unb.ca/cic/datasets/nsl.html)

---

## Project Structure

```
rogueshield/
├── data/              # Raw and processed datasets
├── notebooks/         # Jupyter notebooks for EDA and modeling
├── models/            # Saved models (h5 format)
├── app/               # Streamlit app files
├── explainability/    # SHAP plots and scripts
├── requirements.txt   # Python dependencies
├── LICENSE            # MIT License
└── README.md          # You are here
```

---

##  Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/rogueshield-ai-threat-detector.git
cd rogueshield-ai-threat-detector
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app/app.py
```

---

## Sample Outputs



---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or collaboration:  
**Mahasweta Roy**  
[LinkedIn](https://www.linkedin.com/in/mahasweta-roy-9b79b6150/) | [Email](mailto:mahaswetaroy123@gmail.com)

---


