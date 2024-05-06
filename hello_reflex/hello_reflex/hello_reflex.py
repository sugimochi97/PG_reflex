import reflex as rx

class Stats(rx.State):
    number: float
    password: str
    number_text:str
    password_text: str
    
    def push_texts(self):
        self.number_text = f"1.2 + 0.5 = {self.number}" if self.number else ""
        self.passrowd_text = f"パスワードは{self.password}" if self.password else ""
        
def index():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.form_control(
                    rx.form("1.2 + 0.5 ="),
                    rx.input(on_change=rx.State.set_number, placeholder="計算結果を入力",type="float",is_required=True),
                ),
                rx.form_control(
                    rx.form_label("パスワード入れてね"),
                    rx.input(on_change=rx.State.set_number,placeholder="計算結果を入力",type="float",is_required=True),
                ),
                rx.form_control(
                    rx.form_label("パスワード入れてね"),
                    rx.password(on_change=rx.State.set_password),
                    rx.form_helper_text("助言は役に立たない"),
                ),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=rx.State.put_texts,
        ),
        rx.divider(),
        rx.text(rx.State.number_text),
        rx.text(rx.State.password_text),
    )

app = rx.App(state=Stats)
app.add_page(index)
app.compile()