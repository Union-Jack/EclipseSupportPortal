from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from EclipseSupportPortal import db
from EclipseSupportPortal.forms.ticket_form import TicketForm
from EclipseSupportPortal.models.ticket_model import TicketModel


tickets = Blueprint('tickets', __name__) 

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