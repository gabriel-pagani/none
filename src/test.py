def close_my_account_dialog(e=None):
    account_username_input.error = None
    current_master_password_input.error = None
    new_master_password_input.error = None
    confirm_new_master_password_input.error = None

    current_master_password_input.value = ""
    new_master_password_input.value = ""
    confirm_new_master_password_input.value = ""
    confirm_new_master_password_input.visible = False

    self.page.pop_dialog()

def open_my_account_dialog(e):
    account_username_input.value = self.user.username
    current_master_password_input.value = ""
    new_master_password_input.value = ""
    confirm_new_master_password_input.value = ""
    confirm_new_master_password_input.visible = False

    account_username_input.error = None
    current_master_password_input.error = None
    new_master_password_input.error = None
    confirm_new_master_password_input.error = None

    self.page.show_dialog(my_account_dialog)

def save_account_changes(e):
    # reset errors
    account_username_input.error = None
    current_master_password_input.error = None
    new_master_password_input.error = None
    confirm_new_master_password_input.error = None

    current_pw = (current_master_password_input.value or "").strip()
    new_username = (account_username_input.value or "").strip()
    new_pw = (new_master_password_input.value or "").strip()
    new_pw_confirm = (confirm_new_master_password_input.value or "").strip()

    has_error = False

    if not current_pw:
        current_master_password_input.error = "Current master password is required!"
        has_error = True

    if new_pw:
        if not new_pw_confirm:
            confirm_new_master_password_input.error = "Please confirm the new master password!"
            has_error = True
        elif new_pw != new_pw_confirm:
            confirm_new_master_password_input.error = "The new passwords don't match!"
            has_error = True
        elif not validate_master_password(new_pw):
            new_master_password_input.error = "Weak password! Use at least 15 characters."
            has_error = True

    if has_error:
        account_username_input.update()
        current_master_password_input.update()
        new_master_password_input.update()
        confirm_new_master_password_input.update()
        return

    # treat unchanged/empty as None
    new_username_arg = None
    if new_username and new_username != self.user.username:
        new_username_arg = new_username

    new_pw_arg = new_pw if new_pw else None

    if new_username_arg is None and new_pw_arg is None:
        show_message(self.page, 2, "Nothing to update.")
        return

    updated = self.user.update(
        current_master_password=current_pw,
        new_username=new_username_arg,
        new_master_password=new_pw_arg,
    )

    if not updated:
        show_message(self.page, 3, "Error updating account. Check your current password and try again.")
        return

    # If master password changed, user.salt was rotated inside User.update()
    if new_pw_arg:
        self.user_key = derive_master_password(new_pw_arg, self.user.salt)

    close_my_account_dialog(e)
    show_message(self.page, 1, "Account updated successfully!")
    refresh_tiles_list()

my_account_dialog = ft.AlertDialog(
    modal=True,
    title=ft.Text("Update account"),
    content=ft.Column(
        controls=[
            current_master_password_input,
            account_username_input,
            new_master_password_input,
            confirm_new_master_password_input,
        ],
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        height=360,
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    ),
    actions=[
        ft.TextButton("Cancel", on_click=close_my_account_dialog),
        ft.TextButton("Save", on_click=save_account_changes),
    ],
    actions_alignment=ft.MainAxisAlignment.END,
)
