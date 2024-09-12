import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# 페이지 이름 설정
st.set_page_config(page_title="A회사 렌터카 사업 전략 제안", layout="wide")


st.title("지점 안내")
