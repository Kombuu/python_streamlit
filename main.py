import streamlit as st
import time

st.title('Streamlit')

st.write('プログレスバーを表示する')
'Start!!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range (100):
     latest_interation.text(f'Interation {i+1}')
     bar.progress(i+1)
     time.sleep(0.1)

'Done!!!!!!!!!!!!!!!!!!'


st.write('DisplayImage')

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
     right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせを開く')
expander.write('問い合わせを開く2')

# if st.checkbox('Show Imagae'):
#      img = Image.open('u_profile.jpg')
#      st.image(img, caption='profile', use_column_width=True)


text = st.selectbox('好きな趣味は',list(range(1,11)))
condition = st.slider('あなたの今の調子は？',0,100,50)



'あなたの趣味：', text



'あなたのコンディション:', condition


#表を表示する
#df = pd.DataFrame({
#    '1列目': [1,2,3,4],
#    '21列目': [10,20,30,40]
#})



#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat', 'lon']
#)

#最大値にハイライトをつける
#st.dataframe(df.style.highlight_max(axis=0))
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
#st.map(df)


# マークダウン可能
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """