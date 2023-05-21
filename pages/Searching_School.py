import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components


# Introduction

st.set_page_config(page_title='Searching Schools')
st.write("SEARCHING SCHOOLS")

components.html('''<div class='tableauPlaceholder' id='viz1684655964036' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16843000630040&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz' style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='School_16843000630040&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sc&#47;School_16843000630040&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div> <script type='text/javascript'> var divElement = document.getElementById('viz1684655964036'); var vizElement = divElement.getElementsByTagName('object')[0]; if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1450px';vizElement.style.width='100%';vizElement.style.minHeight='1087px';vizElement.style.maxHeight='2187px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1450px';vizElement.style.width='100%';vizElement.style.minHeight='1087px';vizElement.style.maxHeight='2187px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1277px';} var scriptElement = document.createElement('script'); scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement); </script>''', width=1200, height=1060)




st.markdown('''
### Rút ra giải pháp
Từ phần phân tích dữ liệu, có thể thấy overall score của một trường phụ thuộc nhiều nhiều vào Score Research, Score Teaching
Score Citations. Overall score ít phụ thuộc vào tỉ lệ nam nữ, số lượng sinh viên, tỉ lệ sinh viên nước ngoài và tỉ lệ sinh viên trên nhân viên.
Do đó muốn nâng cao overall score cần phải tập trung nâng cao chất lượng dạy học, tăng cường hoạt động nghiên cứu và sáng tạo cũng như 
có các công bố khoa học trên các tạp chí và hội nghị quốc tế. 

Ngoài ra teaching scores và research scores có quan hệ  tương quan dương với nhau biểu thị việc giảng dạy đi đôi với việc nghiên cứu khoa học. 
''')

img = Image.open('images/vnm.jpg')
st.image(img, use_column_width=True)

st.markdown('''
Các trường đại học có thể bị loại khỏi Bảng xếp hạng THE nếu không đào tạo cử nhân, hoặc nếu số nghiên cứu của trường đó đạt ít hơn 1.000 bài báo khoa học từ năm 2014 đến 2018 (với tối thiểu 150 bài/năm). 
Các trường đại học cũng sẽ bị loại nếu từ 80% nghiên cứu trở lên chỉ thuộc về một trong 11 lĩnh vực chủ đề của THE.

Từ các biểu đồ có thể thấy Việt Nam có các chỉ số về teaching scores, research, citations thấp, dưới 50 điểm. 
Do đó cần tập trung tăng cường việc dạy học và nghiên cứu để có điểm và thứ hạng cao hơn. 
Đồng thời số lượng trường còn thấp nên cần cải thiện thông qua các biện pháp sau:

- Tăng cường đầu tư vào giáo dục: Chính phủ cần tăng cường nguồn lực và nguồn vốn cho giáo dục, đặc biệt là cho các trường đại học. Điều này có thể bao gồm cung cấp nguồn lực vật chất, cơ sở hạ tầng và trang thiết bị hiện đại để tạo điều kiện tốt nhất cho giảng dạy và nghiên cứu.

- Thúc đẩy hoạt động nghiên cứu và phát triển: Các trường đại học cần khuyến khích giảng viên và sinh viên tham gia vào hoạt động nghiên cứu và sáng tạo. Điều này có thể được thực hiện thông qua việc cung cấp tài trợ và hỗ trợ cho các dự án nghiên cứu, tổ chức hội thảo và hội nghị khoa học, và tạo ra môi trường động lực để khuyến khích sáng tạo và đổi mới.

- Xây dựng mạng lưới hợp tác quốc tế: Các trường đại học cần tăng cường quan hệ hợp tác với các trường đại học và viện nghiên cứu quốc tế. Việc hợp tác này có thể bao gồm trao đổi giảng viên và sinh viên, chia sẻ tài liệu và công trình nghiên cứu, và thực hiện các dự án chung. Điều này sẽ giúp mở rộng phạm vi nghiên cứu và tiếp cận nguồn lực và kiến thức quốc tế.

- Đánh giá chất lượng: Hệ thống đánh giá chất lượng giáo dục và nghiên cứu cần được tăng cường và thực hiện một cách công bằng và minh bạch. Điều này giúp tạo động lực cho các trường đại học cải thiện chất lượng dạy học và nghiên cứu, đồng thời cung cấp thông tin đáng tin cậy để phụ huynh và sinh viên có thể lựa chọn trường phù hợp với mình.

- Thu hút nhân tài và đào tạo giảng viên: Các trường đại học cần đầu tư vào đào tạo và phát triển giảng viên để nâng cao năng lực giảng dạy và nghiên cứu. Điều này có thể bao gồm chương trình đào tạo chuyên sâu, khuyến khích tham gia vào các khóa học và hội thảo, và tạo điều kiện để giảng viên phát triển sự nghiệp trong lĩnh vực của mình.
''')