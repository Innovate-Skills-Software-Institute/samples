from taipy.gui import Gui
import taipy.gui.builder as tgb

with tgb.Page() as page:
    tgb.html("p", "User Information :")
    tgb.input("John", label="First Name")
    tgb.button("Submit")

Gui(page).run()