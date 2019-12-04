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
