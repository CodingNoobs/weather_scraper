# Import Flask-WTF specific classes.
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# Create the form for a generic Book. Chicago style footnote or endnote.
class BookForm(FlaskForm):
    first_name = StringField('First name')
    last_name = StringField('Last name')
    book_title = StringField('Book title')
    place_of_publication = StringField('Place of publication')
    publisher = StringField('Publisher')
    year_published = StringField('Year published')
    page_number = StringField('Page number')
