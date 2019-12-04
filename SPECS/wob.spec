Name:           wob
Version:        0.2
Release:        1%{?dist}
Summary:        Wayland Overlay Bar

License:        ISC
URL:            https://github.com/francma/%{name}
Source0:        https://github.com/francma/%{name}-%{version}.tar.bz2

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  wayland-protocols-devel
BuildRequires:  wlroots-devel
Requires: wlroots

%description
wob provides a screen-overlay bar that can be used in
Wayland to display the value of some given gauge.  Typical uses
include providing a graphical indicator whilst making volume or
brightness adjustments via the keyboard.


%prep
%autosetup

%build
%meson # build-release --buildtype release
%meson_build #-C build-release

%install
cd %_vpath_builddir
%ninja_install 
# ninja -C build-release install

%check
%meson_test

%files
%license LICENSE
%{_bindir}/%{name}



%changelog
* Fri Nov  8 2019 Geoffrey J. Teale <tealeg@gmail.com> - 0.2-1
- Add initial build
