from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas 

popular_books = pickle.load(open('popularbooks.pkl', 'rb'))
# pt = pickle.load(open('pt.pkl', 'rb'))
pt = pandas.read_pickle('pt.pkl')
# books = pickle.load(open('books.pkl', 'rb'))
books = pandas.read_pickle('books.pkl')
similarity_score = pickle.load(open('similarity_score.pkl','rb'))

app = Flask(__name__, template_folder='templates', static_folder='templates')


@app.route('/')

def index():
    return render_template('interface.html', section='hero')

@app.route('/recommend')

def recommend():
    return render_template('interface.html', section='recommend')

@app.route('/recommend_books', methods=['POST'])

def recommender():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_books = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []

    for bk in similar_books:
        book_items = []
        temp_df = books[books["Book-Title"] == pt.index[bk[0]]]
        book_items.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Title"].values))
        book_items.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Author"].values))
        book_items.extend(list(temp_df.drop_duplicates("Book-Title")["Image-URL-M"].values))

        data.append(book_items)
    
    print(data)

    return render_template('interface.html', section='recommender', data=data)

@app.route('/books')

def trending_book():
    return render_template('interface.html', section='books')

@app.route('/contact')

def contact():
    return render_template('interface.html', section='contact')

if __name__ == '__main__':
    app.run(debug=True)