from flask import render_template, url_for, redirect, request, flash, Blueprint
from flask_login import login_required, current_user

from puppy_company_blog import db
from puppy_company_blog.models import BlogPost
from puppy_company_blog.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)

# View for creating a blog post.
@blog_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():

    form = BlogPostForm()

    if form.validate_on_submit():

        blog_post = BlogPost(title=form.title.data, text=form.text.data, user_id=current_user.id)

        db.session.add(blog_post)
        db.session.commit()
        flash('Blog post created')
        return redirect(url_for('core.index'))
    
    return render_template('create_post.html', form=form)

# View for reading blog post.
# Login not required.
# We use an id to the views so that url stays unique.
# we use int: in <int: blog_post_id> to cast it as an integer.
@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    return render_template('blog_post.html', title=blog_post.title, date=blog_post.date, post=blog_post)

# Update to blog post

@blog_posts.route('/<int:blog_post_id>/update', methods=['GET', 'POST'])
@login_required
def update(blog_post_id):

    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    form = BlogPostForm()

    if form.validate_on_submit():

        blog_post.title = form.title.data
        blog_post.text = form.text.data

        # We don't need to add, because we just changed the post.
        db.session.commit()
        flash('Blog post updated')
        return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))

    # When the user opens the blog post page to edit, the title and text should be filed with existing details and not empty.

    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text

    return render_template('create_post.html', title='Updating', form=form)

# delete blog post.

@blog_posts.route('/<int:blog_post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(blog_post_id):

    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog post deleted')

    return render_template(url_for('core.index'))