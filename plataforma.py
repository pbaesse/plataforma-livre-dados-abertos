from app import create_app, db, cli
from app.models import User, Post, Software, Similar, Comment, Report

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Software': Software,
        'Similar': Similar, 'Comment': Comment, 'Report': Report}
