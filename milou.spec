#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v26
# autospec commit: 99a7985
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : milou
Version  : 6.3.5
Release  : 118
URL      : https://download.kde.org/stable/plasma/6.3.5/milou-6.3.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.3.5/milou-6.3.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.3.5/milou-6.3.5.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: milou-data = %{version}-%{release}
Requires: milou-lib = %{version}-%{release}
Requires: milou-license = %{version}-%{release}
Requires: milou-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : krunner-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the milou package.
Group: Data

%description data
data components for the milou package.


%package lib
Summary: lib components for the milou package.
Group: Libraries
Requires: milou-data = %{version}-%{release}
Requires: milou-license = %{version}-%{release}

%description lib
lib components for the milou package.


%package license
Summary: license components for the milou package.
Group: Default

%description license
license components for the milou package.


%package locales
Summary: locales components for the milou package.
Group: Default

%description locales
locales components for the milou package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n milou-6.3.5
cd %{_builddir}/milou-6.3.5
pushd ..
cp -a milou-6.3.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747161637
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1747161637
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/milou
cp %{_builddir}/milou-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/milou/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/milou-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/milou/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/milou-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/milou/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/milou-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/milou/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/milou-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/milou/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/milou-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/milou/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/milou-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/milou/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/milou-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/milou/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/milou-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/milou/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/milou-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/milou/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang milou
%find_lang plasma_applet_org.kde.milou
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/metainfo/org.kde.milou.appdata.xml
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/SearchField.qml
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/globals.js
/usr/share/plasma/plasmoids/org.kde.milou/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.milou/metadata.json

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/qml/org/kde/milou/libmilouqmlplugin.so
/usr/lib64/qt6/qml/org/kde/milou/ResultDelegate.qml
/usr/lib64/qt6/qml/org/kde/milou/ResultsListView.qml
/usr/lib64/qt6/qml/org/kde/milou/ResultsListViewDelegate.qml
/usr/lib64/qt6/qml/org/kde/milou/ResultsView.qml
/usr/lib64/qt6/qml/org/kde/milou/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/milou/libmilouqmlplugin.so
/usr/lib64/qt6/qml/org/kde/milou/milouqmlplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/milou/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/milou/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/milou/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/milou/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/milou/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/milou/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/milou/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/milou/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f milou.lang -f plasma_applet_org.kde.milou.lang
%defattr(-,root,root,-)

