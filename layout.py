import streamlit as st


def start():
    st.set_page_config(page_title='Streamlit Layout', page_icon='random', layout='wide')
    st.title('Streamlit Layout')
    st.write('Streamlit, sayfa düzenini oluşturmak için bir dizi yerleşim yöntemi sunar.')
    st.divider()
    # Columns: Sayfayı sütunlara bölmek için kullanılır.
    col1, col2 = st.columns((1, 2))
    with col1:
        st.subheader('Sol sütun')
        st.image('https://picsum.photos/800/450?random=1', caption='Random Image 1', use_container_width=True)
    with col2:
        st.subheader('Sağ sütun')
        data = {
            'Name': ['John', 'Jane', 'Doe'],
            'Age': [25, 30, 35],
            'City': ['New York', 'Los Angeles', 'Chicago']
        }
        st.table(data)
    st.subheader('Resim Galerisi')
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.image('https://picsum.photos/800/450?random=2', caption='Random Image 2', use_container_width=True)
    with c2:
        st.image('https://picsum.photos/800/450?random=3', caption='Random Image 3', use_container_width=True)
    with c3:
        st.image('https://picsum.photos/800/450?random=4', caption='Random Image 4', use_container_width=True)
    with c4:
        st.image('https://picsum.photos/800/450?random=5', caption='Random Image 5', use_container_width=True)
    with c5:
        st.image('https://picsum.photos/800/450?random=6', caption='Random Image 6', use_container_width=True)

if __name__ == '__main__':
    start()
