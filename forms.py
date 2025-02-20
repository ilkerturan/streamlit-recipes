import streamlit as st


def start():
    st.set_page_config(page_title='Streamlit Forms', page_icon='random')
    st.title('Streamlit Forms')
    st.write(
        'Formlar, bir dizi girdi alanı ve bir dizi düğme içerir. Formlar, kullanıcıdan veri almak için kullanılır.')
    st.divider()
    # Form: with bloğu ile birlikte bir takım girdi alanları ve düğmeler tek bir form içerisinde toplanır.
    with st.form(key='my_form'):
        # TextInput: Kullanıcıdan metin girişi almak için kullanılır.
        name = st.text_input(label='Adınız')

        # NumberInput: Kullanıcıdan sayısal giriş almak için kullanılır.
        age = st.number_input(label='Yaşınız', min_value=0, max_value=100)

        # DateInput: Kullanıcıdan tarih girişi almak için kullanılır.
        date = st.date_input(label='Doğum Tarihiniz')

        # Checkbox: Kullanıcıdan çoklu seçim yapmasını sağlar.
        sigara = st.checkbox(label='Sigara içiyor musunuz?')
        alkol = st.checkbox(label='Alkol tüketiyor musunuz?')

        # Radio: Kullanıcıdan tek seçim yapmasını sağlar.
        gender = st.radio(label='Cinsiyetiniz', options=['Erkek', 'Kadın'])

        # Submit Button: Formun gönderilmesini sağlar.
        submitted = st.form_submit_button(label='Gönder')

        if submitted:
            st.write(f'Merhaba {name}! Yaşınız {age}. Doğum tarihiniz {date}.')

    st.divider()
    # Selectbox: Kullanıcıya bir seçenek listesi sunar.
    country = st.selectbox(label='Ülkenizi seçin', options=['Türkiye', 'Amerika', 'Almanya', 'Fransa'])

    # Multiselect: Kullanıcıya çoklu seçenek listesi sunar.
    cities = st.multiselect(label='Şehirlerinizi seçin', options=['İstanbul', 'Ankara', 'İzmir', 'Antalya'])

if __name__ == '__main__':
    start()
