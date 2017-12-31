from robsite import * 


@app.route('/')
def home():
    articles = Article.query.all()
    return render_template('home.html', articles=articles)


@app.route('/view/<a_id>')
def view(a_id):
    a = Article.query.get(a_id)
    return render_template('view.html', a=a)

@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')

@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/admin/')
def admin():
    return render_template('admin_home.html')

@app.route('/admin/articles/')
def admin_articles():
    articles = Article.query.all()
    return render_template('admin_articles.html', articles=articles)


@app.route('/admin/articles/add/')
def admin_articles_add():

    return render_template('admin_articles_add.html')


@app.route('/add/', methods=['GET', 'POST'])
def add():
    title = request.form['title']
    body = request.form['body']
    date = datetime.now()
    
    article = Article(title, date, body)
    db.session.add(article)
    db.session.flush()
    db.session.commit()
    
    return redirect(url_for('admin_articles'))


@app.route('/delete/<a_id>', methods=['GET', 'POST'])
def delete(a_id):
    a = Article.query.get(a_id)
    db.session.delete(a)
    db.session.flush()
    db.session.commit()
    
    
    return redirect(url_for('admin_articles'))

@app.route('/admin/articles/edit/<a_id>', methods=['GET', 'POST'])
def admin_edit(a_id):
    a = Article.query.get(a_id)
    return render_template('admin_articles_edit.html', a=a)


@app.route('/edit/<a_id>', methods=['GET', 'POST'])
def edit(a_id):
    a = Article.query.get(a_id)
    title = request.form['title']
    body = request.form['body']
    
    a.article = title
    a.body = body
    
    
    db.session.commit()
    
    return redirect(url_for('admin_articles'))
    
    