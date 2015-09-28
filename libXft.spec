#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXft
Version  : 2.3.2
Release  : 4
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXft-2.3.2.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXft-2.3.2.tar.gz
Summary  : X FreeType library
Group    : Development/Tools
License  : MIT
Requires: libXft-lib
Requires: libXft-doc
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xrender)

%description
Xft
X FreeType library
Xft version 2.1 was the first stand alone release of Xft, a library that
connects X applications with the FreeType font rasterization library. Xft
uses fontconfig to locate fonts so it has no configuration files.

%package dev
Summary: dev components for the libXft package.
Group: Development
Requires: libXft-lib

%description dev
dev components for the libXft package.


%package doc
Summary: doc components for the libXft package.
Group: Documentation

%description doc
doc components for the libXft package.


%package lib
Summary: lib components for the libXft package.
Group: Libraries

%description lib
lib components for the libXft package.


%prep
%setup -q -n libXft-2.3.2

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/Xft/Xft.h
/usr/include/X11/Xft/XftCompat.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
