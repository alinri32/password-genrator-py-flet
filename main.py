#import libries (flet for page designe | random for select char for pass | clipboard for copy and paste pass)
import flet as ft
from random import choice
import clipboard

#define global variables
str_lower = "abcdefghijklmnopqrstuvwxyz"
str_upper = str_lower.upper()
str_digit = "01234567890123456789"
str_chars = "~!@#$%^&*_~!@#$%^&*_"

#program is starting here
def main (page: ft.Page):

    
    #buttom password gen logic
    def btn_gen_clicked (e):
        str_pass = ''
        if sw_lower.value:
            str_pass += str_lower
        if sw_upper.value:
            str_pass += str_upper
        if sw_digit.value:
            str_pass += str_digit
        if sw_char.value:
            str_pass += str_chars
        
        try:
            password = ''
            for i in range (int(slider_length.value)):
                password += choice(str_pass)
        except:
            if (sw_lower.value == False) and (sw_upper.value == False) and (sw_digit.value == False) and (sw_char.value == False) :
                password = "یکی از مقادیر را روشن کنید"

        text_pass.value=password
        page.update()
    
    #page size
    page.rtl=True
    page.window.height = 720
    page.window.width = 400

    #make O/F buttom
    sw_lower = ft.Switch(label="حروف الفبای کوچک", value=True)
    sw_upper = ft.Switch(label="حروف الفبای بزرگ", value=False)
    sw_digit = ft.Switch(label="ارقام", value=False)
    sw_char = ft.Switch(label="کاراکتر ویژه", value=False)

    #top show text
    lbl_header = ft.Text(
        value="تولید کننده رمز",
        size=32,
        font_family="b yekan",
        width= page.window.width,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.INDIGO

    )

    #password window
    text_pass = ft.TextField(
        hint_text="پسورد",
        password=True,
        can_reveal_password=True,
        height=60,
        text_align=ft.TextAlign.CENTER,
        text_size=24,
        border_radius=15
    )

    #slider for password length
    lbl_length = ft.Text(value="طول رمز عبور: 8", size=16)
    def slider_changed(e):
        lbl_length.value = f"طول رمز عبور: {int(slider_length.value)}"
        page.update()

    slider_length = ft.Slider(
        min=4,
        max=32,
        value=8,
        divisions=28,
        label="{value}",
        width=360,
        on_change=slider_changed
    )

    #buttom password gen design
    btn_generate = ft.ElevatedButton(
        text="تولید رمز عبور",
        width=360,
        height=60,
        on_click=btn_gen_clicked
    )

    #column design
    col_sw = ft.Column(
        controls=[lbl_header ,lbl_length , slider_length, text_pass , sw_lower , sw_upper , sw_digit , sw_char ,btn_generate],
        height=700,
        spacing=10
    )
    
    page.add(col_sw)
    page.update()

ft.app(target=main)