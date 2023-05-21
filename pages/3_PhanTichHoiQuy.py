import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components


st.set_page_config(page_title="Overview")

# Introduction
img = Image.open('images/Overview.jpg')
st.image(img, use_column_width=True)

st.title("Overview")
st.markdown("""
    On this page, we will using Linear Regression to make prediction on our data.
    """)

# Sidebar
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(2011, 2024))))
# Prepare data
path_file = 'data.csv' 
df = pd.read_csv(path_file)

df_grouped = df.groupby('year')

# Print DataFrame
st.markdown("# Our Data Set")
st.markdown(f"## Rank of all school from 2011 to 2023.")
st.dataframe(df)

df1 = pd.read_excel("data.xlsx",sheet_name='Sheet1')

st.markdown("""
 ###   1. Predict Scores Overall
##### Sử dụng các thuộc tính ```scores_teaching```, ```scores_research```, ```scores_citations```, ```scores_industry_income```, ```scores_international_outlook```
    """)

import statsmodels.formula.api as smf
results = smf.ols('Q("scores_overall") ~ Q("scores_teaching") + scores_research + scores_citations + scores_industry_income + scores_international_outlook', data=df).fit()
st.write(results.summary())

st.markdown('''
#### Nhận xét: 
- ```scores_teaching```, ```scores_research```, ```scores_citations```, ```scores_industry_income```, ```scores_international_outlook``` có tác động dương tới ```scores_overall```. 
- 5 biến trên có thể giải thích được 66.0 % sự thay đổi của biến ```scores_overall```. 
- 5 biến có ý nghĩa đối với mô hình về mặt thống kê (p-value: 0.000). Do đó mô hình có giá trị mô tả dữ liệu về mặt thống kê.
- Dựa theo coef, có thể thấy thứ tự các biến có tác động tới ```scores_overall``` là : ```scores_research```, ```scores_teaching```, ```scores_citations```. ```scores_international_outlook``` và ```scores_industry_income``` ít có tác động tới ```scores_overall```
- Mô hình: \
	

''')
st.markdown(''' 
	```python 
	scores_overall = 0.6802 + 0.3060*scores_teaching + 0.3179*scores_research + 0.2442*scores_citations + 0.0307*scores_industry_income + 0.0653*score_international_outlook
''') 

st.markdown("""
##### Sử dụng các thuộc tính  ```stats_number_students```, ```stats_student_staff_ratio```, ```stats_female_male_ratio```

    """)
results = smf.ols('Q("scores_overall") ~ stats_number_students + stats_student_staff_ratio + stats_female_male_ratio', data=df1).fit()
st.write(results.summary())
st.markdown('''Từ kết quả phân tích có thể thấy ```stats_number_students```, ```stats_student_staff_ratio```, ```stats_female_male_ratio``` không có tác động tới ```scores_overall``` và không thể mô tả ``` scores_overall``
''')
st.markdown('''
 ###   2. Predict scores_teaching
##### Sử dụng các thuộc tính ```scores_research```, ```scores_citations```, ```scores_industry_income```, ```scores_international_outlook```
    ''')

results = smf.ols('Q("scores_teaching") ~ scores_research + scores_citations + scores_industry_income + scores_international_outlook ', data=df).fit()
st.write(results.summary())
st.markdown('''
#### Nhận xét: 
- ```scores_research```, ```scores_citations```, ```scores_industry_income```, ```scores_international_outlook``` có tác động dương tới ```scores_teaching```.
- 4 biến trên có thể giải thích được 83.8 % sự thay đổi của biến ```scores_teaching```. 
- 4 biến có ý nghĩa đối với mô hình về mặt thống kê (p-value: 0.000). Do đó mô hình có giá trị mô tả dữ liệu về mặt thống kê.
- Dựa theo coef, có thể thấy biến có tác động lớn tới ```scores_teaching``` là  ```scores_research```. Các biến ```scores_citations```, ```scores_industry_income```, ```scores_international_outlook``` tác động không đáng kể tới```scores_teaching```
- Mô hình: \
	

''')
st.markdown(''' 
	```python 
	scores_teaching = 14.6193 + 0.7749*scores_research + 0.0234*scores_citations - 0.0407*scores_industry_income - 0.0877*score_international_outlook
''') 

st.markdown('''
 ###   3. Predict stats_number_students
##### Sử dụng các thuộc tính ```scores_overall``` , ```scores_teaching``` , ```scores_research```  , ```scores_industry_income``` ,```scores_international_outlook```
    ''')

results = smf.ols('Q("stats_number_students") ~ scores_overall + scores_teaching + scores_research  + scores_industry_income + scores_international_outlook ', data=df1).fit()
st.write(results.summary())
st.markdown('''Từ kết quả phân tích có thể thấy ```scores_overall``` , ```scores_teaching``` , ```scores_research```  , ```scores_industry_income``` ,```scores_international_outlook``` không có tác động tới ```stats_number_students``` và không thể mô tả ``` stats_number_students```
''')


