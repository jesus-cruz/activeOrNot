import signal
import os
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
#from gi.repository import Notify as notify
# Notify is disabled due to the option -t(time) not working

APPINDICATOR_ID = 'activeOrNot'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('~/projects/indicator/icon.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    #notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)

    item_sixty = gtk.MenuItem('Change to 60 seconds')
    item_sixty.connect('activate', change_to_sixty)

    item_never = gtk.MenuItem('Change to never')
    item_never.connect('activate', change_to_never)

    menu.append(item_sixty)
    menu.append(item_never)
    menu.append(item_quit)

    menu.show_all()
    return menu

def change_to_sixty(source):
    #notify.Notification.new("Changed to 60 seconds").show()
    os.system("gsettings set org.gnome.desktop.session idle-delay 60")

def change_to_never(source):
    #notify.Notification.new("Changed to never").show()
    os.system("gsettings set org.gnome.desktop.session idle-delay 0")

def quit(source):
    #notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
