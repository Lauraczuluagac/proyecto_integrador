import streamlit as st
import math

angulo_grados = float(input("Ingresa el ángulo en grados: "))
angulo_radianes = math.radians(angulo_grados)
seno = math.sin(angulo_radianes)
coseno = math.cos(angulo_radianes)

print(f"Seno({angulo_grados}°) = {seno}")
print(f"Coseno({angulo_grados}°) = {coseno}")

st.header("Aplicacón 2")