import streamlit as st 
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
st.set_page_config(
    page_title='Welcome',
    page_icon="👋"
)
st.write("# Data Visualization ! 👋")
st.sidebar.success("Select a demo above")
st.markdown(
       """
    ---
    
    ### About Dataset
    This web is about Ranking of university around the World
    ### Author's words
    Hope this dataset helps the data analysis community.

    ---
""""""Product of Ngô Hữu Nhật Thanh 

"""
)

# st.set_page_config(page_title="Overview")
st.markdown("""Statistics""")
# Introduction
img = Image.open('images/Overview.jpg')
st.image(img, use_column_width=True)

st.title("Overview")
st.markdown("""
    On this part, we will explore and understand the dataset for a specific year of your choice.
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

st.markdown("""
        ### What do the columns in data mean?
        Sure! Here's the meaning of each column in the provided dataset:

        1. `rank_order`: The order/ranking of the university.
        2. `rank`: The ranking position of the university.
        3. `name`: The name of the university.
        4. `scores_overall`: The overall score of the university.
        5. `scores_overall_rank`: The ranking of the university based on the overall score.
        6. `scores_teaching`: The score of the university in the teaching category.
        7. `scores_teaching_rank`: The ranking of the university based on the teaching score.
        8. `scores_research`: The score of the university in the research category.
        9. `scores_research_rank`: The ranking of the university based on the research score.
        10. `scores_citations`: The score of the university in the citations category.
        11. `scores_citations_rank`: The ranking of the university based on the citations score.
        12. `scores_industry_income`: The score of the university in the industry income category.
        13. `scores_industry_income_rank`: The ranking of the university based on the industry income score.
        14. `scores_international_outlook`: The score of the university in the international outlook category.
        15. `scores_international_outlook_rank`: The ranking of the university based on the international outlook score.
        16. `location`: The location/country of the university.
        17. `stats_number_students`: The number of students at the university.
        18. `stats_student_staff_ratio`: The ratio of students to staff at the university.
        19. `stats_pc_intl_students`: The percentage of international students at the university.
        20. `stats_female_male_ratio`: The ratio of female to male students at the university.
        21. `aliases`: Any aliases or alternative names for the university.
        22. `subjects_offered`: The subjects offered by the university.
        23. `year`: The year of the ranking data.

        These columns provide information about the ranking, scores, location, student demographics, and other details of each university in the dataset.
    """)

st.markdown(f"## Rank of all school  in year {selected_year}.")
st.dataframe(df_grouped.get_group(selected_year))
# Data Explorations

st.markdown("Shape and Quantity of duplicated data")
df_ex = pd.DataFrame([df.shape[0], df.shape[1], df.duplicated().sum()],
                     index=['Rows', 'Columns', 'Duplicated Rows'], columns=['Quantity'])
st.dataframe(df_ex)

st.markdown("## Data Types")
dtypes = pd.DataFrame([df.dtypes])
st.dataframe(dtypes.astype(str))

st.markdown("## Numeric columns")
nume_col_list = list(df.select_dtypes(include='float64'))
nume_df = df[nume_col_list]
df1 = pd.DataFrame([nume_df.isna().mean() * 100], index=["missing_ratio"])
df2 = df[nume_col_list].describe()
nume_col_profiles_df = np.round(pd.concat([df1, df2], axis=0), 2)
st.dataframe(nume_col_profiles_df.astype(str))

# Comment
st.markdown("""
    `Are they abnormal?`
    """)
st.markdown("The data is normal and ready to visualization")
st.markdown("## Further distribution for Numeric columns")
median_df = pd.DataFrame([nume_df.median()], index=["median"])
nume_col_profiles_df = pd.concat([nume_col_profiles_df, median_df], axis=0)
st.dataframe(nume_col_profiles_df.astype(str))

st.markdown("## Categorical columns")
cate_df = df[['name','location','aliases','subjects_offered']]  
cate_col_profiles_df = pd.DataFrame([
    cate_df.isna().mean() * 100,
    cate_df.apply(lambda x: pd.unique(x.dropna()).size),
    cate_df.apply(lambda x: pd.unique(x.dropna()))],
    index=["missing_ratio", "num_diff_vals", "diff_vals"])
st.dataframe(cate_col_profiles_df.astype(str))

# Comment
st.markdown("""
    `Are they abnormal?`
    """)
st.markdown("The data is normal and ready to visualization")
st.markdown("## Number of school in each location")
num_each_category = df[['name', 'location']]
num_each_category = num_each_category.groupby('location').count()
num_each_category.rename(columns={'name': 'Quantity'}, inplace=True)
st.dataframe(num_each_category.astype(str))


st.markdown("## Change of Overal Score of University in VietNam over Year ")
components.html('''<div class='tableauPlaceholder' id='viz1684493928400' style='position: relative'><noscript><a href='#'><img alt='Change of Overal Score of University in VietNam over Year  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet3' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684493928400');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1250, height=950)
st.markdown("-	Nhìn chung, Overall Scores các Đại học của Việt Nam có mặt trong top ranking thế giới rất thấp, chỉ khoảng tầm 19-20 đến hơn 30 điểm (trên thang 100).")
st.markdown("-	Đến năm 2020 mới có các Đại học được vào top ranking như Đại học Quốc gia TP.HCM, Đại học Quốc gia Hà Nội và Đại học Bách Khoa Hà Nội.")
st.markdown("-	Đại học Quốc gia TP.HCM có tăng điểm vào năm 2021 (25.2 so với 22.1 của năm 2020). Tuy nhiên các năm tiếp theo 2022 và 2023, họ lại không có mặt trong danh sách top ranking.")
st.markdown("-	Đại học Quốc gia Hà Nội vẫn hiện diện trong danh sách từ 2020 đến 2023. Năm 2021 điểm của họ có tăng nhẹ đến 30.2 từ 28.2 năm 2020.")
st.markdown("-	Đại học Bách Khoa Hà Nội lại có Overall Scores giảm dần từ 2020 đến 2023: 28.2 (năm 2020), 25.0 (năm 2021), 22.3 (năm 2022) và 18.3 (năm 2023).")
st.markdown("-	Bất ngờ nhất lại là Đại học Duy Tân và Đại học Tôn Đức Thắng khi họ lại có mặt trong top ranking 2 năm trở lại đây với số điểm rất cao (44.0 vào năm 2022 và lại tăng nhẹ tới 44.9 vào năm 2023).")

# st.markdown("## Box plot of overall score in some countries")
# components.html('''<div class='tableauPlaceholder' id='viz1684495442851' style='position: relative'><noscript><a href='#'><img alt='Box plot of overall score in some country  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet13&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet13' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet13&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684495442851');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=600)
# st.markdown("## Nhận xét:")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")

# st.markdown("## Number of Universities which offered each subject")
# components.html('''<div class='tableauPlaceholder' id='viz1684495695452' style='position: relative'><noscript><a href='#'><img alt='Count Subject over Year  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet15&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet15' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet15&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684495695452');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=700)
# st.markdown("## Nhận xét:")
# st.markdown("- Dựa vào bán kính lớn-nhỏ của biểu đồ, các ngành mũi nhọn như Computer Science, Business & Management, Mathematics & Statistics và ngành Languages, Literature & Linguistics, ... được hơn 1300 đến hơn 1400 Đại học đào tạo và có mặt trong world ranking.")
# st.markdown("- Một số ngành cũng không kém cạnh như: Economics & Econometrics, Education, Electrical & Electronic Engineering, Physics & Astronomy,... cũng được rất nhiều trường Đại học đào tạo, với gần và hơn 1200 trường.")
# st.markdown("- Có thể thấy rằng những môn học, ngành học trong biểu đồ dưới đều là những ngành mũi nhọn, quan trọng trong việc phát triển đất nước ở rất nhiều lĩnh vực khác nhau như kinh tế, văn hoá, giáo dục, khoa học - công nghệ,... Chính vì thế hầu hết các trường Đại học đều chú trọng và mở đào tạo các ngành để phục vụ nhu cầu học và phát triển đất nước cho các thế hệ sau.")

# st.markdown("## Number of subjects over Continents")
# components.html('''<div class='tableauPlaceholder' id='viz1684500200353' style='position: relative'><noscript><a href='#'><img alt='Number of subject over Continent  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet16&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet16' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet16&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684500200353');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=650)
# st.markdown("## Nhận xét:")
# st.markdown("Nhìn chung, ngành Computer Science các năm gần đây đang rất được quan tâm và chú trọng đào tạo rất nhiều bởi các trường Đại học ở tất cả các khu vực và châu lục. Kế đến là Business & Management, các ngành về Sinh học, Hoá học, Toán học, Kinh tế - Tài chính và Ngôn ngữ - Văn học.")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")

# st.markdown("# Quan hệ giữa hai biến")

# st.markdown("## Score Research and Teaching of Top University")
# components.html('''<div class='tableauPlaceholder' id='viz1684494074580' style='position: relative'><noscript><a href='#'><img alt='Score Research and Teaching of Top University ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet4&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet4' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet4&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684494074580');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=650)
# st.markdown("## Nhận xét:")
# st.markdown("-	Nhìn chung trung bình chất lượng giảng dạy (Teaching Scores) các Đại học top đầu thế giới ở phân khúc này không chênh lệch quá nhiều.")
# st.markdown("-	Điểm trung bình các bài nghiên cứu khoa học lại có những chênh lệch giữa top dưới so với top trên. Các Đại học top trên thì không chênh lệch quá nhiều với nhau.")
# st.markdown("-	Columbia University chỉ có 82.03 điểm Nghiên cứu khoa học so với các số điểm hơn 90.0 của các Đại học khác. Peking University cũng chỉ có 77.24 điểm nghiên cứu khoa học, khá thấp so với các trường trong top khác.")

# st.markdown("## Overall Scores and Rank of Viet Nam University")
# components.html('''<div class='tableauPlaceholder' id='viz1684505473797' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1_16844017282960&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book1_16844017282960&#47;Dashboard2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1_16844017282960&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684505473797');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='577px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='577px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=550)
# st.markdown("## Nhận xét:")
# st.markdown("-	Nhìn chung, các trường Đại học khác của Việt Nam đều nằm trong top 1000+, tuy nhiên đến năm 2022, thứ hạng của họ đã tuột xuống 1200+, và năm 2023 gần đây nhất, họ tiếp tục tuột xuống hạng 1500+ và Overall Scores cũng không được tốt.")
# st.markdown("-	Có thể thấy rằng năm 2022 và 2023, sự xuất hiện mới mẻ của Đại học Duy Tân và Đại học Tôn Đức Thắng của Việt Nam với Overall Scores là 44.0 và 44.9 đã giúp họ lọt vào top 500+ Trường Đại học hàng đầu thế giới.")

# st.markdown("## Teaching Scores and Research Scores of Universities Over Years")
# components.html('''<div class='tableauPlaceholder' id='viz1684505507855' style='position: relative'><noscript><a href='#'><img alt='Dashboard 3 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1_16844017282960&#47;Dashboard3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book1_16844017282960&#47;Dashboard3' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1_16844017282960&#47;Dashboard3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684505507855');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='577px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='577px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=550)
# st.markdown("## Nhận xét:")
# st.markdown("-	Nhìn chung điểm trung bình về chất lượng đào tạo qua các năm của các Đại học Việt Nam còn khá thấp so với các trường top đầu, chỉ khoảng từ dưới 14 đến hơn 20 trên thang điểm 100.")
# st.markdown("")
# st.markdown("-	Về các kết quả Nghiên cứu khoa học, các Đại học ở Việt Nam cũng có những số điểm khá thấp, khoảng từ 8 đến 16 trên 100.")
# st.markdown("-	Đại học Quốc gia Hà Nội có điểm trung bình Teaching Scores cao hơn hẳn các Đại học còn lại của Việt Nam (20.6 điểm). Tuy nhiên, điểm các bài Nghiên cứu khoa học lại khá thấp khoảng 9.7.")
# st.markdown("-	Trong khi đó, Đại học Tôn Đức Thắng lại có điểm Research khá cao so với phần còn lại (khoảng 16.0). Tuy nhiên, chất lượng đào tạo của họ lại thấp nhất (khoảng 13.0) trong 6 Đại học của Việt Nam trong danh sách Ranking thế giới.")

# st.markdown("## Research Scores and Citations Scores of Viet Nam Universities")
# components.html('''<div class='tableauPlaceholder' id='viz1684505565273' style='position: relative'><noscript><a href='#'><img alt='Dashboard 4 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1_16844017282960&#47;Dashboard4&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book1_16844017282960&#47;Dashboard4' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1_16844017282960&#47;Dashboard4&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684505565273');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='577px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='577px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=550)
# st.markdown("## Nhận xét:")
# st.markdown("-	Đại học Tôn Đức Thắng và Đại học Duy Tân có Citations Scores rất cao (lần lượt 99.2/100 và 100/100). Cùng với đó là Research Scores của 2 Đại học này (16.0 và 12.6) lại là những con số khá thấp. Điều đó có nghĩa là tuy các kết quả nghiên cứu khoa học của họ không được đánh giá cao nhưng những bài báo nghiên cứu của họ được trích dẫn khá nhiều và có tầm ảnh hưởng khá rộng rãi trên toàn thế giới.")

# st.markdown("## Score Research and Teaching of Top University")
# components.html('''<div class='tableauPlaceholder' id='viz1684494717453' style='position: relative'><noscript><a href='#'><img alt='Score Research and Teaching of Top University ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet4&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet4' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet4&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684494717453');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=750)
# st.markdown("## Nhận xét:")
# st.markdown("-	Nhìn chung trung bình chất lượng giảng dạy (Teaching Scores) các Đại học top đầu thế giới ở phân khúc này không chênh lệch quá nhiều.")
# st.markdown("-	Điểm trung bình các bài nghiên cứu khoa học lại có những chênh lệch giữa top dưới so với top trên. Các Đại học top trên thì không chênh lệch quá nhiều với nhau.")
# st.markdown("-	Columbia University chỉ có 82.03 điểm Nghiên cứu khoa học so với các số điểm hơn 90.0 của các Đại học khác. Peking University cũng chỉ có 77.24 điểm nghiên cứu khoa học, khá thấp so với các trường trong top khác.")

# st.markdown("## Number of University in a country and Stats Pc Intl Student")
# components.html('''<div class='tableauPlaceholder' id='viz1684494243238' style='position: relative'><noscript><a href='#'><img alt='Number of University in a country  and Stats Pc Intl Student  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet5&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet5' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet5&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684494243238');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=700)
# st.markdown("## Nhận xét:")
# st.markdown("-	Nhìn vào hình ảnh ta có thể thấy, United Kingdom, United States và Japan có số lượng Đại học trong top ranking nhiều nhất thế giới. Trong đó United Kingdom có 163 Đại học, United States có 179 và Japan có 152 Đại học.")
# st.markdown("-	Tiếp đến là Russia (103), China (95), India (101) và Turkey (80) cũng có kha khá trường lọt vào danh sách ranking.")

# st.markdown("## Number of Universities and Average Score Overall group by Continent over Year")
# components.html('''<div class='tableauPlaceholder' id='viz1684495560197' style='position: relative'><noscript><a href='#'><img alt='Number of country and avg Score Overall of Continent  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet14&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet14' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet14&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684495560197');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=600)
# st.markdown("## Nhận xét:")
# st.markdown("- Nhìn chung, khu vực châu Âu và Bắc Mỹ có nền giáo dục rất tiên tiến và phát triển khi đóng góp số lượng lớn trường Đại học vào danh sách World Ranking Universities.")
# st.markdown("Ở châu Âu, có hơn 180 trường Đại học có mặt trong danh sách, con số này gấp 3 lần với châu Á khi khu vực này chỉ có hơn 60 trường Đại học nằm trong top đầu thế giới.")
# st.markdown("Ở Bắc Mỹ, khu vực này cũng có hơn 130 trường Đại học trong World Ranking. Tuy nhiên, dù có số lượng trường Đại học được vào top ít hơn so với châu Âu nhưng Average Overall Score của Bắc Mỹ lại cao hơn rất nhiều với số điểm 40.4, gấp đôi so với con số 26.14 của châu Âu. Vậy có thể kết luận rằng, nền giáo dục bậc Đại học ở Bắc Mỹ là tốt nhất thế giới, là mơ ước của hàng triệu sinh viên.")
# st.markdown("Đối lập với Bắc Mỹ, khu vực Nam Mỹ chỉ có 3 trường Đại học trong danh sách và Average Overall Score của họ thuộc hàng thấp nhất thế giới. Bên cạnh đó tuy châu Phi cũng chỉ có 3 trường nhưng Average Overall Score lại cao ngang ngửa so với châu Đại Dương (18.78) và châu Á (18.75) với số điểm là 16.83.")

# st.markdown("## Histogram of Score Industry Income and International Outlook")
# components.html('''<div class='tableauPlaceholder' id='viz1684494899807' style='position: relative'><noscript><a href='#'><img alt='Histogram of Score Industry Income and International Outlook ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet7&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet7' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet7&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684494899807');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=700)
# st.markdown("## Nhận xét:")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")

# st.markdown("## Correlation between Scores Overall and Score Teaching")
# components.html('''<div class='tableauPlaceholder' id='viz1684494957465' style='position: relative'><noscript><a href='#'><img alt='Correlation between Scores Overall and Score Teaching  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet8&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet8' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet8&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684494957465');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=600)
# st.markdown("## Nhận xét:")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")

# st.markdown("# Quan hệ giữa ba biến")

# st.markdown("## Average Number of Male and Female and Ratio between students-staff of some Universities")
# components.html('''<div class='tableauPlaceholder' id='viz1684495053636' style='position: relative'><noscript><a href='#'><img alt='Sheet 6 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet6&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet6' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet6&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684495053636');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=700)
# st.markdown("## Nhận xét:")
# st.markdown("-	Nhìn chung tỉ lệ giữ sinh viên nam và sinh viên nữ ở các Đại học khá đồng đều nhau hoặc chênh nhau không đáng kể.")
# st.markdown("-	Tuy nhiên, tỉ lệ giữa số sinh viên và giảng viên lại có sự khác biệt khá rõ rệt giữa các trường với nhau. Có trường số sinh viên gấp hơn 120 lần so với số giảng viên như University of California, Berkeley. Có trường tỉ lệ giữa sinh viên và giảng viên chỉ là hơn 41 như Yale University.")

# st.markdown("## Correlation between Score Overall and Score Teaching and Score Research")
# components.html('''<div class='tableauPlaceholder' id='viz1684495204347' style='position: relative'><noscript><a href='#'><img alt='Correlation between Score Overall and Score Teaching and Score Research  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet9&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet9' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet9&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684495204347');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=700)
# st.markdown("## Nhận xét:")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")

# st.markdown("## Correlation between Score Overall and Score Industry Income and Score Citations")
# components.html('''<div class='tableauPlaceholder' id='viz1684495250347' style='position: relative'><noscript><a href='#'><img alt='Correlation between Score Overall and Score Industry Income and Score Citations   ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet10&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet10' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet10&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684495250347');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=700)
# st.markdown("## Nhận xét:")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")

# st.markdown("## Correlation between Stats Female and International Student and Student Staff Ratio")
# components.html('''<div class='tableauPlaceholder' id='viz1684495303748' style='position: relative'><noscript><a href='#'><img alt='Correlation between Stats Female and International Student and Student Staff Ratio  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet112&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet112' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet112&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684495303748');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=700)
# st.markdown("## Nhận xét:")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")
# st.markdown("")

# st.markdown("## Number of Students of some Universities In VietNam ")
# components.html('''<div class='tableauPlaceholder' id='viz1684495342804' style='position: relative'><noscript><a href='#'><img alt='Number of Student of University In VietNam  ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet12&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Sheet12' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Sheet12&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684495342804');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1000, height=700)
# st.markdown("## Nhận xét:")
# st.markdown("-	Đại học Quốc gia TP.HCM có số lượng sinh viên trung bình qua các năm khá cao (hơn 69000 sinh viên theo học mỗi năm). Con số này gần gấp đôi Đại học Quốc gia Hà Nội (hơn 32000 sinh viên).")
# st.markdown("-	Đại học Huế cũng là một Đại học được các bạn sinh viên lựa chọn theo học khi lượng sinh viên trung bình mỗi năm vào khoảng hơn 47500.")