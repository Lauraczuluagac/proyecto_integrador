import streamlit as st
import cv2

# Cargar una imagen
imagen = cv2.imread('dogcat.avif')

# Aplicar un filtro de desenfoque
imagen_desenfocada = cv2.GaussianBlur(imagen, (15, 15), 0)

# Mostrar la imagen original y la imagen desenfocada
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Desenfocada', imagen_desenfocada)
cv2.waitKey(0)

cv2.destroyAllWindows()
st.header("Aplicacón 2")