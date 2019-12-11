Name:           grim
Version:        1.1
Release:        1%{?dist}
Summary:        Grab images from any Wayland

License:        MIT
URL:            https://wayland.emersion.fr/grim/
Source0:        https://github.com/emersion/grim/archive/v1.1.tar.gz

BuildRequires:  wayland-protocols-devel
BuildRequires:  cairo-devel
BuildRequires:	libjpeg-turbo-devel
Requires:	cairo
Requires:	libjpeg-turbo

%description 
Grab images from a Wayland compositor. Works great with slurp and with sway


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%check
%meson_test


%files 
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
* Wed Dec 11 2019 Geoffrey J. Teale <tealeg@gmail.com> - 1.1-1
- Add initial build.

