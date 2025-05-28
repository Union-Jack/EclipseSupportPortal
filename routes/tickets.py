from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from extensions import db
from forms.ticket_form import TicketForm
from forms.comment_form import CommentForm
from models.ticket_model import TicketModel
from models.comment_model import CommentModel
from models.user_model import UserModel
from datetime import datetime

tickets = Blueprint('tickets', __name__) 

@tickets.route('/homepage')
@login_required
def homepage():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    if current_user.admin:
        tickets = TicketModel.query.order_by(TicketModel.date_created.desc()).paginate(page=page, per_page=per_page, error_out=False)
    else:
        tickets = TicketModel.query.filter_by(author=current_user).order_by(TicketModel.date_created.desc()).paginate(page=page, per_page=per_page, error_out=False)

    return render_template('homepage.html', tickets=tickets, per_page=per_page)


@tickets.route('/tickets/create', methods=['GET', 'POST'])
@login_required
def create_ticket():
    form = TicketForm()

    if current_user.admin:
        form.assignee.choices = [(0, "")] + [(user.id, user.username) for user in UserModel.query.filter_by(admin=True).all()]
    else:
        form.assignee.choices = [(0, "")]
    
    form.status.data = "Open"
    
    if form.validate_on_submit():
        assignee_id = None if form.assignee.data == 0 else form.assignee.data
        ticket = TicketModel(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            status=form.status.data,
            author_id=current_user.id,
            assignee_id=assignee_id
        )
        db.session.add(ticket)
        db.session.commit()

        return redirect(url_for('tickets.homepage'))

    else: 
        print(form.errors)

    return render_template('create.html', form=form)

@tickets.route('/tickets/<int:id>')
@login_required
def view_ticket(id):
    ticket = TicketModel.query.get_or_404(id)
    form = CommentForm() 
    return render_template('view.html', ticket=ticket, form=form)

@tickets.route('/tickets/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_ticket(id):
    ticket = TicketModel.query.get_or_404(id)
    form = TicketForm()

    if current_user.admin:
        form.assignee.choices = [(0, "")] + [(user.id, user.username) for user in UserModel.query.filter_by(admin=True).all()]
    else:
        form.assignee.choices = [(0, "")]

    if form.validate_on_submit():
        ticket.title = form.title.data
        ticket.description = form.description.data
        ticket.priority = form.priority.data
        ticket.updated_at = datetime.now()

        if current_user.admin:
            assignee_id = None if form.assignee.data == 0 else form.assignee.data
            ticket.assignee_id = assignee_id
            ticket.status = form.status.data

        db.session.commit()
        
        return redirect(url_for('tickets.view_ticket', id=id))

    elif request.method == 'GET':
        form.title.data = ticket.title
        form.description.data = ticket.description
        form.priority.data = ticket.priority
        if current_user.admin:
            form.assignee.data = ticket.assignee_id

    return render_template('edit.html', form=form, ticket=ticket)

@tickets.route('/tickets/<int:id>/delete', methods=['GET'])
@login_required
def delete_ticket(id):
    #Need this so that regular users can't navigate to the delete url manually to delete tickets
    if not current_user.admin:
        return redirect(url_for('tickets.homepage'))


    ticket = TicketModel.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    return redirect(url_for('tickets.homepage'))

@tickets.route('/tickets/<int:ticket_id>/comment', methods=['POST'])
@login_required
def add_comment(ticket_id):
    ticket = TicketModel.query.get_or_404(ticket_id)
    form = CommentForm()
    
    if form.validate_on_submit():
        comment = CommentModel(
            content=form.content.data,
            author=current_user,
            ticket=ticket
        )
        db.session.add(comment)
        db.session.commit()
    
    return redirect(url_for('tickets.view_ticket', id=ticket_id))

@tickets.route('/tickets/<int:ticket_id>/comments/<int:comment_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_comment(ticket_id, comment_id):
    comment = CommentModel.query.get_or_404(comment_id)
    
    if comment.author != current_user:
        flash("You can only edit your own comments.", "danger")
        return redirect(url_for('tickets.view_ticket', id=ticket_id))

    form = CommentForm(obj=comment)

    if form.validate_on_submit():
        comment.content = form.content.data
        comment.date_updated = datetime.now() 
        db.session.commit()
        return redirect(url_for('tickets.view_ticket', id=ticket_id))

    return render_template('edit_comment.html', form=form, ticket_id=ticket_id, comment=comment)
