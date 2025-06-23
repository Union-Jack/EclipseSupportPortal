#Routes were implemented following the Flask-Login documentation and a 'Learn Flask Login' tutorial (Flask-Login, no date)(Neupane, 2021).
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from extensions import db
from forms.ticket_form import TicketForm
from forms.comment_form import CommentForm
from models.ticket_model import TicketModel
from models.comment_model import CommentModel
from models.user_model import UserModel
from datetime import datetime
from flask import flash, abort

#Blueprint for grouping ticket related routes and logic
tickets = Blueprint('tickets', __name__) 

#Route for the homepage
@tickets.route('/homepage')
@login_required
def homepage():
    #Defaults to display 5 tickets on the first page
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    #Admin users see all tickets and standard users only see their own
    if current_user.admin:
        tickets = TicketModel.query.order_by(TicketModel.date_created.desc()).paginate(page=page, per_page=per_page, error_out=False)
    else:
        tickets = TicketModel.query.filter_by(author=current_user).order_by(TicketModel.date_created.desc()).paginate(page=page, per_page=per_page, error_out=False)

    return render_template('homepage.html', tickets=tickets, per_page=per_page)

#Route for the create ticket page
@tickets.route('/tickets/create', methods=['GET', 'POST'])
@login_required
def create_ticket():
    form = TicketForm()

    #The assignee field can take the option for no assignee which needs to be added to the list of admin users 
    if current_user.admin:
        form.assignee.choices = [(0, "")] + [(user.id, user.username) for user in UserModel.query.filter_by(admin=True).all()]
    else:
        form.assignee.choices = [(0, "")]
    
    #Default initial status to open
    form.status.data = "Open"
    
    #If form is valid commit ticket to database
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

    #Validates input errors
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{field.capitalize()}: {error}", "danger") 
    
    return render_template('create.html', form=form)

#Route for the view ticket page
@tickets.route('/tickets/<int:id>')
@login_required
def view_ticket(id):
    ticket = TicketModel.query.get_or_404(id)
    
    #If the user is not an admin and is trying to view a ticket that is not their own present a forbidden error
    if not current_user.admin and ticket.author_id != current_user.id:
        abort(403) 

    form = CommentForm() 
    return render_template('view.html', ticket=ticket, form=form)

#Route for the edit ticket page
@tickets.route('/tickets/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_ticket(id):
    ticket = TicketModel.query.get_or_404(id)

    #If the user is not an admin and is trying to edit a ticket that is not their own present a forbidden error
    if not current_user.admin and ticket.author_id != current_user.id:
        abort(403)

    form = TicketForm()

    #The assignee field can take the option for no assignee which needs to be added to the list of admin users 
    if current_user.admin:
        form.assignee.choices = [(0, "")] + [(user.id, user.username) for user in UserModel.query.filter_by(admin=True).all()]
    else:
        form.assignee.choices = [(0, "")]

    #If form is valid commit edited ticket to database
    if form.validate_on_submit():
        ticket.title = form.title.data
        ticket.description = form.description.data
        ticket.priority = form.priority.data
        ticket.updated_at = datetime.now()

        #Additionaly if the user is an admin commit the admin only fields
        if current_user.admin:
            assignee_id = None if form.assignee.data == 0 else form.assignee.data
            ticket.assignee_id = assignee_id
            ticket.status = form.status.data

        db.session.commit()
        
        return redirect(url_for('tickets.view_ticket', id=id))

    #Gets the ticket's data when loading the page
    elif request.method == 'GET':
        form.title.data = ticket.title
        form.description.data = ticket.description
        form.priority.data = ticket.priority
        if current_user.admin:
            form.assignee.data = ticket.assignee_id

    #Validates input errors
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{field.capitalize()}: {error}", "danger") 

    return render_template('edit.html', form=form, ticket=ticket)

#Route for deleting a ticket
@tickets.route('/tickets/<int:id>/delete', methods=['POST'])
@login_required
def delete_ticket(id):
    ticket = TicketModel.query.get_or_404(id)

    # Prevents non admin from deleting tickets and presents a a forbidden error
    if not current_user.admin:
        abort(403)

    db.session.delete(ticket)
    db.session.commit()
    return redirect(url_for('tickets.homepage'))

#Route for adding a comment
@tickets.route('/tickets/<int:ticket_id>/comment', methods=['POST'])
@login_required
def add_comment(ticket_id):
    ticket = TicketModel.query.get_or_404(ticket_id)
    form = CommentForm()

    #If form is valid commit comment to database
    if form.validate_on_submit():
        comment = CommentModel(
            content=form.content.data,
            author=current_user,
            ticket=ticket
        )
        db.session.add(comment)
        db.session.commit()
    
    return redirect(url_for('tickets.view_ticket', id=ticket_id))

#Route for the edit comment page
@tickets.route('/tickets/<int:ticket_id>/comments/<int:comment_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_comment(ticket_id, comment_id):
    comment = CommentModel.query.get_or_404(comment_id)
    
    #If the user is not the user who created the comment present a forbidden error
    if comment.author_id != current_user.id:
        abort(403)

    form = CommentForm(obj=comment)

    #If form is valid edited commit comment to database
    if form.validate_on_submit():
        comment.content = form.content.data
        comment.date_updated = datetime.now() 
        db.session.commit()
        return redirect(url_for('tickets.view_ticket', id=ticket_id))

    return render_template('edit_comment.html', form=form, ticket_id=ticket_id, comment=comment)
