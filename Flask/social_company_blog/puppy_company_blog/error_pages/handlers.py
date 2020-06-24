from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

# This is not a typical view, we use app_errorhandler instead of route.
# Google for other errors.
@error_pages.app_errorhandler(404)
def error_404(error):
    # We are returning a tuple here.
    return render_template('error_pages/404.html'), 404

@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html'), 403