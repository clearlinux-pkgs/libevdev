#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : libevdev
Version  : 1.13.1
Release  : 46
URL      : https://www.freedesktop.org/software/libevdev/libevdev-1.13.1.tar.xz
Source0  : https://www.freedesktop.org/software/libevdev/libevdev-1.13.1.tar.xz
Source1  : https://www.freedesktop.org/software/libevdev/libevdev-1.13.1.tar.xz.sig
Summary  : Handler library for evdev events
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: libevdev-bin = %{version}-%{release}
Requires: libevdev-lib = %{version}-%{release}
Requires: libevdev-license = %{version}-%{release}
Requires: libevdev-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32check)
BuildRequires : pkgconfig(check)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libevdev - wrapper library for evdev input devices
==================================================

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


%package man
Summary: man components for the libevdev package.
Group: Default

%description man
man components for the libevdev package.


%prep
%setup -q -n libevdev-1.13.1
cd %{_builddir}/libevdev-1.13.1
pushd ..
cp -a libevdev-1.13.1 build32
popd
pushd ..
cp -a libevdev-1.13.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683298592
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1683298592
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libevdev
cp %{_builddir}/libevdev-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libevdev/408b8caca51347634ebeb7be4bf8a1e8b782adac || :
cp %{_builddir}/libevdev-%{version}/doc/style/LICENSE %{buildroot}/usr/share/package-licenses/libevdev/5a48bb048772f9029b604fbdd869d92fddae1cef || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/libevdev-tweak-device
/V3/usr/bin/mouse-dpi-tool
/V3/usr/bin/touchpad-edge-detector
/usr/bin/libevdev-tweak-device
/usr/bin/mouse-dpi-tool
/usr/bin/touchpad-edge-detector

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libevdev.so
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
/V3/usr/lib64/libevdev.so.2
/V3/usr/lib64/libevdev.so.2.3.0
/usr/lib64/libevdev.so.2
/usr/lib64/libevdev.so.2.3.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libevdev.so.2
/usr/lib32/libevdev.so.2.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libevdev/408b8caca51347634ebeb7be4bf8a1e8b782adac
/usr/share/package-licenses/libevdev/5a48bb048772f9029b604fbdd869d92fddae1cef

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/libevdev-tweak-device.1
/usr/share/man/man1/mouse-dpi-tool.1
/usr/share/man/man1/touchpad-edge-detector.1
