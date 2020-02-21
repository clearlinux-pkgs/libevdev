#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : libevdev
Version  : 1.8.901
Release  : 34
URL      : https://www.freedesktop.org/software/libevdev/libevdev-1.8.901.tar.xz
Source0  : https://www.freedesktop.org/software/libevdev/libevdev-1.8.901.tar.xz
Source1  : https://www.freedesktop.org/software/libevdev/libevdev-1.8.901.tar.xz.sig
Summary  : Wrapper library for evdev devices
Group    : Development/Tools
License  : Apache-2.0 HPND
Requires: libevdev-bin = %{version}-%{release}
Requires: libevdev-lib = %{version}-%{release}
Requires: libevdev-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32check)
BuildRequires : pkgconfig(check)
BuildRequires : valgrind

%description
# Doxygen-Bootstrap
This is a small project for integrating Doxygen output with Twitter Bootstrap.

%package bin
Summary: bin components for the libevdev package.
Group: Binaries
Requires: libevdev-license = %{version}-%{release}

%description bin
bin components for the libevdev package.


%package dev
Summary: dev components for the libevdev package.
Group: Development
Requires: libevdev-lib = %{version}-%{release}
Requires: libevdev-bin = %{version}-%{release}
Provides: libevdev-devel = %{version}-%{release}
Requires: libevdev = %{version}-%{release}
Requires: libevdev = %{version}-%{release}

%description dev
dev components for the libevdev package.


%package dev32
Summary: dev32 components for the libevdev package.
Group: Default
Requires: libevdev-lib32 = %{version}-%{release}
Requires: libevdev-bin = %{version}-%{release}
Requires: libevdev-dev = %{version}-%{release}

%description dev32
dev32 components for the libevdev package.


%package lib
Summary: lib components for the libevdev package.
Group: Libraries
Requires: libevdev-license = %{version}-%{release}

%description lib
lib components for the libevdev package.


%package lib32
Summary: lib32 components for the libevdev package.
Group: Default
Requires: libevdev-license = %{version}-%{release}

%description lib32
lib32 components for the libevdev package.


%package license
Summary: license components for the libevdev package.
Group: Default

%description license
license components for the libevdev package.


%prep
%setup -q -n libevdev-1.8.901
cd %{_builddir}/libevdev-1.8.901
pushd ..
cp -a libevdev-1.8.901 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582301612
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1582301612
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libevdev
cp %{_builddir}/libevdev-1.8.901/COPYING %{buildroot}/usr/share/package-licenses/libevdev/5a9e6860301d6944285c7fe35b0c311599974bc1
cp %{_builddir}/libevdev-1.8.901/doc/style/LICENSE %{buildroot}/usr/share/package-licenses/libevdev/5a48bb048772f9029b604fbdd869d92fddae1cef
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
/usr/share/man/man3/libevdev.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libevdev.so
/usr/lib32/pkgconfig/32libevdev.pc
/usr/lib32/pkgconfig/libevdev.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libevdev.so.2
/usr/lib64/libevdev.so.2.3.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libevdev.so.2
/usr/lib32/libevdev.so.2.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libevdev/5a48bb048772f9029b604fbdd869d92fddae1cef
/usr/share/package-licenses/libevdev/5a9e6860301d6944285c7fe35b0c311599974bc1
