import streamlit as st
from wqi_calculator import WQICalculator

def main():
	st.title("Water Quality Index (WQI) Evaluator")

	# Input fields
	ph = st.slider("pH", min_value=0., max_value=14., step=0.1)
	tds = st.slider("Total Dissolved Solids (mg/L)", min_value=0, max_value=2000, step=1)
	tur = st.slider("Turbidity (NTU)", min_value=0, max_value=100, step=1)
	do = st.slider("Dissolved Oxygen (mg/L)", min_value=0., max_value=20., step=0.1)
	
	# Calculate WQI when user clicks button
	if st.button("Evalulate WQI"):
		calculator = WQICalculator(ph, tds, tur, do)
		result = calculator.evaluate_wqi()
		st.write(f"Water Quality: {result}")

if __name__ == '__main__':
	main()
