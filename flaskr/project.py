from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('project', __name__, url_prefix='/project')


@bp.route('/')
def index():
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    return render_template('project/index.html')


@bp.route('/create', methods=['get', 'post'])
def create():
    if request.method == 'post':
        return redirect('/project/aggrement')
    else:
        return render_template('project/create.html')


@bp.route('/aggrement', methods=['get', 'post'])
def aggrement():
    if request.method == 'post':
        return redirect('/project/metadata')
    else:
        return render_template('project/aggrement.html')


@bp.route('/metadata', methods=['get', 'post'])
def metadata():
    return render_template('project/metadata.html')
