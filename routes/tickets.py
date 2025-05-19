from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from extensions import db
from forms.ticket_form import TicketForm
from models.ticket_model import TicketModel


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
    
    return render_template('create.html', form=form)

@tickets.route('/tickets/<int:id>')
@login_required
def view_ticket(id):
    ticket = TicketModel.query.get_or_404(id)
    return render_template('view.html', ticket=ticket)
