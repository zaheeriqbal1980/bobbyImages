import streamlit as st
import streamlit.components.v1 as components

HtmlFile = open("image_comparison.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code,width=600,height=600)