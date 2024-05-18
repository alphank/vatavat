from flask import Blueprint, session, render_template, current_app
from app.helpers import admin_login_required
from app.models.admin import User
from icecream import ic

bp_admin = Blueprint("bp_admin", __name__)


# Home page
@bp_admin.route("/admin", methods=["GET"])
@admin_login_required
def admin_home():

    user_results = User.query.filter(User.deletedat == None).order_by(User.id).all()
    users = []
    for result in user_results:
        ic(result)
        user = {}
        user['user_id'] = getattr(result, 'id')

        for attr in User.Attrs:
            if getattr(result, attr):
                user[attr] = getattr(result, attr)

        roles = user['role'].split(",")
        roles = [int(i) for i in roles]

        rolesStr = User.Role(roles[0]).name
        for idx in range(1, len(roles)):
            rolesStr += ", " + User.Role(roles[idx]).name
        user['role'] = rolesStr

        users.append(user)

    roles = []
    for e in User.Role:
        roles.append({
            'name': e.name,
            'value': e.value
        })

    adminhomeinfo = {
        'session': session,
        'users': users,
        'numUsers': len(users),
        'roles': roles,
        'numRoles': len(roles),
        'showTestPanel': current_app.config['SHOW_TEST_PANEL'],
    }

    return render_template("admin_home.html", adminhomeinfo=adminhomeinfo)
