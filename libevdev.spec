#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : libevdev
Version  : 1.5.9
Release  : 28
URL      : https://www.freedesktop.org/software/libevdev/libevdev-1.5.9.tar.xz
Source0  : https://www.freedesktop.org/software/libevdev/libevdev-1.5.9.tar.xz
Source99 : https://www.freedesktop.org/software/libevdev/libevdev-1.5.9.tar.xz.sig
Summary  : Handler library for evdev events
Group    : Development/Tools
License  : HPND
Requires: libevdev-bin
Requires: libevdev-lib
Requires: libevdev-doc
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32check)
BuildRequires : pkgconfig(check)

BuildRequires : python3
BuildRequires : valgrind

%description
No detailed description available

%package bin
Summary: bin components for the libevdev package.
Group: Binaries

%description bin
bin components for the libevdev package.


%package dev
Summary: dev components for the libevdev package.
Group: Development
Requires: libevdev-lib
Requires: libevdev-bin
Provides: libevdev-devel

%description dev
dev components for the libevdev package.


%package dev32
Summary: dev32 components for the libevdev package.
Group: Default
Requires: libevdev-lib32
Requires: libevdev-bin
Requires: libevdev-dev

%description dev32
dev32 components for the libevdev package.


%package doc
Summary: doc components for the libevdev package.
Group: Documentation

%description doc
doc components for the libevdev package.


%package lib
Summary: lib components for the libevdev package.
Group: Libraries

%description lib
lib components for the libevdev package.


%package lib32
Summary: lib32 components for the libevdev package.
Group: Default

%description lib32
lib32 components for the libevdev package.


%prep
%setup -q -n libevdev-1.5.9
pushd ..
cp -a libevdev-1.5.9 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522111789
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1522111789
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libevdev-tweak-device
/usr/bin/mouse-dpi-tool
/usr/bin/touchpad-edge-detector

%files dev
%defattr(-,root,root,-)
/usr/include/libevdev-1.0/libevdev/libevdev-uinput.h
/usr/include/libevdev-1.0/libevdev/libevdev.h
/usr/lib64/libevdev.so
/usr/lib64/pkgconfig/libevdev.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libevdev.so
/usr/lib32/pkgconfig/32libevdev.pc
/usr/lib32/pkgconfig/libevdev.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libevdev.so.2
/usr/lib64/libevdev.so.2.1.21

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libevdev.so.2
/usr/lib32/libevdev.so.2.1.21
