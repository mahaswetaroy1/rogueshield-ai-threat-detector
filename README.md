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
- **Data**: [UNSW-NB15 Dataset](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/)


---

## Project Structure

```
rogueshield-ai-threat-detector/
├── data/                    # Raw dataset CSVs
├── notebooks/
│   ├── eda_unsw_nb15.ipynb
│   ├── forecasting/
│   │   ├── attack_volume/forecast.png
│   │   ├── attack_volume_forecast.ipynb
│   │   └── attack_category_forecast.ipynb
├── models/                  # Saved TensorFlow models
├── explainability/          # SHAP, MITRE mappings
├── app/                     # Streamlit/Flask app (upcoming)
├── requirements.txt
├── README.md
├── LICENSE

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

## Attack Volume Forecasting

This module uses time-series forecasting to analyze and predict the volume of cyberattacks over time from the UNSW-NB15 dataset. This helps SOC teams forecast potential spikes in attack traffic for proactive mitigation.

### Objective
- Predict future attack volumes (14-day horizon)
- Identify temporal patterns and seasonal behaviors in attack frequencies

### Tools & Methods
- Facebook Prophet (additive time-series model)
- Pandas, Plotly, Matplotlib

### Results
- **Trend:** Slightly decreasing trend over the forecast horizon
- **Weekly Pattern:** Highest attack activity observed on **Thursdays**
- **Forecast Confidence Interval:** 95%
- **Forecast Accuracy Visuals** RMSE and MAE plots show how forecast error varies over time horizons. Actual vs. forecast overlay indicates consistent prediction performance over observed periods.



### Output

![Forecast](notebooks/forecasting/attack_volume/forecast.png)

![Actual vs Forecast](notebooks/forecasting/attack_volume/actual_vs_forecast.png)

[View Forecast Notebook](notebooks/forecasting/attack_volume_forecast.ipynb)
[View EDA Notebook](notebooks/eda_unsw_nb15.ipynb)



---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or collaboration:  
**Mahasweta Roy**  
[LinkedIn](https://www.linkedin.com/in/mahasweta-roy-9b79b6150/) | [Email](mailto:mahaswetaroy123@gmail.com)

---


