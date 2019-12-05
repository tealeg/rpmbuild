Name:           waybar
Version:        0.8.0
Release:        1%{?dist}
Summary:        Alternative toolbar for wayland

License:        MIT
URL:            https://github.com/Alexays/%{name}
Source0:        https://github.com/Alexays/%{name}/archive/%{version}.tar.gz

BuildRequires:  gtkmm30-devel
BuildRequires:  jsoncpp-devel
BuildRequires:	libinput-devel
BuildRequires:	libsigc++-devel
BuildRequires:  fmt-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  wlroots-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	libnl3-devel
BuildRequires:	sway
BuildRequires:	libdbusmenu-gtk3-devel
BuildRequires:	libmpdclient-devel
Requires:       gtkmm30
Requires:	jsoncpp
Requires:	libinput
Requires:	libsigc++
Requires:	fmt-devel
Requires:	wlroots
Requires:	pulseaudio-libs
Requires:	libnl3
Requires:	sway
Requires:	libdbusmenu-gtk3
Requires:	libmpdclient

%description


%prep
%autosetup


%build
%meson
%meson_build


%install

%ninja_install

%check
%meson_test

%files
%license LICENSE




%changelog
* Wed Dec  4 2019 Geoffrey J. Teale <tealeg@gmail.com>
- 
%global srcname waybar
%define build_timestamp %{lua: print(os.date("%Y.%m.%d_%H.%M"))}

Name:           %{srcname}
Version:        %{build_timestamp}
Release:        0%{?dist}
Summary:        Highly customizable Wayland bar for Sway and Wlroots based compositors 
License:        MIT
URL:            https://github.com/Alexays/Waybar
Source0:        https://github.com/Alexays/Waybar/archive/master.zip
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig(fmt) >= 5.3.0
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libinput) 
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(spdlog) >= 1.3.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  scdoc
Recommends:     fontawesome-fonts

%description
Highly customizable Wayland bar for Sway and Wlroots based compositors

%prep
%autosetup -n Waybar-master 

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config
%config(noreplace) %{_sysconfdir}/xdg/%{name}/style.css
%{_bindir}/%{name}
%{_mandir}/man5/%{name}*
/usr/lib/systemd/user/waybar.service
