# Import Flask specific classes.
from flask import Flask, render_template, redirect, url_for, session

# Import application specific classes.
from forms import BookForm

# Create Flask app.
app = Flask(__name__)

# Set secret key. This is used for CSRF protection and is needed for Flask WTF 
# to work.
app.secret_key = 'Thisisasupersecretkey'

# The index (home) route.
@app.route("/")
def index():
    return render_template('index.html')

# The Book route.
@app.route("/book", methods=('GET', 'POST'))
def book():
    # Set the form for this route to the BookForm
    form = BookForm()

    # Check if BookForm is validated:
    if form.validate_on_submit():
        # Save the entered form data to Flask's session
        # variable. This will persist the data between requests.
        session['first_name'] = form.first_name.data
        session['last_name'] = form.last_name.data
        session['book_title'] = form.book_title.data
        session['place_of_publication'] = form.place_of_publication.data
        session['publisher'] = form.publisher.data
        session['year_published'] = form.year_published.data
        session['page_number'] = form.page_number.data

        # Once saved, reset the form field to blank.
        form.first_name.data = ''
        form.last_name.data = ''
        form.book_title.data = ''
        form.place_of_publication.data = ''
        form.publisher.data = ''
        form.year_published.data = ''
        form.page_number.data = ''

        # Redirect to the same page to prevent a page
        # refresh resending the form.
        return redirect(url_for('result'))
        
    # If the form is not submitted, render this:
    return render_template("book.html", form=form)

# A route to display the result of what was submitted from the BookForm.
@app.route('/result')
def result():
    # Pass the session variables in to the result.html template.
    return render_template("result.html",
                            first_name=session['first_name'],
                            last_name=session['last_name'],
                            book_title=session['book_title'],
                            place_of_publication=session['place_of_publication'],
                            publisher=session['publisher'],
                            year_published=session['year_published'],
                            page_number=session['page_number'])    

# Check if the Python file being run is equal to the python file the Flask
# app is defined in (this file).
if __name__ == "__main__":
    # Run the Flask app.
    app.run()