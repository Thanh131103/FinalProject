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

components.html('''<div class='tableauPlaceholder' id='viz1684509542012' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16844937289010&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16844937289010&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684509542012');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1200px';vizElement.style.height='1087px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1200px';vizElement.style.height='1087px';} else { vizElement.style.width='100%';vizElement.style.height='1277px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>''', width=1200, height=1060)