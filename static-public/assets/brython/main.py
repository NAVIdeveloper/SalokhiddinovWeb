from browser import document,window

key_class_mobile = 'mobile'
def mobile_open_menu(event):
    button = document["menu-btns"]
    if key_class_mobile in button['class'].split():
        button['class'] = ''.join(button['class'].split()[:-1])
    else:
        button['class'] += f' {key_class_mobile}'


document["mobile-menu"].bind("click", mobile_open_menu)

def css_var(var):
    return window.getComputedStyle(document.documentElement).getPropertyValue(var).strip()

def switch_mode():
    root = document.documentElement
    if window.localStorage["mode"] == 'light':
        # Switch to light mode
        root.style.setProperty('--bgcolor', css_var('--light-bg'))
        root.style.setProperty('--fgcolor', css_var('--light-fg'))
        root.style.setProperty('--mode', css_var('--light-mode'))
        root.style.setProperty('--menu-bg', css_var('--light-menu-bg'))
        root.style.setProperty('--btn-mobile-menu', css_var('--light-btn-mobile-menu'))
    else:
        # Switch to dark mode
        root.style.setProperty('--bgcolor', css_var('--dark-bg'))
        root.style.setProperty('--fgcolor', css_var('--dark-fg'))
        root.style.setProperty('--mode', css_var('--dark-mode'))
        root.style.setProperty('--menu-bg', css_var('--dark-menu-bg'))
        root.style.setProperty('--btn-mobile-menu', css_var('--dark-btn-mobile-menu'))

def color_mode_switch(event):
    if window.localStorage["mode"] == 'light':
        window.localStorage["mode"] = 'dark'
    else:
        window.localStorage["mode"] = 'light'
    switch_mode()

# Attach the event listener to the button
document["switcher"].bind("click", color_mode_switch)

if not "mode" in window.localStorage:
    window.localStorage["mode"] = "light"

switch_mode()