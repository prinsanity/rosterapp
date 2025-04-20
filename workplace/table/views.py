from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Table
import json
from bs4 import BeautifulSoup

# Helper function to determine the user's role
def get_user_role(user):
    if user.username.startswith('P'):
        return 'Planning'
    elif user.username.startswith('E'):
        return 'Editor'
    elif user.username.startswith('V'):
        return 'Viewer'
    return 'Unknown'

# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard view
@login_required
def dashboard(request):
    role = get_user_role(request.user)

    if role == 'Planning':
        # Show all tables owned by the Planning user
        tables = Table.objects.filter(owner=request.user)
    elif role == 'Editor':
        # Show all tables no matter their status (created by Planning)
        tables = Table.objects.all()
    elif role == 'Viewer':
        # Show all tables only in the 'viewing' status
        tables = Table.objects.all()
    else:
        tables = []

    return render(request, 'dashboard.html', {'tables': tables, 'role': role})
# Create table view
@login_required
def create_table(request):
    if get_user_role(request.user) != 'Planning':
        return redirect('dashboard')

    if request.method == 'POST':
        table_name = request.POST.get('name', '').strip()
        rows = int(request.POST.get('rows', 0))
        columns = int(request.POST.get('columns', 0))

        if table_name and rows > 0 and columns > 0:
            # Initialize table data with empty cells
            table_data = [["" for _ in range(columns)] for _ in range(rows)]
            Table.objects.create(name=table_name, owner=request.user, data=json.dumps(table_data))
            return redirect('dashboard')
        else:
            return render(request, 'create_table.html', {
                'error': 'Table name, rows, and columns must all be valid and greater than zero.'
            })

    return render(request, 'create_table.html')

# Edit table view
@login_required
def edit_table(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    role = get_user_role(request.user)

    # Parse JSON data to a Python list
    try:
        table_data = json.loads(table.data)  # Deserialize JSON
    except json.JSONDecodeError:
        table_data = []

    if role == 'Planning' and table.owner != request.user:
        return redirect('dashboard')
    if role == 'Editor' and table.status not in ['editing', 'viewing']:
        return redirect('dashboard')
    if role == 'Viewer' and table.status != 'viewing':
        return redirect('dashboard')

    if request.method == 'POST':
        table_data = request.POST.get('data')
        if table_data:
            try:
                cleaned_data = json.loads(table_data)  # Validate JSON data
                table.data = json.dumps(cleaned_data)
                table.save()
            except json.JSONDecodeError:
                return render(request, 'edit_table.html', {
                    'table': table,
                    'role': role,
                    'error': 'Invalid table data format.',
                })
            
        if 'exit' in request.POST:
            table.status = 'editing'
            table.save()
            return redirect('dashboard')
        
        if role == 'Planning' and 'send_to_editor' in request.POST:
            table.status = 'editing'
            table.save()
            return redirect('edit_table', table.id)
        
        if role == 'Editor' and 'send_to_viewer' in request.POST:
            table.status = 'viewing'
            table.save()
            return redirect('edit_table', table.id)

        # Save table data when editing

    return render(request, 'edit_table.html', {
        'table': table,
        'role': role,
        'table_data': table_data  # Pass parsed data to template
    })

# View table view (Viewer role only)
@login_required
def view_table(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    role = get_user_role(request.user)

    # Parse JSON data to a Python list
    try:
        table_data = json.loads(table.data)  # Deserialize JSON
    except json.JSONDecodeError:
        table_data = []

    return render(request, 'view_table.html', {
        'table': table,
        'role': role,
        'table_data': table_data  # Pass parsed data to template
    })

# Delete table view (Planning role only)
@login_required
def delete_table(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    if get_user_role(request.user) != 'Planning' or table.owner != request.user:
        return redirect('dashboard')

    if request.method == 'POST':
        table.delete()
        return redirect('dashboard')

    return render(request, 'delete_table.html', {'table': table})
