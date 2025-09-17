from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.views.auth import bp
from app.models.user import User
from app.extensions import db
from datetime import datetime

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            # Update last login
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for('user.dashboard'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('auth/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Contact Information
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        company = request.form.get('company')
        telephone = request.form.get('telephone')
        
        # Subscription Information
        account_type = request.form.get('account_type')
        monthly_news = request.form.get('monthly_news')
        search_access = request.form.get('search_access')
        database_access = request.form.get('database_access')
        
        # Login Information
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return render_template('auth/register.html')
            
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
            return render_template('auth/register.html')
            
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('auth/register.html')
        
        # Create user
        user = User(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            company=company,
            telephone=telephone,
            account_type=account_type,
            subscription_status='pending'  # Will be activated after payment
        )
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please check your email for account activation.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'error')
            return render_template('auth/register.html')
    
    return render_template('auth/register.html')

@bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            # TODO: Implement password reset email logic
            # For now, just show success message
            flash('Password reset instructions have been sent to your email address. Please check your inbox and follow the instructions to reset your password.', 'success')
        else:
            flash('If an account with this email exists, you will receive password reset instructions.', 'info')
        return redirect(url_for('auth.login'))
    return render_template('auth/forgot_password.html')

@bp.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    # TODO: Implement token verification and password reset
    if request.method == 'POST':
        new_password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if new_password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('auth/reset_password.html', token=token)
        
        # TODO: Update user password with token verification
        flash('Your password has been reset successfully', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/reset_password.html', token=token)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))


# from flask import render_template, redirect, url_for, flash, request
# from flask_login import login_user, logout_user, login_required, current_user
# from app.views.auth import bp
# from app.models.user import User
# from app.extensions import db

# @bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
#         user = User.query.filter_by(email=email).first()
        
#         if user and user.check_password(password):
#             login_user(user)
#             next_page = request.args.get('next')
#             if next_page:
#                 return redirect(next_page)
#             return redirect(url_for('user.dashboard'))
#         else:
#             flash('Invalid email or password', 'error')
    
#     return render_template('auth/login.html')

# @bp.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # Contact Information
#         first_name = request.form.get('first_name')
#         last_name = request.form.get('last_name')
#         email = request.form.get('email')
#         company = request.form.get('company')
#         telephone = request.form.get('telephone')
        
#         # Subscription Information
#         account_type = request.form.get('account_type')
#         monthly_news = request.form.get('monthly_news')
#         search_access = request.form.get('search_access')
#         database_access = request.form.get('database_access')
        
#         # Login Information
#         username = request.form.get('username')
#         password = request.form.get('password')
#         confirm_password = request.form.get('confirm_password')
        
#         # Validation
#         if User.query.filter_by(email=email).first():
#             flash('Email already registered', 'error')
#             return render_template('auth/register.html')
            
#         if User.query.filter_by(username=username).first():
#             flash('Username already taken', 'error')
#             return render_template('auth/register.html')
            
#         if password != confirm_password:
#             flash('Passwords do not match', 'error')
#             return render_template('auth/register.html')
        
#         # Create user
#         user = User(
#             email=email,
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             company=company,
#             telephone=telephone,
#             account_type=account_type,
#             subscription_status='pending'  # Will be activated after payment
#         )
#         user.set_password(password)
        
#         try:
#             db.session.add(user)
#             db.session.commit()
#             flash('Registration successful! Please check your email for account activation.', 'success')
#             return redirect(url_for('auth.login'))
#         except Exception as e:
#             db.session.rollback()
#             flash('Registration failed. Please try again.', 'error')
#             return render_template('auth/register.html')
    
#     return render_template('auth/register.html')

# @bp.route('/forgot-password', methods=['GET', 'POST'])
# def forgot_password():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         user = User.query.filter_by(email=email).first()
#         if user:
#             # TODO: Implement password reset email logic
#             # For now, just show success message
#             flash('Password reset instructions have been sent to your email address. Please check your inbox and follow the instructions to reset your password.', 'success')
#         else:
#             flash('If an account with this email exists, you will receive password reset instructions.', 'info')
#         return redirect(url_for('auth.login'))
#     return render_template('auth/forgot_password.html')

# @bp.route('/reset-password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
#     # TODO: Implement token verification and password reset
#     if request.method == 'POST':
#         new_password = request.form.get('password')
#         confirm_password = request.form.get('confirm_password')
        
#         if new_password != confirm_password:
#             flash('Passwords do not match', 'error')
#             return render_template('auth/reset_password.html', token=token)
        
#         # TODO: Update user password with token verification
#         flash('Your password has been reset successfully', 'success')
#         return redirect(url_for('auth.login'))
    
#     return render_template('auth/reset_password.html', token=token)

# @bp.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You have been logged out', 'info')
#     return redirect(url_for('index'))