%global extuuid		gtk4-ding@smedius.gitlab.com
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		desktop-icons-ng
%global giturl		https://gitlab.com/smedius/%{gitname}
%global srcdir		%{_builddir}/%{gitname}-%{version}/src

Name:		gnome-shell-extension-gtk4-desktop-icons-ng
Version:	79
Release:	1%{?dist}
Summary:	GNOME Shell Extension - Gtk4 Desktop Icons NG (DING)

License:	GPLv2+
URL:		https://extensions.gnome.org/extension/5263/gtk4-desktop-icons-ng-ding/
Source0:	 %{giturl}/-/archive/Gtk4-%{version}/desktop-icons-ng-Gtk4-%{version}.zip
BuildArch:	noarch

BuildRequires:  gobject-introspection
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  gettext

%description
Libadwaita/Gtk4 port of Desktop Icons NG with multiple fixes and new features.

Icons can be positioned anywhere on desktop or are snapped to a grid. Can make links on the Desktop. GSconnect Integration, can send files to connected devices. Drag and Drop support on to Dock, Dash, or from Dock, Dash to the Desktop.

Updated and modified code base, uses Gio menus, all translations on Weblate. All functions are asynchronous where possible. It is ported to ESM modules, supports Gnome  45 and higher.

Multiple fixes and new features-

* The stock gnome shell background menu can now be shown from the Gtk4 DING desktop right click menu. All shell settings can be accessed from that menu.
* Icons can be placed on any arbitrary position. Make a mess! - icons can overlap each other etc. Neat people can keep the default behavior and have the icons always snapped to a grid. Controlled in preferences, tweaks, 'Snap to grid'. Affects the shape of icons and drag and drop behavior as well. Free positioning has trapezoidal icons, drop only works with direct overlap. Grid positioning has rectangular icons, and drag and drop works on overlap with the grid holding the icon. This behavior is consistent with other desktop environments.
* Icons on background on overview, improved gesture switching icons appear to be on all work spaces on the background with workspace switching, with no flashing.
* Support for dragging icons onto the dock - Drag icons from desktop to and drop over application icon to open them with the app. Works with Dash to Dock and Dash to Panel.
* Support for dragging icons from desktop directly to Trash on Dash to Dock, or to mounted volumes on the dock, to copy them directly.
* Set the correct cursor with proposed action on drop on dock.
* Drag Navigation on Dock - dragging an icon over the Gnome Files icon on the dock or mounted drives, and hovering over it for 1/2 seconds will open a Gnome Files Window. Behavior can be changed in preferences.
* Drag Navigation - dragging an icon over a folder icon or a drive icon, and then hovering over it for one and half seconds will open that location in Gnome Files.
* Sets correct hovering behavior during drag and drop on the Dock, enables scrolling in the dock to icons when they are hidden.
* Drag and drop Favorite apps from Dash to Dock, Dash to Panel directly to Desktop. Pressing shift, ctr or alt while doing this will copy or move the app to Desktop, allowing launching from the desktop. Just dropping an app from the dock to the desktop will remove from Dash/Dock.
* Follows xdg-terminal-exec to display the correct terminal in right click menus, and will launch the correct terminal, even if xdg-terminal-exec is not installed.
* Shows the correct file manager in the right click menu and give the user the option to change the file manager.
* Gio menus, menus display all keyboard shortcuts.
* Uses Gtk4 AlertDialog, uses asynchronous promises for dialog's, shows button to launch URL for help and troubleshooting information.
* Automatically zip Folders if mailing them.
* Tool tips are now positioned correctly to not go under the dash or make it auto hide, or go over/under any gnome shell actors on the edge of the screen.
* Right Click Menus will not go under the dock.
* Make Links on Desktop with Alt button on Wayland. Shift, Ctr or Alt button control the effect, move, copy, drop or link. (Linking may not work on X11)
* Copied/dropped/pasted files retain dropped position. Undo action after trashing or moving files puts icons back in the old position.
* Better multi monitor support, preference to place icons on non primary monitor.
* GSconnect extension integration, can send files from desktop directly to connected mobile device.
* Accessibility support with screen readers
* Deals correctly with appimage files on desktop.
* Display GIMP thumbnails, even for snap and flatpack installs.

Please see Readme for full details of new features. Works best on Wayland. However your mileage may vary on X11. Multiple bugs fixed on X11.

Please report all issues on the Gitlab link below, this page is not monitored. All known issues as well as all the features are detailed there.

Extension Homepage
    https://gitlab.com/smedius/desktop-icons-ng 

%prep
%autosetup -n %{gitname}-Gtk4-%{version}
sed -e "/meson_post_install/d" -i meson.build

%build
%meson --localedir=%{_datadir}/locale
%meson_build

%install
%meson_install

%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
  %{_bindir}/glib-compile-schemas %{extdir}/schemas &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%{_bindir}/glib-compile-schemas %{extdir}/schemas &> /dev/null || :

%files
%{extdir}
/usr/share/locale/*/LC_MESSAGES/gtk4-ding.mo
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.gtk4-ding.gschema.xml

%changelog
* Mon Aug 12 2024 Cameron Knauff
Switched from Make to Meson

* Sun Aug 11 2024 Cameron Knauff
- Initial package
