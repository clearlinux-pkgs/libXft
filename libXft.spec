#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xACEB29740C9A4E97 (mattst88@gmail.com)
#
Name     : libXft
Version  : 2.3.8
Release  : 21
URL      : https://www.x.org/releases/individual/lib/libXft-2.3.8.tar.gz
Source0  : https://www.x.org/releases/individual/lib/libXft-2.3.8.tar.gz
Source1  : https://www.x.org/releases/individual/lib/libXft-2.3.8.tar.gz.sig
Summary  : X FreeType library
Group    : Development/Tools
License  : HPND
Requires: libXft-lib = %{version}-%{release}
Requires: libXft-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xrender)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libXft - X FreeType library
---------------------------
libXft is the client side font rendering library, using libfreetype,
libX11, and the X Render extension to display anti-aliased text.

%package dev
Summary: dev components for the libXft package.
Group: Development
Requires: libXft-lib = %{version}-%{release}
Provides: libXft-devel = %{version}-%{release}
Requires: libXft = %{version}-%{release}

%description dev
dev components for the libXft package.


%package lib
Summary: lib components for the libXft package.
Group: Libraries
Requires: libXft-license = %{version}-%{release}

%description lib
lib components for the libXft package.


%package license
Summary: license components for the libXft package.
Group: Default

%description license
license components for the libXft package.


%prep
%setup -q -n libXft-2.3.8
cd %{_builddir}/libXft-2.3.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681767348
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1681767348
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libXft
cp %{_builddir}/libXft-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libXft/cb03b5ef1e3d983356601be29e306eebdc6a9257 || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/Xft/Xft.h
/usr/include/X11/Xft/XftCompat.h
/usr/lib64/libXft.so
/usr/lib64/pkgconfig/xft.pc
/usr/share/man/man3/Xft.3
/usr/share/man/man3/XftCharExists.3
/usr/share/man/man3/XftCharFontSpecRender.3
/usr/share/man/man3/XftCharIndex.3
/usr/share/man/man3/XftCharSpecRender.3
/usr/share/man/man3/XftColorAllocName.3
/usr/share/man/man3/XftColorAllocValue.3
/usr/share/man/man3/XftColorFree.3
/usr/share/man/man3/XftDefaultHasRender.3
/usr/share/man/man3/XftDefaultSet.3
/usr/share/man/man3/XftDefaultSubstitute.3
/usr/share/man/man3/XftDrawChange.3
/usr/share/man/man3/XftDrawCharFontSpec.3
/usr/share/man/man3/XftDrawCharSpec.3
/usr/share/man/man3/XftDrawColormap.3
/usr/share/man/man3/XftDrawCreate.3
/usr/share/man/man3/XftDrawCreateAlpha.3
/usr/share/man/man3/XftDrawCreateBitmap.3
/usr/share/man/man3/XftDrawDestroy.3
/usr/share/man/man3/XftDrawDisplay.3
/usr/share/man/man3/XftDrawDrawable.3
/usr/share/man/man3/XftDrawGlyphFontSpec.3
/usr/share/man/man3/XftDrawGlyphSpec.3
/usr/share/man/man3/XftDrawGlyphs.3
/usr/share/man/man3/XftDrawPicture.3
/usr/share/man/man3/XftDrawRect.3
/usr/share/man/man3/XftDrawSetClip.3
/usr/share/man/man3/XftDrawSetClipRectangles.3
/usr/share/man/man3/XftDrawSetSubwindowMode.3
/usr/share/man/man3/XftDrawSrcPicture.3
/usr/share/man/man3/XftDrawString16.3
/usr/share/man/man3/XftDrawString32.3
/usr/share/man/man3/XftDrawString8.3
/usr/share/man/man3/XftDrawStringUtf16.3
/usr/share/man/man3/XftDrawStringUtf8.3
/usr/share/man/man3/XftDrawVisual.3
/usr/share/man/man3/XftFontCheckGlyph.3
/usr/share/man/man3/XftFontClose.3
/usr/share/man/man3/XftFontCopy.3
/usr/share/man/man3/XftFontInfoCreate.3
/usr/share/man/man3/XftFontInfoDestroy.3
/usr/share/man/man3/XftFontInfoEqual.3
/usr/share/man/man3/XftFontInfoHash.3
/usr/share/man/man3/XftFontLoadGlyphs.3
/usr/share/man/man3/XftFontMatch.3
/usr/share/man/man3/XftFontOpen.3
/usr/share/man/man3/XftFontOpenInfo.3
/usr/share/man/man3/XftFontOpenName.3
/usr/share/man/man3/XftFontOpenPattern.3
/usr/share/man/man3/XftFontOpenXlfd.3
/usr/share/man/man3/XftFontUnloadGlyphs.3
/usr/share/man/man3/XftGetVersion.3
/usr/share/man/man3/XftGlyphExtents.3
/usr/share/man/man3/XftGlyphFontSpecRender.3
/usr/share/man/man3/XftGlyphRender.3
/usr/share/man/man3/XftGlyphSpecRender.3
/usr/share/man/man3/XftInit.3
/usr/share/man/man3/XftInitFtLibrary.3
/usr/share/man/man3/XftListFonts.3
/usr/share/man/man3/XftLockFace.3
/usr/share/man/man3/XftNameParse.3
/usr/share/man/man3/XftNameUnparse.3
/usr/share/man/man3/XftTextExtents16.3
/usr/share/man/man3/XftTextExtents32.3
/usr/share/man/man3/XftTextExtents8.3
/usr/share/man/man3/XftTextExtentsUtf16.3
/usr/share/man/man3/XftTextExtentsUtf8.3
/usr/share/man/man3/XftTextRender16.3
/usr/share/man/man3/XftTextRender16BE.3
/usr/share/man/man3/XftTextRender16LE.3
/usr/share/man/man3/XftTextRender32.3
/usr/share/man/man3/XftTextRender32BE.3
/usr/share/man/man3/XftTextRender32LE.3
/usr/share/man/man3/XftTextRender8.3
/usr/share/man/man3/XftTextRenderUtf16.3
/usr/share/man/man3/XftTextRenderUtf8.3
/usr/share/man/man3/XftUnlockFace.3
/usr/share/man/man3/XftXlfdParse.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXft.so.2
/usr/lib64/libXft.so.2.3.8

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libXft/cb03b5ef1e3d983356601be29e306eebdc6a9257
