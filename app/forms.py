from flask_wtf import FlaskForm
import wtforms as wf

from . import app
from .models import Category


def get_categories():
    with app.app_context():
        categories = Category.query.all()
        choices = []
        for category in categories:
            choices.append((category.id, category.name))
        return choices

class CategoryForm(FlaskForm):
    name = wf.StringField(label="Категории")
    code = wf.StringField(label="ивентраный код", validators=[
        wf.validators.Length(min=4, max=4)
    ])


class ItemForm(FlaskForm):
    name = wf.StringField(label="Инвентарь")
    code_end = wf.StringField(label="ивентраный код кончания", validators=[
        wf.validators.Length(min=4, max=4)
    ])
    summ = wf.IntegerField(label='Остаточная стоимость')
    category_id = wf.SelectField(label='категори9', choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category_id.choices = get_categories()


class UserForm(FlaskForm):
    username = wf.StringField(label="Логин пользователя", validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=8, max=24)
    ])
    password = wf.PasswordField(label="Пароль", validators=[
        wf.validators.DataRequired()
    ])

    def validate_password(self, field):
        if field.data.isdigit() or field.data.isalpha():
            raise wf.validators.ValidationError('Пароль должен быть с числами и буквами')