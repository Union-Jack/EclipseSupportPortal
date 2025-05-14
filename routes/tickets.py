from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from EclipseSupportPortal.forms.ticket_form import TicketForm

tickets = Blueprint('tickets', __name__) 

@tickets.route('/tickets/create', methods=['GET', 'POST'])
@login_required
def create_ticket():
    form = TicketForm()
    return render_template('create.html', form=form)