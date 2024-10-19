from flaskblog import app,db

if __name__ == '__main__':
    app.run(debug=True)
    
    # python
    #from flaskblog import app, db
    #from flaskblog.models import User, Post

'''with app.app_context():                                         
...     db.create_all()
...     print("Database created successfully!")'''

'''with app.app_context():
...     user = User(username='testuser', email='testuser@example.com', password='password')
...     db.session.add(user)
...     db.session.commit()
...     print("User created successfully!")'''

''' with app.app_context():
...     user = User.query.first()  # Get the first user you created
...     post = Post(title='My First Post', content='This is the content of my first post.', author=user)
...     db.session.add(post)
...     db.session.commit()
...     print("Post created successfully!")'''

'''from flaskblog import app, db
>>> from flaskblog.models import User, Post
>>> with app.app_context():
...     users = User.query.all()  # Get all users
...     for user in users:
...         print(f'Username: {user.username}, Email: {user.email}')'''
#inga irundu copy paste terminal le pannuna it will give indentation error so paste this in chatgpt or doc and then use it in temrinal