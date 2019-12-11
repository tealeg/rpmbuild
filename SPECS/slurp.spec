Name:           slurp
Version:        1.1.0
Release:        1%{?dist}
Summary:        Print a region from the Wayland compositor to standard output.

License:        MIT
URL:            https://wayland.emersion.fr/slurp/
Source0:        https://github.com/emersion/slurp/archive/v1.1.0.tar.gz


BuildRequires:  wayland-protocols-devel
BuildRequires:  cairo-devel
BuildRequires:  scdoc
Requires:	cairo


%description
Select a region in a Wayland compositor and print it to the standard output. Works well with grim.  

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
* Wed Dec 11 2019 Geoffrey J. Teale <tealeg@gmail.com> - 1.1.0-1
- Add initial build
