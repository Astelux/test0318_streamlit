import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Matplotlibのグラフを表示する
def show_matplotlib_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)

# Streamlitアプリケーションの作成
def main():
    st.title('Matplotlib in Streamlit')

    # ボタンをクリックするとグラフが表示される
    if st.button('Show Plot'):
        show_matplotlib_plot()

if __name__ == "__main__":
    main()