st.markdown('''
 ###   4. Predict rank of a univerity below 100 
##### Rank của trường đại học phụ thuộc vào  ```scores_overall``` nên tập thuộc tính dùng để dự đoán bao gồm ```scores_overall``` , ```scores_teaching``` , ```scores_research```  , ```scores_industry_income``` ,```scores_international_outlook```.
    Thực hiện bài toán phân lớp sử dụng cây quyết định với nhãn là 1 (tương ứng với rank <= 100) và 0 (tương ứng với rank > 100)
    ''')
df_2016 = df[df.year > 2015]
df_2016.loc[df_2016['rank']<=100,'rank_less_100'] = 1
df_2016.loc[df_2016['rank']>100,'rank_less_100'] = 0

X = df_2016[['scores_overall','scores_teaching','scores_research','scores_citations','scores_industry_income','scores_international_outlook']]
y = df_2016['rank_less_100']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

class_0_indices = np.where(y_test == 0)[0]
class_1_indices = np.where(y_test == 1)[0]

random_class_0_indices = np.random.choice(class_0_indices, 250, replace=False)
selected_indices = np.concatenate((random_class_0_indices, class_1_indices))

# Get the corresponding rows from feature matrix x
random_X = X_test.iloc[selected_indices]
random_y = y_test.iloc[selected_indices]

from sklearn import tree
from sklearn.model_selection import cross_validate
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)
clf_gini.fit(X_train, y_train)
y_pred_train_gini = clf_gini.predict(X_train)
st.text('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train_gini)))

y_pred_en = clf_gini.predict(random_X)

st.text('Test-set accuracy score: {0:0.4f}'. format(accuracy_score(random_y, y_pred_en)))

from PIL import Image
st.image("1.png", use_column_width=True)
st.markdown('''
    Từ cây quyết định có thể thấy ```overall_scores``` quyết định rank của trường đại học. Để đạt được thứ hạng dưới 100, 
    các trường đại học phải có điểm overall > 63.05 hoặc điểm ```scores_research``` ít nhất nhất lơn 47.15
    ''')

st.markdown('''
##### ```Overall_score``` có quan hệ với các thuộc tính còn lại. Do đó có thể thực hiện phân lớp rank mà không sử dụng thuộc tính ```Overall_score``` 
    ''')

X_train = X_train[['scores_teaching','scores_research','scores_citations','scores_industry_income','scores_international_outlook']]

# Get the corresponding rows from feature matrix x
random_X = random_X[['scores_teaching','scores_research','scores_citations','scores_industry_income','scores_international_outlook']]

clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)
clf_gini.fit(X_train, y_train)
y_pred_train_gini = clf_gini.predict(X_train)
st.text('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train_gini)))

y_pred_en = clf_gini.predict(random_X)

st.text('Test-set accuracy score: {0:0.4f}'. format(accuracy_score(random_y, y_pred_en)))

st.image("2.png", use_column_width=True)
st.markdown('''
    Loại bỏ ```Overall_score``` không làm giảm độ chính xác của mô hình nhiều. Do đó, có thể xác định yếu tố giúp một trường đại học nằm trong top 100 bao gồm ```scores_research```,```scores_teaching```,```scores_citations```
    ''')

st.markdown(''' #### Correlation Matrix using HeatMap''')

import seaborn as sns
df_2016 = df[df.year > 2015] 
cor = df_2016[['scores_overall','scores_teaching','scores_research','scores_citations','scores_industry_income','scores_international_outlook','stats_number_students', 'stats_student_staff_ratio','stats_female_male_ratio']].corr()
mask = np.triu(np.ones_like(cor, dtype=bool))
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(230, 20, as_cmap=True)


sns.heatmap(cor,annot=True, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.title("Correlation Matrix using HeatMap",fontweight="bold")
st.pyplot(f)

st.markdown('''Từ kết quả trực quan có thể thấy ```score_overall```, ```scores_teaching``` , ```scores_research```, ```scores_citations``` có quan hệ tương quan dương với nhau, ```stats_number_students``` có quan hệ tương quan dương với ```stats_student_staff_ratio```. 
''')

# src = "https://public.tableau.com/views/MarketingDashboard_16631517860700/DigitalMarketing?:embed=y&:display_count=yes&:toolbar=no&:origin=viz_share_link&:showVizHome=no"
# components.html('''<div class='tableauPlaceholder' id='viz1684483334235' style='position: relative'><noscript><a href='#'><img alt='Top University over year by Overall Score  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16843000630040&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16843000630040&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='no' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16843000630040&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='origin' value='viz_share_link' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684483334235');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''',height=768,width = 1300)
