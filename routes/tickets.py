from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from extensions import db
from forms.ticket_form import TicketForm
from models.ticket_model import TicketModel
from datetime import datetime

tickets = Blueprint('tickets', __name__) 

@tickets.route('/tickets')
@login_required
def tickets_list():
    if current_user.admin:
        tickets = TicketModel.query.order_by(TicketModel.date_created.desc()).all()
    else:
        tickets = TicketModel.query.filter_by(author=current_user).order_by(TicketModel.date_created.desc()).all()
    return render_template('tickets.html', tickets=tickets)


@tickets.route('/tickets/create', methods=['GET', 'POST'])
@login_required
def create_ticket():
    form = TicketForm()

    if form.validate_on_submit():
            ticket = TicketModel(
                title=form.title.data,
                description=form.description.data,
                priority=form.priority.data,
                author=current_user
            )
            db.session.merge(ticket)
            db.session.commit()
            return redirect(url_for('tickets.tickets_list'))

    return render_template('create.html', form=form)

@tickets.route('/tickets/<int:id>')
@login_required
def view_ticket(id):
    ticket = TicketModel.query.get_or_404(id)
    return render_template('view.html', ticket=ticket)

@tickets.route('/tickets/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_ticket(id):
    ticket = TicketModel.query.get_or_404(id)
    form = TicketForm()

    if form.validate_on_submit():
        ticket.title = form.title.data
        ticket.description = form.description.data
        ticket.priority = form.priority.data
        ticket.updated_at = datetime.now()

        db.session.commit()
        
        return redirect(url_for('tickets.view_ticket', id=id))

    elif request.method == 'GET':
        form.title.data = ticket.title
        form.description.data = ticket.description
        form.priority.data = ticket.priority

    return render_template('edit.html', form=form, ticket=ticket)

@tickets.route('/tickets/<int:id>/delete', methods=['GET'])
@login_required
def delete_ticket(id):
    #Need this so that regular users can't navigate to the delete url manually to delete tickets
    if not current_user.admin:
        return redirect(url_for('tickets.tickets_list'))


    ticket = TicketModel.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    return redirect(url_for('tickets.tickets_list'))