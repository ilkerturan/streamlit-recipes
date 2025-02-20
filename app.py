import streamlit as st


def start():
    st.set_page_config(page_title="Streamlit App", page_icon=":shark:", layout="centered")
    st.title("Streamlit App Title")
    st.header("App Section Header")
    st.subheader("App Section SubHeader")

    st.write(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tincidunt non erat in efficitur. Sed blandit porta urna, sed gravida nulla consequat non. Maecenas lobortis, sapien eleifend pretium hendrerit, nisi metus ullamcorper erat, sit amet auctor neque orci eget dolor. Cras id ultricies ipsum, et pellentesque ipsum. Etiam aliquet nisi vulputate, condimentum orci a, viverra purus. Pellentesque feugiat libero at elementum facilisis. Cras elit neque, porttitor at neque blandit, mollis vehicula libero. In eu tellus vitae enim ultrices elementum placerat et augue.")

    st.text(
        "Praesent varius ipsum at quam fringilla malesuada. Nam efficitur erat urna, sit amet lobortis metus dictum et. Duis nec elit nisl. Duis placerat massa a ligula dapibus, vel porttitor leo aliquam. Praesent ut finibus eros, ac sagittis tellus. Sed metus nibh, dapibus mollis dapibus eget, facilisis eget justo. Proin ac convallis elit. Aliquam sollicitudin, ligula nec porta faucibus, libero eros mattis augue, eu efficitur mi dui non velit. Morbi eget fermentum nibh, vitae elementum tortor. Nunc porta at neque porta tristique. Suspendisse eu venenatis elit, dictum tincidunt nunc. Curabitur finibus lectus nec elit venenatis lacinia. Pellentesque vehicula metus in est pulvinar tempus. Nulla eleifend dapibus hendrerit. Pellentesque iaculis vitae metus non vehicula.")

    st.markdown("## Markdown Section Header")
    st.divider()
    sayilar = [1, 2, 3, 4, 5]
    st.write(sayilar)
    st.text(sayilar)
    kisi = {"ad": "Ahmet", "soyad": "Mehmet", "yas": 25}
    st.write(kisi)
    st.text(kisi)
    st.divider()
    st.markdown("### Forms:")
    # Text Input
    name = st.text_input("Enter Your Name:")
    st.write(f"Name: {name}")

    paragraph = st.text_area("Enter Your Paragraph:")
    st.write(f"Paragraph: {paragraph}")

    code = '''def hello(): 
    print("Hello, World!")'''
    st.code(code, language="python")

    json_data = {"name": "Ahmet", "surname": "Mehmet", "age": 25}
    st.json(json_data)


if __name__ == '__main__':
    start()
